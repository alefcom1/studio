# Фаза A — перепозиционирование IT + EN: план реализации для агентов

## Статус выполнения

Ветка `claude/new-project-prep-zhmkg5`. Все этапы 1–4 выполнены 14.07.2026.

| Этап | Состав | Коммиты |
|---|---|---|
| 1. Копирайт (WP-1) | Финальные тексты IT/EN всех новых/изменяемых блоков → `docs/copy-fase-A.md` | `38ee7b4` (план), `cdf6f39` (copy deck) |
| 2. Реализация (WP-3…WP-6) | CSS-компоненты, IT-паттерны главной (hero-таймлайн, 4-я гарантия, tre-numeri, week-chips, Lingue e mercati), страница `/prezzi/` с таблицей noi-vs-mercato, полное EN-зеркало | `284e69d` (IT-главная), `c280fc3` (prezzi + EN-зеркало) |
| 3. Сквозные тесты (WP-7) | `php -l`/CSS/JS-проверки всех изменённых файлов, Playwright-скрины IT/EN главной и prezzi (1440/800/390), регрессия 3-шаговой формы заявки, сквозные грепы на противоречия сроков | этот коммит (consistency pass) |
| 4. Документация (WP-8) | Статус в `strategia-riposizionamento.md` и `piano-contenuti-seo.md`, устранение найденных противоречий контента (FAQ IT/EN, `consegna in` для siti-aziendali/e-commerce, US-формат цифр в EN FAQ) | этот коммит (consistency pass) |

Итог этапа 3 (устранение противоречий): FAQ (`patterns/faq.php`, `patterns/lang-en/faq.php`) и сервисные
страницы `siti-aziendali`/`e-commerce` приведены к контрактным срокам 2/3/6 недель; диапазоны PWA (5–8),
restyling (2–4), SEO tecnica (3–5), multilingue (4–6) и web-app (6–10) **сознательно не тронуты** —
решение владельца по ним ещё не принято.

---

> Дата: 14.07.2026. Основание: `strategia-riposizionamento.md` (решения Д-1…Д-5),
> ответы владельца: сроки **подтверждены** (vetrina 2 нед. / aziendale 3 нед. /
> e-commerce 6 нед., с неустойкой), таблица «noi vs mercato» — **публикуем**,
> hero продаёт **sito aziendale**, RU-версия — **отдельная фаза B** (самодостаточная
> воронка, не зависящая от IT/EN; упор: через бюро переводов выводим клиента
> на рынок Италии и Европы).
>
> Исполнители: **Opus** — копирайт, дизайн-чувствительные решения, EN-редактура
> уровня носителя, работа с генератором страниц. **Sonnet** — механическая
> имплементация по утверждённым текстам/макетам, CSS, тесты, прогоны, коммиты.

---

## 0. Правила для всех агентов (обязательные)

1. **Ветка:** `claude/new-project-prep-zhmkg5`. Коммиты — атомарные по пакетам,
   сообщения на английском, без упоминания моделей/ID.
2. **RU-файлы не трогать вообще:** `patterns/lang-ru/*`, `patterns/pages/ru-*.php`,
   RU-строки в `inc/multilang.php` НЕ редактировать и НЕ регенерировать
   (`translate_pages.py ru` НЕ запускать). RU — фаза B с нуля.
3. **Протокол проверки** (без исключений): PHP — `php -l` каждого изменённого файла;
   JS — parse-check `new Function(src)`; CSS — баланс скобок; визуально — рендер
   на **реальном** `remarka.css` через Playwright
   (`executablePath: '/opt/pw-browsers/chromium'`, `NODE_PATH=/opt/node22/lib/node_modules`),
   скриншоты 1440 / 800 / 390 px; логика — стаб-харнесс по образцу
   `scratchpad/test_form3.php` (WP-функции стабятся, тестируемые функции
   извлекаются из исходника).
4. **Известные грабли проекта** (все уже задокументированы, не наступать заново):
   - контент `patterns/**` живёт в БД как `post_content` → после правок нужен
     полный деплой-цикл `REMARKA_FORCE=1 wp eval-file deploy-import.php`;
     статика (`assets/**`, `functions.php`, `inc/**`) — обычной синхронизацией темы;
   - `wp eval-file file.php --force` не работает — только env `REMARKA_FORCE=1`;
   - точечный `curl` с raw.githubusercontent.com — **только по SHA коммита**;
   - слаги `home`, `en`, `ru` защищены от orphan-sweep — список
     `$current_slugs` в `deploy-import.php` при добавлении страниц пополнять;
   - `[hidden]` перебивается `display` от `.wp-block-button__link` — в новых
     компонентах учитывать (`.sr-stepform [hidden]` — прецедент);
   - у `.sr-section` есть собственный фолбэк центрирования/паддингов —
     новые секции строить на `sr-section`/`sr-section--bianco`;
   - `translate_pages.py` падает с exit 1 при непереведённых итальянских
     узлах — это фича: пополнять словари, не подавлять отчёт.
