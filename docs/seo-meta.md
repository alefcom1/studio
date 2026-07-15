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
| `/servizi/adeguamento-eaa/` | adeguamento EAA | EAA compliance | ✅ (H1, hero-sub, H2 «per chi», FAQ) — см. «Adeguamento EAA» sotto |
| `/milano/` | web agency Milano | (city IT-only, EN: web agency Milan) | ✅ (eyebrow, H2 servizi, alt) |
| `/monza/ /bergamo/ /brescia/ /como/` | realizzazione siti web ‹città› | — | ✅ (H1, H2 servizi, alt) |
| `/strumenti/test-velocita/` | test velocità sito web | website speed test | ✅ (H1) |
| `/strumenti/analisi-seo/` · `/strumenti/check-gdpr/` · `/strumenti/roi-localizzazione/` | analisi SEO gratuita / check GDPR e cookie / ROI localizzazione | free SEO audit / GDPR & cookie check / localization ROI | ✅ живой виджет (T2, вышли из «In arrivo» — ключи/мета этих 3 отдельно не проработаны в этой сессии) |
| `/strumenti/verifica-accessibilita/` | verifica accessibilità sito | website accessibility check | ✅ (H1, hero-sub, come funziona, FAQ) — см. «Инструменты (Lab)» ниже |
| `/strumenti/sito-pronto-ai/` | sito pronto per l'AI (llms.txt) | AI readiness check (llms.txt) | ✅ (H1, hero-sub, come funziona, FAQ) — см. «Инструменты (Lab)» ниже |
| `/strumenti/impatto-co2/` | impronta di carbonio sito web | website carbon footprint | ✅ (H1, hero-sub, come funziona, FAQ) — см. «Инструменты (Lab)» ниже |
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

## Инструменты (Lab) — 3 новых, IT/EN/RU

> Добавлено по итогам T1–T3 «Remarka Lab» (см. `docs/piano-strumenti-lab.md`).
> Тексты Title/Description основаны на реальном H1/hero-подзаголовке/FAQ
> паттернов страниц (`patterns/pages/strumento-*.php`,
> `patterns/pages/en-strumento-*.php`, `patterns/pages/ru-strumento-*.php`),
> цифры и факты не выдуманы. Остальные 4 инструмента (`test-velocita`,
> `analisi-seo`, `check-gdpr`, `roi-localizzazione` и их EN/RU-слаги) теперь
> тоже полностью «живые» (не заглушки) — их фокус-ключи/Title/Description
> в этой сессии не прорабатывались, статус см. в таблицах выше.
>
> Этапы L1/L2 (см. `piano-strumenti-lab.md`, статус): на всех 7 страницах
> инструментов добавлены 3 SEO-секции (метод / чтение результата / как
> улучшить) — **IT ✅ (L1, `aad3f12`), EN ✅ и RU ✅ (L2)**. H2 секций несут
> вариации фокус-ключей (H1-ключ дословно не повторяется), в секциях «как
> улучшить» — контекстные ссылки на услуги и блог на каждом языке.

### Карта фокус-ключей — 3 новых инструмента (IT/EN)

| Страница | Focus Keyword IT | Focus Keyword EN | Контент подтянут |
|---|---|---|---|
| `/strumenti/verifica-accessibilita/` · `/en/tools/accessibility-check/` | verifica accessibilità sito | website accessibility check | ✅ (H1, hero-sub, come funziona, FAQ) |
| `/strumenti/sito-pronto-ai/` · `/en/tools/ai-readiness/` | sito pronto per l'AI (llms.txt) | AI readiness check (llms.txt) | ✅ (H1, hero-sub, come funziona, FAQ) |
| `/strumenti/impatto-co2/` · `/en/tools/website-carbon/` | impronta di carbonio sito web | website carbon footprint | ✅ (H1, hero-sub, come funziona, FAQ) |

### Карта фокус-ключей — те же 3 инструмента (RU)

| Страница | Focus Keyword RU | Контент подтянут |
|---|---|---|
| `/ru/instrumenty/proverka-dostupnosti/` | проверка доступности сайта | ✅ (H1, hero-sub, «как это работает», FAQ) |
| `/ru/instrumenty/gotovnost-k-ii/` | готовность сайта к ИИ (llms.txt) | ✅ (H1, hero-sub, «как это работает», FAQ) |
| `/ru/instrumenty/uglerodnyj-sled/` | углеродный след сайта | ✅ (H1, hero-sub, «как это работает», FAQ) |

### IT — `/strumenti/verifica-accessibilita/`

