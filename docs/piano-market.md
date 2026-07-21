# Remarka Market — ТЗ v2: Telegram Mini App на нашей инфраструктуре

> Замена исходного ТЗ «для Codex» (remarkamarketcodexspec.md). Ключевые
> решения владельца (20.07.2026): не строить с нуля — встраивать в
> существующую платформу; на первом плане бесплатные инструменты; платежи
> пока только Telegram Stars и Crypto Pay (Криптобот); WhatsApp — потом,
> но ядро строить канало-независимым.

## 0. Правила (обязательны, как во всех агентских этапах)

- Действуют правила `docs/piano-implementazione-fase-A.md` §0: атомарные
  коммиты без ID моделей, протокол верификации (typecheck + build + тесты +
  runtime-прогон ПЕРЕД отчётом), никаких недоделок под видом готового.
- Принцип продукта: **«бесплатное делает ИИ, платное делают люди»**. Каждый
  ИИ-результат помечен бейджем «Сделано ИИ»; работу специалиста не имитируем
  (E-E-A-T, честные оговорки — требование владельца ко всему контенту).
- Цены, лимиты, тексты карточек — только из админки/настроек. Коммерческие
  цены не хардкодить (правило из исходного ТЗ, подтверждено).
- Секреты — только в `.env` на сервере; `.env.example` без значений.
- Существующие remarka.biz, Lab, кабинет продолжают работать без изменений;
  ничего не перезапускать без необходимости, перед деплоем — backup.

## 1. Что переиспользуем (и что НЕ строим)

| Нужно | Берём готовое | НЕ строим |
|---|---|---|
| БД | тот же Postgres, additive-модели `Mkt*` в `packages/db` | второй Postgres |
| Очереди | тот же Redis + BullMQ worker (`apps/worker`) | второй Redis/worker |
| API | `apps/api` (Fastify), новые роуты `/api/market/*` | NestJS-дубль |
| Краулер сайтов | движок Monitor (лимиты, SSRF-защита уже есть) | новый crawler |
| AI-слой | существующий (Anthropic Messages API) | свой AiProvider с нуля |
| TMS | контракт `workers/oru-gateway/src/integrations/tms.js` (портировать на TS) | свою TMS |
| Расчёт цены перевода | тарифная логика `oru-gateway/src/routes/quote.js` (перенести, таблицу — в настройки) | новый pricing engine |
| Reverse proxy / TLS | Caddy, +1 site-блок `market.remarka.biz` | Nginx |
| Админка | staff-раздел кабинета (`cab.remarka.biz/staff`, auth уже есть) | отдельный /admin с паролями, TOTP, RBAC на 6 ролей |
| i18n | RU-ключевой словарь + `translate()/useT()` (паттерн Monitor) | i18n-библиотека |
| Дизайн | дизайн-система Remarka (carta/inchiostro/oltremare, Clash Display/General Sans/Fragment Mono) | чёрный glassmorphism из исходного ТЗ |

Также НЕ строим сейчас: ClamAV, MinIO, Stripe, PayPal, банковские счета в
приложении (B2B-счета остаются в кабинете), Playwright-рендер сайтов,
Storybook иконок. Всё это — осознанно отложено, не забыто.

## 2. Архитектура

```
market.remarka.biz ── Caddy ─┬─ /api/*  → api:3001  (роуты /api/market/*)
                             └─ /*      → market:80 (статика SPA)

apps/market      НОВОЕ  React + Vite + TS strict, SPA, без SSR.
                        TanStack Query, Zustand (локальный UI), Zod.
                        Telegram WebApp SDK через официальный скрипт;
                        безопасный browser-режим (демо + будущий WhatsApp).
                        Прод: static-контейнер (caddy file-server, ~16 МБ RAM).

apps/api         + роуты /api/market/* (auth, tools, orders, payments,
                        webhooks). Тяжёлое — только через очередь.
apps/worker      + новые job-типы: market-tool-run, market-deliver,
                        market-notify.
packages/db      + модели Mkt* (additive, prisma db push).
packages/market-core  НОВОЕ  канало-независимое ядро: типы, Zod-контракты,
                        интерфейс ChannelAdapter (Telegram сейчас,
                        WhatsApp потом) — тонкий слой, без бизнес-логики.
```

Telegram-бот: **без отдельного процесса**. Webhook-режим:
`POST /api/market/webhooks/telegram` в apps/api; тяжёлые обновления — в
очередь. Инвойсы Stars и уведомления — исходящие вызовы Bot API из api/worker.