5. **Гейты утверждения владельцем:** GATE-1 после макетов (WP-2),
   GATE-2 после полной сборки перед деплоем. Между гейтами не спрашивать.

---

## 1. Пакет копирайта (WP-1) — Opus

**Цель:** финальные тексты IT + EN всех новых/изменяемых блоков.
**Выход:** `docs/copy-fase-A.md` с парами IT/EN. Черновики ниже — Opus полирует
(тон: числа вместо прилагательных, «voi»-форма, без англицизмов в IT).

### 1.1. Hero (patterns/hero-home.php · lang-en/hero-home.php)

- H1 IT: `Il sito nuovo in 3 settimane. A prezzo chiuso.`
- Sub IT: `Consegna a data fissa con penale in contratto, prezzo bloccato alla firma, PageSpeed 90+ garantito. Siti in quattro lingue con redattori madrelingua, dal 2001.`
- H1 EN: `Your new website in 3 weeks. At a fixed price.`
- Sub EN: `Fixed delivery date with a contractual penalty, price locked at signing, PageSpeed 90+ guaranteed. Websites in four languages with native-speaking editors, since 2001.`
- Кнопки не меняются (Analizza… / Preventivo in 24 ore).
- Мелкий шрифт под кнопками (новый): IT `3 settimane: sito aziendale. Vetrina: 2. E-commerce: 6.` / EN `3 weeks: business website. Brochure site: 2. E-commerce: 6.`

### 1.2. Виджет hero справа — «таймлайн 21 giorno» (замена PageSpeed-виджета)

Карточка `sr-card`: заголовок mono `DALLA FIRMA ALL'ONLINE — 21 GIORNI`,
три строки-полосы (реюз компонента `sr-barra` + `data-sr-target`):
- `Settimana 1 — Analisi e design` (полоса 33%)
- `Settimana 2 — Sviluppo` (66%)
- `Settimana 3 — Contenuti, test, online` (100%)
Подпись: IT `La data è nel contratto: ogni giorno lavorativo di ritardo vale l'1% di sconto.` /
EN `The date is in the contract: every working day of delay is 1% off.`
PageSpeed-виджет из hero удаляется (инструмент остаётся на /strumenti/test-velocita/).

### 1.3. Tre numeri (patterns/tre-numeri.php)

| Число | Подпись IT | Пояснение IT |
|---|---|---|
| `3 settimane` | Dalla firma al sito online | Sito aziendale completo. La media di mercato: 6–10 settimane. |
| `± 0 giorni` | Di ritardo sulle consegne | Data fissa in contratto, penale dell'1% per giorno lavorativo. |
| `4` | Lingue native in ogni progetto | Italiano, inglese, tedesco e francese — redattori madrelingua, non plugin. |

(97 PageSpeed переезжает из tre-numeri в Nero su bianco, где уже есть 90+.)
EN — зеркально.

### 1.4. Garanzie «Nero su bianco» — 4-я плитка (patterns/garanzie-dark.php)

Новая плитка: число `€ 0`, титул IT `Sorprese in fattura`, текст
`Il prezzo firmato è il prezzo finale. Ogni extra si concorda per iscritto prima — o è a carico nostro.`
EN: `€ 0 / Invoice surprises / The signed price is the final price. Any extra is agreed in writing first — or it's on us.`
Порядок плиток: 90+ PageSpeed · ±0 gg · € 0 sorprese · 12 mesi.

### 1.5. Come lavoriamo → «Le 3 settimane, giorno per giorno» (patterns/come-lavoriamo.php)

Те же 5 шагов, сгруппированные чипами недель: `SETTIMANA 1` (Analisi, Preventivo
fisso, Design) · `SETTIMANA 2` (Sviluppo) · `SETTIMANA 3` (Consegna e assistenza).
Сноска: IT `Tempi del sito aziendale. Vetrina: 2 settimane. E-commerce: 6.` EN зеркально.

### 1.6. Таблица «noi vs mercato» (prezzi + тизер на главной)

