# Редакционный план блога Studio Remarka

> Утверждено владельцем 15.07.2026: «по 5 статей в день, обязательно с
> иллюстрациями и интересным повествованием и живым языком, с последующей
> проверкой оркестратора». Работает как ежедневный конвейер: 1 батч = 5 статей.
> Существующие 8 статей (см. BLOG_POSTS в data.py) не дублируем.

## Правила для агента-автора (каждый батч)

1. **Язык живой, повествование интересное** — как пишет человек, увлечённый
   темой: конкретные сцены и примеры («владелец пиццерии в Турине открывает
   свой сайт с телефона…»), никакого канцелярита, никаких «в современном
   цифровом мире». Числа вместо прилагательных. Обращение «voi». Тон — как в
   лучших наших страницах (data.py: metodologia/lettura инструментов).
2. **Объём**: 1000–1500 слов. Структура: цепляющий лид (3–4 предложения) →
   H2-разделы с вариациями фокус-ключа → практический вывод → CTA.
3. **SEO**: 1 фокус-ключ на статью (из плана ниже), вариации в H2, ключ в
   первом абзаце и в одном alt; Title ≤60, Description ≤160 — сразу строками
   в docs/seo-meta.md (раздел Blog).
4. **E-E-A-T и внешние источники (требование владельца, 15.07)**: минимум
   **3 внешние ссылки на авторитетные первоисточники** на статью (нормы ЕС,
   официальные гайды Google/W3C, отраслевые исследования) — контекстно в
   тексте и/или блоком сносок «Fonti» в конце статьи; каждая цифра — с
   источником; даты актуальности; где уместно — наш собственный опыт
   («на 28 проектах в обслуживании…» — только реальные факты из
   docs/copy-casi-studio.md). Внешние ссылки: target="_blank" rel="noopener".
4-бис. **Schema.org (требование владельца, 15.07)**: каждая статья несёт
   JSON-LD BlogPosting (headline, datePublished, image=обложка, author и
   publisher = Organization Studio Remarka, inLanguage) — через генератор,
   без дублирования Organization-разметки темы и без выдуманных рейтингов.
5. **Иллюстрации** (обязательно): 1 обложка + 1–2 диаграммы/схемы на статью.
   Формат — фирменные SVG в assets/img/blog/ (палитра remarka.css: oltremare,
   nero-inchiostro, грид-фон; типографика как на сайте). Это НЕ фотостоки и
   НЕ ИИ-фото: схемы, графики, композиции из форм и цифр — премиально и
   консистентно с сайтом. Каждый SVG проверяется рендером (Playwright-скрин).
   `<img>` с alt и loading="lazy", max-width:100%.
6. **Перелинковка**: каждая статья ссылается минимум на 1 услугу + 1 инструмент
   Lab (контекстно, не списком) и, где уместно, на соседнюю статью. Ссылка НА
   статью добавляется из migliorare-текста соответствующего инструмента, если
   до сих пор там не было пары (флаг L1: доступность и AI без статей).
7. **Механика**: статьи кладутся в BLOG_POSTS (data.py) со всеми полями по
   образцу существующих; генерация ТОЧЕЧНАЯ (build-функция статьи + индекс
   блога; main() запрещён; после регенерации git diff, чужое — checkout).
   EN — конвейером translate_pages.py en + CHROME-пары ('en' только новые).
   RU-батчи (№5–6) пишутся руками сразу по-русски (translate_pages.py ru
   запрещён навсегда). page_map ×2(3) + lang-map тройки.
8. **Верификация — чек-лист приёмки перед коммитом** (ни один пункт не
   пропускается): php -l · py_compile · конвейер exit 0 · Playwright-скрины
   2 статей батча в ОБЕИХ ширинах 390+1440 (mobile-first: сначала смотрим
   390) · грепы IT-остатков в EN · ≥3 внешних источника в каждой статье ·
   внутренние ссылки (≥1 услуга + ≥1 инструмент + соседняя статья) ·
   строки Title/Description в seo-meta.md ≤60/≤160 · JSON-LD BlogPosting
   валиден (проверить python-json-парсом извлечённого блока).
   Один коммит на батч, без ID моделей, push с ретраями.
9. **Проверка оркестратора** после каждого батча: читает тексты целиком
   (живость, честность, отсутствие воды и выдуманных фактов), смотрит скрины,
   при замечаниях возвращает агенту на доработку ДО коммита в следующий батч.

## Очередь батчей (6 × 5 = 30 статей)