## 3. Аутентификация (Mini App)

1. Фронт отправляет сырую строку `Telegram.WebApp.initData` на
   `POST /api/market/auth/telegram`.
2. Бэкенд: проверка HMAC-подписи по bot token → проверка `auth_date`
   (отклонять старше 6 часов) → upsert `MktUser` по числовому
   `telegramId` → выдача opaque-токена сессии (hash в БД, TTL 7 дней,
   sliding renewal — тот же паттерн, что CabSession).
3. `initDataUnsafe` не используется нигде. Username — только display-поле.
4. Browser-режим (вне Telegram): read-only витрина без авторизации;
   инструменты требуют открытия в Telegram (кнопка-ссылка на бота).
5. Связка с единой учёткой: поле `MktUser.cabUserId?` — заполняется позже
   через подтверждение e-mail magic-ссылкой кабинета (этап M4, не MVP).

## 4. Навигация и витрина

Нижнее меню: **Главная · Инструменты · Мои проекты · Профиль**.

Главная (первый экран — только бесплатное, решение владельца):

```
Remarka Market
Перевести. Локализовать. Создать.
Бесплатные инструменты — сразу, без регистрации и карты.
```

Пять крупных карточек бесплатных инструментов (§5), под ними — три
направления услуг (перевод / локализация / разработка), блок «мои
незавершённые результаты», блок доверия (живой счётчик из витрины Monitor —
переиспользовать `/api/public/showcase`), кнопка «Связаться».

Карточка инструмента: SVG-иконка (рисуем свои, стиль мегаменю — stroke 1.6,
currentColor), название, результат в одну строку, бейдж «Бесплатно · ИИ»,
лимит («до N в сутки»), CTA. Никаких «Попробовать бесплатно» — только
«Бесплатные инструменты» (правило исходного ТЗ сохраняется).

## 5. Бесплатные инструменты (все — ИИ/автоматика, все с лимитами из настроек)

### 5.1 AI-перевод текста
Вход: текст (лимит N знаков) или файл (DOCX/PDF/TXT, лимит МБ) + пара языков
(RU/EN/IT + авто). Выход: перевод, найденные термины, предупреждения
(даты/суммы/имена). Файл — перевод фрагмента до лимита.
CTA: «Перевести весь документ (ИИ)» → Stars; «Перевод специалистом» → §7.

### 5.2 Оценка стоимости перевода
Вход: файл + языки + срочность. Анализ в worker: формат, страницы,
знаки/слова, язык, необходимость OCR, таблицы. Цена: тарифная таблица
(портированная из oru-gateway, редактируется в админке) → вилка + срок +
`isFinalPrice:false` + честный дисклеймер.
CTA: «Заказать перевод» → заказ в TMS (§7) с этой оценкой в
`estimated_price`.

### 5.3 AI-локализация 5 страниц сайта
Вход: URL + целевой язык. Worker: краулер Monitor забирает до 5 публичных
страниц (существующие лимиты/robots/SSRF-защита) → ИИ переводит текстовые
блоки с сохранением структуры → выдача: HTML/MD-файлы + мини-аудит
готовности к локализации (hreflang, переключатель, смешение языков — движок
Monitor). Лимит: 1 сайт/сутки на пользователя.
CTA: «Остальные страницы (ИИ)» → Stars; «Локализация под ключ со
специалистом» → лид/расчёт.

### 5.4 Прототип сайта или приложения
Мастер 5–6 вопросов (что строим, для кого, проблема, must-have функции,
языки) → ИИ: концепция, аудитория, sitemap, MVP-список (обязательно /
желательно / позже), **кликабельный HTML-вайрфрейм главной страницы**
(рендерится в iframe внутри мини-аппа; генерация — в worker, шаблонная
сетка + контент от ИИ, не «свободный» HTML).
CTA: «Blueprint всех страниц (PDF)» → Stars; «Прототип от дизайнера» → лид.

### 5.5 Макет и первичный дизайн
На основе §5.4 (или отдельного ввода): одностраничный макет в 2–3 стилевых
вариантах (палитры/типографика — предопределённые темы нашей
дизайн-системы; ИИ подбирает контент и вариант, не рисует пиксели).
Сравнение вариантов — простым переключателем.
CTA: «Дизайн от специалиста с итерациями» → лид.

Общее для всех инструментов: очередь (никакого ИИ в HTTP-запросе), статус
«в работе» с прогрессом, результат сохраняется в `MktToolRun` и виден в
«Мои проекты», rate limit на пользователя и на IP, дневной лимит стоимости
ИИ (settings: `market.ai_daily_cost_cap`), при исчерпании — честное «на
сегодня лимит исчерпан, вернитесь завтра», версия промпта пишется в run.

