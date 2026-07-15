# План: «Check-up completo del sito» — сводный тест + PDF-отчёт на e-mail

> Дата: 14.07.2026. Решение владельца: выносим на главную общий тест сайта,
> объединяющий данные всех 7 инструментов; обширные результаты бесплатно на
> странице, самый полный отчёт — PDF на e-mail. Уровень — премиальный, виден
> с первых блоков главной.
>
> Правила для всех агентов — `docs/piano-implementazione-fase-A.md` §0
> (ветка, атомарные коммиты без ID моделей, протокол верификации, грабли:
> никакого `main()` в generate_pages.py, никакого `translate_pages.py ru`).
>
> **Требования владельца ко всем этапам (14.07, вечер):**
> 1. **Mobile-first** — все новые блоки проектируются от 390px; каждый агент
>    снимает скриншоты в двух ширинах (390 и 1440) и сам их просматривает.
> 2. **E-E-A-T** — сигналы экспертности/доверия в текстах, PDF и разметке:
>    кто мы (S.r.l., группа Remarka с 2001), на каких движках меряем, честные
>    границы метода, источники цифр; schema.org (Organization + WebApplication
>    на странице check-up). Никаких выдуманных экспертов и отзывов.
> 3. **SEO** — фокус-ключи из docs/seo-meta.md, вариации в H2, alt, мета.

## 0. Архитектура

**Клиент (JS, всё по существующим рельсам):**
- 1 запрос PSI API с 4 категориями (`performance, accessibility, seo,
  best-practices`) — расширение текущего `psiFetch` (сейчас 3).
- GDPR-эвристика и AI-готовность — через существующий эндпоинт
  `remarka_tool_fetch` (SSRF-защита и rate-limit уже стоят).
- CO₂ — модель SWD по byte weight из того же PSI-ответа (модуль уже есть).
- Новый модуль-оркестратор `data-sr-tool="checkup"`: запускает всё
  параллельно, собирает нормализованный объект результатов.

**Рефакторинг M2 (обязательный):** каждый существующий модуль инструмента
выделяет чистую функцию `run<Tool>(url, locale) -> Promise<result>`
(данные отдельно от рендера), чтобы check-up переиспользовал логику, а не
копировал её. Отдельные страницы инструментов продолжают работать как раньше
— регрессия обязательна.

**Сводный балл «Salute del sito» 0–100 (веса — финализирует M1):**
ориентир: performance 25 · seo 20 · accessibilità 15 · gdpr 15 ·
best-practices 10 · ai-readiness 10 · co2 5. Каждое измерение — светофор +
балл + 2–3 главных замечания бесплатно на странице; полный разбор — в PDF.

**Сервер (новое, M3):** AJAX-эндпоинт `remarka_tool_report`:
- вход: JSON результатов с клиента (cap 64 КБ, санитизация строк, числовые
  границы), e-mail, обязательный чекбокс согласия (privacy), honeypot;
- rate-limit по IP (transient, как у tool_fetch) + nonce `remarka_tools`;
- PDF: dompdf (LGPL, шрифт DejaVu — кириллица из коробки), бандлится в
  `remarka-studio/lib/dompdf/`; шаблон отчёта — PHP-вью на 3 языках;
- отправка `wp_mail` с вложением (FluentSMTP уже настроен);
- лид: приватный CPT `sr_lead` (e-mail, url, балл, локаль, дата) — база
  видна в админке штатными средствами WP.

**Страницы:** `/strumenti/check-up-completo/` ·
`/en/tools/full-site-checkup/` · `/ru/instrumenty/polnaya-proverka-sajta/`
(page_map + lang-map + меню + featured-позиция на индексе /strumenti/).

**Главная (3 языка):** новый премиальный блок сразу после hero
(hero продолжает продавать sito aziendale — решение фазы A не трогаем):
крупный ввод URL + «7 test in uno, gratis» + мини-иконки измерений;
сабмит ведёт на страницу check-up с `?url=…&autostart=1`.

## 1. Этапы и агенты