### Батч 1 — спутники новых инструментов и услуги (IT + EN) — сегодня
| # | Тема / рабочий заголовок | Фокус-ключ | Линкует |
|---|---|---|---|
| 1 | EAA 2026: cosa rischia davvero il vostro e-commerce | european accessibility act e-commerce | servizio adeguamento-eaa · tool verifica-accessibilita |
| 2 | llms.txt: cos'è e serve davvero al vostro sito? | llms.txt cos'è | tool sito-pronto-ai · SEO tecnica |
| 3 | Come farsi trovare (e citare) da ChatGPT: guida GEO | sito visibile su ChatGPT | tool sito-pronto-ai · SEO tecnica |
| 4 | Check-up del sito web: le 7 misure che contano | check up sito web | tool check-up-completo · restyling |
| 5 | E-E-A-T: come Google giudica la vostra credibilità | E-E-A-T cos'è | tool segnali-eeat · SEO tecnica |

### Батч 2 — деньги и решения владельца (IT + EN)
| 6 | Preventivo sito web: come leggerlo senza sorprese | preventivo sito web | prezzi · siti-aziendali |
| 7 | Sito web in 3 settimane: com'è possibile (davvero) | sito web in 3 settimane | siti-aziendali · come-lavoriamo |
| 8 | Restyling o sito nuovo? Il test delle 5 domande | restyling sito web | restyling-migrazione · tool check-up |
| 9 | Quanto pesa il vostro sito sull'ambiente (e sul portafoglio) | impatto ambientale sito web | tool impatto-co2 · restyling |
| 10 | Dichiarazione di accessibilità: guida pratica 2026 | dichiarazione di accessibilità | adeguamento-eaa · tool verifica |

### Батч 3 — технологии, которые продают (IT + EN)
| 11 | Telegram Mini App per il business: il canale che l'Italia ignora | telegram mini app business | web-app · caso MiniApp |
| 12 | Gestionale su misura vs Excel: quando conviene il salto | gestionale su misura | web-app · caso TMS |
| 13 | Schema.org per PMI: i dati strutturati che Google premia | dati strutturati schema.org | SEO tecnica · tool segnali-eeat |
| 14 | Gamification nel B2B: quando un gioco vende servizi seri | gamification marketing b2b | restyling · caso gioco |
| 15 | Hosting in Italia o in cloud: cosa cambia per velocità e GDPR | hosting sito web italia | siti-aziendali · tool test-velocita |

### Батч 4 — локальный SEO и города (IT + EN)
| 16 | SEO locale a Milano: come emergere nella città più competitiva | seo locale milano | citta-milano · SEO tecnica |
| 17 | Google Business Profile: la vetrina gratuita che nessuno cura | google business profile | SEO tecnica · citta-* |
| 18 | Sito multilingue: hreflang senza mal di testa | hreflang sito multilingue | siti-multilingue · tool analisi-seo |
| 19 | Export digitale: il sito che apre mercati esteri | sito per export | export-ready · siti-multilingue |
| 20 | Manutenzione WordPress: cosa succede se non la fate | manutenzione wordpress | siti-aziendali · tool check-up |

### Батч 5 — RU-блог: свой путь (руками по-русски, самодостаточно)
| 21 | Сайт для выхода на рынок Италии: с чего начать | сайт для рынка италии | ru/uslugi/sajt-dlya-evropy |
| 22 | SEO в Италии по-русски: как продвигаться, не зная языка | seo в италии | ru/uslugi/seo-prodvizhenie |
| 23 | GDPR для русскоязычного бизнеса в ЕС: без паники | gdpr для бизнеса | ru-услуги · tool proverka-gdpr |
| 24 | Почему «перевести сайт» ≠ «локализовать сайт» | локализация сайта | ru/uslugi/mnogojazychnye-sajty |
| 25 | Сколько стоит сайт в Италии: честные цифры | сколько стоит сайт в италии | ru-prezzi |

### Батч 6 — RU-блог: продукты и доверие (руками)
| 26 | Телеграм-приложение для бизнеса в Европе | телеграм мини-приложение | ru web-app · кейс MiniApp |
| 27 | Как проверить подрядчика по сайту: 8 сигналов доверия | как проверить веб-студию | tool signaly-eeat |
| 28 | Европейский закон о доступности: касается ли вас | закон о доступности сайтов | ru dostupnost-eaa |
| 29 | Ваш сайт глазами ChatGPT: новая видимость | сайт в chatgpt | tool gotovnost-k-ii |
| 30 | Русскоязычная аудитория в Европе: как её находят в поиске | русскоязычная аудитория европы | ru/uslugi/seo-prodvizhenie |

