# SEO: тематические кластеры, каннибализация и план ранжирования

> Составлено 22.07.2026. Анализ сделан по фактическому контенту репозитория:
> `docs/seo-meta.md` (карта фокус-ключей), `build-tools/data.py` (39 статей
> блога с внутренними ссылками), `build-tools/lang.py` (карта страниц).
> Рынок таргетинга — **Италия (IT)**. EN/RU — зеркальные переводы под
> `/en/` и `/ru/`, разделены `hreflang`, поэтому **между языками
> каннибализации нет** — весь анализ ниже про IT-версию.

---

## 0. Резюме за 30 секунд

- Каннибализации «страница vs страница» в остром виде — **мало** (7 точек,
  из них 1 высокого риска). Это хорошо: фокус-ключи изначально разводились.
- Главная структурная проблема — **не каннибализация, а отсутствие
  верхних ссылок (pillar → cluster)**. Снизу вверх (статья → услуга)
  перелинковка уже есть в каждой статье. Сверху вниз (услуга/инструмент →
  свои статьи-спутники) — **нет почти нигде**. Именно это не даёт Google
  собрать «тематический авторитет» вокруг денежных страниц.
- Решение — не писать много нового, а **достроить кластерную архитектуру**
  на уже существующем контенте: 13 кластеров, у каждого один pillar,
  двусторонняя перелинковка, одна каноничная цель-запрос на страницу.
- Быстрые победы (Фаза 0–1) дают максимум эффекта при минимуме работы.

---

## 1. Методология (модель pillar–cluster)

1. **Один канонический запрос на страницу.** Каждая страница «владеет» ровно
   одним head-запросом. Денежные страницы (услуги, /prezzi/, инструменты)
   владеют коммерческими/транзакционными запросами; статьи блога — только
   информационным long-tail («cos'è», «come», «guida», «X vs Y»,
   «quanto costa ‹конкретная вертикаль›»). Пересечение = каннибализация.
2. **Pillar (столб)** — денежная страница, которую мы двигаем в топ. Она
   получает ссылки со всех статей своего кластера (это уже есть) **и сама
   ссылается вниз** на 4–8 лучших статей кластера блоком «Approfondimenti /
   Guide» (этого нет — главная работа).
3. **Cluster (спутники)** — статьи блога, которые раскрывают подтемы и
   передают релевантность своему pillar через анкор с ключом.
4. **Хабы** — индексные страницы (`/servizi/`, `/strumenti/`,
   `/dove-lavoriamo/`, `/blog/`) связывают кластеры между собой.
5. **Проверка на каннибализацию** = один URL на один запрос в Search Console.
   Если по запросу мигают два URL — переопределяем каноничную цель.

---

## 2. Каннибализация — горячие точки и что делать