| Этап | Модель | Содержание |
|---|---|---|
| **M1** | Opus | Скоринговая модель (веса, пороги светофоров), копирайт IT/EN/RU: блок главной, страница check-up, экран результатов, письмо, структура PDF (обложка → сводный балл → 7 разделов → рекомендации → CTA). HTML-макеты блока главной и экрана результатов на реальном CSS. Копи-дек в `docs/copy-checkup.md`. |
| **M2** | Sonnet | Рефакторинг модулей на `run*()`, оркестратор, экран результатов, страница IT + блок главной IT (паттерны), lang-map/page_map/меню. |
| **M3** | Sonnet | Эндпоинт `remarka_tool_report` + dompdf + шаблон PDF + CPT лидов + форма e-mail с согласием; стаб-харнесс тестов (по образцу test_tool_fetch.php). |
| **M4** | Sonnet | EN/RU: страницы (конвейер en / руками ru), блок главной EN/RU, CHROME-пары, PDF/письмо EN/RU; QA: скриншоты, грепы, регрессия 7 инструментов и главных; docs + деплой-пакет. |

Последовательно (общий worktree). Верификация на каждом этапе — по протоколу §0.

## 2. Очередь после check-up (утверждено владельцем 14.07)

1. Услуга «Adeguamento EAA» — **утверждено владельцем 14.07: da € 1 900,
   3 settimane контрактных с неустойкой** (как у остальной линейки). Этап E1
   после M4: страница услуги IT/EN/RU, prezzi, меню, CTA инструмента
   доступности → услуга.
2. CrUX-мониторинг с e-mail-отчётом — переиспользует базу лидов и почтовый
   шаблон из M3 (в форме check-up сразу заложить необязательный чекбокс
   «отчёт ежемесячно» с записью флага в лид).
3. axe-core a11y v2 + GDPR v2 (Blacklight-подход) — по памяти сервера
   (`free -m` 14.07: 3915 МБ всего, ~1516 доступно, swap уже используется
   на 1,1 ГБ) вердикт: headless Chromium НА ПРОДАКШЕН-VPS только со строгой
   очередью в 1 проверку и лимитом памяти; безопаснее отдельный дешёвый VPS.
   Реализация — отдельным этапом после E1/CrUX, с раннбуком установки.

## Статус выполнения

- **M1 — выполнено (14.07.2026).** Скоринговая модель финализирована (веса
  25·20·15·15·10·10·5, нормализация GDPR/AI/CO₂ на 0–100, пороги светофоров
  90/75/50 с 4 вердиктами, правило деградации при N/D), копи-дек IT/EN/RU
  (блок главной, страница check-up, экран результатов, письмо, структура PDF на
  12 страниц с E-E-A-T-блоком), мокапы на реальном CSS (блок главной + экран
  результатов, 390 и 1440 px, mobile-first). Всё в `docs/copy-checkup.md`
  (§5 — новые CSS-классы и schema.org для M2). Мокапы в scratchpad:
  `m1_home-block.png` / `m1_home-block-mobile.png` / `m1_results.png` /
  `m1_results-mobile.png`.
- **M2 — выполнено (14.07.2026).** Рефакторинг модулей `remarka.js` на пары
  «чистая функция расчёта + рендер» (`runGdprCheck`/`gdprSignalFlags`,
  `runAiCheck` — GDPR и AI; `psiFetch` уже был чистым, расширен 4-й
  категорией `BEST_PRACTICES` → `scores.bp`); регрессия 7 старых виджетов
  подтверждена (см. юнит-тест ниже). Новый оркестратор `data-sr-tool="checkup"`:
  параллельный запуск (1 PSI-вызов + `remarka_tool_fetch` для GDPR/AI),
  скоринг строго по `docs/copy-checkup.md` §1 (веса 25/20/15/15/10/10/5,
  нормализация GDPR/AI/CO₂, пороги 90/75/50, деградация с ренормализацией,
  guardia ≥4/7 и Prestazioni|SEO), экран результатов (gauge, 7 карточек,
  топ-3 приоритета, форма e-mail с TODO-хуком `remarka_tool_report` для M3),
  автозапуск `?url=&autostart=1`. Новые CSS-классы `.sr-checkup`/`.sr-gauge`/
  `.sr-dim-grid`/`.sr-dim-card`/`.sr-priorities`/`.sr-checkup-lead`/
  `.sr-consent` — mobile-first (390px база, `min-width` для десктоп).
  Страница IT `/strumenti/check-up-completo/` (генератор: `data.py` TOOLS
  + `generate_pages.py build_tool`, тип `checkup`, точечная генерация —
  `git diff --stat` подтверждает изменение только `strumenti-index.php` +
  новый файл страницы), featured-позиция на `/strumenti/` перед сеткой
  остальных 7. Блок главной IT `patterns/checkup-home.php` сразу после
  hero-home (`deploy-import.php` `$home_sections`; RU-набор не тронут).
  JSON-LD `WebApplication` + `FAQPage` на странице check-up
  (`functions.php`, без дублирования `Organization`, без `aggregateRating`).
  Верификация: `php -l`/`python3 -c`/JS-parse/баланс скобок CSS — все чисто;
  юнит-тест скоринга на Node (`scratchpad/m2/scoring_test.js`, 38 проверок
  в 10 группах) — все зелёные; Playwright на реальном CSS с замоканным
  fetch (390/1440 px) — страница результатов и блок главной; регрессия
  `test-velocita`/`impatto-co2`/`check-gdpr`/`sito-pronto-ai` подтверждена.
