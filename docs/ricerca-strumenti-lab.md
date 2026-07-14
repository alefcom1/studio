# Remarka Lab — исследование: инструменты международного рынка и дыры итальянского

> Дата: 14.07.2026. Статус: предложение владельцу (реализация — после утверждения).
> Контекст: на /strumenti/ работает 1 из 4 инструментов (Test velocità на PSI API);
> Check GDPR, Analisi SEO, ROI localizzazione — заглушки «In arrivo».

---

## 1. Что предлагают современные сайты (международная картина)

Категории бесплатных инструментов-лидмагнитов у сильных западных студий/SaaS:

1. **Аудиторы по URL** (ввёл адрес → балл + разбор): скорость, SEO, доступность,
   безопасность, «AI-готовность». Классика конверсии: результат → CTA «исправим».
2. **Калькуляторы** (ROI, стоимость, экономия): наш ROI localizzazione из этой серии.
3. **Генераторы** (llms.txt, política privacy, schema.org): дешёвый трафик, вирусность.
4. **Мониторинги с e-mail-отчётом** (ежемесячный балл скорости/доступности):
   захват почты → нуртуринг. Уровень выше разовой проверки.

Свежий тренд 2025–2026 — **GEO/AEO** (Generative Engine Optimization): проверka
видимости сайта для ChatGPT/Perplexity/AI Overviews. В мае 2026 Google добавил
llms.txt в аудит Lighthouse «Agentic Browsing» — «AI-готовность» стала
официальным сигналом ([llmstxtgenerator](https://llmstxtgenerator.org/),
[SEOptimer GEO checks](https://www.seoptimer.com/blog/new-geo-checks/)).

## 2. Открытый код и бесплатные API под нашу инфраструктуру

| Основа | Что даёт | Лицензия/доступ | Сервер? |
|---|---|---|---|
| **PSI API v5 (уже интегрирован!)** | Кроме performance отдаёт категории Lighthouse: **accessibility, seo, best-practices** | бесплатно, ключ уже в Customizer | нет — наш JS уже умеет |
| [co2.js](https://github.com/thegreenwebfoundation/co2.js/) (Green Web Foundation) | CO₂-след страницы по весу трафика (модель SWD v4) + проверка «зелёного» хостинга | Apache-2.0 | нет (вес берём из PSI total-byte-weight) |
| [axe-core](https://github.com/dequelabs/axe-core) | Глубокий WCAG-аудит (v2 инструмента доступности) | MPL-2.0 | да (headless) — этап 2 |
| Mozilla HTTP Observatory API v2 | Балл безопасности заголовков | бесплатный API | нет |
| [geo-optimizer-skill](https://github.com/Auriti-Labs/geo-optimizer-skill) | Открытый GEO/AEO-аудит: llms.txt, structured data, AI-краулеры | open source | частично (fetch через мини-прокси) |
| CrUX API | Полевые Core Web Vitals (реальные пользователи) для мониторинга с e-mail | бесплатно | крон + почта (SMTP уже есть) |
| Blacklight-collector (The Markup) | Скан трекеров/кук до согласия — движок для Check GDPR | open source | да (puppeteer) — этап 2 |

**Ключевая находка:** два наших «In arrivo» — Analisi SEO и (базовая) проверка
доступности — запускаются **на уже существующих рельсах PSI API** почти без
нового кода: тот же запрос с `category=SEO&category=ACCESSIBILITY`.

## 3. Дыры итальянского рынка

### 3.1. 🔴 Verifica accessibilità EAA — регуляторная волна, слабая конкуренция

С 28.06.2025 действует European Accessibility Act: WCAG 2.1 AA обязателен для
e-commerce/услуг, исключение только для микропредприятий (<10 чел., <€2 млн);
**в Италии штрафы до 5% годового оборота**, во Франции уже пошли иски к
ритейлерам ([Bird & Bird](https://www.twobirds.com/en/insights/2025/a-guide-to-navigating-the-european-accessibility-act-for-online-retailers-service-providers-and-plat),
[AccessibleEU](https://accessible-eu-centre.ec.europa.eu/content-corner/news/eaa-comes-effect-june-2025-are-you-ready-2025-01-31_en)).
По-итальянски есть лишь несколько маленьких чекеров ([пример](https://tabnav.com/it/test-accessibilita-sito-web)) —
ниша не занята сильным игроком. Спрос будет расти с первыми итальянскими штрафами.
**Плюс это не только инструмент — это новая услуга «Adeguamento EAA»** (аудит +
исправление + accessibility statement), которой нет в нашей линейке.

### 3.2. 🔴 «Il tuo sito è pronto per l'AI?» — по-итальянски НЕ существует

GEO-чекеры на английском уже есть, по-итальянски — пусто. Проверки: llms.txt,
robots.txt для AI-краулеров (GPTBot и др.), structured data, цитируемость.
Первопроходец в SERP «llms.txt cos'è», «sito visibile su ChatGPT» забирает нишу
целиком + сильный PR-повод. Синергия с нашей SEO tecnica.

### 3.3. 🟡 Impatto CO₂ del sito — редкость в Италии, дёшево строится

Websitecarbon/Ecograder — западная классика на co2.js; итальянских аналогов
почти нет. Нулевой бэкенд (PSI вес + co2.js). B2B-угол: крупным клиентам нужны
данные для CSRD-отчётности. Хорошо звучит в прессе и соцсетях.

### 3.4. 🟡 Check GDPR (наша заглушка) — движок Blacklight, этап 2

Скан трекеров до согласия — сильно, но требует серверного puppeteer.
Рынок конкурентнее (экосистема iubenda). Делать после 3.1–3.3.

### 3.5. ⚪ Security headers по-итальянски «без жаргона» — низкий приоритет

Легко (Observatory API), но аудитория SMB слабо ищет.

## 4. Рекомендация (приоритет реализации)

| # | Инструмент | Стройматериал | Оценка работ | Зачем |
|---|---|---|---|---|
| 1 | **Verifica accessibilità (EAA)** v1 | PSI accessibility + наш виджет теста скорости | ~2–3 дня | регуляторный спрос, штрафы 5%, ведёт в новую услугу Adeguamento EAA |
| 2 | **Analisi SEO on-page** (оживить заглушку) | PSI seo category | ~1–2 дня | обещание уже висит на сайте |
| 3 | **Sito pronto per l'AI?** (новый) | llms.txt/robots/schema-чеки + geo-optimizer идеи | ~3–4 дня | пустая ниша, PR, официальный сигнал Lighthouse |
| 4 | **Impatto CO₂** (новый) | co2.js + PSI byte weight | ~2 дня | дифференциация, CSRD-угол |
| 5 | ROI localizzazione (заглушка) | чистый калькулятор | ~1 день | закрыть обещание |
| 6 | Check GDPR v2 (Blacklight) + axe-core a11y v2 + CrUX-мониторинг с e-mail | серверные | по 3–5 дней | этап 2, после SMTP/крона |

Каждый инструмент заканчивается CTA в свою услугу: EAA → Adeguamento EAA (новая),
AI → SEO tecnica/contenuti, CO₂ → Restyling/performance, SEO → SEO tecnica.

**Стратегическая заметка:** самое ценное в списке — не инструмент, а
**услуга «Adeguamento EAA»**: дедлайн прошёл, санкции реальные, итальянские
SMB массово не готовы, а у нас уже есть вся упаковка (prezzo chiuso, сроки,
гарантии). Инструмент №1 — её лидогенератор.

## 5. SEO-запросы под инструменты

verifica accessibilità sito · sito conforme EAA / European Accessibility Act ·
test accessibilità WCAG · llms.txt cos'è · sito visibile su ChatGPT ·
ottimizzazione AI (GEO) · impronta di carbonio sito web · sito sostenibile ·
analisi SEO gratuita · сколько инструмент — столько статей-спутников в блог.