| # | Запрос-конфликт | Страница A (оставляем pillar) | Страница B (переориентируем) | Риск | Решение |
|---|---|---|---|---|---|
| 1 | **sito per l'export / export** | `/servizi/export-ready/` — «sito web per l'export» | блог `sito-per-export` — «Export digitale: il sito che apre mercati esteri» | **выс.** | Статью переориентировать на инфо-long-tail «**vendere all'estero online: da dove iniziare**» (запрос «vendere all'estero», не «sito export»). H1/Title/estratto переписать, фокус увести от «sito export». Ссылка вверх на услугу — усилить анкор «sito multilingua per l'export». |
| 2 | **llms.txt** | `/strumenti/sito-pronto-ai/` + `/strumenti/generatore-llms-txt/` — инструменты | блог `llms-txt-cos-e` — «llms.txt: cos'è» | сред. | Инструмент владеет транзакционным «generatore/test llms.txt / sito pronto per l'AI»; статья — чисто информационным «llms.txt cos'è e a cosa serve». Убедиться, что на странице инструмента H1 не «cos'è». Статья канонично ссылается на инструмент (уже есть). |
| 3 | **quanto costa un sito** | `/prezzi/` — «quanto costa un sito web» (коммерческая) | блоги `quanto-costa-sito-aziendale-italia`, `quanto-costa-ecommerce-italia`, `preventivo-sito-web-come-leggerlo` | сред. | `/prezzi/` держит head «quanto costa un sito web / prezzi sito web». Блоги — по вертикалям («…sito aziendale», «…e-commerce») и «come leggere un preventivo». Проверить, что `/prezzi/` НЕ оптимизирована под конкретные вертикали. Все 3 статьи → CTA на `/prezzi/` (у 2 из 3 уже есть; добавить `quanto-costa-sito-aziendale-italia`). |
| 4 | **sito multilingua** | `/servizi/siti-multilingue/` — «sito web multilingua» | блоги `sito-quattro-lingue-costi-tempi`, `hreflang-sito-multilingue` | сред. | Услуга держит «sito multilingua». Статьи — «sito in quattro lingue: costi/tempi» (long-tail) и «hreflang» (техническая). Обе → услуга (у `hreflang` уже есть; добавить `sito-quattro-lingue`). |
| 5 | **restyling / rifacimento sito** | `/servizi/restyling-migrazione/` — «rifacimento sito web» | блоги `restyling-o-sito-nuovo-5-domande`, `migrare-wordpress-senza-perdere-seo` | низ.-сред. | Услуга держит «rifacimento/restyling». Статьи — «restyling o sito nuovo?» (решение) и «migrare WordPress senza perdere SEO» (техническая). Перелинковка есть. Только проследить, чтобы Title статей не начинались с «Rifacimento sito». |
| 6 | **Milano** | `/milano/` — «web agency Milano» | блог `seo-locale-milano` — «SEO locale a Milano» | низ.-сред. | Разные головы («web agency» vs «seo locale»). Оставляем обе, усиливаем взаимную ссылку `/milano/ ↔ seo-locale-milano` + обе → `/servizi/seo-tecnica/`. Не давать `/milano/` оптимизацию под «seo milano». |
| 7 | **check-up / velocità** | инструменты `/strumenti/test-velocita/`, `/strumenti/check-up-completo/` | блоги `sito-lento-cause-costi`, `check-up-sito-web-7-misure` | низ. | Инструмент = транзакционный виджет, статья = информ. Разный интент, риск мал. Просто держать анкоры разными. |

**Вывод по каннибализации:** остро — только пункт 1 (export). Остальное
решается уточнением Title/H1 и достройкой ссылок, без удаления страниц.
Ни одну страницу удалять/склеивать не нужно.

---

## 3. Карта тематических кластеров (13)

Обозначения: **PILLAR** — страница, которую двигаем; ⚙️ — инструмент Lab;
📄 — статья блога (спутник). «Дыра» = не хватает спутников под сильный pillar.

### C1 · Realizzazione siti aziendali (ядро)
- **PILLAR:** `/` (home, «realizzazione siti web») + `/servizi/siti-aziendali/` («sito web aziendale»)
- 📄 sito-web-in-3-settimane · hosting-sito-web-italia · manutenzione-wordpress · area-clienti-agenzia-web
- Дыра: мало «что входит в сайт / этапы / как выбрать агентство». +1–2 статьи.

### C2 · Prezzi e preventivi
- **PILLAR:** `/prezzi/` («quanto costa un sito web»)
- 📄 quanto-costa-sito-aziendale-italia · quanto-costa-ecommerce-italia · preventivo-sito-web-come-leggerlo
- Сильный кластер. Достроить `/prezzi/ → эти 3 статьи`.

### C3 · E-commerce
- **PILLAR:** `/servizi/e-commerce/` («realizzazione siti e-commerce»)
- 📄 quanto-costa-ecommerce-italia · european-accessibility-act-ecommerce (частично)
- **Дыра:** слабый кластер. +2 статьи («piattaforma e-commerce: quale scegliere», «e-commerce che vende: checklist»).

### C4 · Restyling e migrazione
- **PILLAR:** `/servizi/restyling-migrazione/` («rifacimento sito web»)
- 📄 restyling-o-sito-nuovo-5-domande · migrare-wordpress-senza-perdere-seo · check-up-sito-web-7-misure · impatto-ambientale-sito-web · gamification-b2b
- ОК.