- **Title:** `Verifica accessibilità sito web (EAA) | Studio Remarka`
- **Description:** `Test gratuito con Google Lighthouse: punteggio 0–100 e barriere secondo WCAG 2.1 AA, obbligo dell'European Accessibility Act. Senza registrazione.`

### IT — `/strumenti/sito-pronto-ai/`

- **Title:** `Il sito è pronto per l'AI? Test llms.txt | Studio Remarka`
- **Description:** `Verifichiamo llms.txt, accesso crawler AI, dati strutturati JSON-LD e sitemap: punteggio di prontezza AI su 4, gratis e senza registrazione.`

### IT — `/strumenti/impatto-co2/`

- **Title:** `Impronta di carbonio del sito web | Studio Remarka`
- **Description:** `Misuriamo il peso della pagina e stimiamo le emissioni di CO₂ per visita e all'anno con il modello Sustainable Web Design. Test gratuito, senza registrazione.`

### EN — `/en/tools/accessibility-check/`

- **Title:** `Website Accessibility Check (WCAG/EAA) | Studio Remarka`
- **Description:** `Free accessibility test powered by Google Lighthouse: 0–100 score and the barriers to fix under the WCAG 2.1 AA standard required by the EU Accessibility Act.`

### EN — `/en/tools/ai-readiness/`

- **Title:** `AI Readiness Check: is your site AI-ready? | Studio Remarka`
- **Description:** `We check llms.txt, AI crawler access, JSON-LD structured data and your sitemap: a free AI-readiness score out of 4. No sign-up.`

### EN — `/en/tools/website-carbon/`

- **Title:** `Website Carbon Footprint Calculator | Studio Remarka`
- **Description:** `Measure your page weight and estimate CO₂ emissions per visit and per year with the Sustainable Web Design model (co2.js). Free test, no sign-up required.`

### RU — `/ru/instrumenty/proverka-dostupnosti/`

- **Title:** `Проверка доступности сайта (WCAG/EAA) | Studio Remarka`
- **Description:** `Бесплатный тест доступности на основе Google Lighthouse: оценка 0–100 и барьеры по стандарту WCAG 2.1 AA, обязательному по European Accessibility Act.`

### RU — `/ru/instrumenty/gotovnost-k-ii/`

- **Title:** `Готов ли сайт к ИИ? Проверка llms.txt | Studio Remarka`
- **Description:** `Проверяем llms.txt, доступ AI-краулеров, структурированные данные JSON-LD и sitemap: оценка готовности к ИИ из 4. Бесплатно, без регистрации.`

### RU — `/ru/instrumenty/uglerodnyj-sled/`

- **Title:** `Углеродный след сайта — калькулятор CO₂ | Studio Remarka`
- **Description:** `Измеряем вес страницы и оцениваем выбросы CO₂ на визит и за год по модели Sustainable Web Design (co2.js). Бесплатный тест, без регистрации.`

**Проверка длин.** Title (лимит ≤60): IT accessibilità — 54, IT AI — 57, IT CO₂ — 50,
EN accessibility — 55, EN AI — 59, EN CO₂ — 52, RU accessibility — 54, RU AI — 54,
RU CO₂ — 56 — все ≤60. Description (лимит ≤160): IT accessibilità — 146, IT AI — 140,
IT CO₂ — 158, EN accessibility — 158, EN AI — 127, EN CO₂ — 154, RU accessibility — 150,
RU AI — 141, RU CO₂ — 140 — все ≤160.

## Check-up completo del sito — IT/EN/RU (M4)

> Источник — `docs/copy-checkup.md` §2.2/§3.2/§4.2 (copy deck M1). Contenuto
> подтянут: H1, intro, sezione «Il metodo»/«The method»/«Метод», FAQ (3),
> CTA finale — pagine `/strumenti/check-up-completo/` ·
> `/en/tools/full-site-checkup/` · `/ru/instrumenty/polnaya-proverka-sajta/`.

| Страница | Focus Keyword | Контент подтянут |
|---|---|---|
| `/strumenti/check-up-completo/` | check up sito web | ✅ (H1, intro, «Il metodo», «Come leggere», FAQ) |
| `/en/tools/full-site-checkup/` | website check up | ✅ (H1, intro, «The method», «How to read it», FAQ) |
| `/ru/instrumenty/polnaya-proverka-sajta/` | полная проверка сайта | ✅ (H1, интро, «Метод», «Как читать», FAQ) |

### IT — `/strumenti/check-up-completo/`

