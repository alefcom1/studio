# Кабинет заказчика Remarka — этап K2: детальная спецификация

> Задача #62 в трекере. Этап K2 «MVP-фичи»: согласования (approve/comment),
> обмен файлами, счета (показ), тикеты, архив, staff-режим студии,
> e-mail-уведомления. Строится ПОВЕРХ K1 (`docs/piano-cabinet-k1.md`) —
> ветка `claude/cabinet-k2` от `claude/cabinet-k1` в репо
> `alefcom1/1russian.com`. Деплой-конфиг — `deploy/remarka-lab/` в studio.
>
> Решения владельца (16.07.2026): staff-режим — В КАБИНЕТЕ (не CLI);
> e-mail-уведомления — ВКЛЮЧЕНЫ в K2 (не отложены в K3).

---

## 0. Резюме для оркестратора (TL;DR)

1. **Тот же контейнер `apps/cabinet`** — ни одного нового сервиса. Файлы —
   на **bind-mount `./cabinet-files`** хоста (не в БД, не в S3), отдача
   ТОЛЬКО через авторизованный Route Handler со стримингом и tenant-чеком.
2. **Staff-режим**: `CabUser.isStaff` (Boolean). Staff входит тем же
   magic-link'ом, видит ВСЕХ клиентов, управляет стадиями/файлами/
   согласованиями/счетами/тикетами через раздел `/staff/**`. Клиентская
   изоляция НЕ ослабляется: `requireStaff()` — отдельный guard, обычная
   сессия в `/staff/**` получает 404.
3. **Права клиента**: `CabMembership.role` начинает работать —
   `owner` может approve/request-changes, `viewer` — только смотреть и
   писать в тикеты. В сидах пилота все клиенты — `owner`.
4. **Новые модели** (аддитивно, префикс `Cab*`): `CabFile`, `CabApproval`,
   `CabInvoice`, `CabTicket`, `CabTicketMessage` + поле `isStaff` в
   `CabUser` + значение роли. Monitor-таблицы не трогаем (`git diff -w`
   схемы = только добавления).
5. **Уведомления** — синхронные транзакционные письма через уже готовый
   Brevo-слой K1 (`lib/email.ts`), fire-and-forget с логом ошибки (письмо
   упало ≠ действие упало). Без очередей/Redis — объёмы пилота копеечные.
6. **Архив** — НЕ новая модель: стадия `ARCHIVED` + табы «Attivi/Archivio»
   на `/projects` + staff-кнопка «В архив».

Полный чек-лист приёмки — §9; деплой-дельта — §7 (пересборка cabinet,
+1 bind-mount, +2 env-переменные, backup файлов).

---

## 1. Что уже есть после K1 (реюз)

- Auth: magic-link + серверные сессии (`CabSession`), `requireSession()`,
  `assertProjectAccess()` (404 на чужое + аудит `access_denied`).
- Мультитенантность: `allowedClientIds` из membership'ов; слой `cab-db.ts`,
  где tenant-фильтр подмешивается всегда.
- E-mail: `lib/email.ts` — Brevo API, dev-режим при пустом ключе
  (ссылка/письмо в stdout). Шаблон на фирменных токенах, IT/EN/RU.
- UI-кит: токены carta/inchiostro/oltremare, компоненты
  `ui/{button,card,input,badge}`, степпер стадий, i18n-словари it/en/ru.
- Rate-limit (in-memory), аудит `CabAuthAudit`, сид-скрипт.
- Деплой: сервис `cabinet` (384M) в docker-compose.prod, Caddy-блок
  `cab.remarka.biz` без basic_auth.

K2 ничего из этого не переписывает — только расширяет.

### 1.1. Полировка K1 (входит в объём K2)

1. **Степпер**: на ≥sm подписи «Разработка»/«Наполнение» слипаются —
   дать подписям равную ширину колонки/перенос, проверить все 3 языка
   на 390/768/1440.
2. **Cookie при скользящем продлении**: при продлении `expiresAt` в БД
   переустанавливать и cookie `cab_session` с новым `Max-Age` (сейчас
   браузерный cookie умирает по исходным 7 дням).

---

## 2. Модель данных (аддитивные изменения схемы)

