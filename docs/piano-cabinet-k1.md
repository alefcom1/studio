# Кабинет заказчика Remarka — этап K1: детальная спецификация

> Задача #61 в трекере. Этап K1 «фундамент (бета)»: вход по magic-link,
> модель Client → Project, мультитенантность, пилот на 1–2 клиентах.
> Стадии K2/K3 — вне этой спеки (см. `docs/server-hetzner.md`, раздел
> «Кабинет заказчика — план K1–K3»).
>
> Опорная кодовая база — платформа **Remarka Lab · Monitor** (репо
> `alefcom1/1russian.com`, код в `sitelens/`). Прод-конфиг —
> `deploy/remarka-lab/`. Спека написана после READ-ONLY-изучения кода;
> все выводы о реюзе выверены по факту (см. §1.1).

---

## 0. Резюме для оркестратора (TL;DR)

Пять ключевых архитектурных решений:

1. **Кабинет — отдельное приложение `apps/cabinet`** (Next.js App Router)
   со **своим бэкендом на Route Handlers** (`app/api/**`), а НЕ расширение
   `apps/web` и НЕ отдельный Fastify-сервис. Один новый контейнер, полная
   изоляция от Monitor-API (который целиком за basic_auth), минимум памяти.
2. **Та же БД Postgres, та же Prisma-схема** (`packages/db`), новые модели
   с префиксом `Cab*` (маппинг на таблицы `cab_*`). Monitor-модели не
   трогаем. `ClientProject` — отдельная сущность от Monitor-`Project`
   (разная семантика), опциональная nullable-ссылка на Monitor для K3.
3. **Magic-link:** случайный токен 32 байта, в БД только SHA-256-хэш,
   TTL 15 мин, одноразовый; сессия — **серверная** (таблица `CabSession`,
   opaque-токен в httpOnly/Secure/SameSite=Lax cookie) ради ревокации и
   аудита. JWT-вариант отклонён (нет отзыва).
4. **Мультитенантность** через membership-scoping: сессия → `clientUserId`
   → список разрешённых `clientId` → каждый запрос Prisma фильтруется по
   нему хелпером `requireSession()` + `assertProjectAccess()`. Аудит-лог
   всех событий входа.
5. **Деплой:** новый сервис `cabinet` в `docker-compose.prod.yml`
   (лимит 384M), **отдельный site-блок `clienti.remarka.biz` в Caddyfile
   БЕЗ basic_auth**, `prisma db push` (аддитивно), бэкап уже покрыт
   (общая БД) — но теперь в дампе PII.

Открытые вопросы владельцу — §10 (поддомен, e-mail-провайдер, пилотные
клиенты).

---

## 1. Изучение опорной базы: что реюзается, что строим с нуля

### 1.1. Факты о коде Monitor (выверено чтением)

- **Стек:** pnpm-монорепо (`pnpm-workspace.yaml`: `apps/*`, `packages/*`).
  `apps/api` — Fastify 4 (ESM, `type: module`), `apps/web` — Next.js 14
  (App Router, `output: 'standalone'`), `apps/worker` — BullMQ+Chromium,
  `packages/db` — Prisma 5.8 + Postgres.
- **Авторизации в приложении НЕТ вообще.** Весь сайт `lab.remarka.biz`
  закрыт HTTP Basic Auth на Caddy (`deploy/remarka-lab/Caddyfile`,
  директива `basic_auth`). Это ключевое ограничение: кабинет — публичный
  вход клиентов, его нельзя ставить за тот же basic_auth.
- **API-роуты** регистрируются с литеральным префиксом `/api/...` внутри
  файлов (не через Fastify-`prefix`); envelope ответа — `{ data: ... }`.
  Ни одного guard'а: `GET /api/projects` отдаёт ВСЕ проекты без проверок.
- **БД:** одна база `sitelens`, схема применяется через **`prisma db push`**
  (см. `apps/api/docker-entrypoint.sh` → `db:push`; каталога
  `packages/db/prisma/migrations` НЕТ — истории миграций нет).
- **E-mail:** реального отправителя НЕТ. В `.env.prod.template` есть
  пустые `SMTP_*`, но в коде отправка — заглушка (`crawl-worker.ts:371`
  просто `console.log('[Alert] … Send email to …')`). Пакета `nodemailer`
  нет ни в одном `package.json`. => отправку писем строим с нуля.
- **Дизайн-система уже перенесена в Monitor** (редизайн 16.07): токены
  бренда в `apps/web/tailwind.config.js` (`carta #F7F6F2`, `inchiostro
  #14161A`, `oltremare/brand #2440C8`, `grigio`, `bordo`, шрифты Clash
  Display / General Sans / Fragment Mono), базовые стили и «бумажная
  сетка» в `apps/web/src/app/globals.css`. Всё это копируем в кабинет.
- **Prisma-клиент** экспортируется из `@sitelens/db` (`prisma`,
  `PrismaClient`, `Prisma`, типы моделей). Кабинет импортирует тот же пакет.
- **Web-сборка:** `output: 'standalone'`, Dockerfile строит standalone
  и запускает `node apps/web/server.js` на порту 3000.
- **Прод-память (текущие лимиты, 4 ГБ box):** db 512 + redis 256 + api 512
  + worker 1024 + web 512 + caddy 128 = **2944M** сумма лимитов.

### 1.2. Матрица реюза