## 6. Платная ступень

### 6.1 Telegram Stars (цифровые товары, выдача сразу в приложении)
- Полный AI-перевод документа; полный QA-отчёт (PDF/XLSX); +N страниц
  AI-локализации; Blueprint PDF.
- Поток: `createInvoiceLink` (Bot API, `currency=XTR`, payload = короткий id
  заказа) → `WebApp.openInvoice` → webhook: `pre_checkout_query` (сверка
  user/order/сумма, ответ <10 с) → **только** `successful_payment` переводит
  заказ в `paid` и запускает job выдачи. Charge id сохраняем; idempotency по
  telegram charge id; refund — официальным методом; команда `/paysupport`.
- Цены в Stars — из настроек (`MktProduct.priceStars`).

### 6.2 Crypto Pay (Криптобот) — индивидуальные/крупные работы
- Создание invoice через Crypto Pay API (сначала testnet), `web_app_invoice_url`
  открывается из мини-аппа; webhook с проверкой подписи; idempotency;
  expiration; сумма и курс фиксируются на момент создания.
- Не предлагать Crypto Pay как альтернативу Stars для того же мелкого
  цифрового товара (правило Telegram, сохраняем из исходного ТЗ).

### 6.3 Работы специалистов → TMS и лиды
- «Перевод специалистом»: `POST /public/upload` → `POST /public/widget-orders`
  (контракт tms.js: X-API-Key, contact, language_pair, service_type,
  file_ids, urgency, estimated_price) → номер заказа клиенту; статусы —
  `GET /public/orders/{id}` (поллинг из worker, уведомления в бота);
  результат — `GET /public/orders/{id}/result` кнопкой в «Моих проектах».
- Разработка/дизайн/локализация под ключ: карточка «Запросить расчёт» →
  `MktLead` + мгновенное уведомление владельцу в Telegram (ADMIN_CHAT_ID).
- Lead scoring (упрощённый): +балл за файл, скан сайта, выбор языков,
  дохождение до оплаты, повторное открытие результата. Порог «горячего» —
  в настройках.

## 7. Модель данных (Prisma, additive, префикс Mkt)

```
MktUser        telegramId (uniq, BigInt), username?, firstName?, locale,
               cabUserId?, isBlocked, createdAt, lastSeenAt
MktSession     tokenHash, userId, expiresAt, revokedAt, lastSeenAt
MktProduct     slug, category(translation|localization|development),
               tier(free|stars|custom), priceStars?, estPriceEur?, sort,
               isActive, badge?
MktProductI18n productId, locale, title, result, description, faq(Json)
MktToolRun     userId, tool, status(queued|running|done|failed), input(Json),
               result(Json?), aiModel?, promptVersion?, costUsd?, createdAt
MktOrder       userId, productId?, kind(stars|crypto|tms|lead),
               status(draft|awaiting_payment|paid|processing|delivered|
               cancelled|refunded), amountStars?, amountMinor?, currency?,
               tmsOrderId?, payload(Json), createdAt, updatedAt
MktPayment     orderId, provider(stars|cryptopay), providerChargeId (uniq),
               status, raw(Json), createdAt
MktDeliverable orderId?, toolRunId?, kind, fileId?, meta(Json)
MktFile        uuid-имя на диске, origName, mime, size, sha256, status
               (quarantined|clean|deleted), retentionUntil
MktLead        userId, source(tool|card), score, summary(Json), status
               (new|contacted|converted|dropped)
MktEvent       userId?, name, props(Json), createdAt   ← своя аналитика
MktSetting     key (uniq), value(Json)                 ← лимиты/тарифы/промпты
```

Деньги — integer minor units; Stars — целое `XTR`. Статусы наружу — только
локализованными подписями, не enum'ами.

## 8. API (`/api/market/*`, в guard'е apps/api — свой exempt-префикс + собственная MktSession-проверка)