```prisma
// ─── Кабинет заказчика (K2) ──────────────────────────────────────────────────

// CabUser: + isStaff Boolean @default(false)
//   Staff видит всех клиентов и получает доступ к /staff/**.
//   Membership'ы для staff не нужны (доступ по флагу).

// CabMembership.role: 'viewer' | 'owner'
//   owner  — может approve / request changes по согласованиям;
//   viewer — read-only по согласованиям, но может писать в тикеты.

model CabFile {
  id         String   @id @default(cuid())
  clientId   String                       // денормализовано для tenant-фильтра
  projectId  String?
  project    CabProject? @relation(fields: [projectId], references: [id], onDelete: Cascade)
  uploaderId String                       // CabUser.id (staff или клиент)
  kind       String                       // deliverable | client_upload | invoice
  fileName   String                       // оригинальное имя (сан-но, для показа)
  mimeType   String
  sizeBytes  Int
  storageKey String   @unique             // случайное имя на диске: <cuid>.<ext-из-allowlist>
  createdAt  DateTime @default(now())

  approvals  CabApproval[]
  invoices   CabInvoice[]

  @@index([clientId])
  @@index([projectId])
  @@map("cab_file")
}

model CabApproval {
  id              String    @id @default(cuid())
  projectId       String
  project         CabProject @relation(fields: [projectId], references: [id], onDelete: Cascade)
  title           String                   // «Макет главной v2», «Тексты раздела Servizi»
  note            String?                  // сопроводительный текст студии
  fileId          String?                  // приложенный макет/док (опц. — может быть ссылка в note)
  file            CabFile?  @relation(fields: [fileId], references: [id], onDelete: SetNull)
  status          String    @default("pending") // pending | approved | changes_requested
  decisionComment String?                  // комментарий клиента при решении
  decidedById     String?                  // CabUser.id клиента
  decidedAt       DateTime?
  createdById     String                   // CabUser.id staff
  createdAt       DateTime  @default(now())

  @@index([projectId, status])
  @@map("cab_approval")
}

model CabInvoice {
  id          String    @id @default(cuid())
  clientId    String
  client      CabClient @relation(fields: [clientId], references: [id], onDelete: Cascade)
  projectId   String?                      // счёт может быть не привязан к проекту
  number      String                       // номер счёта студии (fattura)
  issueDate   DateTime
  dueDate     DateTime?
  amountCents Int                          // в центах, только показ
  currency    String    @default("EUR")
  status      String    @default("issued") // issued | paid | overdue
  method      String?                      // bonifico | SDI — справочно
  fileId      String?                      // PDF счёта
  file        CabFile?  @relation(fields: [fileId], references: [id], onDelete: SetNull)
  createdAt   DateTime  @default(now())
  updatedAt   DateTime  @updatedAt

  @@index([clientId, status])
  @@map("cab_invoice")
}

model CabTicket {
  id          String    @id @default(cuid())
  clientId    String
  client      CabClient @relation(fields: [clientId], references: [id], onDelete: Cascade)
  projectId   String?                      // вопрос может быть общий, не по проекту
  subject     String
  status      String    @default("open")   // open | answered | closed
  createdById String                       // CabUser.id (клиент ИЛИ staff)
  createdAt   DateTime  @default(now())
  updatedAt   DateTime  @updatedAt

  messages    CabTicketMessage[]

  @@index([clientId, status])
  @@map("cab_ticket")
}

model CabTicketMessage {
  id        String    @id @default(cuid())
  ticketId  String
  ticket    CabTicket @relation(fields: [ticketId], references: [id], onDelete: Cascade)
  authorId  String                         // CabUser.id
  body      String                         // plain text, рендер с экранированием
  createdAt DateTime  @default(now())

  @@index([ticketId])
  @@map("cab_ticket_message")
}
```

Замечания:
- `CabFile.clientId` денормализован сознательно: tenant-фильтр файлов
  не должен зависеть от join'а (файл без проекта — например PDF счёта —
  всё равно принадлежит клиенту).
- Статусы — строки, не enum'ы: `db push` на общей с Monitor схеме — новые
  enum'ы добавлять можно, но строки проще эволюционировать без миграций
  (урок K1: enum `CabProjectStage` оставляем как есть, новые не плодим).