| Компонент | Реюз / с нуля |
|---|---|
| pnpm-монорепо, tsconfig.base, паттерн Dockerfile | **реюз** (копируем паттерн web-Dockerfile) |
| `packages/db` (Prisma-клиент, коннект к Postgres) | **реюз** — добавляем в ту же схему модели `Cab*` |
| Дизайн-токены (tailwind.config, globals.css, UI-компоненты `ui/*`) | **реюз** — копируем в `apps/cabinet` |
| Postgres, Redis, Caddy, backup.sh | **реюз инфраструктуры** (общие сервисы) |
| Аутентификация, magic-link, сессии | **с нуля** (в Monitor нет) |
| Отправка e-mail | **с нуля** (заглушка в Monitor) |
| Route Handlers бэкенда кабинета | **с нуля** (Monitor-бэкенд на Fastify не реюзаем) |
| UI кабинета (login/projects/project) | **с нуля** на реюзнутых токенах |
| Мультитенантность, tenant-scoping | **с нуля** |

---

## 2. Архитектура: где живёт кабинет

### 2.1. Три варианта и выбор

| Вариант | Плюсы | Минусы | Вердикт |
|---|---|---|---|
| **A. Расширить `apps/web`** (добавить роуты кабинета в существующий Next) | ноль новых контейнеров | `apps/web` целиком за basic_auth → клиент не войдёт; смешение публичного и внутреннего кода в одном бандле; общий `NEXT_PUBLIC_API_URL` указывает на Monitor-api без auth; Caddy маршрутизирует по хосту, разделить сложно | **отклонён** |
| **B. `apps/cabinet` (Next UI) + `apps/cabinet-api` (отд. Fastify)** | чистое разделение фронт/бэк, как в Monitor | **два** новых контейнера (~300M + ~400M ≈ 700M) на 4 ГБ box; дублирование Fastify-обвязки; лишняя сетевая граница | отклонён (память) |
| **C. `apps/cabinet` — Next.js со своим бэкендом на Route Handlers** (`app/api/**`), Prisma напрямую из серверных хендлеров | **один** новый контейнер (~384M); полная изоляция от Monitor-api (тот вообще не публикуется на `clienti`); нет второго Node-процесса; auth/сессии/Prisma — всё server-side в одном месте; Caddy-блок `clienti` проксирует ВСЁ в `cabinet:3002`, без жонглирования путями | **✅ рекомендуется** |

### 2.2. Обоснование выбора C

- **Безопасность публичного входа.** Monitor-api не имеет ни одного guard'а
  и живёт за basic_auth. Если бы кабинет ходил в него (вариант B с реюзом
  api, или A), пришлось бы точечно открывать публично отдельные пути через
  Caddy — одна ошибка конфига раскрывает `/api/projects` всех клиентов
  Monitor. В варианте C **Monitor-api не проксируется на `clienti`
  вообще**; изоляция обеспечена на уровне разных хостов Caddy, а не
  фильтрацией путей. Это наименее хрупко.
- **Память.** 4 ГБ box уже несёт 2944M лимитов. Вариант C добавляет один
  контейнер Next standalone (~384M) → ~3328M, остаётся запас под ОС/Docker.
  Вариант B добавил бы ~700M → впритык.
- **Простота для Sonnet-агента.** Route Handlers Next 14 (App Router)
  дают POST/GET-эндпоинты рядом со страницами, cookie-сессии через
  `next/headers`, серверные компоненты для чтения. Меньше движущихся
  частей, чем поднимать второй Fastify.
- **Разделяемое всё равно разделяется:** БД (Postgres), дизайн-токены,
  инфраструктура, бэкап — общие. «Синергия auth» из плана реализуется
  тем, что модель клиента и magic-link живут в общей БД; если позже
  Monitor захочет тот же вход — переиспользует таблицы `Cab*`.

**Порт кабинета:** 3002 (3000 занят web, 3001 — api).

### 2.3. Итоговая топология

```
 clienti.remarka.biz ──HTTPS──▶ Caddy (site-блок, БЕЗ basic_auth)
                                   │  весь трафик
                                   ▼
                              cabinet:3002  (Next.js: UI + Route Handlers)
                                   │ Prisma
                                   ▼
                               db:5432 (общая Postgres, таблицы cab_*)
                                   ▲
 lab.remarka.biz ──HTTPS──▶ Caddy (site-блок, basic_auth) ─▶ web:3000 / api:3001
```

Кабинет НЕ ходит в Redis/worker (в K1 нет фоновых задач; письма шлём
синхронно из Route Handler). БД — единственная общая точка.

---

## 3. Модель данных (Prisma)

### 3.1. Решение по размещению

- **Та же БД `sitelens`, та же схема** `packages/db/prisma/schema.prisma`.
  Отдельная БД/Postgres-схема — оверкилл на одном 4 ГБ box (лишний коннект-
  пул, усложнение бэкапа). Изоляция обеспечивается на уровне приложения
  (tenant-scoping), а не на уровне БД.
- Новые модели — **префикс `Cab`** и `@@map("cab_...")`, чтобы визуально и
  физически не смешивать с таблицами Monitor.
- **`ClientProject` ≠ Monitor-`Project`.** Monitor-`Project` — это домен
  под краулинг/SEO. Кабинетный проект — заказ/сайт-под-ключ со стадиями
  сдачи. Семантика разная → отдельная модель. Для будущего K3 (метрики из
  Monitor) кладём nullable-ссылку `monitorProjectId` без FK-констрейнта
  между «мирами» (мягкая связь).

### 3.2. Схема (добавить в `schema.prisma`)

