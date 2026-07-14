# SEO-мета и фокус-ключи после перепозиционирования

> Вставляется вручную: админка → страница → панель Rank Math → «Edit Snippet»
> (Title ≤ 60, Description ≤ 160) + поле **Focus Keyword** — из таблицы ниже.
> Оценка Rank Math — чек-лист против фокус-ключа: без заданного ключа она
> всегда ~20/100 и ничего не говорит о реальном SEO. Владелец правит
> мету/заголовки сам; контент под ключи подтягивается кодом (см. статус).
> RU-мета фазы B готова — см. раздел «RU-версия (фаза B)» ниже.

## Карта фокус-ключей (IT / EN)

| Страница | Focus Keyword IT | Focus Keyword EN | Контент подтянут |
|---|---|---|---|
| `/` · `/en/` | realizzazione siti web | business website | ✅ (eyebrow, FAQ, alt) |
| `/prezzi/` · `/en/pricing/` | quanto costa un sito web | website cost | ✅ (интро-вопрос) |
| `/servizi/siti-aziendali/` | sito web aziendale | business website design | ✅ (hero-sub, H2 «per chi») |
| `/servizi/e-commerce/` | realizzazione siti e-commerce | e-commerce website | ✅ (hero-sub, H2 «per chi») |
| `/servizi/siti-pwa/` | progressive web app | progressive web app | ✅ (hero-sub, H2 «per chi») |
| `/servizi/restyling-migrazione/` | rifacimento sito web | website redesign | ✅ (hero-sub, H2 «per chi») |
| `/servizi/seo-tecnica/` | SEO tecnica | technical SEO | ✅ (eyebrow, hero-sub, H2 «per chi») |
| `/servizi/siti-multilingue/` | sito web multilingua | multilingual website | ✅ (hero-sub, H2 «per chi») |
| `/servizi/export-ready/` | sito web per l'export | export website | ✅ (hero-sub, H2 «garanzie») |
| `/servizi/web-app/` | sviluppo web app | custom web app | ✅ (hero-sub, H2 «per chi») |
| `/milano/` | web agency Milano | (city IT-only, EN: web agency Milan) | ✅ (eyebrow, H2 servizi, alt) |
| `/monza/ /bergamo/ /brescia/ /como/` | realizzazione siti web ‹città› | — | ✅ (H1, H2 servizi, alt) |
| `/strumenti/test-velocita/` | test velocità sito web | website speed test | ✅ (H1) |
| блог-статьи | целевой запрос из заголовка (уже заложен при написании) | то же | ✅ с рождения |
| `/chi-siamo/`, `/casi-studio/` | брендовые — фокус-ключ не задавать, оценку RM игнорировать | — | — |

Что сознательно НЕ делаем по чек-листу Rank Math: плотность 1% («Keyword
Density») набивкой, точный ключ в каждом H2, «Content AI» (платный апселл) —
это ухудшает премиальный копирайт и не влияет на Google. Целевой ориентир
после простановки ключей: 75–90/100.

## Главная `/` (IT)

- **Title:** `Sito web in 3 settimane, a prezzo chiuso | Studio Remarka`
- **Description:** `Sito aziendale online in 3 settimane, prezzo bloccato alla firma e PageSpeed 90+ garantiti da contratto. Studio a Milano. Preventivo chiuso in 24 ore.`

## Главная EN `/en/`

- **Title:** `Business website in 3 weeks, at a fixed price | Studio Remarka`
- **Description:** `Your website live in 3 weeks, price locked at signing, PageSpeed 90+ — all guaranteed by contract. Milan studio, 4 languages. Fixed quote in 24 hours.`

## `/prezzi/` (IT)

- **Title:** `Prezzi siti web a listino chiuso | Studio Remarka`
- **Description:** `Sito vetrina da € 1.900, aziendale da € 3.900, e-commerce da € 7.500 — prezzi chiusi in contratto, consegna in 2/3/6 settimane, confronto con le forbici di mercato.`

## `/en/pricing/`

- **Title:** `Website prices with a fixed quote | Studio Remarka`
- **Description:** `Brochure site from € 1,900, business website from € 3,900, e-commerce from € 7,500 — fixed contract prices, delivered in 2/3/6 weeks. Compared with market rates.`

## Сервисные страницы (по мере обновления сроков)

- `/servizi/siti-aziendali/` Title: `Sito aziendale in 3 settimane, prezzo chiuso | Studio Remarka`
- `/servizi/e-commerce/` Title: `E-commerce in 6 settimane, prezzo chiuso | Studio Remarka`
- Description строить по формуле: `<продукт> consegnato in <N> settimane a prezzo bloccato, PageSpeed 90+ e 12 mesi di assistenza da contratto. Preventivo in 24 ore.`

---

## RU-версия (фаза B)

> Источник текстов — `docs/copy-fase-B.md`, Часть 3 «SEO-мета» (главная и оба
> лендинга — из копидека B1; `/ru/ceny/` построена здесь по образцу IT
> `/prezzi/`, поскольку в copy-fase-B.md её нет). Формат Title —
> `<фраза> | Studio Remarka`, единый с фазой A. Цены и сроки — из
> `patterns/pages/ru-prezzi.php` (визитка € 1 900–2 800/2 нед., корпоративный
> € 3 900–5 800/3 нед., магазин € 7 500–14 000/6 нед.), формат евро — с
> пробелом-тысячником.

### Карта фокус-ключей (RU)

| Страница | Focus Keyword RU | Контент подтянут |
|---|---|---|
| `/ru/` | сайт для выхода на рынок Италии | ✅ (hero H1/sub, eyebrow) |
| `/ru/uslugi/sajt-dlya-evropy/` | сайт для бизнеса в Италии | ✅ (H1, hero-sub, секция 1) |
| `/ru/uslugi/seo-prodvizhenie/` | SEO-продвижение в Италии | ✅ (H1, hero-sub, секция 1) |
| `/ru/ceny/` | сколько стоит сайт | ✅ (H1/lead уже отвечают на вопрос, таблица цен) |

### `/ru/`

- **Title:** `Сайт для выхода на рынок Италии и Европы | Studio Remarka`
- **Description:** `Итальянская студия с русскоязычной командой: сайт за 3 недели, локализация носителями и SEO в стране назначения — под одним договором. Смета за 24 часа.`

### `/ru/uslugi/sajt-dlya-evropy/`

- **Title:** `Сайт для бизнеса в Италии и Европе | Studio Remarka`
- **Description:** `Сайт под европейского покупателя: дизайн уровня итальянского рынка, тексты носителей, юридическая часть и GDPR под ЕС. За 3 недели, цена в договоре.`

### `/ru/uslugi/seo-prodvizhenie/`

- **Title:** `SEO-продвижение в Италии и Европе | Studio Remarka`
- **Description:** `Продвижение в Google Италии и ЕС и работа с русскоязычной аудиторией: русский, украинский, грузинский, армянский, казахский. Прозрачно, с отчётом каждый месяц.`

### `/ru/ceny/`

- **Title:** `Сколько стоит сайт в Италии: цены и сроки | Studio Remarka`
- **Description:** `Визитка от € 1 900, корпоративный сайт от € 3 900, интернет-магазин от € 7 500. Цена фиксируется в договоре, срок — 2/3/6 недель, сравнение с рынком Италии.`

**Проверка длин.** Title: `/ru/` — 57 зн., лендинг 1 — 51, лендинг 2 — 50, `/ru/ceny/` — 58 —
все ≤60. Description: `/ru/` — 152, лендинг 1 — 148, лендинг 2 — 159, `/ru/ceny/` — 156 —
все ≤160.