```
POST /api/market/auth/telegram          initData → сессия
POST /api/market/auth/logout
GET  /api/market/me
GET  /api/market/catalog                продукты+переводы (public, cache)
POST /api/market/uploads                multipart, → MktFile (quarantine→clean)
POST /api/market/tools/:tool            запуск (fragment-translate |
                                        translation-estimate | site-l10n |
                                        prototype | mockup)
GET  /api/market/tool-runs/:id          статус+результат (поллинг фронта)
GET  /api/market/projects               мои runs/заказы/результаты
POST /api/market/orders                 создать заказ (kind по продукту)
POST /api/market/orders/:id/stars       → invoice link
POST /api/market/orders/:id/cryptopay   → web_app_invoice_url
POST /api/market/orders/:id/tms         → заказ в TMS
GET  /api/market/orders/:id
GET  /api/market/deliverables/:id       подписанная одноразовая выдача файла
POST /api/market/webhooks/telegram      секрет в пути или header (X-Telegram-
                                        Bot-Api-Secret-Token), идемпотентно
POST /api/market/webhooks/cryptopay     проверка подписи, идемпотентно
GET  /api/market/admin/*                только staff (cab_session, isStaff):
                                        products CRUD, settings, leads,
                                        orders, tool-runs, events
```

## 9. Файлы

Приватный volume `market-files` (вне WP и вне public). UUID-имена, MIME по
содержимому (magic bytes), нормализация имени, лимит размера из настроек,
запрет исполняемых и архивов-в-архивах, quarantine до проверки (без ClamAV
на MVP — sniff + расширение + размер), retention из настроек + ежедневный
job очистки, журнал выдач (`MktDeliverable` + подписанные ссылки TTL 10 мин).

## 10. Админка (внутри staff-раздела кабинета)

Новая вкладка «Market» на `cab.remarka.biz/staff` (auth и isStaff уже есть):
- продукты: тексты ×3 языка, цены Stars/EUR-ориентир, порядок, вкл/выкл;
- инструменты: вкл/выкл, дневные лимиты, лимит размера, промпт (с
  версионированием: новая запись, старую не перезаписывать), cost cap;
- лиды: список с score, статусы, ссылка на Telegram-профиль;
- заказы: статусы, ручной refund Stars, лог платёжных webhook'ов;
- события: простая сводка воронки (app_opened → tool_started →
  tool_completed → checkout → paid) по дням.

## 11. i18n

RU — основной (аудитория Telegram), EN/IT — полные. Паттерн Monitor:
RU-строка = ключ, `dict.ts` `{en, it}`, `useT()`. Язык: `remarka_lang`
кука (если пришёл из наших сайтов) → `Telegram.WebApp initData language_code`
→ RU. Ручной переключатель в профиле, выбор сохраняется в `MktUser.locale`.
Контент каталога — из `MktProductI18n` (админка), не из словаря.

## 12. Бот (webhook, без отдельного контейнера)

Команды: `/start` (открыть Mini App + deep link на инструмент), `/app`,
`/orders`, `/support`, `/paysupport`, `/privacy`, `/terms`.
Уведомления: результат готов, статус TMS-заказа изменился, оплата прошла,
напоминание о незавершённом результате (максимум 1, без спама).
Владельцу: горячий лид, новая крупная заявка, ошибка платежа.
BotFather: Main Mini App, menu button, описание, splash — в docs/setup.

## 13. Безопасность (сводно)

- initData: только серверная проверка подписи + свежесть; сессии opaque+hash.
- Rate limits: паттерн `checkRateLimit` из api (per-user и per-IP на каждый
  инструмент и на auth).
- Краулер: существующие лимиты Monitor (SSRF, private IP, redirects, размер,
  timeout, robots).
- Платежи: выдача только после `successful_payment`/подтверждённого webhook;
  idempotency-ключи; сверка суммы и получателя.
- ИИ: файлы пользователей уходят провайдеру только для явно запрошенной
  операции; сказать об этом в Privacy/AI Notice; cost cap в сутки.
- Webhook Telegram: секретный токен; Crypto Pay: подпись.
- Никаких новых открытых портов: api и market — только за Caddy.

## 14. Деплой