```prisma
// ─── Кабинет заказчика (K1) ──────────────────────────────────────────────────

model CabClient {
  id          String   @id @default(cuid())
  name        String                    // юр./бренд-название клиента (компания)
  vatId       String?                   // P.IVA / codice fiscale (для K2 счетов)
  createdAt   DateTime @default(now())
  updatedAt   DateTime @updatedAt

  memberships CabMembership[]
  projects    CabProject[]

  @@map("cab_client")
}

model CabUser {
  id           String   @id @default(cuid())
  email        String   @unique          // нормализованный lower-case
  name         String?
  locale       String   @default("it")   // it | en | ru — язык интерфейса/писем
  lastLoginAt  DateTime?
  createdAt    DateTime @default(now())
  updatedAt    DateTime @updatedAt

  memberships  CabMembership[]
  magicTokens  CabMagicToken[]
  sessions     CabSession[]

  @@map("cab_user")
}

model CabMembership {
  id        String   @id @default(cuid())
  userId    String
  user      CabUser   @relation(fields: [userId], references: [id], onDelete: Cascade)
  clientId  String
  client    CabClient @relation(fields: [clientId], references: [id], onDelete: Cascade)
  role      String   @default("viewer")  // viewer (K1). owner/editor — задел K2
  createdAt DateTime @default(now())

  @@unique([userId, clientId])
  @@index([clientId])
  @@map("cab_membership")
}

model CabProject {
  id               String   @id @default(cuid())
  clientId         String
  client           CabClient @relation(fields: [clientId], references: [id], onDelete: Cascade)
  name             String
  stage            CabProjectStage @default(BRIEF)
  monitorProjectId String?          // мягкая ссылка на Monitor Project (K3), без FK
  createdAt        DateTime @default(now())
  updatedAt        DateTime @updatedAt

  @@index([clientId])
  @@map("cab_project")
}

// Стадии сдачи сайта. В K1 — только отображение (readonly).
enum CabProjectStage {
  BRIEF        // бриф / согласование ТЗ
  DESIGN       // дизайн-макеты
  DEVELOPMENT  // вёрстка/разработка
  CONTENT      // наполнение/переводы
  REVIEW       // приёмка клиентом
  LAUNCH       // запуск
  MAINTENANCE  // поддержка
  ARCHIVED     // архив
}

model CabMagicToken {
  id         String   @id @default(cuid())
  userId     String
  user       CabUser  @relation(fields: [userId], references: [id], onDelete: Cascade)
  tokenHash  String   @unique          // SHA-256(raw token); raw в БД НЕ хранится
  expiresAt  DateTime                  // now + 15 мин
  consumedAt DateTime?                 // одноразовость: непусто → использован
  requestIp  String?
  createdAt  DateTime @default(now())

  @@index([userId])
  @@index([expiresAt])
  @@map("cab_magic_token")
}

model CabSession {
  id          String   @id @default(cuid())
  userId      String
  user        CabUser  @relation(fields: [userId], references: [id], onDelete: Cascade)
  tokenHash   String   @unique          // SHA-256(opaque session token из cookie)
  expiresAt   DateTime                  // now + 7 дней (скользящее продление)
  revokedAt   DateTime?
  ip          String?
  userAgent   String?
  createdAt   DateTime @default(now())
  lastSeenAt  DateTime @default(now())

  @@index([userId])
  @@index([expiresAt])
  @@map("cab_session")
}

model CabAuthAudit {
  id        String   @id @default(cuid())
  userId    String?                     // может быть null (запрос на несуществующий e-mail)
  email     String?                     // всегда пишем нормализованный e-mail попытки
  event     String                      // magic_requested | magic_consumed | magic_invalid |
                                         // magic_expired | session_created | session_revoked |
                                         // login_ratelimited | access_denied
  ip        String?
  userAgent String?
  meta      Json?
  createdAt DateTime @default(now())

  @@index([email])
  @@index([createdAt])
  @@map("cab_auth_audit")
}
```

Замечания:
- `CabUser.email` уникален глобально — один e-mail = один пользователь, он
  может состоять в нескольких `CabClient` через `CabMembership` (агентство
  ведёт несколько юрлиц клиента и т. п.).
- Роли в K1 фактически одна (`viewer`, всё readonly), но поле заложено под
  K2 (approve/comment требуют разграничения).
- `onDelete: Cascade` от `CabClient`/`CabUser` вниз — для GDPR-удаления
  одним действием.

---

## 4. Magic-link аутентификация

### 4.1. Поток

```
1. Клиент вводит e-mail на /login  →  POST /api/auth/request
2. Сервер: нормализует e-mail, находит CabUser (по e-mail).
   • Пользователь не найден → НЕ раскрываем (см. §4.4), но всё равно
     показываем «проверьте почту». Письмо не шлём.
   • Найден → генерим токен, пишем хэш в CabMagicToken (TTL 15м), шлём письмо
     со ссылкой https://clienti.remarka.biz/auth/verify?token=<raw>
3. Клиент кликает ссылку → GET /auth/verify?token=… → POST /api/auth/verify
   • Валидируем: hash существует, не consumed, не expired.
   • Ставим consumedAt, создаём CabSession, ставим httpOnly cookie.
   • Редирект на /projects.
4. Дальше — cookie-сессия; magic-токен использован и мёртв.
```

### 4.2. Генерация и хранение токена

- Raw-токен: `crypto.randomBytes(32).toString('base64url')` (~43 симв.,
  256 бит энтропии).