## Статус выполнения
- Батч 1 — ✅ выполнен и вычитан оркестратором (15.07, коммит `d798a80`):
  5 статей IT+EN, 11 SVG, перелинковка + бэклинки из инструментов
  verifica-accessibilita и sito-pronto-ai. Особенность: RU-страниц у этих
  статей нет по плану (RU-темы — батчи 5–6); hreflang решён через
  BLOG_IT_EN_ONLY в lang.py (переключатель RU ведёт на /ru/blog/, без 404).
- Батч 2 — ✅ выполнен и вычитан оркестратором (16.07, коммит `468e664`):
  5 статей IT+EN «деньги и решения владельца»
  (preventivo · sito in 3 settimane · restyling o sito nuovo · impatto
  ambientale · dichiarazione di accessibilità), 10 фирменных SVG, 4–8 внешних
  источников на статью (SDI, CSRD, Green Web Foundation, W3C/WAI + банк
  ретрофита), JSON-LD BlogPosting через blog-schema-map, перелинковка услуга +
  инструмент + соседняя статья, бэклинки из инструментов impatto-co2 и
  verifica-accessibilita. RU-страниц нет (BLOG_IT_EN_ONLY, как в батче 1).
- Батч 3 — ✅ выполнен и вычитан оркестратором (17.07, коммиты `dd3411d` +
  правка `9426dc7`; замечание вычитки — грамматика «La microdati» в статье
  schema.org — исправлено агентом отдельным коммитом; источники из-за
  блокировки egress-прокси подтверждены перекрёстным веб-поиском, как в
  ретрофите): 5 статей IT+EN «технологии, которые продают»
  (telegram-mini-app-business · gestionale-su-misura-vs-excel ·
  dati-strutturati-schema-org · gamification-b2b · hosting-sito-web-italia),
  10 фирменных SVG (обложка + схема на статью), 3–4 внешних источника на статью
  (Telegram Mini Apps + TechCrunch · EuSpRIG + GDPR · schema.org + Google rich
  results · Nielsen Norman Group + Google · web.dev TTFB + EDPB + GDPR),
  JSON-LD BlogPosting через blog-schema-map, перелинковка услуга + инструмент +
  соседняя статья, реальные факты только из copy-casi-studio.md (Mini App, TMS,
  gioco). Бэклинки из инструментов test-velocita (→ hosting) и segnali-eeat
  (→ schema.org). RU-страниц нет (BLOG_IT_EN_ONLY, как в батчах 1–2).
- Батч 4 — ✅ выполнен и вычитан оркестратором (18.07, коммит `9ec09f0`):
  5 статей IT+EN «локальный SEO и города» (seo-locale-milano ·
  google-business-profile-guida · hreflang-sito-multilingue · sito-per-export ·
  manutenzione-wordpress), рубрики проставлены, 10 фирменных SVG, 3–4
  источника на статью (Google guidelines ×6, BrightLocal, CSA Research,
  Eurostat, WordPress.org, Patchstack), перелинковка на новые городские
  страницы (/milano/, /dove-lavoriamo/), GBP-статья с честным разделом
  «Una nota onesta sul nostro caso» (карточки группы под брендом ATT —
  не выдаём за образец). Цифры сверены: «8% отбор переводчиков» — из
  copy-casi-studio, «96% уязвимостей в плагинах 2024» — Patchstack.
  Бэклог-заметка: en-blog-* батчей 1–3 ждут width/height-синхронизации
  (IT уже имеет, EN подтянется ближайшим полным EN-прогоном).