Заголовок IT: `Prezzi e tempi, accanto a quelli di mercato.`
Вводка: `Le forbici di mercato vengono dai listini pubblici delle web agency italiane (2026). Le nostre cifre sono quelle del contratto.`

| Prodotto | Prezzo di mercato | Prezzo Remarka | Tempi di mercato | Tempi Remarka |
|---|---|---|---|---|
| Sito vetrina | € 1.000–3.000 | **€ 1.900–2.800** | 2–4 settimane | **2 settimane** |
| Sito aziendale | € 2.500–8.000 | **€ 3.900–5.800** | 6–10 settimane | **3 settimane** |
| E-commerce | € 6.000–25.000 | **€ 7.500–14.000** | 8–14 settimane | **6 settimane** |

Сноска-источник: ссылка на наш же блог-разбор цен (`/blog/quanto-costa-sito-aziendale-italia/`),
где рыночные вилки уже разобраны с источниками. На главной — компакт-версия
(3 строки, 2 колонки: mercato/Remarka) в prezzi-teaser.

### 1.7. Новый блок «Lingue e mercati» (новый паттерн lingue-mercati.php)

Eyebrow `Lingue`, H2 IT `Ogni lingua ha il suo redattore madrelingua.`,
вводка `Dal 2001 il gruppo Remarka lavora con la traduzione professionale: la versione estera del vostro sito non è un plugin, è un deliverable con nome e cognome.`
Сетка mono-кодов по группам: `UE — EN · DE · FR · ES` / `Nord America — EN-US` /
`CSI e Caucaso — RU · UK · KA · HY · KK`. Без флагов. CTA → /servizi/siti-multilingue/.
EN зеркально.

---

## 2. Пакеты реализации

### WP-2 · Макеты (Opus) → **GATE-1**

Собрать HTML-макеты на реальном CSS (метод: как `manifesto_mock.html` →
скриншоты 1440/390) для: hero+таймлайн, garanzie×4, come-lavoriamo с чипами
недель, таблица noi-vs-mercato (полная и тизер), lingue-mercati.
Отправить владельцу одним сообщением (SendUserFile). Ждать утверждения.

### WP-3 · CSS-компоненты (Sonnet, после GATE-1)

В `assets/css/remarka.css`, в конце соответствующих секций:
- `.sr-timeline` (hero-карточка недель: строки label+barra, реюз `.sr-barra`);
- `.sr-week-chip` (mono-чип недели в come-lavoriamo);
- `.sr-market-table` (таблица: рынок серым, Remarka — `--sr-inchiostro` жирным,
  на мобиле — горизонтальный скролл в контейнере, стиль как `.sr-price-table`);
- `.sr-langs` (сетка групп: mono-коды, разделители, тёмный+светлый фон);
- у garanzie проверить 4 колонки: на ≤782px — 2×2 (см. текущие правила
  `.sr-stat`/`wp-block-columns`).
Критерий: баланс скобок, ни одного inline-стиля, работает на carta и dark.

### WP-4 · IT-паттерны (Sonnet, после WP-3)

Правки по утверждённому копирайту:
- `patterns/hero-home.php` — H1/sub/мелкий шрифт, правая колонка → `sr-timeline`
  (PageSpeed-виджет и его wp:html удалить из hero);
- `patterns/tre-numeri.php`, `patterns/garanzie-dark.php` (4-я плитка),
  `patterns/come-lavoriamo.php` (чипы недель + сноска),
  `patterns/prezzi-teaser.php` (компакт-таблица);
- новый `patterns/lingue-mercati.php` (позиция на главной: после manifesto,
  перед servizi-cards);
- `build-tools/deploy-import.php`: добавить `lingue-mercati` в `$home_sections`
  (IT-массив; EN добавится в WP-6).
Проверка: `php -l` всё; прогон Playwright собранной главной из паттернов.

### WP-5 · Страница /prezzi/ (Opus)

1. Разведка: определить, генерируется ли `patterns/pages/prezzi.php` скриптом
   из `build-tools/data.py` (найти генератор в build-tools; если страница
   генерируемая — данные таблицы добавить в `data.py` и регенерить только её,
   если правится руками — править паттерн напрямую, зафиксировав это в шапке файла).
2. Вставить полную таблицу noi-vs-mercato после текущей сравнительной таблицы.
3. JSON-LD/наши мета не трогать.

### WP-6 · EN-зеркало (Opus — тексты, Sonnet — механика)

