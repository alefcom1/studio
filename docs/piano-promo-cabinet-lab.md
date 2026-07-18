# Продвижение кабинета (cab.remarka.biz) и Remarka Lab на сайте — позиционирование и план

> Дата: 18.07.2026. Статус: **предложение владельцу** (реализация — после
> утверждения и ответов на вопросы §7). Основание: `piano-cabinet-k1.md`,
> `piano-cabinet-k2.md`, `piano-strumenti-lab.md`, `piano-ai-tools.md`,
> `ricerca-strumenti-lab.md`, `strategia-riposizionamento.md` (Д-1…Д-5).
> Правила реализации — `piano-implementazione-fase-A.md` §0 (без `main()`,
> `translate_pages.py ru` запрещён, атомарные коммиты, mobile-first 390px,
> E-E-A-T: только реальные факты).

---

## 0. Резюме (TL;DR)

1. **Кабинет продаём не как «личный кабинет», а как гарантию прозрачности.**
   Он — продолжение ДНК бренда «числа вместо прилагательных» и «nero su
   bianco»: клиент не верит на слово — он **видит** стадию проекта, историю
   согласований, файлы и счета. На IT-версии это усиливает козырь №1 (срок
   с неустойкой): срок, за которым можно следить, убедительнее срока на
   словах.
2. **Название на сайте — локализованное:** IT «Area clienti», EN «Client
   area», RU «Кабинет клиента». Домен cab.remarka.biz — только в href
   (для итальянца «CAB» читается как банковский код — оговорка из
   piano-cabinet-k1 §10.2; в текстах аббревиатуру не используем).
3. **Remarka Lab — зонтичный бренд «продуктового крыла» студии** с двумя
   ярусами: **Gratis** — 12 бесплатных инструментов на remarka.biz/strumenti/
   (без регистрации, работают на настоящих движках: Google PageSpeed,
   Lighthouse, модель SWD, Claude AI); **Pro — Remarka Lab · Monitor**
   (lab.remarka.biz) — постоянный мониторинг для клиентов студии: краулы,
   аптайм, полевые Core Web Vitals, позиции, ежемесячный PDF-отчёт.
4. **⚠️ Ключевая оговорка:** lab.remarka.biz сейчас за basic auth. Прямую
   ссылку на него давать нельзя, пока там пароль-заглушка. До открытия
   публичной витрины все ссылки «инструменты» ведут на /strumenti/, а
   Monitor упоминается как платформа (без ссылки или со ссылкой-якорем
   на секцию Free vs Pro). Варианты решения — §7, вопрос 1.
5. **Честность копирайта по стадиям кабинета:** рекламируем только то, что
   задеплоено. Копирайт подготовлен в двух версиях: **база K1** (вход без
   пароля, стадии проекта, 3 языка, данные в ЕС) и **расширение K2**
   (согласования, файлы, счета, тикеты) — вторая публикуется только после
   выхода K2 в прод (§7, вопрос 2).
6. Реализация на сайте: новый промо-блок кабинета (главная + services),
   отдельная страница «Area clienti» ×3 языка, апгрейд hero на
   /strumenti/ в «Remarka Lab» с секцией Free vs Pro, ссылка в футере,
   строка в prezzi «cosa è incluso». Этапы M1–M4 — §6.

---

## 1. Фактура (что есть на самом деле — база E-E-A-T)

### 1.1. Кабинет cab.remarka.biz

Из спецификаций K1/K2 (утверждены владельцем 16.07.2026):

- Вход **без пароля**: одноразовая magic-ссылка на e-mail, действует
  15 минут; серверные сессии с возможностью отзыва.
- **8 стадий проекта** (бриф → дизайн → разработка → наполнение → приёмка
  → запуск → поддержка → архив), видимых клиенту в реальном времени.
- Интерфейс и письма **на трёх языках** (IT/EN/RU) — по выбору клиента.
- Данные — **на сервере в ЕС** (Hetzner, Германия), письма — через
  EU-провайдера (Brevo); минимизация данных, аудит входов, GDPR by design.
- K2 (после выката): **согласования** макетов и текстов онлайн с историей
  («кто, что, когда»), **обмен файлами**, **счета** со статусами оплаты,
  **тикеты** вместо потерянных писем, архив проектов.
- K3 (после запуска сайта клиента): дашборд метрик (PSI/CrUX, аптайм,
  позиции из Monitor), ежемесячный PDF-отчёт.

Сильные стороны для рекламы (все — правда, без натяжек):