- **M3 — выполнено (15.07.2026).** Эндпоинт `remarka_tool_report`
  (`functions.php`): nonce `remarka_tools` → honeypot (`sr_checkup_hp`,
  successo muto) → rate-limit 3/ora/IP (transient `remarka_rpt_`, separato
  da `remarka_tl_`) → email/consenso obbligatori → payload JSON sanificato
  (whitelist chiavi, punteggi clamp 0–100, url solo http/https, locale
  whitelist it|en|ru; composito **ricalcolato sempre lato server**, mai
  fidandosi del client). CPT privato `sr_lead` (solo `manage_options`,
  colonne Email·Sito·Punteggio·Lingua·Monitoraggio·Data; cancellazione =
  cancellazione GDPR completa). PDF: dompdf 3.1.5 bundlato a mano in
  `lib/dompdf/` (src/lib trimmati, niente test/doc superflue, 3 font DejaVu
  invece dei ~40 upstream, dipendenze reali — php-font-lib/php-svg-lib/
  masterminds-html5/sabberworm-css-parser + un sottoinsieme di 4 funzioni
  di thecodingmachine/safe — autoloader PSR-4 scritto a mano, non composer;
  versioni/licenze in `lib/dompdf/VERSIONS.md`). Template 12 pagine
  (`inc/checkup-report-pdf.php`, `remarka_checkup_render_html`/`_pdf`) —
  copy deck verbatim da `docs/copy-checkup.md` §2.5/3.5/4.5 nelle 3 lingue,
  colori di brand replicati da `remarka.css`, semafori a pallino, pagina
  E-E-A-T con dati societari reali per lingua. Verifica runtime estensioni
  PHP (`dom`/`mbstring`/`gd`) con errore JSON `pdf_unavailable` invece di
  fatal. E-mail con allegato via `wp_mail` (oggetto/corpo dal deck §2.4/
  3.4/4.4), file temporaneo in `wp-content/uploads/checkup-reports/`
  (index.php-заглушка) cancellato subito dopo l'invio. Verifica: `php -l`
  su tutti i file toccati/aggiunti (incl. l'intero bundle dompdf), JS
  parse-check, `git diff --stat` conferma solo i file attesi
  (`functions.php`, `remarka.js` — 1 campo honeypot minimale, il pattern
  della pagina — 1 riga honeypot, + i file nuovi `inc/checkup-report-pdf.php`
  e `lib/dompdf/**`). Stub-harness Node/PHP (`scratchpad/test_checkup_report.php`,
  39 controlli): nonce/honeypot/rate-limit/email/consenso/payload oversize/
  XSS-escaping/happy-path IT-EN-RU/embedding font cirillico nel PDF —
  tutti verdi. 3 PDF di esempio renderizzati in scratchpad
  (`m3_report_it.pdf`/`_en.pdf`/`_ru.pdf`, ~76–86 KB l'uno, verificati
  pagina per pagina via rendering PNG).
- **M4 — completato (15.07.2026). Feature «Check-up completo del sito»
  terminata su tutti e 3 le lingue.** EN: `python3 translate_pages.py en`
  (dizionario esteso di ~170 coppie `CHROME_CHECKUP` in `chrome_strings.py`,
  ATTRS regex di `translate_pages.py` estesa a `data-word-*`/
  `data-composite-*`/`data-verdict-[0-9]`/`data-calc-note`/`data-na-text`/
  `data-ai-suffix` — mancavano nel contratto M2, individuate confrontando
  ogni nodo di `strumento-check-up-completo.php` col dizionario prima del
  run) → `en-strumento-check-up-completo.php` + `en-strumenti-index.php`
  (card in evidenza) rigenerati, `git diff --stat` conferma solo questi 2
  file. RU: `ru-strumento-check-up-completo.php` scritto a mano
  (`docs/copy-checkup.md` §4.2/§4.3, testo autonomo) + card in evidenza su
  `ru-strumenti-index.php`. Blocchi home `patterns/lang-en/checkup-home.php`
  e `patterns/lang-ru/checkup-home.php` (testo §3.1/§4.1); `checkup-home`
  inserito in `$home_sections_ru` subito dopo `hero-home` in
  `deploy-import.php` (IT/EN già presenti da M2). **Bug di M2 corretto:**
  `initCheckupHomeForm()` in `remarka.js` reindirizzava sempre a
  `/strumenti/check-up-completo/` — ora legge `data-sr-locale` dal form
  (stesso contratto `toolLocale()` dei widget strumento) e manda alla
  pagina check-up della lingua propria via `CHECKUP_PAGE_PATH`. **Bug
  scoperto in QA:** `data-ai-suffix` (badge «N / 4 segnali» sulla card
  AI-readiness) non faceva parte del contratto dati di M2 — l'EN/RU
  mostravano l'italiano «segnali» in chiaro (l'euristica `ITALIAN_HINT` del
  conveyor non lo intercetta, nessuna parola italiana frequente nella
  stringa); aggiunto l'attributo alle 3 pagine + voce dizionario, riscontro
  visivo confermato via screenshot mirato sulla card. Schema.org:
  `remarka_checkup_tool_schema()` (`functions.php`) copriva solo
  `is_page('check-up-completo')` (IT) — esteso con `is_page()` ad array dei
  3 slug, `name`/`featureList`/FAQ localizzati per `remarka_current_lang()`,
  `provider` da `remarka_company_lang_data()`; verificato con harness PHP
  dedicato (`m4_schema_test.php`, JSON-LD delle 3 lingue via `eval()` della
  funzione reale, non una riscrittura). `lang.py` `TOOLS_SLUGS` +
  `check-up-completo`, `inc/lang-map.php` rigenerato (`python3 lang.py`,
  diff di una sola riga), `deploy-import.php` `$page_map` + 2 voci EN/RU.
  Footer-menu EN/RU verificati **invariati** — linkano solo alla sezione
  `/tools/`/`/instrumenty/`, non ai singoli strumenti (stesso comportamento
  di T3, nessuna riga da aggiungere). Verifica: `php -l` su tutti i file
  toccati/nuovi, `node -e` parse su `remarka.js`, `python3 -m py_compile`
  sui `.py` toccati — tutti puliti; grep anti-residuo IT
  («Analizza il sito»/«Il report completo»/«misurazioni su») e anti-formato
  IT dell'euro (`€ N.NNN`) su RU — puliti; hreflang a 3 vie in
  `lang-map.php` corretta. Playwright (Chromium `/opt/pw-browsers/chromium`,
  `reducedMotion`) su `remarka.css` reale con `fetch`/`admin-ajax.php`
  mockati (PSI 4 categorie + GDPR/AI): pagina check-up EN/RU con risultati
  renderizzati (composito 63/100, verdetti confermati in inglese/russo) a
  390 e 1440px, blocco home EN/RU a 390/1440px — 8 screenshot in
  `scratchpad/m4/m4_*.png`, ognuno rivisto. Regressione: pagina check-up IT
  ancora in italiano (stessa run, stesso mock), `test-velocita` IT
  funzionante, home IT con blocco `checkup-home` dopo l'hero — 3 screenshot
  di controllo aggiuntivi. `git diff --stat` finale: 14 file modificati
  (10 codice + `docs/seo-meta.md`/`deploy-ssh.md`/`piano-checkup-sito.md`)
  + 4 nuovi, nessun file toccato fuori scope. Meta SEO IT/EN/RU della
  pagina check-up in `docs/seo-meta.md` (Title/Description/focus keyword,
  verbatim da `docs/copy-checkup.md` §2.2/§3.2/§4.2). Fase «Check-up
  completo del sito» conclusa: M1→M4 tutte completate.