- В БД — **только** `sha256(raw)` (hex). Raw уходит лишь в письме. Компромат
  БД не даёт войти без перебора SHA-256 от 256-битного секрета (невозможно).
- **TTL 15 минут** (`expiresAt`). **Одноразовость** — `consumedAt`;
  повторный клик по использованной ссылке → `magic_invalid`, показать
  «ссылка уже использована, запросите новую».
- При выдаче нового токена тому же юзеру — старые непогашенные помечаем
  использованными (только последняя ссылка активна).
- Фоновая очистка просроченных: лёгкий `DELETE where expiresAt < now()-1d`
  при каждом N-ном запросе (или крон — но в K1 достаточно ленивой чистки).

### 4.3. Сессия

- **Серверная сессия** (таблица `CabSession`), не чистый JWT — ради
  ревокации (logout, «выйти на всех устройствах», отзыв при инциденте) и
  аудита. Opaque session-токен = `randomBytes(32).base64url`, в БД — SHA-256.
- Cookie: имя `cab_session`, **httpOnly, Secure, SameSite=Lax**, `Path=/`,
  `Max-Age` 7 дней. SameSite=Lax достаточно (magic-ссылка — top-level GET-
  навигация, cookie доедет), при этом защищает от CSRF на сторонние POST.
- Скользящее продление: если `lastSeenAt` старше суток — продлеваем
  `expiresAt` и обновляем `lastSeenAt`.
- Секрет для подписи не нужен (токен opaque, проверяется по хэшу в БД).
  *(Альтернатива — JWT HS256; отклонена: нет отзыва, а для портала с PII
  ревокация обязательна.)*

### 4.4. Rate-limit и защита от перебора

- **Лимит на запрос magic-link:** не чаще 1 письма / 60 сек на e-mail и
  ≤ 5 / час на e-mail; ≤ 20 / час на IP. Хранилище счётчиков — таблица или
  in-memory на процесс (в K1 один инстанс cabinet → in-memory Map с TTL
  достаточно; при масштабировании → Redis).
- **Enumeration-защита:** ответ `/api/auth/request` **одинаков** для
  существующего и несуществующего e-mail («Если такой адрес зарегистрирован,
  мы отправили ссылку»). Тайминг выравниваем (не делать раннего return).
- **Verify:** неверный/просроченный токен → generic-ошибка + аудит
  `magic_invalid`/`magic_expired`. Лимит попыток verify по IP (≤ 30/час).
- **HTTPS-only, HSTS** (Caddy добавляет по умолчанию на TLS-хосте).
- Все события (`magic_requested`, `magic_consumed`, `magic_invalid`,
  `login_ratelimited`, `session_created`, `access_denied`) → `CabAuthAudit`.

### 4.5. Отправка письма — путь SMTP

Реального отправителя в проекте нет, строим с нуля. Варианты:

| Путь | Плюсы | Минусы |
|---|---|---|
| **Resend (регион EU)** | простой API, высокая доставляемость транзакционных писем, EU-хранение (GDPR), быстрый старт, есть DPA | новый вендор + ключ; лимит бесплатного тарифа |
| **SMTP студии** (`remarka.biz` через nodemailer) | ноль новых вендоров, письмо с фирменного домена | нужно настроить SPF/DKIM/DMARC, риск попадания login-писем в спам, ручной мониторинг доставки |
| **Gmail relay** (`alefcom1@gmail.com`) | уже есть | не для транзакционных рассылок, лимиты/блокировки, плохой брендинг |

**Рекомендация:** **Resend (EU-регион)** как основной путь — для писем
входа доставляемость критична (не доехало письмо = клиент не вошёл).
Абстрагировать за интерфейсом `sendMagicLinkEmail()`, чтобы SMTP-студии
подключался как fallback/замена одной функцией. Отправитель:
`no-reply@remarka.biz` (домен верифицировать в Resend: SPF+DKIM).
**Финальный выбор — за владельцем** (§10, вопрос 2).

Письмо: минимальный HTML на фирменных токенах, IT/EN/RU по `CabUser.locale`,
одна кнопка «Войти», текст «ссылка действительна 15 минут», плюс plain-text
альтернатива.

---

## 5. Мультитенантность

### 5.1. Модель доступа

```
cookie cab_session → CabSession (по tokenHash) → userId
  → CabMembership[] по userId → множество allowedClientIds
    → всякий запрос данных: where { clientId: { in: allowedClientIds } }
```

### 5.2. Реализация (server-side хелперы)

- `getSession()` — читает cookie, валидирует `CabSession` (не revoked, не
  expired), возвращает `{ user, allowedClientIds }` или null. Используется
  в каждом Route Handler и серверном компоненте страниц.
- `requireSession()` — как выше, но кидает 401/редирект на `/login`.
- `assertProjectAccess(projectId)` — грузит `CabProject`, проверяет, что
  его `clientId ∈ allowedClientIds`; иначе **404** (не 403 — не раскрываем
  существование чужого ресурса) + аудит `access_denied`.
- **Никаких clientId из клиента как источника истины.** clientId всегда
  выводится из сессии на сервере. Query-параметры/URL используются только
  для выбора среди уже разрешённых.
- Единая точка Prisma-доступа: тонкий слой `cabDb` с функциями
  `listProjects(session)`, `getProject(session, id)`, которые ВСЕГДА
  подмешивают tenant-фильтр — чтобы забыть его было негде.

### 5.3. Аудит