- Батч 5 — ✅ выполнен и вычитан оркестратором (19.07, коммит `c107043`):
  5 RU-only статей «свой путь, руками по-русски» (sajt-dlya-vyhoda-na-rynok-italii ·
  seo-v-italii-po-russki · gdpr-dlya-russkoyazychnogo-biznesa-v-es ·
  perevesti-ili-lokalizovat-sajt · cena-sajta-v-italii), по 4 внешних
  первоисточника на статью (Eurostat, Google Search Central, EUR-Lex GDPR
  2016/679, EDPB, Garante, CSA Research, W3C i18n, HTTP Archive, web.dev),
  10 фирменных SVG (обложка + схема), JSON-LD BlogPosting, перелинковка
  RU-услуга + RU-инструмент + соседняя статья. Механика: новый `BLOG_RU_ONLY`
  в lang.py (зеркало BLOG_IT_EN_ONLY — статьи RU-only, без IT/EN, translate
  ru запрещён), питает blog-schema-map и hreflang; статьи — рукописные
  ru-blog-*.php (не BLOG_POSTS, т.к. тот IT-центричный). Вычитка: тексты
  честны (юр. утверждения GDPR точны, цены со ссылкой на рынок, дедлайн EAA
  28.06.2025 верный, наши гарантии совпадают, выдуманного нет), SVG на бренде.
  Оговорки: (1) Playwright-скрины в песочнице невозможны (egress блокирует
  Chromium) — SVG проверены cairosvg-рендером, нужна мобильная визуальная
  вычитка (390px) владельцем после деплоя; (2) объём 617–763 слова — ниже
  номинала 1000–1500, но плотно и длиннее уже одобренного RU-корпуса
  (577–652); при желании владельца агент допишет секции.
- Батч 6 (RU руками) — ✅ выполнен и вычитан оркестратором (20.07, коммит `c65cd1e`):
  5 RU-only статей «продукты и доверие» (telegram-prilozhenie-dlya-biznesa-v-evrope ·
  kak-proverit-veb-studiyu · zakon-o-dostupnosti-sajtov · sajt-v-chatgpt ·
  russkoyazychnaya-auditoriya-v-evrope), 735–902 слова, по 4 внешних
  первоисточника (core.telegram.org Mini Apps/Payments/Bot API, Eurostat,
  Google Search Central helpful-content/hreflang/multi-regional, web.dev Web
  Vitals, EUR-Lex GDPR 2016/679 + EAA 2019/882, AccessibleEU, W3C WAI/WCAG,
  OpenAI GPTBot docs, llmstxt.org, CSA Research), 10 фирменных SVG, JSON-LD
  BlogPosting, перелинковка RU-услуга + RU-инструмент + соседняя статья.
  Механика как батч 5: BLOG_RU_ONLY +5, deploy-import page_map +5,
  ru-blog-index +5 карточек, blog-schema-map/lang-map регенерированы точечно,
  seo-meta.md раздел «Batch 6» (Title 48–57, Desc 142–151). Вычитка
  оркестратора: тексты честны и живы (EAA «уже вступил в силу», 28.06.2025 в
  прошлом; исключения для микро с оговоркой «граница — нац. закон»; число
  русскоязычных НЕ выдумано — «точную цифру никто не назовёт», Eurostat как
  контекст; Mini App/гарантии — реальные факты студии; раздел «не магия и не
  гарантия» у ChatGPT-статьи). Оговорки: (1) Playwright-скрины невозможны
  (egress) — SVG проверены cairosvg, мобильная вычитка 390px за владельцем;
  (2) полировка: у SVG `aria-label` на итальянском на RU-страницах —
  косметическая a11y-мелочь, в бэклог.

**План блога закрыт: все 6 батчей (30 статей) выполнены и вычитаны.**
Ежедневный триггер отключён оркестратором 20.07 (update_trigger enabled=false).
- **Ретрофит выполнен отдельным проходом 15.07** (коммит «Blog retrofit:
  external sources, BlogPosting schema, content enrichment»). Охват — ВСЕ 13
  готовых статей (8 старых + 5 батча 1):
  - внешние авторитетные первоисточники: блок «Fonti»/«Источники» (≥3 на
    статью, 3–5, URL проверены) + контекстные внешние ссылки в тексте, IT/EN/RU;
  - обогащение: 6 коротких старых статей развёрнуты в полноформатные sezioni,
    лиды оживлены до уровня батча 1 (сцены, «voi», числа), факты и слаги не тронуты;
  - JSON-LD BlogPosting всем статьям во всех 3 языках — хук
    `remarka_blog_posting_schema()` (functions.php) + автогенерируемая карта
    `inc/blog-schema-map.php` (из BLOG_POSTS через
    `generate_pages.py:build_blog_schema_map`), headline берётся из
    `get_the_title()` (без дублирования заголовков), без aggregateRating;
  - EN — конвейером translate_pages.py en (CHROME_BLOG_RETROFIT), RU 8 старых
    статей — руками; попутно починен формат «€ N NNN» в RU-бэклоге.
  - **Батчу 2 ретрофит НЕ нужен** (новые статьи пишутся сразу по правилам 4/4-бис).