- Обратные relation-поля добавить в `CabClient`/`CabProject`/`CabUser`
  по требованию Prisma — это тоже аддитивно.

---

## 3. Файлы: хранение и отдача (самая чувствительная часть K2)

### 3.1. Хранение

- **Bind-mount `./cabinet-files:/data/cabinet-files`** в сервисе cabinet
  (docker-compose.prod). Не volume — чтобы backup.sh мог взять tar без
  докер-эквилибристики. Внутри — плоская структура `<storageKey>`,
  подкаталог по клиенту НЕ нужен (ключ случайный, метаданные в БД).
- `storageKey = cuid() + '.' + ext`, где ext — ИЗ ALLOWLIST по факту
  валидации, НЕ из имени файла пользователя. Оригинальное имя — только
  поле БД для показа (санитизация: обрезать до 200 симв., убрать
  управляющие символы).
- Env: `CABINET_FILES_DIR=/data/cabinet-files` (dev-дефолт —
  `.data/cabinet-files` в репо, в .gitignore).

### 3.2. Ограничения загрузки

- **Max 25 MB** на файл (multipart через `request.formData()`; в
  route-хендлере проверять `Content-Length` ДО чтения тела и size по
  факту записи).
- **Allowlist** (mime + расширение согласованы): pdf, png, jpg/jpeg, webp,
  svg — НЕТ (XSS при inline-отдаче), zip, docx, xlsx, pptx, txt.
  Несовпадение mime↔ext → отказ.
- Rate-limit: ≤ 30 загрузок/час на пользователя (in-memory, как в K1).
- Квота на клиента: ≤ 500 MB суммарно (проверка по `sum(sizeBytes)`),
  превышение → понятная ошибка.

### 3.3. Отдача

- ТОЛЬКО `GET /api/files/[id]` под сессией: файл → `clientId` →
  проверка `clientId ∈ allowedClientIds` (или staff) → стрим с диска.
  Чужой/несуществующий id → **404** + аудит `access_denied`.
- Заголовки: `Content-Disposition: attachment; filename="<сан-имя>"`
  (attachment по умолчанию — не рендерим пользовательский контент в
  origin кабинета; для pdf/изображений допустим `inline` — решить в
  реализации, но тогда `X-Content-Type-Options: nosniff` обязателен).
- Никакого `next/static`/public-каталога для пользовательских файлов.
- Путь на диске строится ТОЛЬКО как `join(FILES_DIR, row.storageKey)` —
  storageKey из БД, не из URL (path traversal исключён по построению).

---

## 4. Фичи клиентской стороны

### 4.1. Согласования (`/projects/[id]` — блок «Da approvare» + история)

- Список согласований проекта: pending сверху (жёлтый бейдж), затем
  история (approved — verde, changes_requested — терракота) с датами и
  комментариями.
- Карточка: title, note, ссылка на файл (если есть), кнопки для `owner`:
  **«Approva»** и **«Richiedi modifiche»** (вторая требует комментарий,
  textarea обязательна). `viewer` видит статус без кнопок.
- POST `/api/approvals/[id]/decide` — `{ decision, comment? }`;
  идемпотентность: решение по уже решённому → 409; tenant-чек через
  проект; роль owner обязательна (403 → на UI кнопок и так нет, но
  сервер проверяет сам).
- После решения — уведомление staff (§6).

### 4.2. Файлы (`/projects/[id]` — вкладка/блок «File»)

- Список файлов проекта (kind=deliverable от студии + client_upload):
  имя, размер, дата, кто загрузил (Studio/имя клиента), кнопка скачать.
- Клиент МОЖЕТ загружать (kind=client_upload) — материалы, логотипы,
  тексты. Форма: input file + submit, ошибки лимитов — человеческие.

### 4.3. Счета (`/invoices` — отдельная страница уровня клиента)

- Таблица: номер, дата, сумма (формат €1.234,56 по locale), статус-бейдж
  (issued — oltremare, paid — verde, overdue — терракота), метод
  (bonifico/SDI), PDF-скачивание (через /api/files/).
