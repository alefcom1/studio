# Гео-страницы по городам Италии — план (утверждён владельцем 17.07.2026)

> Цель: покрыть локальный спрос «realizzazione siti web ‹città›» по ~100
> городам Италии БЕЗ doorway-паттерна (Google spam policies 03.2024:
> doorway pages / scaled content abuse). Вместо 100 клонов — три уровня:
> ручные страницы крупных городов, программатик с уникальными данными,
> региональные хабы.
>
> **Ключевой факт от владельца (17.07): у студии есть офисы в Турине и
> Риме** (помимо основного присутствия). Страницы Torino и Roma — флагманы
> с реальным локальным присутствием: офис, встречи вживую. Это НЕ
> «удалёнка с честной оговоркой», это настоящий local — использовать
> в копирайте, FAQ и (после получения адресов) в LocalBusiness-schema.

## Запросы

- Фокус-ключ страницы: `realizzazione siti web [città]` (как у 5 готовых).
- Вариации в H2: `creazione siti web [città]`, `web agency [città]`.
- FAQ-блок: `quanto costa un sito web a [città]` (+ prezzo chiuso),
  `siti web per [отрасль] a [città]` — где у города выраженная отрасль.
- Города — ТОЛЬКО IT-версии (интент итальянский). Milano EN/RU — искл.

## Уровни

### Tier 1 — ручной копирайт (≈15 городов)
Готово: Milano (расшир.), Bergamo, Brescia, Como, Monza.
Новые 12: **Roma**, **Torino** (флагманы, офисы), Napoli, Bologna,
Firenze, Genova, Verona, Padova, Bari, Venezia-Mestre, Palermo, Catania.

Батчи реализации:
- **G1a — Roma + Torino** (особая тщательность, решение владельца):
  объём и глубина ≥ citta-milano; офисы в копирайте («ci incontriamo di
  persona»), локальные FAQ, отраслевой профиль города с реальными цифрами
  (Camera di Commercio/ISTAT), релевантные кейсы. LocalBusiness-schema —
  ЗАБЛОКИРОВАНО до получения адресов офисов от владельца (см. «Открытые
  вопросы»); до тех пор Service+areaServed, как у остальных.
- **G1b — остальные 10** (по 2 связки: Nord/Centro/Sud), тем же уровнем,
  но без офисной легенды — честная формула «lavoriamo in tutta Italia,
  uffici a Torino e Roma, incontri in video o di persona su appuntamento».

### Tier 2 — программатик (~35–40 средних городов) — ПОСЛЕ G1
Обязательные уникальные блоки на город: отрасли/дистретты, число imprese
(источник), лид-сценарий, локальные FAQ, релевантный кейс. Без выдумок.

### Tier 3 — 20 регионов — ПОСЛЕ первых порций Tier 2
`realizzazione siti web in [regione]` + список городов; город получает
свою страницу только при реальных показах в GSC.

## Правила (все уровни)

1. Анти-doorway: у каждой страницы уникальные данные и причина
   существовать; никакой подстановки города в шаблонный текст.
2. Честность E-E-A-T: офисы — только Torino/Roma (реальные); НЕ выдумывать
   адреса/отзывы/«команда в [città]». Цифры — с источником.
3. Schema: Service + areaServed(City); LocalBusiness — только Torino/Roma
   и только после адресов. Никаких фейковых GBP.
4. Слаги плоские `/[città]/` (как /milano/), page_map, deploy-import,
   Title ≤60 / Description ≤160 в seo-meta.md, mobile-first 390.
5. Перелинковка: хаб «Dove lavoriamo» (сделать в G1b) ↔ города ↔ услуги ↔
   инструменты Lab; соседние города региона между собой.
6. Выкат порциями (≤15 страниц/неделя), контроль индексации GSC + позиции
   в Monitor. Стоп-кран: нет индексации/показов после 2 порций Tier 2 —
   пауза и пересмотр.
7. Механика конвейера — как всегда: точечные build-вызовы (main()
   запрещён), git diff, php -l, коммит без ID моделей.

## Решения владельца (17.07, вторая волна)