- Все входы/отказы — в `CabAuthAudit` (§3.2, §4.4).
- `access_denied` при попытке дотянуться до чужого проекта — с `userId`,
  `email`, `meta: { projectId }`.
- Ретенция аудита — 12 месяцев (§8).

---

## 6. Каркас UI K1 (mobile-first 390px, фирменный стиль)

### 6.1. Экраны и маршруты

| Маршрут | Тип | Содержимое |
|---|---|---|
| `/login` | публичный | поле e-mail + кнопка «Получить ссылку для входа»; ссылка на смену языка |
| `/check-email` | публичный | «Проверьте почту» + подсказка «письмо действительно 15 минут», кнопка «отправить ещё раз» (с rate-limit) |
| `/auth/verify?token=…` | публичный | серверная проверка токена → ставит cookie → редирект на `/projects`; при ошибке — экран «ссылка недействительна/истекла» + «запросить новую» |
| `/projects` | защищённый | список проектов клиента (карточки: название, стадия-бейдж, дата обновления). Если проектов нет — пустое состояние |
| `/projects/[id]` | защищённый | страница проекта: название, клиент, **горизонтальный степпер стадий** (BRIEF→…→LAUNCH) с подсветкой текущей, **всё readonly в K1** |
| `/logout` | защищённый | POST → ревокация `CabSession` → редирект `/login` |

### 6.2. Дизайн

- Копируем токены и базовые стили из Monitor (`tailwind.config.js`,
  `globals.css`): `carta` фон + бумажная сетка, `inchiostro` текст,
  акцент `oltremare #2440C8`, шрифты Clash Display / General Sans /
  Fragment Mono (eyebrow — mono uppercase). Переиспользуем UI-компоненты
  `components/ui/{button,card,input,badge}.tsx`.
- **Mobile-first от 390px:** одноколоночные карточки, степпер стадий на
  мобиле — вертикальный (переворачивается в горизонтальный от `sm:`),
  тач-таргеты ≥44px, поле e-mail крупное. Проверка на 390/768/1440.
- Бейдж стадии — цветовая карта: активные стадии `oltremare`, пройденные
  `verde #1E7F4F`, будущие `bordo`/`grigio`, `ARCHIVED` — приглушённый.
- Layout: минимальный хедер (лого Remarka + переключатель языка +
  «выйти»), без сайдбара Monitor (у клиента 1–N проектов, навигация плоская).

### 6.3. Тексты интерфейса IT/EN/RU

Строки в словаре `apps/cabinet/src/i18n/{it,en,ru}.ts`, ключ выбирается по
`CabUser.locale` (для публичных экранов до входа — по `Accept-Language`,
дефолт `it`, с ручным переключателем).

| key | it | en | ru |
|---|---|---|---|
| `login.title` | Area clienti Remarka | Remarka client area | Кабинет клиента Remarka |
| `login.emailLabel` | La tua email | Your email | Ваш e-mail |
| `login.submit` | Ricevi il link di accesso | Get login link | Получить ссылку для входа |
| `login.langSwitch` | Lingua | Language | Язык |
| `checkEmail.title` | Controlla la posta | Check your email | Проверьте почту |
| `checkEmail.body` | Se l'indirizzo è registrato, ti abbiamo inviato un link. È valido per 15 minuti. | If the address is registered, we've sent you a link. It's valid for 15 minutes. | Если адрес зарегистрирован, мы отправили ссылку. Она действует 15 минут. |
| `checkEmail.resend` | Invia di nuovo | Resend | Отправить ещё раз |
| `verify.expiredTitle` | Link non valido | Link not valid | Ссылка недействительна |
| `verify.expiredBody` | Il link è scaduto o è già stato usato. Richiedine uno nuovo. | The link has expired or was already used. Request a new one. | Ссылка истекла или уже использована. Запросите новую. |
| `verify.requestNew` | Richiedi un nuovo link | Request a new link | Запросить новую ссылку |
| `projects.title` | I tuoi progetti | Your projects | Ваши проекты |
| `projects.empty` | Non ci sono ancora progetti. | No projects yet. | Проектов пока нет. |
| `projects.updatedAt` | Aggiornato il | Updated | Обновлён |
| `project.stageLabel` | Fase | Stage | Стадия |
| `project.readonlyNote` | Vista di sola lettura (beta) | Read-only view (beta) | Только просмотр (бета) |
| `stage.BRIEF` | Brief | Brief | Бриф |
| `stage.DESIGN` | Design | Design | Дизайн |
| `stage.DEVELOPMENT` | Sviluppo | Development | Разработка |
| `stage.CONTENT` | Contenuti | Content | Наполнение |
| `stage.REVIEW` | Revisione | Review | Приёмка |
| `stage.LAUNCH` | Lancio | Launch | Запуск |
| `stage.MAINTENANCE` | Manutenzione | Maintenance | Поддержка |
| `stage.ARCHIVED` | Archiviato | Archived | Архив |
| `nav.logout` | Esci | Log out | Выйти |
| `email.subject` | Il tuo link di accesso a Remarka | Your Remarka login link | Ваша ссылка для входа в Remarka |
| `email.cta` | Accedi | Log in | Войти |
| `email.ttlNote` | Il link è valido per 15 minuti. | The link is valid for 15 minutes. | Ссылка действует 15 минут. |
| `error.ratelimited` | Troppi tentativi. Riprova tra qualche minuto. | Too many attempts. Try again in a few minutes. | Слишком много попыток. Повторите через несколько минут. |

---

## 7. Деплой