- ТОЛЬКО показ: никаких оплат/интеграций. Пустое состояние — «счетов нет».
- В хедере — пункт меню «Fatture / Invoices / Счета».

### 4.4. Тикеты (`/tickets` + `/tickets/[id]`)

- Список тикетов клиента: тема, статус (open/answered/closed), дата
  обновления. Кнопка «Nuova richiesta» → форма (тема + сообщение,
  опционально привязка к проекту из своих).
- Страница тикета: лента сообщений (клиент справа, студия слева, имена
  и даты), форма ответа. `closed` — форма скрыта, кнопка «Riapri»
  (переводит в open).
- Plain text, рендер с экранированием (никакого HTML от пользователя),
  максимум 5000 симв./сообщение, rate-limit ≤ 20 сообщений/час.
- Статус-машина: клиент написал → open; staff ответил → answered;
  закрывает — staff (или клиент свой тикет).

### 4.5. Архив (`/projects`)

- Табы «Attivi» / «Archivio»: активные — stage ≠ ARCHIVED (дефолт),
  архив — stage = ARCHIVED. Пустые состояния для обоих.
- Архивный проект открывается readonly: согласования/файлы видны,
  загрузка и решения отключены.

---

## 5. Staff-режим (`/staff/**`)

### 5.1. Доступ

- `CabUser.isStaff = true` — заводится ТОЛЬКО сидом/скриптом
  (`seed -- --staff --email studio@remarka.biz --locale ru`), никакой
  самоэскалации через API.
- `requireStaff()`: `requireSession()` + проверка флага; не-staff на
  `/staff/**` и staff-API → **404** (не раскрываем существование раздела).
- Staff-сессия видит все клиенты БЕЗ membership'ов: в `cab-db.ts`
  добавить staff-ветку (`isStaff ? {} : { clientId: { in: allowed } }`)
  строго в ОДНОМ месте — хелпере тенант-фильтра, не размазывать по коду.

### 5.2. Экраны

| Маршрут | Содержимое |
|---|---|
| `/staff` | дашборд: счётчики (pending-согласования, open-тикеты по всем клиентам), список клиентов |
| `/staff/clients/[id]` | клиент: проекты, участники (кто owner/viewer), счета, тикеты |
| `/staff/projects/[id]` | проект: смена стадии (select+save), файлы (загрузка deliverable, удаление своего файла), создание согласования (title+note+файл), список согласований |
| `/staff/invoices/new` (+список на клиенте) | форма счёта: клиент, проект (опц.), номер, даты, сумма, метод, PDF; смена статуса issued→paid/overdue |
| `/staff/tickets` | все тикеты (open сверху), ответ, закрытие |

- Тот же лейаут/токены, но с бейджем «STAFF» в хедере, чтобы владелец
  всегда видел, в каком режиме находится.
- Mobile-first необязателен для staff (владелец за десктопом), но не
  ломать 390px совсем (просто вертикальная раскладка).
- Смена стадии проекта — уведомление клиенту (§6) и это закрывает
  фичу №1 плана («статус проекта с этапами» становится управляемым).

### 5.3. Безопасность staff-режима

- Все staff-мутации — POST/DELETE Route Handlers c `requireStaff()`.
- Удаление файлов: только staff, и только файлы kind=deliverable/invoice
  (client_upload не трогаем — это данные клиента); удаление = БД-запись +
  unlink с диска.
- Аудит: staff-мутации (стадия, счёт, удаление файла) писать в
  `CabAuthAudit` с event=`staff_action`, meta `{ action, entityId }`.

---

## 6. E-mail-уведомления (Brevo, слой K1)

| Событие | Кому | Когда |
|---|---|---|
| `approval_created` | всем участникам клиента (по locale каждого) | staff создал согласование |
| `approval_decided` | staff (`STAFF_NOTIFY_EMAIL`) | клиент решил (approve/changes) |
| `stage_changed` | участникам клиента | staff сменил стадию |
| `invoice_created` | участникам клиента | staff выставил счёт |
| `ticket_created` | staff | клиент создал тикет |
| `ticket_replied` | «другой стороне» (клиент↔staff) | новое сообщение в тикете |
| `file_uploaded` (kind=deliverable) | участникам клиента | staff загрузил файл БЕЗ согласования (например, готовые материалы) |