- **Адреса офисов получены** (Milano Vicolo Privato Lavandai 2a · Torino
  Corso Regina Margherita 94 · Roma Via Flaminia 122; Tel./WhatsApp
  +39 347 83 11141, info@remarka.biz, P.IVA GE 302230994). Приём только
  по записи. Карточки Google Maps существуют давно, НО зарегистрированы
  под брендом **ATT · Agenzia di Traduzione Tecnica** (переводческое
  агентство группы, те же офисы) — на страницах подаём как козырь
  доверия с пояснением, в schema бренды не смешиваем (LocalBusiness =
  Studio Remarka, hasMap не указываем). Апдейт U1 запущен.
- **Доставка документов**: без карт пунктов выдачи; на страницах городов
  без офисов — одна строка в блоке «Come lavoriamo»: печатные документы
  (traduzioni giurate, contratti) доставляем по всей Италии курьером
  **BRT / Poste Italiane / DHL** (только эти три — реально используемые).
- **CTA-блок «Parliamo» сливается с футером** (замечание владельца):
  перекрасить CTA-полосу в oltremare #2440C8, кнопки инвертировать.
  Делает оркестратор после U1.

## Открытые вопросы владельцу

1. ~~**Адреса офисов Torino и Roma**~~ — закрыт 17.07 (см. «Решения владельца,
   вторая волна» + «Статус», батч U1): адреса получены и опубликованы.
2. Основная юр. точка (Milano? юр. адрес юрлица) — как позиционируем.
3. ~~Google Business Profile~~ — закрыт 17.07: владелец оставляет карточки
   ATT как есть, отдельные GBP «Studio Remarka» не заводим. Страницы
   честно ссылаются на карточки ATT с пояснением — этого достаточно.

## Статус
- 17.07: план утверждён; G1a (Roma+Torino) запущен.
- 17.07: **G1a выполнен и вычитан оркестратором** (коммит `eddf4f7`; проверены
  честность цифр — автокомпоненты поданы как общеитальянские с оговоркой,
  аэроспейс как пьемонтский; «160 progetti dal 2001» и цены сверены с
  casi-studio/prezzi; пустой блок на превью — штатный [sr_shot]-плейсхолдер).
  Страницы `/roma/` и `/torino/` (флагманы с офисами)
  сгенерированы (`build_city_flagship` в generate_pages.py, данные в
  data.py `CITIES`), зарегистрированы в deploy-import (page_map + footer-studio),
  мета в seo-meta.md. Цифры настроя с источниками (Camera di Commercio Roma/
  Torino, ANFIA, Regione Piemonte, Roma Capitale). Офис — без адреса (не выдуман),
  LocalBusiness-schema НЕ добавлена. Открытый вопрос №1 (адреса) остаётся:
  после получения — добавить NAP в /roma/, /torino/, /contatti/ и LocalBusiness.
- 17.07: **G1b-2 выполнен и вычитан оркестратором** (коммит `b5be5b4`):
  Firenze, Napoli, Bari, Palermo, Catania + хаб `/dove-lavoriamo/` (3 офиса
  с адресами и ATT-пояснением, 17 городов по макрозонам, метка футера —
  ссылка на хаб) + строка доставки BRT/Poste/DHL во всех 10 городах без
  офисов. **Tier 1 полностью завершён: 17 городских страниц + хаб.**
  Следующий шаг после деплоя и 2–3 недель наблюдения GSC/Monitor — Tier 2.
- 17.07: **U1 выполнен и вычитан оркестратором** (коммит `7014617`) — открытый вопрос №1 закрыт. NAP публичный
  (Studio Remarka S.r.l., индирiзzo/tel/email/P.IVA) добавлен на `/roma/`,
  `/torino/`, `/milano/` + `/en/milan/` + `/ru/milan/`: карточка адреса,
  карта Google click-to-load (GDPR — nessuna richiesta prima del click,
  `office_dove_siamo()` in generate_pages.py, CSS `.sr-mappa` in remarka.css,
  JS `initOfficeMap()` in remarka.js), спокойное пояснение про ATT ·
  Agenzia di Traduzione Tecnica (стоит на тех же картах Maps — подано как
  козырь доверия, не спрятано). LocalBusiness-schema (ProfessionalService,
  legalName/vatID/parentOrganization) — новый хук
  `remarka_office_local_business_schema()` в functions.php, на слагах
  `milano`/`torino`/`roma`/`milan` (EN+RU). Milano получил офисный блок
  флагманского уровня (раньше был плейсхолдер с вымышленным адресом/
  телефоном — исправлено). Открытый вопрос №2 (юр. точка) остаётся.