### 7.1. Новый сервис в `docker-compose.prod.yml`

```yaml
  cabinet:
    build:
      context: .
      dockerfile: apps/cabinet/Dockerfile
      args:
        # Публичный origin кабинета (для абсолютных ссылок в письмах и т.п.)
        NEXT_PUBLIC_CABINET_URL: ${CABINET_URL:-https://clienti.remarka.biz}
    restart: unless-stopped
    environment:
      DATABASE_URL: ${DATABASE_URL:?set DATABASE_URL in .env}
      NODE_ENV: production
      CABINET_URL: ${CABINET_URL:-https://clienti.remarka.biz}
      SESSION_TTL_DAYS: 7
      MAGIC_TTL_MINUTES: 15
      # e-mail (Resend, EU) — либо SMTP-переменные при выборе SMTP-пути
      RESEND_API_KEY: ${RESEND_API_KEY:?set RESEND_API_KEY in .env}
      EMAIL_FROM: ${EMAIL_FROM:-no-reply@remarka.biz}
    env_file: .env
    ports: !reset []          # Caddy достаёт как cabinet:3002 по внутренней сети
    depends_on:
      db:
        condition: service_healthy
    deploy:
      resources:
        limits:
          memory: 384M        # Next standalone (SSR + Route Handlers), без Chromium
```

- **Порт 3002** (Dockerfile выставляет `PORT=3002`), не публикуется на хост.
- Prisma-клиент в контейнере кабинета: тот же `packages/db`; при сборке
  `prisma generate`. Схему в БД накатывает **api-контейнер** своим
  `docker-entrypoint.sh` (`db push`) — модели `Cab*` попадут туда же, т.к.
  схема одна. Чтобы не зависеть от порядка, дублировать `db push` в
  entrypoint кабинета НЕ обязательно, но безопасно (push идемпотентен).

### 7.2. Caddyfile — новый site-блок

```caddy
clienti.remarka.biz {
	# НЕТ basic_auth — это публичный вход клиентов (в отличие от lab.*).
	# Приложение само делает auth (magic-link + сессия).
	reverse_proxy cabinet:3002

	# (опц.) базовый rate-limit на публичный вход — если версия Caddy с
	# модулем rate_limit; иначе полагаемся на app-level лимиты (§4.4).

	log {
		output stdout
		format console
	}
}
```

Caddy сам выпустит отдельный TLS-сертификат Let's Encrypt для нового хоста
(порты 80/443 уже открыты). **Предусловие:** DNS-запись
`clienti.remarka.biz → 178.105.192.76` (A-record) должна существовать до
первого старта, иначе ACME-challenge не пройдёт.

### 7.3. Бюджет памяти (4 ГБ box)

| Сервис | Лимит |
|---|---|
| db | 512M |
| redis | 256M |
| api | 512M |
| worker | 1024M |
| web | 512M |
| caddy | 128M |
| **cabinet (новый)** | **384M** |
| **Сумма лимитов** | **3328M** |

Остаётся ~700M на ОС+Docker-демон на 4 ГБ. Приемлемо, **но впритык при
пиках worker (Chromium)**. Подстраховки, если начнёт OOM'ить:
понизить `cabinet` до 320M (Next standalone влезает), либо worker
1024→768M с краул-concurrency=1 (см. `setup.md` → «OOM»). Мониторить
`docker stats` после запуска пилота.

### 7.4. Миграции: `prisma db push` — риски

- Monitor использует `db push` без истории миграций. Добавление моделей
  `Cab*` — **аддитивно** (новые таблицы), риск минимален: `db push` не
  тронет существующие таблицы Monitor, если их модели не менялись.
- **Риск `db push`:** если в схеме окажется случайное изменение
  существующей модели (переименование поля и т. п.), push может выполнить
  **разрушающее** изменение без предупреждения о потере данных так явно,
  как migrate. Поэтому:
  - **Обязательный бэкап ДО push** (`backup.sh` вручную перед деплоем схемы).
  - Diff схемы ревьюить глазами; в K1 менять ТОЛЬКО добавлять `Cab*`.
  - **Рекомендация на будущее:** для кабинета имеет смысл перейти на
    `prisma migrate` (версионные миграции), но это меняет общий workflow
    БД Monitor — согласовать отдельно (не в объёме K1). В K1 остаёмся на
    `db push` ради совместимости.

### 7.5. Бэкап

- Кабинет живёт в **той же БД `sitelens`** → существующий
  `deploy/remarka-lab/backup.sh` (pg_dump всей БД) **уже покрывает** таблицы
  `cab_*`. Отдельный бэкап не нужен.
- **НО:** в дампе теперь **персональные данные** (e-mail, IP, user-agent).
  Следствия: (1) офсайт-копия (`OFFSITE_HOST`) должна ехать в ЕС и на
  зашифрованный носитель; (2) в идеале — шифровать дамп (`gpg`) перед
  отправкой офсайт; (3) отразить в реестре обработки (§8). Дополнить
  комментарий в `backup.sh` про PII (правки самого скрипта в K1 не
  требуются, покрытие есть).

### 7.6. `.env.prod.template` — добавить

```
# ── Кабинет заказчика (K1) ───────────────────────────────────────────────────
CABINET_URL=https://clienti.remarka.biz
RESEND_API_KEY=ВСТАВИТЬ-КЛЮЧ-RESEND        # (или SMTP_* при SMTP-пути)
EMAIL_FROM=no-reply@remarka.biz
SESSION_TTL_DAYS=7
MAGIC_TTL_MINUTES=15
```