### C5 · SEO tecnica & credibilità (E-E-A-T)
- **PILLAR:** `/servizi/seo-tecnica/` («SEO tecnica») + ⚙️ `/strumenti/analisi-seo/`
- 📄 eeat-come-google-giudica-credibilita · dati-strutturati-schema-org · migrare-wordpress-senza-perdere-seo · recensioni-riprova-sociale-onesta · copywriting-sito-web-prima-del-design
- ОК, богатый кластер.

### C6 · Multilingue & export
- **PILLAR:** `/servizi/siti-multilingue/` («sito web multilingua») + `/servizi/export-ready/` («sito web per l'export») + ⚙️ `/strumenti/roi-localizzazione/`
- 📄 sito-quattro-lingue-costi-tempi · hreflang-sito-multilingue · sito-per-export (см. каннибализацию #1)
- Действие: развести sito-per-export от pillar (пункт 1).

### C7 · Web app, gestionali & canali
- **PILLAR:** `/servizi/web-app/` («sviluppo web app»)
- 📄 gestionale-su-misura-vs-excel · telegram-mini-app-business · whatsapp-business-pmi · gamification-b2b · area-clienti-agenzia-web
- Хорошо поддержан кейсами (`/casi-studio/`). ОК.

### C8 · Performance, velocità & manutenzione
- **PILLAR:** ⚙️ `/strumenti/test-velocita/` + `/strumenti/check-up-completo/` (+ поддержка `/servizi/seo-tecnica/`)
- 📄 core-web-vitals-2026 · sito-lento-cause-costi · check-up-sito-web-7-misure · hosting-sito-web-italia · impatto-ambientale-sito-web · manutenzione-wordpress · monitoraggio-sito-dopo-lancio
- Самый насыщенный кластер. ОК.

### C9 · Privacy, GDPR & sicurezza (новый, батч 8)
- **PILLAR:** ⚙️ `/strumenti/check-gdpr/`
- 📄 consent-mode-v2-cosa-cambia · google-analytics-4-privacy-ue · alternative-google-analytics-privacy · cookie-policy-o-privacy-policy · cookie-banner-checklist-garante-2026 · backup-e-sicurezza-sito-web
- Сильный свежий кластер, каннибализации с деньгами нет. Достроить хаб на инструменте.

### C10 · Accessibilità & EAA
- **PILLAR:** `/servizi/adeguamento-eaa/` («adeguamento EAA») + ⚙️ `/strumenti/verifica-accessibilita/`
- 📄 european-accessibility-act-ecommerce · dichiarazione-di-accessibilita-guida-2026
- ОК.

### C11 · AI-readiness / GEO (llms.txt, ChatGPT)
- **PILLAR:** ⚙️ `/strumenti/sito-pronto-ai/` + `/strumenti/generatore-llms-txt/` + `/strumenti/sito-letto-dallai/`
- 📄 llms-txt-cos-e · farsi-trovare-da-chatgpt-geo
- Действие: развести llms-txt-cos-e и инструмент (пункт 2). +1 статья («GEO: ottimizzare per le risposte AI»).

### C12 · SEO locale / città
- **PILLAR:** `/dove-lavoriamo/` (хаб) + 17 city-страниц («realizzazione siti web ‹città›»)
- 📄 seo-locale-milano · google-business-profile-guida
- Города между собой не каннибализируют (гео-модификатор). Дыра: 2 статьи на 17 городов — мало. +2–3 гео-инфо-статьи («scheda Google per ‹settore›», «SEO locale per ristoranti/studi»).

### C13 · Conversione & fiducia
- **PILLAR:** `/servizi/siti-aziendali/` (та же, что C1) + лендинги
- 📄 perche-il-sito-non-converte · landing-page-che-converte · copywriting-sito-web-prima-del-design · recensioni-riprova-sociale-onesta
- ОК.

---

## 4. План работ (по фазам, от максимального ROI)

### Фаза 0 — Снять острую каннибализацию (≈ полдня)
1. Переориентировать статью **sito-per-export** (пункт 1): новый Title/H1/estratto
   на «vendere all'estero online», фокус-ключ увести от «sito export».
2. Проверить `/prezzi/` и `/strumenti/sito-pronto-ai/`: убрать из H1/Title
   пересечения с вертикальными/«cos'è» запросами (пункты 2–3).
3. Добавить недостающие ссылки статья→pillar: `quanto-costa-sito-aziendale-italia → /prezzi/`,
   `sito-quattro-lingue-costi-tempi → /servizi/siti-multilingue/`.
   *(Правки в data.py + seo-meta.md, регенерация точечная, EN-конвейер.)*

### Фаза 1 — Достроить верхнюю перелинковку pillar → cluster (ГЛАВНОЕ, ≈ 1–2 дня)
На каждую денежную страницу добавить блок **«Approfondimenti / Guide»** с
3–6 ссылками на статьи своего кластера (анкор = ключ статьи). Это то, чего
сейчас нет и что даёт основной прирост. Порядок по важности pillar:
`/` → C1 · `/servizi/siti-aziendali/` → C1+C13 · `/prezzi/` → C2 ·
`/servizi/seo-tecnica/` → C5 · `/servizi/web-app/` → C7 ·
`/strumenti/check-gdpr/` → C9 · `/servizi/restyling-migrazione/` → C4 ·
остальные услуги/инструменты → свои кластеры.
*(Реализация: новый паттерн-блок «cluster links» или шорткод
`[remarka_cluster slug="siti-aziendali"]`, данные — карта кластер→статьи.)*

### Фаза 2 — Закрыть дыры кластеров контентом (в очередь блога, батчи 9–12)
- C3 e-commerce: +2 статьи. C11 GEO: +1. C12 гео-инфо: +2–3.
  C1: +1–2 («cosa include un sito», «come scegliere un'agenzia web»).
- Приоритет — pillar с наибольшим коммерческим потенциалом и наименьшей
  поддержкой (e-commerce, export, PWA — у PWA сейчас 0 спутников).

### Фаза 3 — Хабы и навигация
- `/servizi/`, `/strumenti/`, `/dove-lavoriamo/`, `/blog/` — сделать
  настоящими хабами: явные ссылки на кластеры, хлебные крошки, «related».
- Мега-меню уже группирует услуги/инструменты/кейсы — добавить туда
  видимость кластеров блога по темам (norme/prestazioni/seo/…).

### Фаза 4 — Измерение и итерации (ежемесячно)
- Search Console по каждому pillar: позиция канонического запроса, нет ли
  второго URL на том же запросе (сигнал каннибализации).
- Отслеживать переходы pillar↔cluster, дочищать анкоры.
- Remarka Monitor уже считает здоровье страниц — подключить трекинг позиций.

---

## 5. Приоритеты (что делать первым)

| Приоритет | Действие | Усилие | Эффект |
|---|---|---|---|
| 🔴 1 | Фаза 0 (export + 2 проверки + 2 ссылки) | полдня | убирает единственный острый конфликт |
| 🔴 2 | Фаза 1 (pillar→cluster блоки) | 1–2 дня | **главный рычаг ранжирования** |
| 🟠 3 | Фаза 3 хабы + мега-меню | 1 день | распределение авторитета |
| 🟢 4 | Фаза 2 контент дыр (батчи блога) | по конвейеру | долгий рост охвата |
| 🟢 5 | Фаза 4 измерение | постоянно | контроль и итерации |

---

## 6. Принципы «на будущее» (чтобы не плодить каннибализацию)

- Новая статья блога **обязана** объявлять свой pillar и один long-tail
  запрос, отличный от head денежной страницы. Правило — в `docs/piano-blog.md`.
- Денежные страницы не берут информационные «cos'è/come/guida» запросы —
  их отдаём блогу и линкуем вниз.
- Города — только гео-модифицированные запросы; общий head держит `/`.
- Перед публикацией — проверка: нет ли уже страницы под этот запрос
  (греп фокус-ключей по `seo-meta.md` + заголовков по `data.py`).
