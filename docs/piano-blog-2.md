# План блога remarka.biz — вторая волна (статьи 31–60)

> Продолжение `docs/piano-blog.md`. Первые 30 статей (батчи 1–6) выполнены и
> вычитаны (см. «Статус выполнения» в piano-blog.md). Здесь — следующие 30:
> 6 батчей × 5 статей, 1 батч в день. **Все правила автора и приёмки
> (§7–§9 piano-blog.md) действуют без изменений** — их не дублирую, только
> ссылаюсь: живой человеческий язык и «вы»; честность и E-E-A-T (источники,
> оговорки, НИКАКИХ выдуманных фактов/цифр/экспертов/отзывов); ≥3 (цель 4)
> внешних авторитетных первоисточника с реальными URL; внутренние ссылки
> (≥1 услуга + ≥1 инструмент + соседняя статья); 2 фирменных SVG на статью
> (плоские, #2440C8 на светлом фоне); JSON-LD BlogPosting; Title ≤60 /
> Description ≤160 в seo-meta.md; mobile-first от 390px; атомарный коммит
> без ID моделей; чек-лист верификации §8.

## Языковая стратегия (как в первой волне)

- **Батчи 7–10 — IT + EN** (5×4 = 20 статей). IT пишется, EN — конвейером
  `translate_pages.py en` (+ CHROME-пары «en» только новые). RU-версий у
  этих статей нет (BLOG_IT_EN_ONLY), hreflang RU → индекс `/ru/blog/`.
- **Батчи 11–12 — RU руками** (5×2 = 10 статей). Свои темы под русскоязычную
  аудиторию в ЕС, самодостаточно, механизм `BLOG_RU_ONLY` (как батчи 5–6).
  `translate_pages.py ru` запрещён навсегда.

Итог: три языка покрыты по проверенной модели (IT+EN — общие темы; RU —
собственная повестка), а не машинным переводом.

## Что закрываем этой волной (аналитика пробелов)

1. **Инструменты без своей статьи** → `analisi-seo` (§43/44), `roi-localizzazione`
   (§50), `suona-madrelingua` (§49-угол мадреленгва).
2. **Локальное SEO по крупным городам** (кроме Milano): Roma, Torino, Napoli —
   с отраслевым углом, не шаблон (§46–48). Остальные 13 городов держат свои
   лендинги; плодить 17 одинаковых статей — вода, не делаем.
3. **Живые темы 2026**: Consent Mode v2, GA4-приватность, AI Overviews, INP,
   конверсия/CRO, безопасность/бэкапы, WhatsApp-коммерция, выход на рынки.

---

## Батч 7 — Конверсия и доверие (IT + EN)
| # | Тема / рабочий заголовок | Фокус-ключ | Линкует |
|---|---|---|---|
| 31 | Perché il vostro sito non converte: 7 fughe silenziose | perché il sito non converte | siti-aziendali · tool check-up-completo |
| 32 | Landing page che porta contatti: anatomia di una pagina che vende | landing page che converte | siti-aziendali · seo-tecnica |
| 33 | Recensioni e riprova sociale: usarle senza inventarle | recensioni sito web | tool segnali-eeat · google-business-profile (blog) |
| 34 | WhatsApp Business per le PMI: quando il contatto batte il modulo | whatsapp business pmi | web-app · siti-aziendali |
| 35 | Il testo prima del design: perché il copy decide la conversione | copywriting sito web | siti-aziendali · restyling-migrazione |

## Батч 8 — Privacy e dati nel 2026 (IT + EN)
| 36 | Google Consent Mode v2: cosa cambia per annunci e analytics | consent mode v2 | tool check-gdpr · seo-tecnica |
| 37 | Google Analytics 4 e privacy in UE: siete davvero a norma? | google analytics 4 gdpr | tool check-gdpr · seo-tecnica |
| 38 | Alternative privacy-first a Google Analytics (Matomo, Plausible) | alternative google analytics privacy | tool check-gdpr · tool impatto-co2 |
| 39 | Cookie policy e privacy policy: cosa serve davvero e a chi | cookie policy o privacy policy | tool check-gdpr · adeguamento-eaa |
| 40 | Backup e sicurezza del sito: cosa perdete se domani sparisce | sicurezza sito web pmi | tool check-up-completo · siti-aziendali |

## Батч 9 — SEO che regge nel 2026 (IT + EN)
| 41 | AI Overviews di Google: restare visibili quando risponde l'AI | ai overviews google | tool sito-pronto-ai · seo-tecnica |
| 42 | INP, la nuova metrica Core Web Vitals: cosa misura e come si risolve | inp core web vitals | tool test-velocita · seo-tecnica |
| 43 | Autorevolezza tematica: perché un blog batte 100 keyword | topical authority seo | seo-tecnica · tool analisi-seo |
| 44 | Link interni: la SEO gratis che quasi nessuno cura | link interni seo | seo-tecnica · tool analisi-seo |
| 45 | Immagini e velocità: WebP, lazy-load e Core Web Vitals | ottimizzare immagini sito | tool test-velocita · restyling-migrazione |

## Батч 10 — Locale e mercati (IT + EN)
| 46 | SEO locale a Roma: emergere nella capitale dei servizi | seo locale roma | citta-roma · google-business-profile (blog) |
| 47 | SEO locale a Torino: manifattura e industria online | seo locale torino | citta-torino · export-ready |
| 48 | Napoli e il turismo: un sito multilingue che fa prenotare | sito turismo napoli | citta-napoli · siti-multilingue |
| 49 | Traduzione madrelingua vs AI: la differenza che il cliente sente | traduzione madrelingua sito | tool suona-madrelingua · siti-multilingue |
| 50 | ROI della localizzazione: quanto rende tradurre davvero | roi traduzione sito | tool roi-localizzazione · export-ready |

## Батч 11 — RU: продажи и доверие (руками)
| 51 | Почему сайт не приносит заявок: 7 тихих утечек | почему сайт не приносит клиентов | ru siti-aziendali · tool полная-проверка |
| 52 | Отзывы и репутация в Италии: как собирать честно | отзывы на сайте | tool signaly-eeat · соседняя ru-blog |
| 53 | WhatsApp для бизнеса в Европе: когда чат лучше формы | whatsapp для бизнеса | ru web-app · ru siti-aziendali |
| 54 | Реклама или SEO: с чего начать русскоязычному бизнесу в Италии | seo или реклама | ru seo-tecnica · ru prezzi |
| 55 | Как принять оплату на сайте в Италии и ЕС: способы и нюансы | приём оплаты на сайте | ru e-commerce · ru siti-aziendali |

## Батч 12 — RU: рынки и рост (руками)
| 56 | Выход на немецкий рынок: сайт для Германии | сайт для германии | ru export-ready · ru многоязычные |
| 57 | Google Business Profile для локального бизнеса в Италии | google business profile италия | ru seo-tecnica · соседняя ru-blog |
| 58 | Аналитика и приватность: GA4 и закон в ЕС | google analytics закон ес | ru tool проверка-gdpr · ru seo-tecnica |
| 59 | Электронный счёт (fattura elettronica) и сайт: что учесть | электронный счёт италия сайт | ru siti-aziendali · ru e-commerce |
| 60 | Мобильная версия решает: почему клиенты уходят с телефона | мобильная версия сайта | ru tool тест-скорости · ru restyling |

> Слаги, точные RU-пути услуг/инструментов и порядок кейсов автор сверяет по
> факту в `patterns/pages/` и `deploy-import.php` (как в батчах 5–6). Фокус-ключи
> — черновые, автор уточняет по seo-meta.md и не переспамливает.

## Статус выполнения
- Батч 7 — ⬜ очередь.
- Батч 8 — ⬜ очередь.
- Батч 9 — ⬜ очередь.
- Батч 10 — ⬜ очередь.
- Батч 11 (RU руками) — ⬜ очередь.
- Батч 12 (RU руками) — ⬜ очередь.