| Свойство | Почему это продаёт |
|---|---|
| Стадии проекта видны каждый день | материализует гарантию срока («не спрашивайте, на каком мы этапе — смотрите») |
| Согласования с историей (K2) | «nero su bianco» в цифровом виде: решения зафиксированы, споров «мы этого не утверждали» нет |
| Всё в одном месте: файлы, счета, вопросы (K2) | боль малого бизнеса — переписка размазана по почте/мессенджерам |
| Вход без пароля | нечего забывать и нечему утекать; порог входа — один клик из письма |
| 3 языка интерфейса | уникально для студии такого размера; стыкуется с мультиязычным позиционированием |
| Данные в ЕС, GDPR | аргумент и для итальянского B2B, и для RU-клиентов, выходящих в Европу |
| Сделан студией для себя, на своей платформе | доказательство инженерной зрелости: «мы строим web-app — вот наша» |

### 1.2. Remarka Lab

- **12 бесплатных инструментов** на remarka.biz/strumenti/ (×3 языка):
  Test velocità, Analisi SEO, Verifica accessibilità (EAA), Check GDPR,
  Sito pronto per l'AI, Segnali E-E-A-T, Impatto CO₂, ROI localizzazione,
  Check-up completo, плюс 3 AI-инструмента на Anthropic API:
  «Il vostro sito, letto dall'AI», «Suona madrelingua?», Generatore llms.txt.
- Без регистрации и без захвата e-mail; настоящие движки (Google PSI API,
  эвристики по живому HTML, модель Sustainable Web Design, Claude);
  честные дисклеймеры у GDPR/ROI (эвристика/стима, не юрвердикт).
- Уникальность на итальянском рынке (ricerca-strumenti-lab §3): проверка
  готовности к AI и E-E-A-T **по-итальянски не существовали**; verifica
  accessibilità — регуляторная волна EAA со штрафами до 5% оборота.
- **Remarka Lab · Monitor** (lab.remarka.biz): платформа непрерывного
  наблюдения (краулы, аптайм, PSI/CrUX, позиции, PDF-отчёты) — сейчас
  внутренняя (basic auth), по плану K3 её метрики попадают в кабинет
  клиента.

### 1.3. Три воронки (Д-5) — какие акценты где

| Версия | Кабинет — угол подачи | Lab — угол подачи |
|---|---|---|
| IT | прозрачность и срок: «vedete a che punto è il progetto, ogni giorno»; согласования = nero su bianco | комплаенс и первенство: EAA (штрафы), GDPR, «primo check AI-readiness in italiano»; CO₂ для тендеров |
| EN | работать со студией в другой стране без трения: 3 языка, EU-hosting, всё письменно | проверить готовность к рынку ЕС: доступность, GDPR, скорость, локализация |
| RU | «европейское качество процессов»: кабинет как у SaaS, счета и согласования прозрачны — важно при работе с подрядчиком за рубежом | «проверьте сайт перед выходом в Европу»: EAA/GDPR/скорость/ROI локализации; AI-инструменты — на русском |

---

## 2. Позиционирование

### 2.1. Кабинет: «Проект, который видно»

Формула: **не фича, а гарантия**. Кабинет ставим в один ряд с «Nero su
bianco» (PageSpeed 90+, срок с неустойкой, фикс-цена): четвёртый пункт
доверия — «прозрачность по построению». Слоганы-кандидаты:

- IT: **«Vedete il progetto, non solo il preventivo.»**
- EN: **"See the project, not just the quote."**
- RU: **«Вы видите проект, а не только смету.»**

Не обещаем того, чего нет: никаких «24/7 support», «real-time chat».
Только фактические возможности по стадии (K1/K2).

### 2.2. Lab: «Prima misurate, poi decidete» → два яруса

Существующий заголовок карточек на главной («Prima misurate, poi
decidete») уже идеален — он остаётся. Добавляется зонтик:

- **Remarka Lab** = продуктовое/R&D-крыло студии. Легенда: «инструменты,
  которые мы построили для своей работы — открытые для всех».
- **Gratis:** разовые проверки, без регистрации, результат за минуту,
  у каждого инструмента — честный вердикт и что чинить.
- **Pro (Monitor):** то же, но постоянно и с человеком: наблюдение за
  сайтом после запуска, отчёт раз в месяц, алерты — в составе поддержки
  студии (формат/цена — вопрос 3 в §7).

Ключевая связка Free→Pro→Услуга: «проверили бесплатно → увидели проблему
→ мы её чиним (услуга) → дальше следим, чтобы не вернулась (Monitor)».

### 2.3. Кому и чем полезны инструменты (для секции на /strumenti/ и промо)