1. Ручные паттерны: обновить `patterns/lang-en/hero-home.php`, `tre-numeri`,
   `garanzie-dark`, `come-lavoriamo`, `prezzi-teaser`; создать
   `lang-en/lingue-mercati.php`. Тексты — из `docs/copy-fase-A.md`, Opus вычитывает
   как носитель (числа в EN — формат US: `€ 3,900–5,800`).
2. Генерируемая `en-prezzi`: пополнить `build-tools/i18n/corpus_en.json` (или
   `chrome_strings.py` — по типу строки) новыми парами, запустить
   `python3 translate_pages.py en`, добиться пустого отчёта непереведённого.
   **`translate_pages.py ru` НЕ запускать.**
3. `deploy-import.php`: `lingue-mercati` в EN-набор секций главной.
Проверка: Playwright-скрин EN-главной; грепом убедиться, что в EN-паттернах
не осталось итальянских строк (эвристика `ITALIAN_HINT` из translate_pages.py).

### WP-7 · Сквозные тесты (Sonnet) → **GATE-2**

- `php -l` всех изменённых файлов; JS parse; CSS-баланс;
- Playwright: IT-главная и EN-главная целиком (собрать из паттернов, как
  делалось для manifesto): 1440/800/390, скрин + console errors = 0;
- контроль регрессий: `[hidden]`-кнопки формы, отступы `sr-section`,
  манифест и фото на месте, футер-города на месте;
- собрать пакет скриншотов владельцу (SendUserFile) → GATE-2.

### WP-8 · Деплой-инструкция и документация (Sonnet, после GATE-2)

- Обновить `docs/strategia-riposizionamento.md` (статус фазы A → выполнена)
  и `piano-contenuti-seo.md` §4.1 (hero-формула изменена);
- финальный коммит+пуш; выдать владельцу команды деплоя:
  полная синхронизация темы + `REMARKA_FORCE=1 wp eval-file …` + жёсткий
  рефреш и чек-лист проверки (`/`, `/en/`, `/prezzi/`, `/en/pricing/`).

---

## 3. Фаза C (после A, отдельными задачами — Sonnet, Opus-ревью)

- Чипы «Consegnato in N settimane» в кейсах: поле `consegna_settimane` в
  `data.py` (Colombo 3 · Serralta 4 · TecnoIdraulica 3 · Fontana 2), регенерация
  4 кейс-страниц + caso-evidenza, EN-регенерация; **RU не трогать**.
- Статья IT+EN «Un sito in 3 settimane: come è possibile (e cosa firmiamo)» —
  по механике из come-lavoriamo, с ссылкой на гарантии.
- Обновить SEO-title/description главной под новый оффер (через Rank Math,
  инструкция владельцу).

## 4. Фаза B (RU) — рамка, детальный план отдельно

Принципы (утверждены владельцем): самодостаточная воронка, независимая от
IT/EN структуры; hero «Итальянская студия: сайт + вывод на рынок Италии и
Европы»; **приоритетная аудитория — русскоязычный бизнес, уже работающий в
Европе** (Италия, Германия, Испания и т.д.: рестораны, салоны, клиники, студии,
экспортно-импортные компании, услуги для диаспоры); бизнес из СНГ/Кавказа,
идущий в ЕС, — вторичная аудитория. Следствия для контента: примеры и кейсы —
европейские; юридические/практические темы блога — про ЕС (реквизиты, GDPR,
локальный Google), а не про выход из СНГ; SEO-семантика — «сайт для бизнеса в
Италии/Европе на русском», «продвижение в Google Италии», плюс языки диаспор
(армянский, грузинский) как расширение. Ядро оффера — бюро переводов с 2001 г.
как механизм локализации и выхода на итальянский/европейский рынок (сайт →
локализация носителями → SEO в стране назначения); собственные страницы услуг
и блога, собственная карта путей (`lang.py` расширить RU-специфичными
страницами, отсутствующими в IT/EN). Детальный план — после завершения фазы A.

---

## 5. Сводка назначения пакетов

| Пакет | Исполнитель | Зависимости | Гейт |
|---|---|---|---|
| WP-1 копирайт | Opus | — | — |
| WP-2 макеты | Opus | WP-1 | **GATE-1 (владелец)** |
| WP-3 CSS | Sonnet | GATE-1 | — |
| WP-4 IT-паттерны | Sonnet | WP-3 | — |
| WP-5 prezzi | Opus | WP-3 | — |
| WP-6 EN | Opus+Sonnet | WP-4, WP-5 | — |
| WP-7 тесты | Sonnet | WP-6 | **GATE-2 (владелец)** |
| WP-8 деплой/доки | Sonnet | GATE-2 | — |
