# Copy deck — nuovo servizio «Adeguamento EAA»

> **Реализовано (E1) — 15.07.2026, этот коммит.** Все тексты этого дека внесены в репозиторий
> verbatim: `data.py` (`ADEGUAMENTO_EAA`), `generate_pages.py` (`build_adeguamento_eaa()`),
> EN через `translate_pages.py en` (CHROME_EAA), RU вручную (`ru-servizio-adeguamento-eaa.php`).
> Статус и детали — `docs/piano-checkup-sito.md` §«Статус выполнения» → E1.

> Data: 15.07.2026 · Autore: Opus (strategia-copy) · Ветка `claude/new-project-prep-zhmkg5` (SOLO LETTURA).
> Единственный выход этой задачи. Оркестратор сам вносит контент в репо — я НИЧЕГО не менял и git не трогал.
> Тон бренда (piano-implementazione-fase-A §0): числа вместо прилагательных, форма «voi», честные оговорки,
> без англицизмов в IT. RU-версия — самодостаточный текст для русскоязычного бизнеса в Европе, НЕ перевод.
>
> **Утверждённые владельцем параметры (не менять):** цена `da € 1.900` (prezzo chiuso dopo l'audit);
> срок `3 settimane` контрактный с неустойкой 1% за рабочий день просрочки (механика линейки —
> `data.py` garanzie / hero-timeline: «data fissa in contratto, ogni giorno lavorativo di ritardo vale l'1%»);
> пейзаж: **audit (наш бесплатный инструмент — первый шаг) → correzione tema/contenuti/contrasti/navigazione →
> dichiarazione di accessibilità (документ обязателен) → audit di verifica-conferma**.
>
> **Границы:** никаких выдуманных кейсов/отзывов/имён — у EAA нет `mini_caso` (в отличие от 6 базовых услуг).
> Поэтому EAA структурно ближе к `EXPORT_READY` / `WEB_APP` (собственный dict + собственная build-функция),
> чем к типовому `build_servizio`. См. раздел 7 «Для имплементатора».

---

## 1. Слаги (проверено по `build-tools/lang.py` → `SERVICES_SLUGS` и `deploy-import.php`)

| Язык | Финальный слаг (полный путь) | Родитель |
|---|---|---|
| IT | `/servizi/adeguamento-eaa/` | `servizi` |
| EN | `/en/services/eaa-compliance/` | `en/services` |
| RU | `/ru/uslugi/dostupnost-eaa/` | `ru/uslugi` |

Паттерн подтверждён: секция `servizi → services → uslugi`, услуги — вложенные страницы (`servizio-*`, `en-servizio-*`,
`ru-servizio-*`). Добавить в `SERVICES_SLUGS` (`lang.py`) строку:
`'adeguamento-eaa': {'en': 'eaa-compliance', 'ru': 'dostupnost-eaa'}` — тогда hreffang-карта (`inc/lang-map.php`)
получит связку IT↔EN↔RU автоматически при `python3 lang.py`.

---

## 2. SEO-блок (формат `seo-meta.md`: Focus Keyword + Title ≤60 + Description ≤160)

### Фокус-ключи

| Язык | Focus Keyword (основной) | Вторичные (в H2/тексте) |
|---|---|---|
| IT | `adeguamento EAA` | sito conforme European Accessibility Act · accessibilità sito web obbligatoria · dichiarazione di accessibilità |
| EN | `EAA compliance` | European Accessibility Act website · website accessibility compliance · accessibility statement |
| RU | `доступность сайта по EAA` | сайт по European Accessibility Act · требования доступности сайта в ЕС · декларация о доступности |

### Title / Description

**IT — `/servizi/adeguamento-eaa/`**
- **Title (47):** `Adeguamento EAA in 3 settimane | Studio Remarka`
- **Description (152):** `Sito conforme all'European Accessibility Act (WCAG 2.1 AA): audit, correzioni e dichiarazione di accessibilità in 3 settimane. Da € 1.900, prezzo chiuso.`

**EN — `/en/services/eaa-compliance/`**
- **Title (54):** `EAA compliance in 3 weeks, fixed price | Studio Remarka`
- **Description (154):** `Make your site compliant with the European Accessibility Act (WCAG 2.1 AA): audit, fixes and accessibility statement in 3 weeks. From € 1,900, fixed price.`

**RU — `/ru/uslugi/dostupnost-eaa/`**
- **Title (52):** `Доступность сайта по EAA за 3 недели | Studio Remarka`
- **Description (156):** `Приводим сайт в соответствие с European Accessibility Act (WCAG 2.1 AA): аудит, исправления и декларация о доступности за 3 недели. От € 1 900, цена в договоре.`

> Длины: IT Title 47 / Desc 152 · EN Title 54 / Desc 154 · RU Title 52 / Desc 156 — все в лимитах.
> Формат Title `<фраза> | Studio Remarka` единый с фазами A/B.

---

## 3. Полный контент услуги — IT

> Маппинг на структуру (кастомная запись EAA + build-функция по образцу `build_export_ready`).
> Поля ниже названы так, чтобы имплементатор просто заполнил dict.

### hero
- **eyebrow / breadcrumb:** `Servizio / Adeguamento EAA`
- **hero_title (H1):** `Il sito conforme all'European Accessibility Act, in 3 settimane`
- **hero_sub:** `Dal 28 giugno 2025 l'accessibilità è un obbligo di legge per molti siti. Vi portiamo allo standard WCAG 2.1 AA — audit, correzioni e dichiarazione di accessibilità — a prezzo chiuso e con la data nel contratto.`
- **hero_stat_value:** `28.06.2025`
- **hero_stat_label:** `Data da cui l'European Accessibility Act è in vigore in Italia. Le prime sanzioni sono una questione di tempo.`
- **CTA hero:** `Richiedi l'audit di accessibilità` → `/#contatti` · (outline) `Verifica subito il tuo sito` → `/strumenti/verifica-accessibilita/`

### A chi si rivolge (`per_chi`)
- **per_chi_heading:** `L'obbligo riguarda chi vende a consumatori, online`
- **per_chi:**
  1. `E-commerce e servizi digitali che vendono beni o servizi ai consumatori nell'Unione Europea.`
  2. `Banche, assicurazioni, trasporti, biglietterie e sistemi di prenotazione online.`
  3. `Aziende non microimpresa che temono la prima sanzione italiana, o che l'hanno già ricevuta come segnalazione.`

### Cosa include (`include` — 6 bullet «что входит»)
- **include_heading:** `Dall'audit alla dichiarazione, tutto scritto nel preventivo`
- **include:**
  1. `Audit completo: test automatico (Lighthouse) più verifica manuale — tastiera, screen reader, contenuti.`
  2. `Correzione di tema, contrasti, etichette dei moduli e struttura dei titoli.`
  3. `Navigazione da tastiera e focus sempre visibile su ogni elemento interattivo.`
  4. `Dichiarazione di accessibilità pubblicata, il documento che la norma richiede.`
  5. `Audit di verifica finale secondo lo standard WCAG 2.1 AA, a correzioni fatte.`
  6. `Prezzo chiuso dopo l'audit, consegna in 3 settimane con penale in contratto.`

### Le 3 settimane, passo per passo (`processo` — блок недель, реюз `sr-week-chip`/`sr-step`)
- **heading:** `Tre settimane, dalla diagnosi alla conformità`
- **processo:**
  | Settimana | Passo | Testo |
  |---|---|---|
  | `SETTIMANA 1` | `Audit` | `Partiamo dal test automatico gratuito, poi la verifica manuale: tastiera, screen reader, contrasti, contenuti. A fine audit il prezzo è chiuso e la data è fissata.` |
  | `SETTIMANA 2` | `Correzioni` | `Sistemiamo tema, contrasti, etichette dei moduli, gerarchia dei titoli e navigazione da tastiera. Ogni barriera dell'elenco, una per una.` |
  | `SETTIMANA 3` | `Dichiarazione e verifica` | `Pubblichiamo la dichiarazione di accessibilità obbligatoria e ripetiamo l'audit per confermare la conformità WCAG 2.1 AA.` |
- **note sotto la sezione:** `Tempi indicativi per un sito aziendale o vetrina. Un e-commerce con catalogo ampio può richiedere più tempo: lo scriviamo nel preventivo, con la stessa penale.`

### Prezzo (`prezzo_range` + `prezzo_lede` + `prezzo_note`)
- **prezzo_range:** `da € 1.900`
- **prezzo_lede:** `Prezzo chiuso nel preventivo dopo l'audit, da € 1.900. Consegna in 3 settimane, data fissa in contratto. Fattura elettronica, pagamento in tre tranche.`
- **prezzo_note (Cosa fa variare il prezzo):**
  1. `Numero di pagine e modelli (template) da correggere: una vetrina costa meno di un e-commerce a catalogo.`
  2. `Stato di partenza: quante barriere emergono dall'audit iniziale.`
  3. `Contenuti da rifare — testi alternativi, PDF accessibili, sottotitoli ai video.`
- **link contestuale (inserito nella sezione prezzo):** `Non sai da dove partire? L'audit automatico è gratuito → /strumenti/verifica-accessibilita/`

### Garanzie (блок как в линейке — механика неустойки, реюз `sr-garanzie`/`checklist`)
- **heading:** `Nero su bianco, come per ogni nostro servizio`
- **garanzie:**
  1. `± 0 giorni di ritardo — la data è nel contratto: ogni giorno lavorativo di ritardo vale l'1% di sconto.`
  2. `Prezzo chiuso dopo l'audit — quello che firmate è quello che pagate; ogni extra si concorda per iscritto prima.`
  3. `Standard dichiarato — conformità WCAG 2.1 AA verificata a mano, non solo un punteggio automatico.`
  4. `Dichiarazione di accessibilità inclusa — il documento richiesto dalla norma, pubblicato sul vostro sito.`

### FAQ (4 domande — реюз `details_faq`)
1. **`Chi è obbligato dall'EAA? La mia azienda rientra?`**
   `L'European Accessibility Act è in vigore in Italia dal 28 giugno 2025 e obbliga molti siti che vendono beni o servizi ai consumatori: e-commerce, banche, trasporti, servizi digitali. Sono esentate le microimprese che erogano servizi — meno di 10 persone e meno di 2 milioni di euro di fatturato annuo. Nel dubbio verifichiamo il vostro caso prima di firmare: se non siete obbligati, ve lo diciamo.`
2. **`Quali sanzioni sono previste in Italia?`**
   `Il decreto italiano prevede sanzioni fino al 5% del fatturato per i servizi non conformi. In Francia sono già partite le prime cause verso i grandi rivenditori online, e in Italia l'applicazione è appena cominciata. Le fonti sono pubbliche: la guida di Bird & Bird e il centro AccessibleEU della Commissione europea (link in fondo alla pagina).`
3. **`Cos'è la dichiarazione di accessibilità?`**
   `È un documento pubblico, richiesto dalla norma, in cui il sito dichiara il proprio livello di conformità, le eventuali parti non ancora accessibili e un contatto per segnalare problemi. Lo redigiamo e lo pubblichiamo noi, come parte del servizio: senza dichiarazione, il sito non è a norma anche se tecnicamente accessibile.`
4. **`Basta un controllo automatico per essere conformi?`**
   `No, ed è giusto dirlo chiaro. Un test automatico come il nostro strumento gratuito intercetta circa un terzo dei criteri WCAG: quello che una macchina sa misurare. Il resto — navigazione da tastiera, esperienza con screen reader, chiarezza dei contenuti — si verifica solo a mano. Per questo l'audit manuale è il cuore del servizio, non un optional.`

### CTA finale (dark)
- **heading:** `Facciamo il punto sul vostro sito`
- **testo:** `L'audit iniziale trasforma l'obbligo in una lista di cose da fare, con prezzo chiuso e data di consegna. Il primo controllo automatico è gratuito e senza registrazione.`
- **buttons:** `Richiedi l'audit di accessibilità` → `/#contatti` · (outline) `Prova lo strumento gratuito` → `/strumenti/verifica-accessibilita/`

### E-E-A-T — fonti e disclaimer (riga note a piè di pagina o dentro la sezione FAQ)
- `European Accessibility Act (dir. UE 2019/882), in vigore in Italia dal 28 giugno 2025.`
- `Sanzioni fino al 5% del fatturato per i servizi non conformi (recepimento italiano).`
- Fonti citate (link esterni, `rel="nofollow"` a scelta):
  - Bird & Bird — *A guide to navigating the European Accessibility Act* — https://www.twobirds.com/en/insights/2025/a-guide-to-navigating-the-european-accessibility-act-for-online-retailers-service-providers-and-plat
  - AccessibleEU (Commissione europea) — *The EAA comes into effect June 2025* — https://accessible-eu-centre.ec.europa.eu/content-corner/news/eaa-comes-effect-june-2025-are-you-ready-2025-01-31_en
- Standard di riferimento: **WCAG 2.1 livello AA**.
- Disclaimer onesto (uguale allo strumento): `Un controllo automatico copre parte dei criteri WCAG 2.1 AA. La conformità piena richiede la verifica manuale, che è inclusa in questo servizio.`

---

## 4. Полный контент услуги — EN (madrelingua, числа US-формата `€ 1,900`)

### hero
- **eyebrow:** `Service / EAA compliance`
- **hero_title (H1):** `Your website compliant with the European Accessibility Act, in 3 weeks`
- **hero_sub:** `Since 28 June 2025 accessibility is a legal requirement for many websites. We bring yours up to the WCAG 2.1 AA standard — audit, fixes and accessibility statement — at a fixed price, with the date in the contract.`
- **hero_stat_value:** `28 Jun 2025`
- **hero_stat_label:** `The date the European Accessibility Act took effect in Italy. The first fines are only a matter of time.`
- **CTA:** `Request the accessibility audit` → `/en/#contatti` · (outline) `Check your site now` → `/en/tools/accessibility-check/`

### Who it's for (`per_chi`)
- **per_chi_heading:** `The duty applies to those who sell to consumers, online`
- **per_chi:**
  1. `E-commerce and digital services selling goods or services to consumers in the EU.`
  2. `Banks, insurers, transport, ticketing and online booking systems.`
  3. `Non-micro companies facing the first Italian fines, or already flagged for non-compliance.`

### What's included (`include`)
- **include_heading:** `From audit to statement, all spelled out in the quote`
- **include:**
  1. `Full audit: automated test (Lighthouse) plus manual review — keyboard, screen reader, content.`
  2. `Fixes to theme, contrast, form labels and heading structure.`
  3. `Keyboard navigation and a visible focus state on every interactive element.`
  4. `A published accessibility statement, the document the law requires.`
  5. `A final verification audit against the WCAG 2.1 AA standard, once fixes are done.`
  6. `Fixed price after the audit, delivery in 3 weeks with a contractual penalty.`

### The 3 weeks, step by step (`processo`)
- **heading:** `Three weeks, from diagnosis to compliance`
- **processo:**
  | Week | Step | Text |
  |---|---|---|
  | `WEEK 1` | `Audit` | `We start from the free automated test, then the manual review: keyboard, screen reader, contrast, content. By the end of the audit the price is fixed and the date is set.` |
  | `WEEK 2` | `Fixes` | `We correct theme, contrast, form labels, heading hierarchy and keyboard navigation. Every barrier on the list, one by one.` |
  | `WEEK 3` | `Statement and verification` | `We publish the required accessibility statement and re-run the audit to confirm WCAG 2.1 AA compliance.` |
- **note:** `Indicative timing for a business or brochure site. A large-catalogue e-commerce may take longer: we write it in the quote, with the same penalty.`

### Price
- **prezzo_range:** `from € 1,900`
- **prezzo_lede:** `Fixed price locked in the quote after the audit, from € 1,900. Delivery in 3 weeks, date fixed in the contract. E-invoicing, payment in three installments.`
- **prezzo_note (What changes the price):**
  1. `Number of pages and templates to fix: a brochure site costs less than a catalogue e-commerce.`
  2. `Starting point: how many barriers the initial audit reveals.`
  3. `Content to redo — alt text, accessible PDFs, video captions.`
- **contextual link:** `Not sure where to start? The automated audit is free → /en/tools/accessibility-check/`

### Guarantees (`garanzie`)
- **heading:** `In writing, like every service we deliver`
- **garanzie:**
  1. `± 0 days late — the date is in the contract: every working day of delay is 1% off.`
  2. `Fixed price after the audit — what you sign is what you pay; any extra is agreed in writing first.`
  3. `A declared standard — WCAG 2.1 AA compliance verified by hand, not just an automated score.`
  4. `Accessibility statement included — the document the law requires, published on your site.`

### FAQ (4)
1. **`Who is required to comply with the EAA? Does my company qualify?`**
   `The European Accessibility Act took effect in Italy on 28 June 2025 and covers many sites selling goods or services to consumers: e-commerce, banks, transport, digital services. Micro-enterprises providing services are exempt — fewer than 10 people and under € 2 million in annual turnover. If in doubt we check your case before signing: if you're not required to comply, we tell you.`
2. **`What fines apply in Italy?`**
   `The Italian decree sets fines of up to 5% of turnover for non-compliant services. In France the first lawsuits against large online retailers have already begun, and enforcement in Italy has just started. The sources are public: the Bird & Bird guide and the European Commission's AccessibleEU centre (links at the bottom of the page).`
3. **`What is an accessibility statement?`**
   `It's a public document, required by the law, in which the site declares its level of compliance, any parts not yet accessible, and a contact for reporting problems. We write and publish it as part of the service: without a statement a site isn't compliant, even if technically accessible.`
4. **`Is an automated check enough to be compliant?`**
   `No, and it's fair to say so plainly. An automated test like our free tool catches roughly a third of the WCAG criteria: what a machine can measure. The rest — keyboard navigation, screen-reader experience, content clarity — can only be checked by hand. That's why the manual audit is the core of this service, not an add-on.`

### CTA finale (dark)
- **heading:** `Let's take stock of your website`
- **testo:** `The initial audit turns the legal duty into a to-do list, with a fixed price and delivery date. The first automated check is free and needs no sign-up.`
- **buttons:** `Request the accessibility audit` → `/en/#contatti` · (outline) `Try the free tool` → `/en/tools/accessibility-check/`

### E-E-A-T (EN)
- `European Accessibility Act (EU Directive 2019/882), in effect in Italy since 28 June 2025.`
- `Fines up to 5% of turnover for non-compliant services (Italian transposition).`
- Same two sources (Bird & Bird, AccessibleEU). Standard: **WCAG 2.1 level AA**.
- Disclaimer: `An automated check covers part of the WCAG 2.1 AA criteria. Full compliance requires manual review, which is included in this service.`

---

## 5. Полный контент услуги — RU (автономный текст, угол «бизнес в ЕС»)

> Русскоязычная аудитория №1 (`copy-fase-B.md`): бизнес, уже работающий в Европе или выходящий на рынок ЕС.
> Ключевая мысль: **EAA касается и вашего сайта, если он продаёт в ЕС** — вне зависимости от того, где вы
> зарегистрированы. Форма «вы» со строчной, литературный русский, деньги `€ 1 900` (пробел-тысячник).

### hero
- **eyebrow:** `Услуга · Доступность и EAA`
- **hero_title (H1):** `Сайт по European Accessibility Act — за 3 недели`
- **hero_sub:** `С 28 июня 2025 года доступность сайта — требование закона ЕС. Если вы продаёте товары или услуги в Европе, оно касается и вас. Приводим сайт к стандарту WCAG 2.1 AA — аудит, исправления и декларация о доступности — по фиксированной цене, со сроком в договоре.`
- **hero_stat_value:** `28.06.2025`
- **hero_stat_label:** `Дата вступления European Accessibility Act в силу. Первые штрафы в ЕС — вопрос времени.`
- **CTA:** `Запросить аудит доступности` → `/ru/#contatti` · (outline) `Проверить сайт сейчас` → `/ru/instrumenty/proverka-dostupnosti/`

### Для кого это (`per_chi`)
- **per_chi_heading:** `Обязанность касается тех, кто продаёт потребителям в ЕС`
- **per_chi:**
  1. `Интернет-магазины и цифровые сервисы, продающие товары или услуги потребителям в Евросоюзе.`
  2. `Онлайн-бронирование, билеты, финансовые и транспортные сервисы для европейского клиента.`
  3. `Русскоязычный бизнес с сайтом для рынка ЕС: закон смотрит на рынок и аудиторию, а не на страну регистрации.`

### Что входит (`include`)
- **include_heading:** `От аудита до декларации — всё прописано в договоре`
- **include:**
  1. `Полный аудит: автоматический тест (Lighthouse) плюс ручная проверка — клавиатура, скринридер, контент.`
  2. `Исправление темы, контрастов, подписей к полям форм и структуры заголовков.`
  3. `Навигация с клавиатуры и всегда видимый фокус на интерактивных элементах.`
  4. `Опубликованная декларация о доступности — документ, которого требует закон.`
  5. `Финальный аудит-подтверждение по стандарту WCAG 2.1 AA — после исправлений.`
  6. `Фиксированная цена после аудита, сдача за 3 недели с неустойкой в договоре.`

### Три недели, шаг за шагом (`processo`)
- **heading:** `Три недели — от диагностики до соответствия`
- **processo:**
  | Неделя | Шаг | Текст |
  |---|---|---|
  | `НЕДЕЛЯ 1` | `Аудит` | `Начинаем с бесплатного автоматического теста, затем ручная проверка: клавиатура, скринридер, контрасты, контент. По итогам аудита цена зафиксирована, дата назначена.` |
  | `НЕДЕЛЯ 2` | `Исправления` | `Приводим в порядок тему, контрасты, подписи к формам, иерархию заголовков и навигацию с клавиатуры. Каждый барьер из списка, по очереди.` |
  | `НЕДЕЛЯ 3` | `Декларация и проверка` | `Публикуем обязательную декларацию о доступности и повторяем аудит, подтверждая соответствие WCAG 2.1 AA.` |
- **note:** `Ориентировочный срок для сайта-визитки или корпоративного сайта. Интернет-магазину с большим каталогом может понадобиться больше времени — мы пропишем это в смете, с той же неустойкой.`

### Цена
- **prezzo_range:** `от € 1 900`
- **prezzo_lede:** `Цена фиксируется в смете после аудита, от € 1 900. Сдача за 3 недели, дата стоит в договоре. Оплата в евро, инвойс для юрлиц ЕС.`
- **prezzo_note (Из чего складывается цена):**
  1. `Число страниц и шаблонов для правки: визитка дешевле магазина с каталогом.`
  2. `Отправная точка: сколько барьеров вскроет первичный аудит.`
  3. `Контент под переделку — альт-тексты, доступные PDF, субтитры к видео.`
- **контекстная ссылка:** `Не знаете, с чего начать? Автоматический аудит — бесплатно → /ru/instrumenty/proverka-dostupnosti/`

### Гарантии (`garanzie`)
- **heading:** `Чёрным по белому, как и во всех наших услугах`
- **garanzie:**
  1. `± 0 дней просрочки — дата стоит в договоре: каждый рабочий день опоздания — минус 1% от суммы.`
  2. `Фиксированная цена после аудита — сколько подписали, столько и платите; любые доработки согласуем письменно заранее.`
  3. `Заявленный стандарт — соответствие WCAG 2.1 AA проверяется вручную, а не только автоматической оценкой.`
  4. `Декларация о доступности включена — документ, которого требует закон, публикуем на вашем сайте.`

### FAQ (4)
1. **`Кого касается EAA и касается ли он меня, если я не в ЕС?`**
   `European Accessibility Act действует с 28 июня 2025 года и охватывает многие сайты, продающие товары или услуги потребителям в Евросоюзе: интернет-магазины, банки, транспорт, цифровые сервисы. Закон смотрит на рынок, а не на страну регистрации: если ваш сайт обслуживает клиентов в ЕС, он под действие попадает. Освобождены микропредприятия, оказывающие услуги, — меньше 10 человек и менее 2 млн евро годового оборота. Если сомневаетесь, мы проверим ваш случай до подписания договора.`
2. **`Какие штрафы предусмотрены?`**
   `Итальянский закон предусматривает штрафы до 5% оборота за несоответствующие услуги — это одна из самых строгих ставок в ЕС. Во Франции уже начались первые иски к крупным онлайн-ритейлерам. Источники открытые: разбор Bird & Bird и центр AccessibleEU Еврокомиссии (ссылки внизу страницы).`
3. **`Что такое декларация о доступности?`**
   `Это публичный документ, которого требует закон: сайт заявляет свой уровень соответствия, перечисляет ещё недоступные части и указывает контакт для жалоб. Мы составляем и публикуем его как часть услуги — без декларации сайт не считается соответствующим, даже если технически доступен.`
4. **`Достаточно ли автоматической проверки, чтобы пройти по закону?`**
   `Нет, и честнее сказать об этом прямо. Автоматический тест — как наш бесплатный инструмент — ловит около трети критериев WCAG: то, что способна измерить машина. Остальное — навигация с клавиатуры, работа со скринридером, понятность контента — проверяется только вручную. Поэтому ручной аудит — сердце услуги, а не дополнительная опция.`

### CTA finale (dark)
- **heading:** `Разберёмся с вашим сайтом`
- **testo:** `Первичный аудит превращает требование закона в понятный список задач — с фиксированной ценой и датой сдачи. Первая автоматическая проверка бесплатна и без регистрации.`
- **buttons:** `Запросить аудит доступности` → `/ru/#contatti` · (outline) `Попробовать бесплатный инструмент` → `/ru/instrumenty/proverka-dostupnosti/`

### RU-угол — связка с лендингом «Сайт для Европы»
Отдельная строка-ссылка в теле услуги (после блока «Для кого это» или в CTA-зоне):
`Выходите на рынок ЕС с нуля? Доступность закладывается сразу → /ru/uslugi/sajt-dlya-evropy/`
И обратная ссылка на лендинге 1 (`ru-sajt-dlya-evropy.php`, секция 3 «Юридическая часть под ЕС») — см. раздел 6.

### E-E-A-T (RU)
- `European Accessibility Act (Директива ЕС 2019/882), действует в Италии с 28 июня 2025 года.`
- `Штрафы до 5% оборота за несоответствующие услуги (итальянская имплементация).`
- Те же два источника (Bird & Bird, AccessibleEU). Стандарт: **WCAG 2.1 уровень AA**.
- Оговорка: `Автоматическая проверка охватывает часть критериев WCAG 2.1 AA. Полное соответствие требует ручного аудита — он входит в услугу.`

---

## 6. Перелинковка (отдельным списком для имплементатора)

**Входящие ссылки НА услугу (откуда):**
1. `strumento-verifica-accessibilita` (IT) — CTA + «come migliorare» + hero-link инструмента-лидогенератора → `/servizi/adeguamento-eaa/`. Сейчас ведут на `/servizi/siti-aziendali/` — перенаправить (см. раздел 7, точка 5).
2. `en-strumento-verifica-accessibilita` → `/en/services/eaa-compliance/`.
3. `ru-strumento-verifica-accessibilita` → `/ru/uslugi/dostupnost-eaa/`.
4. `servizio-siti-aziendali` и `servizio-e-commerce` (IT/EN/RU) — в секции prezzo уже есть строка «Obbligo di accessibilità (EAA dal 2025): verifica il vostro sito» → инструмент (`SERVICE_TOOL_LINKS` в `generate_pages.py`). Рекомендуется добавить второй линк прямо на услугу: `Adeguamento EAA: audit, correzioni e dichiarazione → /servizi/adeguamento-eaa/`.
5. `servizi-index` / home `servizi-cards` — добавить карточку услуги (см. раздел 7, точка 4).
6. RU: лендинг `ru-sajt-dlya-evropy` (секция 3 «Юридическая часть под ЕС — уже внутри») — добавить строку-ссылку `Обязательная доступность по EAA: приводим сайт к стандарту → /ru/uslugi/dostupnost-eaa/`.
7. `prezzi` / `/en/pricing/` / `/ru/ceny/` — НЕ вставлять EAA в основную сравнительную таблицу (она про продукты «визитка/корпоративный/магазин», а EAA — adeguamento). Вместо этого одна строка-примечание под таблицей: `Sito già online? L'adeguamento all'European Accessibility Act è un servizio a sé → /servizi/adeguamento-eaa/`. **Решение владельца: показывать ли отдельную строку в прайсе — см. «Спорные места».**

**Исходящие ссылки С услуги (куда):**
- → инструмент `verifica-accessibilita` (audit — первый шаг; строка в prezzo + CTA-outline). Двунаправленно.
- → `/servizi/siti-aziendali/` и `/servizi/e-commerce/` («per chi già ha un sito da adeguare» — услуги-соседи).
- → `/prezzi/` («Confronta tutte le tariffe», как у типовых услуг).
- RU → `/ru/uslugi/sajt-dlya-evropy/` (см. выше).

---

## 7. Для имплементатора — точный чеклист изменений (в репо, вне режима read-only этой задачи)

> Все пути от корня репо. Ветка `claude/new-project-prep-zhmkg5`. EAA — «специальная» услуга: у неё нет
> `mini_caso` (запрет выдуманных кейсов) и есть блоки `processo`/`garanzie`, которых нет в типовом
> `build_servizio`. Поэтому реализовывать по образцу `EXPORT_READY`/`WEB_APP`, а не добавлять в список `SERVICES`.

1. **`wordpress/build-tools/data.py`** — добавить модульный dict `ADEGUAMENTO_EAA = dict(...)` (по образцу `EXPORT_READY`) с полями:
   `slug='adeguamento-eaa'`, `title='Adeguamento EAA'`, `eyebrow`, `hero_title`, `hero_sub`, `hero_stat_value`,
   `hero_stat_label`, `per_chi_heading`, `per_chi[]`, `include_heading`, `include[]`, `processo=[(settimana, passo, testo)…]`,
   `processo_note`, `prezzo_range='da € 1.900'`, `prezzo_lede`, `prezzo_note[]`, `garanzie_heading`, `garanzie[]`,
   `faq=[(q,a)×4]`, `fonti[]` (Bird&Bird, AccessibleEU), `disclaimer`, `cta`. Контент — раздел 3 этого дека.
   Импортировать в `generate_pages.py` (`from data import … ADEGUAMENTO_EAA`).
   **Плюс** обновить существующий инструмент `TOOLS`→`slug='verifica-accessibilita'` (строки ~557–572):
   - `migliorare.links` → `[('Vogliamo sistemarle noi: audit, correzioni e dichiarazione — servizio Adeguamento EAA', '/servizi/adeguamento-eaa/')]`
   - `cta.buttons[1]` → `('Scopri il servizio Adeguamento EAA', '/servizi/adeguamento-eaa/', 'outline')`
   (EN/RU-варианты этих строк подтянутся конвейером перевода / вносятся вручную в RU по разделам 4–5.)

2. **`wordpress/build-tools/generate_pages.py`** — добавить `build_adeguamento_eaa()` (по образцу `build_export_ready`:
   hero + per_chi + include(checklist) + processo(week-chips/grid) + garanzie(checklist) + prezzo + faq(details_faq) + fonti + cta),
   вызвать в `main()` рядом с `build_export_ready()`/`build_web_app()`. `write('servizio-adeguamento-eaa', …)`.
   EN/RU-паттерны: либо ручные файлы `en-servizio-adeguamento-eaa.php` / `ru-servizio-adeguamento-eaa.php`
   (RU — автономный текст раздела 5, НЕ прогонять `translate_pages.py ru`), либо конвейер EN (`translate_pages.py en`).

3. **`wordpress/build-tools/lang.py`** — в `SERVICES_SLUGS` добавить:
   `'adeguamento-eaa': {'en': 'eaa-compliance', 'ru': 'dostupnost-eaa'},`
   затем `python3 lang.py` → перегенерит `inc/lang-map.php` (hreffang IT↔EN↔RU).

4. **`wordpress/build-tools/deploy-import.php`** — в `$page_map` добавить три строки:
   - `'servizio-adeguamento-eaa' => array( 'adeguamento-eaa', 'servizi', 'Adeguamento EAA' ),`
   - `'en-servizio-adeguamento-eaa' => array( 'eaa-compliance', 'en/services', 'EAA compliance' ),`
   - `'ru-servizio-adeguamento-eaa' => array( 'dostupnost-eaa', 'ru/uslugi', 'Доступность и EAA' ),`
   `$current_slugs` пополнять НЕ нужно (он строится из `wp_list_pluck($page_map, 0)` — новые слаги попадут сами).
   Услуги — дети `servizi/services/uslugi`, отдельно в меню не заводятся (главное меню = разделы верхнего уровня).

5. **CTA инструмента-лидогенератора** — после правок `data.py` (точка 1) и `python3 generate_pages.py`
   перегенерятся `strumento-verifica-accessibilita.php` (и EN/RU) с новыми ссылками на услугу. Проверить, что
   `/servizi/siti-aziendali/` в этих трёх файлах больше не фигурирует как цель CTA доступности.

6. **Карточка услуги в каталоге** — EAA не входит в список `SERVICES`, поэтому в сетке `build_servizi_index()`
   и в `servizi-cards.php` (home) не появится сама. Добавить её карточку в premium-блок «Oltre il sito»
   (`build_servizi_index`, рядом с Export Ready / Web app) с текстом:
   IT `Adeguamento EAA` / `Il vostro sito già online, portato allo standard WCAG 2.1 AA: audit, correzioni e dichiarazione di accessibilità. Obbligo di legge dal 2025.` → `/servizi/adeguamento-eaa/`.
   На главной (`servizi-cards.php` IT/EN; RU `servizi-cards.php` — фаза B, свой набор) — решение владельца, добавлять ли седьмую карточку (см. «Спорные места»).

7. **`docs/seo-meta.md`** — добавить строки в таблицу «Карта фокус-ключей (IT/EN)» и RU-раздел + три блока Title/Description из раздела 2 этого дека (IT/EN/RU), по образцу существующих сервисных строк.

8. **Деплой** (владельцу, после сборки): контент `patterns/**` живёт в БД → нужен цикл
   `REMARKA_FORCE=1 wp eval-file …/deploy-import.php`; статика темы — обычной синхронизацией.

---

## 8. Резюме и спорные места (для владельца)

**Что готово:** полный трёхъязычный дек новой услуги «Adeguamento EAA» под структуру генератора
(hero, per chi, 6 bullets «cosa include», процесс по 3 неделям, 4 гарантии с механикой неустойки 1%/день,
prezzo `da € 1.900` prezzo chiuso после аудита, 4 FAQ по ТЗ, CTA, E-E-A-T с источниками Bird&Bird/AccessibleEU
и WCAG 2.1 AA, честная оговорка о границах автопроверки). RU — автономный, с углом «бизнес в ЕС» и связкой
с лендингом `sajt-dlya-evropy`. Перелинковка и чеклист имплементатора приложены.

**Финальные слаги:** IT `/servizi/adeguamento-eaa/` · EN `/en/services/eaa-compliance/` · RU `/ru/uslugi/dostupnost-eaa/`.

**Фокус-ключи:** IT `adeguamento EAA` · EN `EAA compliance` · RU `доступность сайта по EAA`.

**Требует решения владельца:**
1. **Прайс.** Показывать ли EAA отдельной строкой/примечанием на `/prezzi/` (и `/en/pricing/`, `/ru/ceny/`)
   или оставить только внутри карточек услуг и инструмента. Я рекомендую примечание-ссылку под таблицей,
   без строки в самой сравнительной таблице (EAA — adeguamento, а не новый сайт).
2. **Карточка на главной.** Добавлять ли седьмую карточку услуги в `servizi-cards.php` на главной, или
   ограничиться premium-блоком в каталоге `/servizi/` и перелинковкой из инструмента. RU-главная — фаза B,
   там свой набор карточек (без EAA по умолчанию); если EAA нужна и там — это правка фазы B.
3. **hero_stat.** Я поставил «дату вступления EAA» как число-крючок вместо продуктового LCP (у adeguamento
   нет замера скорости). Если хотите единообразия с линейкой — заменить на, например, `≈ 30%` (доля критериев
   WCAG, покрываемых автопроверкой) с честной подписью. Оставил дату как более сильный триггер спроса.
4. **Микропредприятия.** В FAQ дан порог освобождения «<10 чел. / <€2 млн» из `ricerca-strumenti-lab.md`.
   Формулировка «esenzione per le microimprese che erogano servizi» — уточнить у юриста точный периметр
   исключения перед публикацией (в тексте уже есть оговорка «verifichiamo il vostro caso prima di firmare»).
5. **EN/RU реализация.** EN можно через конвейер `translate_pages.py en`; RU — вручную по разделу 5
   (правило фазы: `translate_pages.py ru` не запускать, RU-файлы не регенерировать автопереводом).

**Напоминание:** файл лежит в scratchpad (`…/scratchpad/copy-eaa.md`). В репозиторий я ничего не вносил,
git не трогал — внесение в репо выполняет оркестратор.
