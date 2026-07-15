# Remarka Lab — план реализации всех инструментов (для агентов)

## Статус выполнения

Все этапы T1–T4 выполнены 14.07.2026.

| Этап | Состав | Коммиты |
|---|---|---|
| T1 | Движок: AJAX-эндпоинт `remarka_tool_fetch` (SSRF-защита, rate-limit), JS-каркас виджетов, i18n через data-атрибуты | `0b72c86` |
| T2 | IT: 7 страниц инструментов (генератор + `data.py`), `page_map` IT, IT-перелинковка | `f02da69` |
| T3 | EN/RU: конвейер EN (`translate_pages.py en`), RU — вручную, `page_map` EN/RU, меню, EN/RU-перелинковка | `522758c` |
| T4 | QA: функциональные прогоны, линк-аудит, регрессия, локализованные title 8 старых EN/RU записей `page_map`, SEO-мета 3 новых инструментов, документация | `907c941` |
| L1 | Lab-контент IT: 3 SEO-секции («Il metodo», «Leggere il risultato», «Come migliorare») на всех 7 IT-страницах инструментов — данные в `data.py`, рендер в `build_tool()` | `aad3f12` |
| L2 | Lab-контент EN/RU: EN — конвейером (`chrome_strings.py` +141 пара, включая 2 residui T3), RU — 3 секции руками на 7 `ru-strumento-*.php` (самодостаточный текст, ≥350 слов/страницу, RU-перелинковка услуги/блог/лендинги) | `907c941` (после T4) |
| L3 | 8-й инструмент «Segnali E-E-A-T» (модель скоринга: 8 сигналов → 4 асси → punteggio 0–100, docs/copy-eeat.md): JS-модуль `initEeatTool` + юнит-тесты скоринга, IT-страница (`data.py`+генератор), EN конвейером, RU руками, перелинковка (`seo-tecnica`→eeat, `sito-pronto-ai`↔eeat, `analisi-seo`↔eeat), `lang.py`/`lang-map.php`/`page_map` +1 инструмент | текущий коммит |

---

> Дата: 14.07.2026. Основание: `ricerca-strumenti-lab.md` (утверждено владельцем:
> «изготовить все инструменты, потом ссылки в меню и перелинковка»).
> §0 «Правила для всех агентов» из `piano-implementazione-fase-A.md` действуют.
> ⚠️ `translate_pages.py ru` ЗАПРЕЩЁН НАВСЕГДА (перезапишет ручные правки фазы B
> в ru-servizio-*/ru-prezzi). RU-контент — только руками. `translate_pages.py en`
> разрешён (en-страницы принадлежат конвейеру).

## 0. Итоговый состав: 8 инструментов на /strumenti/ (+ check-up completo /00)

| # | Инструмент (IT-slug) | Статус | Движок | EN-slug | RU-slug |
|---|---|---|---|---|---|
| 1 | test-velocita | ✅ работает | PSI performance | speed-test | test-skorosti |
| 2 | analisi-seo | оживить | PSI category=SEO | seo-audit | seo-audit |
| 3 | check-gdpr | оживить (v1) | PHP-fetch + эвристики | gdpr-check | proverka-gdpr |
| 4 | roi-localizzazione | оживить | JS-калькулятор | localization-roi | roi-lokalizacii |
| 5 | verifica-accessibilita | ✅ работает | PSI category=ACCESSIBILITY | accessibility-check | proverka-dostupnosti |
| 6 | sito-pronto-ai | ✅ работает | PHP-fetch (llms.txt/robots/schema) | ai-readiness | gotovnost-k-ii |
| 7 | impatto-co2 | ✅ работает | PSI byte-weight + модель SWD (co2.js) | website-carbon | uglerodnyj-sled |
| 8 | **segnali-eeat** | ✅ работает (L3) | PHP-fetch «html» + regex/JSON-LD, scoring 8 segnali→4 assi (docs/copy-eeat.md) | eeat-signals | signaly-eeat |

CTA инструментов → услуги: accessibilità→/#contatti (позже Adeguamento EAA),
analisi-seo/AI→seo-tecnica, co2→restyling-migrazione+test-velocita,
roi→siti-multilingue/export-ready, gdpr→siti-aziendali.

## 1. Техническая архитектура (этап T1)

### 1.1. PHP: AJAX-эндпоинт `remarka_tool_fetch` (functions.php)
Для GDPR- и AI-инструментов нужен серверный фетч чужих URL (CORS).
- `wp_ajax_(nopriv_)remarka_tool_fetch`: POST url + mode (`html` | `path:llms.txt`
  | `path:robots.txt`), nonce (реюз `remarka_contact`-паттерна не годится —
  свой nonce `remarka_tools`).