---

## 8. Безопасность и GDPR

- **Какие ПД храним:** e-mail (обяз.), имя (опц.), `locale`, IP и user-agent
  в `CabSession`/`CabAuthAudit`, хэши токенов (не сами токены). Название
  компании и P.IVA — данные юрлица (для K2-счетов), не спец-категории.
- **Где:** Hetzner (Германия, ЕС) + e-mail-провайдер в EU-регионе (Resend
  EU). Никаких трансферов за пределы ЕЭЗ. С провайдером письма — **DPA**
  (data processing agreement).
- **Правовое основание:** исполнение договора (клиенту студии оказывается
  услуга; кабинет — инструмент её оказания). Auth-cookie —
  **строго необходимый**, баннер согласия на cookie для него не требуется.
- **Минимизация:** не собираем ничего сверх нужного для входа и связи.
  Аналитику/трекеры в кабинет не ставим (или только cookieless, если
  захочется).
- **Ретенция:**
  - magic-токены — удаляются после истечения (ленивая чистка, §4.2);
  - сессии — по TTL 7 дней + ревокация при logout;
  - `CabAuthAudit` — 12 месяцев, затем удаление (крон/ленивая чистка);
  - учётка клиента — пока действует сотрудничество; по запросу на удаление
    — cascade-delete `CabClient`/`CabUser` (§3.2).
- **Права субъекта:** доступ/удаление реализуемы (экспорт — SQL по `userId`,
  удаление — cascade). В K1 — вручную по запросу (self-service — задел K2/K3).
- **Privacy policy:** дополнить политику remarka.biz разделом про кабинет:
  какие данные (e-mail, имя, логи входа), цель (доступ к área clienti),
  срок, обработчик писем (Resend), права. Ссылка на политику — в футере
  `/login`.
- **Технич. меры:** HTTPS+HSTS, httpOnly/Secure/SameSite cookie, хэш-
  хранение токенов, rate-limit, аудит, tenant-scoping, бэкап (с учётом PII).

---

## 9. Этапность реализации для Sonnet-агента

Один worktree, отдельная ветка. Каждый этап: `pnpm typecheck` зелёный,
Playwright-скрины 390/1440 где есть UI, атомарный коммит **без секретов и
без ID моделей** (правило `docs/piano-implementazione-fase-A.md` §0).
Пилот — на staging-данных (2 фейковых `CabClient`), не на реальных клиентах
до приёмки.

| Этап | Состав | Файлы |
|---|---|---|
| **K1-1 Схема БД** | Добавить модели `Cab*` + enum `CabProjectStage` в схему; `prisma generate`; проверить `db push` на локальной БД (аддитивность, Monitor-таблицы не тронуты); сид-скрипт: 2 `CabClient`, 3 `CabUser` (it/en/ru), membership'ы, по 1–2 `CabProject` | `packages/db/prisma/schema.prisma`, `packages/db/prisma/seed-cabinet.ts` |
| **K1-2 Каркас app** | Новый `apps/cabinet` (Next 14 App Router, standalone); скопировать tailwind-токены + globals + UI-компоненты из web; `next.config.js` (`output: standalone`, порт 3002); Dockerfile по образцу web; подключить `@sitelens/db`; i18n-словари it/en/ru (§6.3) | `apps/cabinet/**`, `pnpm-workspace.yaml` (уже покрывает `apps/*`) |
| **K1-3 Auth-ядро** | `lib/tokens.ts` (генерация/хэш), `lib/session.ts` (`getSession/requireSession`), `lib/email.ts` (`sendMagicLinkEmail`, Resend + абстракция), rate-limit (§4.4); Route Handlers `POST /api/auth/request`, `POST /api/auth/verify`, `POST /api/auth/logout`; запись `CabAuthAudit`; unit-стабы (нет юзера→generic-ответ+нет письма, истёкший токен→invalid, повторный клик→invalid, rate-limit→429) | `apps/cabinet/src/lib/{tokens,session,email,ratelimit}.ts`, `apps/cabinet/src/app/api/auth/**` |
| **K1-4 Tenant-слой** | `lib/cab-db.ts` (`listProjects/getProject` с обязательным tenant-фильтром), `assertProjectAccess` (404 на чужое + аудит); тест: юзер A не видит проект клиента B (404) | `apps/cabinet/src/lib/cab-db.ts` |
| **K1-5 UI** | Экраны `/login`, `/check-email`, `/auth/verify`, `/projects`, `/projects/[id]`, `/logout`; степпер стадий; пустые/ошибочные состояния; переключатель языка; mobile-first 390px | `apps/cabinet/src/app/**`, `apps/cabinet/src/components/**` |
| **K1-6 Деплой-конфиг** | Сервис `cabinet` в `docker-compose.prod.yml` (лимит 384M, `ports: !reset []`); site-блок `clienti.remarka.biz` в Caddyfile (без basic_auth); `.env.prod.template` +переменные; комментарий про PII в `backup.sh`; шаг про DNS A-record и `db push`-бэкап в `setup.md` | `deploy/remarka-lab/{docker-compose.prod.yml,Caddyfile,.env.prod.template,setup.md,backup.sh}` |
| **K1-7 QA/сдача** | Все стабы зелёные; Playwright: полный happy-path (login→письмо-мок→verify→projects→project→logout) + negative (истёкший токен, чужой проект→404, rate-limit); скрины 390/1440; проверка cookie-флагов (httpOnly/Secure/SameSite) и что raw-токен нигде не логируется; деплой-чеклист владельцу | — |