Правила:
- **Fire-and-forget**: отправка в `after()`/`.catch(log)` — сбой Brevo НЕ
  роняет действие и НЕ показывает ошибку пользователю (последствие: письмо
  может не дойти — приемлемо, состояние всегда видно в кабинете).
- Шаблон — тот же фирменный каркас письма из K1; тело: 1 фраза «что
  случилось» + кнопка «Apri il progetto» с прямой ссылкой (`CABINET_URL` +
  путь). Никаких данных сверх необходимого (в письме НЕ дублируем
  содержимое тикета целиком — максимум первые 200 симв.).
- Язык — `CabUser.locale` получателя; для staff — locale staff-юзера.
- Дедупликация не нужна (события дискретные), но при массовых операциях
  сида письма НЕ шлются (guard: сид ставит env `CABINET_SEED=1`).
- Env: `STAFF_NOTIFY_EMAIL` (дефолт — e-mail первого isStaff-юзера, если
  переменная пуста).

---

## 7. Деплой-дельта (без новых контейнеров)

1. `docker-compose.prod.yml`, сервис cabinet:
   - `volumes: - ./cabinet-files:/data/cabinet-files`
   - env: `CABINET_FILES_DIR=/data/cabinet-files`, `STAFF_NOTIFY_EMAIL=…`
   - лимит памяти 384M НЕ трогаем (стриминг файлов не держит их в памяти).
2. `.env.prod.template`: + `STAFF_NOTIFY_EMAIL=info@remarka.biz` (пример).
3. `backup.sh`: после pg_dump — `tar -czf …/cabinet-files-<дата>.tar.gz
   -C <корень> cabinet-files` (файлы клиентов теперь тоже данные;
   ротация та же, что у дампов).
4. `setup.md`: раздел «Cabinet» дополнить: создание каталога
   `mkdir -p cabinet-files`, права (владелец — uid процесса cabinet),
   env, заведение staff-юзера сидом, `db push` (аддитивный) с бэкапом ДО.
5. Caddy: без изменений (лимит тела запроса Caddy по умолчанию не режет;
   лимит 25MB обеспечивает приложение).

---

## 8. i18n — ключевые строки (черновик, агент расширяет по образцу K1 §6.3)

| key | it | en | ru |
|---|---|---|---|
| `nav.invoices` | Fatture | Invoices | Счета |
| `nav.tickets` | Richieste | Requests | Вопросы |
| `projects.tabActive` | Attivi | Active | Активные |
| `projects.tabArchive` | Archivio | Archive | Архив |
| `approvals.title` | Da approvare | To approve | На согласовании |
| `approvals.approve` | Approva | Approve | Согласовать |
| `approvals.requestChanges` | Richiedi modifiche | Request changes | Запросить правки |
| `approvals.commentRequired` | Descrivi le modifiche richieste | Describe the changes you need | Опишите, какие правки нужны |
| `approvals.approved` | Approvato | Approved | Согласовано |
| `approvals.changesRequested` | Modifiche richieste | Changes requested | Запрошены правки |
| `files.title` | File | Files | Файлы |
| `files.upload` | Carica un file | Upload a file | Загрузить файл |
| `files.byStudio` | Studio | Studio | Студия |
| `invoices.status.issued` | Emessa | Issued | Выставлен |
| `invoices.status.paid` | Pagata | Paid | Оплачен |
| `invoices.status.overdue` | Scaduta | Overdue | Просрочен |
| `tickets.new` | Nuova richiesta | New request | Новый вопрос |
| `tickets.status.open` | Aperta | Open | Открыт |
| `tickets.status.answered` | Risposta ricevuta | Answered | Есть ответ |
| `tickets.status.closed` | Chiusa | Closed | Закрыт |
| `tickets.reply` | Rispondi | Reply | Ответить |
| `email.approvalCreated.subject` | Nuovo materiale da approvare — {project} | New item to approve — {project} | Новый материал на согласование — {project} |
| `email.stageChanged.subject` | Il tuo progetto è passato alla fase «{stage}» | Your project moved to “{stage}” | Ваш проект перешёл на стадию «{stage}» |
| `email.invoiceCreated.subject` | Nuova fattura {number} | New invoice {number} | Новый счёт {number} |
| `email.ticketReplied.subject` | Risposta alla tua richiesta «{subject}» | Reply to your request “{subject}” | Ответ на ваш вопрос «{subject}» |