- **SSRF-защита (обязательно):** только http/https; резолв хоста и отказ, если
  IP приватный/зарезервированный (127/8, 10/8, 172.16/12, 192.168/16,
  169.254/16, 0/8, ::1, fc00::/7, fe80::/10); порты только 80/443; редиректы
  максимум 3 с перепроверкой каждого хоста (`wp_remote_get` c `redirection=0`,
  ручной цикл); таймаут 8с; ответ обрезать до 512КБ; Content-Type только text/*.
- Rate-limit по IP: transient, 10 запросов/мин (паттерн из remarka_form_process).
- Ответ: JSON {status, headers(ct), body(truncated)}. Анализ — на клиенте.
- Стаб-тесты обязательны (харнесс как test_form3.php): SSRF-кейсы (localhost,
  127.0.0.1, 10.x, домен-резолв в приватный IP — мокнуть), rate-limit, happy path.

### 1.2. JS (remarka.js): каркас инструментов
- `psiFetch(url)` расширить параметром categories: `&category=PERFORMANCE&category=ACCESSIBILITY&category=SEO` за один вызов; вернуть также
  `lighthouseResult.categories.{accessibility,seo}.score`,
  `audits['total-byte-weight'].numericValue`, топ-аудиты с score<0.9
  (id, title) для списков «что чинить».
- Диспетчер: `initToolWidgets()` → по `data-sr-tool="speed|seo|a11y|co2|gdpr|ai|roi"`.
- **i18n JS-строк**: вердикты/статусы сейчас захардкожены по-итальянски —
  вынести в `data-*`-атрибуты разметки страницы (каждая языковая страница несёт
  свои строки) ИЛИ в `window.remarkaTools` из PHP через remarka_str(). Выбрать
  data-атрибуты (проще, страница уже per-language). Обязательно: EN/RU-страницы
  инструментов показывают вердикты на своём языке.
- Модули:
  - **seo/a11y**: балл 0–100 (та же полоса-шкала, что speed) + список из
    ≤6 проваленных аудитов Lighthouse (title из ответа PSI — Google отдаёт
    локализованные title по `locale=` параметру! передавать locale=it/en/ru).
  - **co2**: вес страницы из total-byte-weight → модель Sustainable Web Design
    (взять коэффициенты из co2.js v0.16+, Apache-2.0, с комментарием-атрибуцией;
    НЕ тащить всю библиотеку — реализовать формулу SWD, ~30 строк) → граммы
    CO₂e/визит + сравнение со средним (~0,8 г) + оценка год/10k визитов.
  - **gdpr v1 (честная эвристика, дисклеймер обязателен)**: через tool_fetch
    html: (1) найден ли CMP (iubenda|cookiebot|complianz|onetrust|cookieyes|
    borlabs|klaro) — да/нет+имя; (2) ссылки privacy/cookie policy; (3) в сыром
    HTML до согласия — маркеры GA4/gtag/fbevents/clarity/hotjar (если есть и
    CMP не найден — красный флаг «трекеры без баннера»); (4) внешние домены
    скриптов (счётчик). Итог — светофор по 4 пунктам, не «юридический вердикт».
  - **ai**: 4 проверки: llms.txt (fetch path, валидность: markdown, H1);
    robots.txt (доступ GPTBot/ClaudeBot/PerplexityBot/Google-Extended:
    allowed/blocked/не упомянут); JSON-LD в html (есть/нет, типы);
    sitemap.xml (есть?). Итог — балл готовности N/4 + рекомендации.
  - **roi**: чистый калькулятор (без сети): визиты/мес × доля иностранных (%)
    × конверсия (%) × средний чек (€) × буст локализации (по CSA-данным
    +40% консервативно; слайдеры) → упущенная выручка/год. Дисклеймер «стима».

## 2. Контент и страницы (этап T2 — IT)

- `data.py` TOOLS: +3 записи (структуру скопировать с существующих; поля
  slug/nome/sub/…). Тексты — T2-агент пишет сам (тон: числа, «voi», без пафоса),
  включая: hero, «come funziona» (3 шага), виджет-разметку, FAQ 3 вопроса,
  CTA-блок. Для существующих 3 заглушек — заменить «In arrivo» на живые виджеты.
- `generate_pages.py`: build_tool рендерит по типу инструмента свой виджет
  (form url + кнопка + [data-sr-tool=...] + результат-контейнер со строками-
  вердиктами в data-атрибутах). ROI — форма-калькулятор без url.
- Регенерация ТОЛЬКО инструментальных страниц + strumenti-index (точечные
  вызовы; main() запрещён — грабли chi-siamo/citta).
- `lang.py`: TOOLS_SLUGS +3 (EN/RU-слаги из таблицы §0) → перегенерить
  `inc/lang-map.php` через emit_php_php... (emit_php_lang_map). Проверить diff:
  только +3 строки.
- **Перелинковка IT (требование владельца):**
  1) strumenti-index: 7 карточек;
  2) главная, секция strumenti-cards: 7 карточек (сетка auto-fit выдержит);
  3) на каждой странице инструмента блок «Gli altri strumenti gratuiti» —
     все остальные 6 (сейчас на заглушках 3 — расширить в генераторе);
  4) контекстные ссылки из услуг (по одной строке-ссылке в существующую
     секцию, без ломки структуры): seo-tecnica→analisi-seo+sito-pronto-ai;
     siti-aziendali и e-commerce→verifica-accessibilita («obbligo EAA dal
     2025»); restyling→impatto-co2; siti-multilingue и export-ready→
     roi-localizzazione. Эти 6 страниц — генерируемые: правки через
     data.py/generator + точечная регенерация.
- `deploy-import.php`: $page_map +3 IT-строки ('strumento-verifica-accessibilita'
  => ['verifica-accessibilita','strumenti',null] и т.д.).

## 3. EN + RU (этап T3)

- EN: CHROME-пары ('en' only) для всех новых строк → `translate_pages.py en`
  → exit 0; диффы только ожидаемые en-файлы. $page_map +3 EN-строки
  (родитель 'en/tools').
- RU: руками (перевод-адаптация уровня носителя) создать
  `ru-strumento-{proverka-dostupnosti,gotovnost-k-ii,uglerodnyj-sled}.php`
  + переписать 3 RU-заглушки (ru-strumento-* существующие: proverka-gdpr,
  seo-audit, roi-lokalizacii) с живыми виджетами + обновить ru-strumenti-index
  на 7 карточек. $page_map +3 RU-строки (родитель 'ru/instrumenty').
  Формат евро «€ N NNN», сроки 2/3/6 при упоминании.
- **Перелинковка EN/RU:** зеркально §2 п.1–3; контекстные ссылки из услуг:
  EN — те же 6 страниц (en-servizio-*, конвейером через те же правки данных);
  RU — руками в ru-servizio-* (соответствующие 6) и с лендингов:
  sajt-dlya-evropy→proverka-dostupnosti; seo-prodvizhenie→seo-audit+gotovnost-k-ii.
- **Меню:** главные меню НЕ расширять (правило 5+CTA). Footer «Pagine»
  (IT/EN/RU) — проверить, есть ли пункт Strumenti/Tools/Инструменты; если нет —
  добавить в remarka_deploy_sync_footer_menu-списки всех трёх языков.

## 4. QA и сдача (этап T4)

- Стаб-тесты PHP-эндпоинта (SSRF/rate-limit/happy) — прогнать; JS parse; php -l
  всего диффа; CSS-баланс.
- Функциональные прогоны Playwright КАЖДОГО инструмента на IT-странице:
  PSI-инструменты — мокнуть fetch фикстурой PSI-ответа (паттерн уже был в
  сессии: 5 node-тестов по фикстуре); gdpr/ai — мокнуть ajax-ответ; roi — живой.
  Скрин каждого результата (fh4_tool_<slug>.png).
- Перелинковка-аудит скриптом: собрать все страницы, извлечь href, проверить
  матрицу «каждый инструмент ← index + home-cards + другие инструменты + свои
  услуги» по всем 3 языкам; отчёт-таблица.
- lang-map/hreflang: стаб-тест multilang — 3 новые тройки путей дают hreflang
  на всех 3 языках.
- Регрессия: главные IT/EN/RU, форма (3 шага).
- Обновить docs: seo-meta.md (ключи+мета 3 новых инструментов ×3 языка,
  строки «агент» для инструментов), ricerca-strumenti-lab.md (статус →
  реализовано), deploy-ssh (ничего нового? если эндпоинт — упомянуть).
- Коммит/пуш; отчёт с деплой-чеклистом.

## 5. Разбиение по агентам

| Этап | Модель | Состав | Гейт |
|---|---|---|---|
| T1 | Opus | §1: эндпоинт+SSRF+тесты, JS-каркас+модули, i18n-механика data-атрибутов | отчёт оркестратору |
| T2 | Opus | §2: data.py+generator, 7 IT-страниц, lang.py/lang-map, IT-перелинковка, page_map | скрины IT |
| T3 | Sonnet | §3: EN-конвейер, RU-руками, page_map EN/RU, меню, EN/RU-перелинковка | скрины EN/RU |
| T4 | Sonnet | §4: тесты, линк-аудит, регрессия, docs, деплой-чеклист | финальный пакет |

Последовательно (общий worktree). Каждый этап: php -l/скрины/атомарный коммит/пуш.