- DNS: `market.remarka.biz` → сервер (как lab/cab).
- Caddy: новый site-блок (market → static-контейнер, /api/* → api:3001).
- Compose (prod-оверлей): +сервис `market` (static, mem limit 32M),
  volume `market-files` монтируется в api и worker.
- `.env` (+ `.env.prod.template`): `MARKET_BOT_TOKEN`,
  `MARKET_WEBHOOK_SECRET`, `MARKET_SESSION_SECRET`, `TMS_BASE_URL`,
  `TMS_API_KEY`, `CRYPTOPAY_TOKEN` (+`CRYPTOPAY_TESTNET=1` на старте),
  `MARKET_ADMIN_CHAT_ID`.
- **Предусловие запуска: апгрейд VPS CX23 → CX32 (8 ГБ)** — текущий бюджет
  памяти 3328M/4096M не оставляет запаса под рост api/worker-нагрузки.
  До апгрейда допустим только этап M1 в тестовом режиме.
- Caddyfile-грабля: изменение = `up -d --force-recreate caddy` (bind-mount
  одиночного файла, reload недостаточно — задокументировано 20.07.2026).
- Backup: `market-files` и таблицы `mkt_*` включить в существующий backup.sh.
- Monitoring: health-роут `/api/market/health`, глубина очереди market-джобов
  и провалы webhook'ов — алерт владельцу в Telegram.

## 15. Аналитика

Только своя (`MktEvent`), события: app_opened, tool_started, tool_completed,
result_viewed, upsell_clicked, checkout_started, payment_success,
quote_requested, order_completed. Содержимое документов и персональные
данные в события не писать. Внешних аналитик нет.

## 16. Тесты (протокол верификации — до отчёта владельцу)

- Unit: проверка initData (валидная/просроченная/подделанная подпись),
  state machine платежа Stars (не выдавать до successful_payment),
  тарифный расчёт, safeUrl краулера, idempotency webhook'ов.
- Integration: TMS-мок по контракту tms.js; Crypto Pay testnet; полный
  цикл tool-run через реальные Redis/Postgres (docker).
- E2E-smoke (Playwright, browser-режим + мок initData): открытие витрины,
  запуск каждого из 5 инструментов до результата, Stars-checkout с моком
  webhook, создание TMS-заказа с моком, админ-CRUD продукта.
- Мобильная проверка: iOS/Android Telegram, маленький viewport, клавиатура,
  медленная сеть, обрыв загрузки файла, повторное открытие.

## 17. Этапы и Definition of Done

**M0 — фундамент (внутри монорепо).**
apps/market (SPA, навигация, i18n, дизайн-система), auth по initData,
MktUser/MktSession, Caddy-блок, compose, health. DoD: мини-апп открывается
из бота, авторизует, витрина каталога из БД, browser-режим работает.

**M1 — переводческая вертикаль (самый короткий путь к деньгам).**
Инструменты §5.1 и §5.2, загрузка файлов, TMS-интеграция (upload → order →
статусы → результат), уведомления в бота, лиды владельцу. DoD: живой
сценарий «загрузил документ → оценка → заказ → статус в “Моих проектах”»,
подтверждённый на testnet TMS-ключах или реальном заказе.

**M2 — остальные инструменты + Stars.**
§5.3–§5.5, Stars-checkout для 4 цифровых товаров, /paysupport, refund.
DoD: каждый инструмент выдаёт реальный результат (не заглушку); Stars-платёж
подтверждается только по successful_payment (тест с реальным маленьким
платежом владельца).

**M3 — Crypto Pay + админка + аналитика.**
Crypto Pay (testnet → прод), вкладка Market в staff-кабинете (продукты,
лимиты, промпты, лиды, заказы), воронка событий. DoD: цена/лимит/текст
меняются из админки без деплоя; testnet-инвойс проходит полный цикл.

**M4 — hardening и рост.**
Retention-джобы, алерты, связка MktUser↔CabUser, Privacy/Terms/AI Notice
(placeholder с пометкой на юр. проверку), A/B текстов CTA, подготовка
ChannelAdapter к WhatsApp. DoD: чек-лист §13 закрыт, backup восстановлен
тестово, документация деплоя в setup.md дополнена.

## 18. Что нельзя делать

Наследуем из исходного ТЗ: не доверять initDataUnsafe; не выдавать товар до
successful_payment; не открывать Postgres/Redis наружу; не хранить файлы в
публичных папках и WP uploads; не запускать ИИ/OCR/краулер в HTTP-потоке;
не коммитить секреты; не делать фиктивные инструменты со случайными
результатами; не менять remarka.biz. Плюс наши: не выдавать ИИ за человека;
не дублировать сервисы, которые уже есть в платформе; не начинать M2+ до
апгрейда VPS.

## 19. Открытые вопросы к владельцу (не блокируют M0–M1)

1. Тарифная таблица оценки перевода: стартовые вилки €/страница по типам
   документов (сейчас в oru-gateway: перевод 25 €, апостиль 70 €, прочее
   45 € — подтвердить/поправить для Market).
2. Цены в Stars для 4 цифровых товаров (можно выставить в админке в M3).
3. Токен бота: новый бот (@RemarkaMarketBot?) или существующий.
4. TMS: подтвердить у оператора выдачу отдельного API-ключа для Market и
   лимиты на /public/catalog.