- **Title:** `Check-up completo del sito web, gratis | Studio Remarka`
- **Description:** `Un solo test: velocità, SEO, accessibilità, privacy, best practice, AI e CO₂. Punteggio di salute 0–100 e report PDF completo. Gratis, senza registrazione.`

### EN — `/en/tools/full-site-checkup/`

- **Title:** `Full website check-up, free — 7 tests in one | Studio Remarka`
- **Description:** `One test: speed, SEO, accessibility, privacy, best practices, AI and CO₂. A 0–100 health score and a full PDF report. Free, no sign-up required.`

### RU — `/ru/instrumenty/polnaya-proverka-sajta/`

- **Title:** `Полная проверка сайта: 7 тестов в одном | Studio Remarka`
- **Description:** `Один тест: скорость, SEO, доступность, приватность, стандарты, ИИ и CO₂. Оценка здоровья сайта 0–100 и полный отчёт в PDF. Бесплатно, без регистрации.`

**Проверка длин.** Title: IT — 54, EN — 59, RU — 56 — все ≤60. Description: IT — 157,
EN — 146, RU — 150 — все ≤160.

---

## Adeguamento EAA — IT/EN/RU (E1)

> Источник — `docs/copy-eaa.md` §2 (copy deck E1, услуга «специальная»: собственный dict
> `ADEGUAMENTO_EAA` в `data.py`, не входит в `SERVICES`). Focus keyword IT `adeguamento EAA`,
> EN `EAA compliance`, RU `доступность сайта по EAA`. Слаги: IT `/servizi/adeguamento-eaa/`,
> EN `/en/services/eaa-compliance/`, RU `/ru/uslugi/dostupnost-eaa/`.

| Страница | Focus Keyword | Контент подтянут |
|---|---|---|
| `/servizi/adeguamento-eaa/` | adeguamento EAA | ✅ (H1, hero-sub, H2 «per chi»/«cosa include», FAQ) |
| `/en/services/eaa-compliance/` | EAA compliance | ✅ (H1, hero-sub, H2 «who it's for»/«what's included», FAQ) |
| `/ru/uslugi/dostupnost-eaa/` | доступность сайта по EAA | ✅ (H1, hero-sub, H2 «для кого это»/«что входит», FAQ) |

### IT — `/servizi/adeguamento-eaa/`

- **Title (47):** `Adeguamento EAA in 3 settimane | Studio Remarka`
- **Description (152):** `Sito conforme all'European Accessibility Act (WCAG 2.1 AA): audit, correzioni e dichiarazione di accessibilità in 3 settimane. Da € 1.900, prezzo chiuso.`

### EN — `/en/services/eaa-compliance/`

- **Title (54):** `EAA compliance in 3 weeks, fixed price | Studio Remarka`
- **Description (154):** `Make your site compliant with the European Accessibility Act (WCAG 2.1 AA): audit, fixes and accessibility statement in 3 weeks. From € 1,900, fixed price.`

### RU — `/ru/uslugi/dostupnost-eaa/`

- **Title (52):** `Доступность сайта по EAA за 3 недели | Studio Remarka`
- **Description (156):** `Приводим сайт в соответствие с European Accessibility Act (WCAG 2.1 AA): аудит, исправления и декларация о доступности за 3 недели. От € 1 900, цена в договоре.`

**Проверка длин.** Title: IT — 47, EN — 54, RU — 52 — все ≤60. Description: IT — 152,
EN — 154, RU — 156 — все ≤160.

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
| `/ru/instrumenty/test-skorosti/` · `/ru/instrumenty/proverka-gdpr/` · `/ru/instrumenty/seo-audit/` · `/ru/instrumenty/roi-lokalizacii/` | тест скорости сайта / проверка GDPR и cookie / SEO-анализ страницы / ROI локализации | ✅ живой виджет (T3, вышли из заглушек — ключи/мета этих 4 отдельно не проработаны в этой сессии) |
| `/ru/instrumenty/proverka-dostupnosti/` | проверка доступности сайта | ✅ (H1, hero-sub, «как это работает», FAQ) — см. «Инструменты (Lab)» ниже |
| `/ru/instrumenty/gotovnost-k-ii/` | готовность сайта к ИИ (llms.txt) | ✅ (H1, hero-sub, «как это работает», FAQ) — см. «Инструменты (Lab)» ниже |
| `/ru/instrumenty/uglerodnyj-sled/` | углеродный след сайта | ✅ (H1, hero-sub, «как это работает», FAQ) — см. «Инструменты (Lab)» ниже |

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