| Аудитория | Инструменты | Боль |
|---|---|---|
| Владелец PMI перед редизайном | Check-up completo, Test velocità, Analisi SEO | «что не так с моим сайтом и сколько это стоит мне» |
| E-commerce / услуги под EAA | Verifica accessibilità, Check GDPR | штрафы до 5% оборота, иски уже идут |
| Маркетолог, проверяющий подрядчика | Analisi SEO, Segnali E-E-A-T, Test velocità | принять работу агентства по числам, а не по словам |
| Экспортёр / выход на новый рынок | ROI localizzazione, Suona madrelingua?, Impatto CO₂ | сколько денег теряется без локализации; не звучит ли текст «переводно» |
| Все, кто хочет быть видимым в ChatGPT/Perplexity | Sito pronto AI, Sito letto dall'AI, Generatore llms.txt | новый канал трафика (GEO), по-итальянски инструментов нет |

---

## 3. Карта размещения на сайте (все 3 языка зеркально)

| # | Место | Что добавляем | Механика |
|---|---|---|---|
| 1 | Главная, после секции come-lavoriamo | **Промо-блок «Area clienti»** (тёмный, в стиле garanzie-dark): слоган, 4 буллета, CTA «Come lavoriamo →» + «Accedi →» (cab.remarka.biz) | новый паттерн `area-clienti-blocco.php` (+lang-en/lang-ru) |
| 2 | Главная, секция strumenti-cards | eyebrow «Strumenti gratuiti» → **«Remarka Lab · Strumenti gratuiti»**; под карточками — 1 строка Pro-тизера со ссылкой на /strumenti/#monitor | правка паттерна strumenti-cards ×3 |
| 3 | **Новая страница** `/area-clienti/`, `/en/client-area/`, `/ru/kabinet-klienta/` | полноценный лендинг кабинета (§4.2): hero, «come funziona» (3 шага), фичи по стадиям, безопасность/GDPR, FAQ, CTA двойной (клиенты → войти; не-клиенты → contatti) | data.py + generate_pages (точечно), page_map +3, lang.py +тройка, hreflang, seo-meta.md |
| 4 | `/strumenti/` index ×3 | hero-апгрейд: бренд Remarka Lab, число «12 strumenti», якорная секция **Free vs Pro (#monitor)** внизу (§4.4) | правка strumenti-index в генераторе |
| 5 | Страницы услуг (9 servizio-* ×3) | 1 строка в секции процесса: «Ogni progetto include l'accesso all'area clienti: fasi, approvazioni e file in un posto solo» + ссылка на /area-clienti/ | data.py, точечная регенерация |
| 6 | `/prezzi/` ×3 | строка в «cosa è incluso»: area clienti в каждом проекте | правка pattern prezzi |
| 7 | Футер ×3 | пункт «Area clienti / Client area / Кабинет» → cab.remarka.biz | deploy-import.php (sync footer menu) |
| 8 | chi-siamo ×3 | абзац «инновации»: своя платформа (Lab + Monitor + кабинет), AI-инструменты — доказательство «строим web-app и для себя» | правка pattern |
| 9 | Блог (очередь piano-blog) | 2 статьи-кандидата: «Area clienti di un'agenzia web: cosa pretendere» (SEO: прозрачность подрядчика) и «Monitoraggio del sito dopo il lancio: cosa misurare ogni mese» (подводка к Monitor) | по конвейеру блога |

Главные меню НЕ расширяем (правило 5+CTA).

---

## 4. Черновики копирайта

Тон: числа, «voi», без пафоса (IT); нейтральный EN; RU на «вы».
Формат евро «€ N NNN». Ниже — версия «после K2»; строки, помеченные
`[K2]`, при публикации до выката K2 опускаются.

### 4.1. Промо-блок кабинета (главная)

**IT**

> *eyebrow:* Area clienti
>
> **Vedete il progetto, non solo il preventivo.**
>
> Ogni progetto Remarka include l'accesso all'area clienti: la fase del
> lavoro è visibile ogni giorno, dal brief al lancio. [K2] Approvate
> bozze e testi con un click, scaricate file e fatture, fate domande
> tracciate — niente email perse.
>
> - 8 fasi del progetto, sempre visibili
> - [K2] Approvazioni con storico: chi ha approvato cosa, e quando
> - [K2] File, fatture e richieste in un unico posto
> - Accesso senza password, dati su server UE, interfaccia in 3 lingue
>
> [Come funziona l'area clienti →](/area-clienti/) · [Accedi →](https://cab.remarka.biz/)

**EN**

> *eyebrow:* Client area
>
> **See the project, not just the quote.**
>
> Every Remarka project includes access to the client area: the current
> stage is visible every day, from brief to launch. [K2] Approve drafts
> and copy in one click, download files and invoices, keep every question
> on record — no lost emails.
>
> - 8 project stages, always visible
> - [K2] Approvals with history: who approved what, and when
> - [K2] Files, invoices and requests in one place
> - Passwordless login, data on EU servers, interface in 3 languages
>
> [How the client area works →](/en/client-area/) · [Log in →](https://cab.remarka.biz/)

**RU**

> *eyebrow:* Кабинет клиента
>
> **Вы видите проект, а не только смету.**
>
> В каждый проект Remarka входит доступ в кабинет клиента: стадия работы
> видна каждый день — от брифа до запуска. [K2] Согласования макетов и
> текстов в один клик, файлы и счета под рукой, вопросы — с историей,
> а не в потерянных письмах.
>
> - 8 стадий проекта — всегда на виду
> - [K2] Согласования с историей: кто, что и когда утвердил
> - [K2] Файлы, счета и вопросы в одном месте
> - Вход без пароля, данные на серверах ЕС, интерфейс на 3 языках
>
> [Как устроен кабинет →](/ru/kabinet-klienta/) · [Войти →](https://cab.remarka.biz/)

### 4.2. Страница «Area clienti» (структура + ключевые тексты)

Секции (mobile-first, от 390px):

1. **Hero.** IT: «L'area clienti Remarka: il progetto, nero su bianco» /
   подзаголовок: «Fasi, [K2] approvazioni, file e fatture — in un unico
   posto, in italiano, inglese o russo». CTA: «Accedi» + «Non siete
   ancora clienti? Parliamone →» (/#contatti).
2. **Come funziona — 3 шага:** (1) inserite la vostra email — niente
   password: vi mandiamo un link che vale 15 minuti; (2) aprite il
   progetto: la fase corrente è evidenziata, dal brief al lancio;
   (3) [K2] approvate, scaricate, chiedete — ogni azione resta agli atti.
3. **Фичи** (карточки, 4–6 шт. по списку §1.1).
4. **Perché l'abbiamo costruita** (доверие/инновации): «Siamo uno studio
   che sviluppa web app — e l'area clienti è la nostra: stessa
   piattaforma, stessi standard che vendiamo. Nessun gestionale di terzi,
   nessun dato fuori dall'UE.»
5. **Sicurezza e privacy:** senza password (link monouso), sessioni
   revocabili, dati minimi necessari, server in Germania (UE), audit
   degli accessi. Ссылка на privacy.
6. **FAQ (3):** «Quanto costa?» — Niente: è inclusa in ogni progetto. /
   «Serve installare qualcosa?» — No, funziona dal browser, anche dal
   telefono. / «In che lingua?» — Italiano, inglese o russo: scegliete voi.
7. **CTA-finale** двойной.

RU-страница — самодостаточный текст (не калька): акцент «работаете со
студией в Италии — процессы прозрачны, как в хорошем SaaS: видно стадию,
[K2] счета и согласования зафиксированы письменно».

### 4.3. Правка секции инструментов на главной

- eyebrow: «Strumenti gratuiti» → **«Remarka Lab · Strumenti gratuiti»**
  (EN: «Remarka Lab · Free tools», RU: «Remarka Lab · Бесплатные
  инструменты»).
- Строка под карточками (все 3 языка), пример IT:
  > 12 strumenti, nessuna registrazione. E per i clienti c'è il livello
  > Pro: [monitoraggio continuo del sito →](/strumenti/#monitor)

### 4.4. Секция Free vs Pro на /strumenti/ (#monitor)

**IT (черновик):**

> *eyebrow:* Remarka Lab
>
> **Gratis oggi. Sotto controllo domani.**
>
> | | **Strumenti gratuiti** | **Remarka Lab · Monitor (per i clienti)** |
> |---|---|---|
> | Che cosa | 12 check una tantum: velocità, SEO, accessibilità EAA, GDPR, AI-readiness, E-E-A-T, CO₂, ROI + 3 strumenti AI | il vostro sito osservato in continuo dopo il lancio |
> | Come | inserite l'URL, risultato in ~1 minuto | crawl periodici, uptime, Core Web Vitals reali degli utenti, report PDF mensile |
> | Registrazione | nessuna | incluso nei progetti con manutenzione; accesso dall'area clienti |
> | Chi corregge | voi (o noi, se volete: ogni strumento indica il servizio giusto) | noi: se un valore peggiora, lo vediamo prima che diventi un problema |
>
> Un punteggio si può misurare gratis una volta. Tenerlo alto nel tempo
> è un lavoro — ed è il nostro.

EN/RU — зеркально (EN конвейером, RU руками; RU-заголовок:
«Бесплатно — сегодня. Под наблюдением — всегда.»).

Примечание: до открытия lab.remarka.biz колонка Pro ведёт не на URL
платформы, а на /#contatti или /area-clienti/ («accesso dall'area
clienti» — честно и без битой ссылки).

### 4.5. Строка для страниц услуг (IT, пример)

> Ogni progetto include l'area clienti: fasi del lavoro[K2], approvazioni
> e file in un unico posto. [Come funziona →](/area-clienti/)

---

## 5. SEO-мета (черновик — финализируется в seo-meta.md при реализации)

| Страница | Focus key | Title (≤60) | Description (≤155) |
|---|---|---|---|
| /area-clienti/ | area clienti agenzia web | Area clienti — Studio Remarka | Fasi del progetto visibili ogni giorno, approvazioni e fatture in un posto solo. Senza password, dati in UE, in 3 lingue. Inclusa in ogni progetto. |
| /en/client-area/ | web agency client portal | Client area — Remarka Studio | Project stages visible every day, approvals and invoices in one place. Passwordless, EU-hosted, in 3 languages. Included in every project. |
| /ru/kabinet-klienta/ | кабинет клиента веб-студии | Кабинет клиента — Студия Remarka | Стадии проекта видны каждый день, согласования и счета в одном месте. Без паролей, данные в ЕС, 3 языка. Входит в каждый проект. |

Страница кабинета — прежде всего **трастовая**, не трафиковая: низкие
частоты, но конверсионная роль в сравнении подрядчиков («у них есть
кабинет — у других переписка в WhatsApp»). Схема: WebPage + FAQPage.

---

## 6. Этапы реализации (после утверждения)

| Этап | Состав | Гейт |
|---|---|---|
| **M0** | Ответы владельца на §7 → фиксация финального копирайта (снять/оставить [K2]-строки) | решение |
| **M1 (IT)** | Паттерн area-clienti-blocco; страница area-clienti (data.py + генератор, точечно); правки strumenti-cards, strumenti-index (#monitor), prezzi, chi-siamo, 9 servizio-*; page_map +1; футер | скрины 390/1440 |
| **M2 (EN)** | CHROME-пары → `translate_pages.py en`; page_map +1; проверка диффов | скрины EN |
| **M3 (RU)** | Всё руками (перевод-адаптация): страница, блоки, строки услуг; page_map +1 | скрины RU |
| **M4 (QA)** | php -l, линк-аудит (нет ссылок на закрытый lab.*), hreflang-тройка, регрессия форм, seo-meta.md, деплой-чеклист с полным блоком команд | пакет владельцу |

Правила: `main()` в generate_pages.py запрещён; `translate_pages.py ru`
запрещён; коммиты атомарные без ID моделей; внешняя ссылка на
cab.remarka.biz — `rel="noopener"`, без nofollow (свой домен).

---

## 7. Открытые вопросы владельцу

1. **lab.remarka.biz за basic auth.** Рекламировать URL, отдающий запрос
   пароля, нельзя. Варианты: **(а)** открыть на lab.remarka.biz публичную
   витрину (лендинг Lab: каталог инструментов + вход в Monitor для
   клиентов) — красиво, но отдельная задача; **(б)** сейчас все ссылки
   ведут на remarka.biz/strumenti/, Monitor упоминается текстом без
   прямой ссылки (как в §4.4). **Рекомендация: (б) немедленно, (а) —
   отдельной задачей после стабилизации Monitor.**
2. **Что реально в проде у кабинета** на момент публикации: K1 (стадии)
   или уже K2 (согласования/файлы/счета/тикеты)? От этого зависит,
   публикуем ли [K2]-строки сразу или вторым коммитом после выката K2.
3. **Monitor как платная возможность:** формат — включён в
   поддержку/retainer (рекомендация: так и писать, без цены) или
   отдельная подписка с публичной ценой? Пока цены нет, копирайт §4.4
   сформулирован без цифр — можно публиковать как есть.
4. **Скриншоты кабинета** для лендинга /area-clienti/: ждём стабильный UI
   (после K2) или публикуем первую версию страницы без скриншотов
   (текст + степпер-иллюстрация на CSS)? Рекомендация: без скриншотов
   не ждать, добавить вторым заходом.
5. **RU-слаг страницы кабинета:** предложен `/ru/kabinet-klienta/` —
   подтвердить (альтернатива `/ru/kabinet/`).