Тон: вежливый деловой итальянский (Lei), без канцелярита; EN — нейтральный;
RU — на «вы».

---

## 9. Этапность и чек-лист приёмки

### 9.1. Этапы для Sonnet-агента

Каждый этап: `pnpm typecheck` зелёный, атомарный коммит без ID моделей.

| Этап | Состав |
|---|---|
| **K2-1 Схема + полировка K1** | Модели §2 + `isStaff`; `prisma validate/generate`; сид-фикстуры K2 (файлы-заглушки, согласования во всех статусах, счета, тикеты, staff-юзер); фиксы §1.1 (степпер, cookie) |
| **K2-2 Файловый слой** | storage-модуль (валидация, allowlist, квоты, запись/unlink), `GET /api/files/[id]` со стримом и tenant-чеком, upload-хендлеры |
| **K2-3 Клиент: согласования + файлы** | UI на `/projects/[id]`, decide-эндпоинт, роль owner/viewer |
| **K2-4 Клиент: счета + тикеты + архив** | `/invoices`, `/tickets[.id]`, табы архива, readonly архивного проекта |
| **K2-5 Staff-режим** | `requireStaff()`, staff-ветка tenant-фильтра (одно место!), экраны §5.2, staff-мутации + аудит |
| **K2-6 Уведомления** | таблица §6, fire-and-forget, guard сида, шаблоны IT/EN/RU |
| **K2-7 Деплой-дельта** | studio: compose/env/backup/setup (§7) |
| **K2-8 QA/сдача** | тесты + живой интеграционный прогон + Playwright-скрины + отчёт |

### 9.2. Чек-лист приёмки

- `git diff -w` схемы: ТОЛЬКО добавления; Monitor-модели не тронуты;
  `apps/web|api|worker` — 0 изменений.
- Юнит: allowlist/квоты/лимиты файлов; статус-машина тикета;
  идемпотентность decide (повтор → 409); role-гейт (viewer не может
  approve); staff-гейт (не-staff → 404 на /staff и staff-API).
- **Живой интеграционный прогон на реальном Postgres** (как в K1),
  два клиента + staff: staff создаёт согласование с файлом → клиент A
  получает (dev-лог письма) → approve → staff видит; клиент B НЕ видит
  ни файла (404 на /api/files/), ни согласования; клиент создаёт тикет →
  staff отвечает → статус answered → письмо клиенту (dev-лог); staff
  выставляет счёт с PDF → клиент видит и скачивает; смена стадии →
  письмо; архивирование → проект уезжает в таб «Archivio», мутации
  отключены. Path traversal: запрос файла с подделанным id → 404.
- Загрузка: файл 26MB → отказ до чтения тела; exe/svg → отказ;
  корректные pdf/png/zip — ок; имя файла с `../../` и юникод-мусором →
  сохранён под storageKey, показ санитизирован.
- Raw-токены/секреты не в логах; письма НЕ шлются при сиде.
- Playwright 390/1440: `/projects/[id]` с согласованиями и файлами,
  `/invoices`, `/tickets/[id]`, `/staff` и `/staff/projects/[id]`;
  0 console errors; степпер-подписи не слипаются (фикс §1.1 виден).
- Полный копипаст-блок команд деплоя (CLAUDE.md-правило): бэкап →
  git pull обеих веток → mkdir cabinet-files → env → build+up → curl →
  сид staff-юзера.

---

## 10. Вне объёма K2 (фиксируем границу)

- Оплата счетов онлайн, интеграция SDI/биллинг — не делаем (показ only).
- Метрики Monitor в кабинете, PDF-отчёты — K3.
- Self-service GDPR-экспорт/удаление — K3 (вручную по запросу, как в K1).
- Версионирование макетов в согласованиях (v1/v2 diff) — при
  необходимости после пилота; сейчас новая версия = новое согласование.
- Push/веб-уведомления, дайджесты — нет, только транзакционные письма.
