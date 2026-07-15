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
4. **E-E-A-T**: каждая цифра — с источником (ссылка на первоисточник);
   даты актуальности; где уместно — наш собственный опыт («на 28 проектах
   в обслуживании мы видим…» — только реальные факты из docs/copy-casi-studio.md).
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
8. **Верификация**: php -l, py_compile, конвейер exit 0, Playwright-скрины
   2 статей батча (390+1440) на реальном CSS, грепы IT-остатков в EN.
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
- Батч 1 — в работе (15.07).
- Батчи 2–6 — очередь, по одному в день.