### 9.1. Чек-лист приёмки

- `pnpm --filter @sitelens/cabinet typecheck` = 0 ошибок; `prisma generate` ок.
- `db push` на копии прод-БД: создаёт только таблицы `cab_*`, `git diff`
  схемы — только добавления, ни одно поле Monitor не изменено; бэкап снят ДО.
- Happy-path Playwright: `/login` → (мок письма даёт raw-токен) →
  `/auth/verify` ставит cookie → `/projects` показывает только проекты
  своего клиента → `/projects/[id]` рисует степпер (readonly) → `/logout`
  чистит сессию. Console errors = 0 на 390 и 1440.
- Negative: истёкший/использованный токен → экран «недействительна»;
  запрос на несуществующий e-mail → тот же «проверьте почту», письмо НЕ
  ушло; попытка открыть чужой `projectId` → 404 + запись `access_denied`;
  >5 запросов/час на e-mail → 429 + `login_ratelimited`.
- Безопасность: cookie `cab_session` — httpOnly+Secure+SameSite=Lax;
  raw magic-токен и session-токен НЕ встречаются в логах/HTML (grep по
  выводу); в БД только хэши (`tokenHash`); секреты не в git.
- i18n: все три языка (it/en/ru) отрисованы, письмо на языке `locale`.
- Деплой: `clienti.remarka.biz` отдаёт `/login` БЕЗ basic_auth; TLS-серт
  выпущен; `lab.remarka.biz` по-прежнему за basic_auth и не задет;
  `docker stats` — cabinet в пределах лимита, суммарно нет OOM.
- Дан **полный копипаст-блок команд для сервера** (правило CLAUDE.md):
  бэкап → git pull → `db push` → build+up сервиса cabinet → проверка
  `curl https://clienti.remarka.biz/login` → логи.

---

## 10. Оценка объёма и открытые вопросы владельцу

### 10.1. Оценка объёма (K1)

- Новый Next-app с нуля, но на готовых токенах и с одним типом данных
  (readonly) — **средний объём**. Ориентир для Sonnet-конвейера: этапы
  K1-1…K1-7, из них auth-ядро (K1-3) и tenant-слой (K1-4) — самые
  ответственные (безопасность), UI (K1-5) — самый объёмный по файлам, но
  простой (readonly, нет форм кроме одного поля e-mail).
- Внешние зависимости, добавляемые в кабинет: `resend` (или `nodemailer`),
  `jose`/встроенный `crypto` (для хэшей достаточно `node:crypto`). Prisma,
  Next, tailwind — уже в монорепо.
- Инфра-дельта: +1 контейнер, +1 Caddy-блок, +1 DNS-запись, +1 e-mail-
  вендор (ключ). Прод-память впритык, но влезает.

### 10.2. Открытые вопросы

1. **Поддомен.** Подтвердить `clienti.remarka.biz` (предложение плана) и
   **создать A-запись** на `178.105.192.76` ДО деплоя (нужна для TLS).
   Альтернативы: `area.remarka.biz`, `clienti.remarka.biz` — решение за
   владельцем.
2. **E-mail-провайдер для писем входа.** Рекомендация — **Resend (EU)**
   ради доставляемости и GDPR; альтернатива — SMTP студии (`remarka.biz`,
   нужны SPF/DKIM/DMARC). Что выбираем? Кто даёт ключ/доступ? Адрес
   отправителя `no-reply@remarka.biz` — ок?
3. **Пилотные клиенты (1–2).** Кого заводим первыми (реальные e-mail,
   названия компаний, языки интерфейса)? Кабинет создаёт учётки вручную
   (в K1 нет самрегистрации) — нужен список от владельца.
4. **Тексты/юр.** Кто финализирует IT/EN/RU-строки (черновик в §6.3 готов)
   и раздел privacy policy про кабинет? Нужен ли DPA с Resend (подписать).
5. **Стадии проекта.** Список `CabProjectStage` (§3.2) — предложен 8-шаговый
   (BRIEF…ARCHIVED). Соответствует ли реальному процессу студии? Правки?
6. **Роли.** В K1 все `viewer` (readonly). Нужны ли уже в K1 несколько
   пользователей на одного клиента (напр. клиент + его подрядчик)? На
   модель `CabMembership` это заложено, вопрос — заводить ли сразу.
7. **Миграции vs db push.** Оставляем `db push` (совместимость с Monitor)
   или для кабинета вводим версионные `prisma migrate`? В K1 предлагаю
   `db push`; решение о переходе — отдельно.

---

## Решения владельца (16.07.2026, после ревью спеки)

- **Отправитель писем: Brevo** (EU, GDPR). Транзакционные письма magic-link
  через Brevo API (HTTPS из контейнера кабинета; ключ в .env, не в репо).
  Перед запуском: в Brevo аутентифицировать домен remarka.biz (SPF/DKIM/DMARC
  DNS-записи), отправитель `no-reply@remarka.biz`. Бесплатного тарифа
  (300 писем/день) для magic-link более чем достаточно.
- **Поддомен: `cab.remarka.biz`** (предложение владельца; см. оговорку ниже).
  A-запись на 178.105.192.76 создать до деплоя (нужна для выпуска TLS).
  Оговорка оркестратора: для итальянской аудитории «CAB» читается как
  банковский код (Codice di Avviamento Bancario) — если смутит клиентов,
  безболезненно переименуем до запуска (стандарт рынка — «area clienti»).
