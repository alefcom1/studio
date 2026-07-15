# Copy-deck — Casi studio / Case studies / Кейсы (IT · EN · RU)

> Дата: 2026-07-15 · Автор: Opus (стратег-копирайтер Studio Remarka)
> Основание: утверждённая концепция переработки раздела кейсов (см. бриф),
> `docs/piano-implementazione-fase-A.md` §0 (тон), `docs/copy-fase-B.md` (стиль RU-воронки),
> `docs/seo-meta.md` (формат мета), `build-tools/lang.py` (URL-слаги), `build-tools/data.py` (услуги).
> Репозиторий НЕ редактировался — единственный выход этот файл.

---

## ⚠️ ВАЖНО ДЛЯ ЧИТАЮЩЕГО — не удалось открыть живые сайты

Все 10 живых проектов заблокированы egress-политикой окружения: и WebFetch, и `curl`
через прокси возвращают **403 на CONNECT-туннеле** (это отказ политики, а не сбой; README
прокси прямо запрещает обходить). Проверить не удалось НИ ОДИН из:
`traduzione.tech`, `tms.perevod4.ru`, `@massimoalefBot`, `ai.perevod4.ru`, `perevod4.ru`,
`traduzione.tech/gioco/`, `ukrinitsy.ru`, `moscowtrans.ru`, `techperevod.com`, `пере.рф`,
`1russian.com`, `moscowtrans.ru/test-perevodchika/`.

**Единственное исключение по фактуре:** для 1russian.com в песочнице есть склонированный
репозиторий `/workspace/1russian.com` (read-only, изучен 15.07): подтверждено — WordPress на
хостинге REG.RU, деплой только через каталог `deploy/` репозитория; в репо также живёт
**SiteLens** — собственный self-hosted SEO-анализатор группы (Node.js/TypeScript, Docker,
монорепо pnpm: краулер, движок SEO-правил, интеграции GSC/PageSpeed), который краулит
1russian.com удалённо. Контент самого сайта в репо не хранится — содержание карточки всё равно
сверить с живым сайтом.

**Следствие:** тексты ниже написаны по описаниям владельца и по логике каждого типа проекта.
Всё, что я не могу подтвердить с экрана (точный стек, состав интерфейса TMS), помечено
`[ПРОВЕРИТЬ: …]`. **Обновление 15.07:** владелец прислал реальные цифры по всем кейсам, кроме
gioco, — они проставлены в основных «вариантах с цифрами» (сводка использованного/опущенного —
§7); варианты «без цифр» сохранены как fallback. **Перед публикацией владелец/имплементатор
обязан сверить каждую карточку с живым сайтом** — особенно подписи скриншотов TMS, названия
версий/языков и описания стека.

---

## 0. Рамка честности (общая для всех языков — держать во всех текстах)

Каждый кейс — **проект нашей собственной группы Remarka** (бюро переводов с 2001 г. + студия).
Мы строили эти системы для себя, под свою нагрузку и свои деньги. Клиент получает **ту же
инженерию**. Никаких выдуманных заказчиков, отзывов и цифр «с потолка»; в каждой карточке —
**живая ссылка** на работающий проект. Без превосходных степеней. Числа — только реальные
(проставит владелец) или честные диапазоны.

---

# 1. SEO-БЛОК (3 языка)

## 1.1. Логика фокус-ключей

**IT.** Из двух кандидатов бренда/интента:
- `casi studio web agency` — низкая частотность, к тому же «caso studio» в итальянском
  двусмысленно (academic case study). Как единственный фокус слабоват.
- `portfolio siti web` — выше коммерческий интент и объём: так ищут «примеры/портфолио
  сделанных сайтов» перед выбором агентства.
- **Решение:** основной фокус-ключ страницы — **`portfolio siti web`**; `casi studio`
  остаётся в H1/навигации как название раздела (бренд-слой), в мету не тащим как единственный
  ключ. Вариация-хвост в H2: `esempi di siti web realizzati`, `progetti web agency`.

**EN.** Аналогично: основной фокус — **`web design portfolio`** (объём + интент выше, чем у
`web development case studies`); `case studies` — название раздела. Хвост: `web projects we built`.

**RU.** Страница-история, не каталог, но SEO нужно. Основной фокус — **`портфолио веб-студии`**
(коммерческий интент), с брендовым слоем `кейсы`. Вторичный смысловой хвост под воронку:
`сайты для бизнеса в Италии`, `вывод бизнеса на рынок Европы` — вплетены в текст естественно,
без набивки (в мету как единственный ключ не ставим, чтобы не конкурировать с лендингами).

## 1.2. Мета — IT `/casi-studio/`

- **Focus Keyword:** `portfolio siti web`
- **Title (≤60):** `Portfolio e casi studio — progetti del gruppo | Remarka`  *(54 зн.)*
- **Description (≤160):** `I progetti che il gruppo Remarka ha costruito per sé: siti, web app, SEO e localizzazione in più lingue. Ogni caso con link al progetto vivo, dal 2001.`  *(157 зн.)*
- **H1:** `Non un portfolio di clienti. I sistemi che abbiamo costruito per noi.`
- **Вариации H2 (по секциям/фильтру):** `Siti aziendali e vetrina` · `Web app e prodotti` ·
  `SEO tecnica e contenuti` · `Restyling e marketing` · `Perché mostriamo i nostri progetti, non quelli dei clienti`

## 1.3. Мета — EN `/en/case-studies/`

- **Focus Keyword:** `web design portfolio`
- **Title (≤60):** `Portfolio & case studies — projects we built | Remarka`  *(55 зн.)*
- **Description (≤160):** `The projects the Remarka group built for itself: websites, web apps, technical SEO and native localisation. Every case links to the live project, since 2001.`  *(159 зн.)*
- **H1:** `Not a client portfolio. The systems we built for ourselves.`
- **H2 variations:** `Business & brochure sites` · `Web apps & products` · `Technical SEO & content` ·
  `Redesign & marketing` · `Why we show our own projects, not clients' logos`

## 1.4. Мета — RU `/ru/kejsy/`

- **Focus Keyword:** `портфолио веб-студии`
- **Title (≤60):** `Кейсы: как мы сами вышли на рынок Европы | Remarka`  *(50 зн.)*
- **Description (≤160):** `Мы сами прошли путь на рынок Италии и Европы: свои проекты — от бюро переводов с 2001 года до веб-приложений. Портфолио, за которым живые ссылки, а не логотипы.`  *(158 зн.)*
- **H1:** `Мы не показываем чужие логотипы. Мы показываем путь, который прошли сами<span class="sr-accent-dot">.</span>`
- **Вариации H2:** `Мы знаем русский рынок` · `Мы вывели эти проекты в Европу` ·
  `Мы умеем не только сайты, но и продукты` · `Что это значит для вашего сайта`

---

# 2. IT — `/casi-studio/`

## 2.1. Интро страницы

- **Eyebrow:** `Casi studio`
- **H1:** `Non un portfolio di clienti. I sistemi che abbiamo costruito per noi<span class="sr-accent-dot">.</span>`
- **Lead (вводка, 2 абзаца):**

  > Molte web agency mostrano loghi di clienti. Il gruppo Remarka lavora con le lingue dal 2001 —
  > e **dallo stesso anno costruisce siti**: già nel 2002–2003 ne realizzava per aziende terze,
  > e alcuni sono online ancora oggi (directindustry.com.ru · ivextrans.eu · beltran.by
  > `[ПРОВЕРИТЬ: сайты 2002–2003 живы]`). Da allora abbiamo realizzato **oltre 160 progetti**;
  > **28** sono oggi in manutenzione continua presso di noi. Studio Remarka è la vetrina nuova
  > di questo lavoro, non il suo inizio.

  > Qui sotto trovate i sistemi che il gruppo ha costruito **per sé**: per gestire il proprio
  > lavoro, portare i propri servizi su Google, vendere in più lingue. Li usiamo ogni giorno, con
  > i nostri soldi e la nostra reputazione in gioco — e quando lavorate con noi ricevete **la
  > stessa ingegneria**. Ogni caso ha un **link al progetto vivo**: potete aprirlo, provarlo,
  > misurarlo da soli. Nessun cliente inventato, nessun numero non verificabile.

- **Подпись под интро (mono):** `Ogni scheda porta al progetto online. I punteggi e le metriche sono verificabili sul posto.`

## 2.2. Фильтр по категориям (подписи)

Строка фильтра над сеткой (кнопки-чипы, `data`-фильтр по категории карточки):

| Ключ фильтра | Подпись IT |
|---|---|
| `all` | `Tutti i progetti` |
| `siti` | `Siti aziendali e vetrina` |
| `webapp` | `Web app e prodotti` |
| `seo` | `SEO tecnica e contenuti` |
| `restyling` | `Restyling e marketing` |

Микроподпись под фильтром (mono, опц.): `11 progetti del gruppo · filtra per tipo di lavoro`

## 2.3. Карточки кейсов (IT) — 11 штук

> Формат каждой карточки: **Titolo · Categoria (chip) · Problema (2–3 фразы) · Soluzione (3–4) ·
> Stack e tempi (строка) · Risultato (2 варианта: с плейсхолдером-цифрой и без цифр) · Alt
> скриншота · CTA-строка со ссылкой на услугу**. `data-cat` = ключ фильтра.

---

### Card 1 — ATT / traduzione.tech
`data-cat="siti"` · **Categoria chip:** `Sito aziendale`

- **Titolo:** `Il sito dell'agenzia di traduzioni, costruito da traduttori`
- **URL проекта:** https://www.traduzione.tech · **label:** `traduzione.tech`
- **Problema:** Un'agenzia di traduzioni con più di vent'anni di storia aveva bisogno di un sito
  che parlasse la lingua del cliente italiano B2B: preventivi rapidi, servizi chiari, fiducia
  immediata. Il vecchio sito non reggeva né i tempi di caricamento né la struttura dei servizi.
- **Soluzione:** Abbiamo riprogettato il sito di ATT (Agenzia di Traduzioni Tecniche) come un sito
  aziendale completo: architettura dei servizi per settore e per lingua, richiesta di preventivo
  in pochi passaggi, contenuti scritti da chi le traduzioni le fa davvero. SEO tecnica e dati
  strutturati dalla prima riga. È il nostro biglietto da visita: se non funzionasse, lo sapremmo per primi.
- **Stack e tempi:** `[ПРОВЕРИТЬ: es. WordPress + tema custom · SEO tecnica · IT/EN] · online dal 2022 · [ПРОВЕРИТЬ: N settimane]`
- **Risultato (с цифрами — основной):** Online dal 2022, il sito porta all'agenzia **circa 20
  ordini al mese**, su **oltre 40 combinazioni e direzioni linguistiche**. È il canale con cui
  ATT acquisisce clienti oggi.
- **Risultato (без цифр — fallback):** Il sito con cui l'agenzia acquisisce clienti oggi:
  servizi leggibili in secondi, preventivo a portata di clic, aperto e verificabile online.
- **Alt скриншота:** `Home page del sito dell'agenzia di traduzioni traduzione.tech, con i servizi in evidenza`
- **CTA:** `Un sito aziendale come questo → /servizi/siti-aziendali/`

---

### Card 2 — TMS / tms.perevod4.ru  ⭐ FLAGSHIP
`data-cat="webapp"` · **Categoria chip:** `Web app`

- **Titolo:** `La web app che manda avanti un'agenzia di traduzioni`
- **URL проекта:** https://tms.perevod4.ru · **label:** `tms.perevod4.ru`
- **Problema:** Gestire centinaia di ordini di traduzione — clienti, traduttori, scadenze,
  preventivi, fatture — con fogli di calcolo e email è un collo di bottiglia che rompe le
  consegne. Ci serviva un solo sistema, non dieci strumenti scollegati.
- **Soluzione:** Abbiamo costruito un TMS completo (Translation Management System): un pannello
  dove ogni ordine ha uno stato, ogni cliente una scheda, ogni traduttore un carico e ogni lavoro
  la sua fattura. Bacheca degli ordini, anagrafiche, preventivi e contabilità in un'unica web app.
  È il sistema operativo interno del gruppo: lo usiamo tutti i giorni per non perdere una consegna.
  **Questo è il nostro progetto di punta:** la stessa ingegneria che mettiamo nelle web app su misura per voi.
- **Stack e tempi:** `[ПРОВЕРИТЬ: es. web app custom (PHP/JS) · area riservata · ruoli utente] · in produzione da 2 anni, sviluppo continuo`
- **Risultato (с цифрами — основной):** In produzione da 2 anni: il sistema gestisce **180 ordini
  al mese, oltre 2.000 l'anno**. Dentro ci lavorano **2 amministratori, 8 project manager e
  4 agenzie partner** con la propria base — e gli ordini non si perdono più tra le email.
- **Risultato (без цифр — fallback):** Un solo posto per ordini, clienti, traduttori e fatture: niente più
  lavoro perso tra fogli di calcolo ed email. Il sistema con cui operiamo ogni giorno.
- **Alt скриншота:** `Pannello del TMS tms.perevod4.ru con la bacheca degli ordini di traduzione`
- **CTA:** `Una web app su misura per la vostra azienda → /servizi/web-app/`

**Подписи к скриншотам интерфейса TMS (итальянские, 5–6 — снять с реальных экранов):**
> ⚠️ Состав экранов не проверен (сайт закрыт). Подписи даны по логичной структуре TMS —
> сверить с реальным интерфейсом и переименовать под фактические разделы.
1. `Bacheca degli ordini: ogni traduzione con stato, scadenza e responsabile a colpo d'occhio.`
2. `Scheda cliente: anagrafica, storico ordini e listino concordato in un'unica vista.`
3. `Gestione traduttori: chi è libero, chi è sotto carico, con quali lingue e specializzazioni.`
4. `Preventivi: dal conteggio parole al prezzo al cliente in pochi passaggi.`
5. `Fatture e contabilità: dallo stato "consegnato" alla fattura senza reinserire i dati.`
6. `Glossari e memorie di traduzione: la terminologia del cliente resta e si riusa.`

---

### Card 3 — Telegram Mini App / @massimoalefBot
`data-cat="webapp"` · **Categoria chip:** `Mini App / PWA`

- **Titolo:** `La Mini App Telegram che quasi nessuno, in Italia, sa ancora fare`
- **URL проекта:** https://t.me/massimoalefBot · **label:** `@massimoalefBot`
- **Problema:** Traduttori e clienti vivono dentro le chat, non nelle scrivanie. Aprire un
  gestionale via browser per controllare un ordine è troppo. Serviva l'accesso al TMS **dentro
  Telegram**, senza installare niente.
- **Soluzione:** Abbiamo portato le funzioni chiave del TMS in una **Telegram Mini App**: ordini,
  stati e notifiche direttamente in chat, con la stessa logica del pannello web. In Italia le Mini
  App Telegram sono ancora rarissime tra le PMI: è esattamente il tipo di prodotto che sappiamo
  costruire quando l'interfaccia deve stare dove sono già le persone.
- **Stack e tempi:** `[ПРОВЕРИТЬ: Telegram Mini App (Web App API) · integrazione TMS] · sviluppata in 2 settimane`
- **Risultato (с цифрами — основной):** Sviluppata in **2 settimane**, oggi la Mini App gestisce
  **oltre 10 utenti e ordini al giorno**: il gestionale entra in tasca, senza app da installare.
- **Risultato (без цифр — fallback):** Il gestionale in tasca, dentro Telegram: niente app da installare,
  niente login da browser. Ordini e notifiche dove il team già lavora.
- **Alt скриншота:** `Mini App Telegram del TMS aperta dentro la chat, con la lista degli ordini`
- **CTA:** `Una Mini App o PWA per il vostro pubblico → /servizi/web-app/`  *(alt. /servizi/siti-pwa/)*

---

### Card 4 — ai.perevod4.ru
`data-cat="seo"` · **Categoria chip:** `SEO tecnica · Multilingue`

- **Titolo:** `Un progetto AI multilingue, italiano incluso`
- **URL проекта:** https://ai.perevod4.ru · **label:** `ai.perevod4.ru`
- **Problema:** Un progetto basato sull'intelligenza artificiale ha senso solo se lo trova la
  persona giusta, nella sua lingua. Costruire un sito AII multilingue che regga la SEO tecnica in
  ogni versione — italiano compreso — è un lavoro di ingegneria, non di plugin di traduzione.
- **Soluzione:** Abbiamo realizzato ai.perevod4.ru come progetto multilingue con **versione
  italiana nativa**: struttura tecnica pulita, dati strutturati e contenuti pensati per la ricerca
  in ogni lingua, non tradotti a macchina. La versione italiana esiste perché sappiamo servire il
  mercato italiano dalla base tecnica alla lingua.
- **Stack e tempi:** `[ПРОВЕРИТЬ: piattaforma AI · SEO tecnica multilingue · IT + altre lingue] · [ПРОВЕРИТЬ: N settimane]`
- **Risultato (с цифрами — основной):** **Oltre 60 lingue** di lavoro e **più di 10.000 richieste
  elaborate al mese**: un progetto AI che si fa trovare — e si usa — in più mercati.
- **Risultato (без цифр — fallback):** Un progetto AI che si fa trovare in più lingue, con la versione
  italiana costruita come nativa e non come traduzione automatica.
- **Alt скриншота:** `Versione italiana del progetto AI multilingue ai.perevod4.ru`
- **CTA:** `SEO tecnica e siti multilingue → /servizi/seo-tecnica/`  *(перелинк: /servizi/siti-multilingue/)*

---

### Card 5 — perevod4.ru
`data-cat="seo"` · **Categoria chip:** `SEO · Contenuti`

- **Titolo:** `Il catalogo che indicizza un intero settore`
- **URL проекта:** https://perevod4.ru · **label:** `perevod4.ru`
- **Problema:** Un portale-catalogo che copre un intero settore — agenzie, città, specializzazioni —
  vive o muore sulla SEO tecnica: se la struttura non regge, Google non indicizza e il contenuto non esiste.
- **Soluzione:** Abbiamo costruito perevod4.ru come portale editoriale/SEO a catalogo: agenzie di
  traduzione schedate per città e specializzazione, con struttura coerente, dati strutturati e
  velocità tenuta sotto controllo su tutto il volume. È la prova che sappiamo far reggere la SEO
  tecnica quando le pagine si contano a centinaia, non a decine.
- **Stack e tempi:** `[ПРОВЕРИТЬ: CMS/portale · architettura SEO su larga scala · contenuti a catalogo] · progetto pluriennale`
- **Risultato (с цифрами — основной):** **Oltre 200 agenzie di traduzione** schedate a catalogo:
  un intero settore reso navigabile e indicizzabile, con la SEO tecnica messa alla prova sulla
  scala, non sulla demo.
- **Risultato (без цифр — fallback):** Un intero settore a catalogo, reso navigabile e
  indicizzabile: la SEO tecnica messa alla prova sulla scala, non sulla demo.
- **Alt скриншота:** `Portale-catalogo perevod4.ru con l'elenco delle agenzie di traduzione per città`
- **CTA:** `SEO tecnica per progetti di contenuto → /servizi/seo-tecnica/`

---

### Card 6 — Gioco «L'Impero delle Traduzioni» / traduzione.tech/gioco
`data-cat="restyling"` · **Categoria chip:** `Marketing · Gamification`

- **Titolo:** `Un gioco per raccontare le traduzioni (in italiano)`
- **URL проекта:** https://traduzione.tech/gioco/ · **label:** `traduzione.tech/gioco`
- **Problema:** Un servizio B2B «serio» come la traduzione fatica a farsi ricordare. Volevamo un
  modo per far restare le persone sul sito e raccontare il nostro mondo senza una brochure noiosa.
- **Soluzione:** Abbiamo creato «L'Impero delle Traduzioni», un gioco browser in italiano dentro
  il sito dell'agenzia: gamification al servizio del marketing, contenuto che intrattiene e allo
  stesso tempo racconta cosa facciamo. È il lato creativo dello stesso team che vi fa il restyling:
  quando serve far restare l'utente, sappiamo anche divertirlo.
- **Stack e tempi:** `[ПРОВЕРИТЬ: gioco browser (JS/HTML5) · integrato nel sito] · [ПРОВЕРИТЬ: N settimane]`
- **Risultato (с цифрой):** 984 partite giocate e oltre 200 ore passate sul sito dell'agenzia
  (12 086 minuti) — un contenuto che trattiene davvero e fa parlare del marchio. *(цифры владельца, 15.07)*
- **Risultato (без цифр — публикуемый):** Un contenuto che trattiene le persone sul sito e dà al marchio qualcosa
  da raccontare: la gamification usata come strumento di marketing, non come gadget.
- **Alt скриншота:** `Schermata del gioco browser "L'Impero delle Traduzioni" in italiano su traduzione.tech`
- **CTA:** `Restyling e idee di marketing per il vostro sito → /servizi/restyling-migrazione/`

---

### Card 7 — пере.рф (punycode xn--e1afkbat.xn--p1ai)
`data-cat="seo"` · **Categoria chip:** `SEO tecnica`

- **Titolo:** `Due lettere di dominio, una lezione di SEO tecnica`
- **URL проекта:** https://пере.рф · **label:** `пере.рф`
- **Problema:** Un dominio brevissimo su alfabeto non latino (IDN/punycode) è un caso limite:
  posizionarlo bene richiede una SEO tecnica impeccabile, perché non si può contare sul nome.
- **Soluzione:** Abbiamo portato пере.рф ai primi posti con lavoro puramente tecnico: struttura,
  velocità, dati strutturati, gestione corretta del dominio internazionalizzato. È uno dei nostri
  casi SEO più forti proprio perché il risultato non arriva dal branding, ma dall'ingegneria.
- **Stack e tempi:** `[ПРОВЕРИТЬ: SEO tecnica · dominio IDN/punycode · ottimizzazione velocità] · progetto SEO continuativo`
- **Risultato (с цифрами — основной):** **Posizione n. 1 su Yandex** — il principale motore di
  ricerca russo — per le query di settore «traduzione notarile» e «traduzione di manuali»
  (link alle SERP disponibili), **9.000–10.000 visitatori al mese**, in vetta **da oltre 1.000
  giorni**. Primi posti ottenuti con la tecnica, non con il nome.
- **Risultato (без цифр — fallback):** Primi posti raggiunti con la sola SEO tecnica su un dominio-caso-limite:
  la prova che il risultato lo fa l'ingegneria, non la fortuna del nome.
- **Alt скриншота:** `Sito пере.рф, caso di SEO tecnica su dominio internazionalizzato`
- **CTA:** `SEO tecnica che porta risultati → /servizi/seo-tecnica/`

---

### Card 8 — ukrinitsy.ru
`data-cat="siti"` · **Categoria chip:** `Sito vetrina`

- **Titolo:** `Un sito vetrina per una piccola attività di ospitalità`
- **URL проекта:** https://ukrinitsy.ru · **label:** `ukrinitsy.ru`
- **Problema:** Una casa vacanze/guest house vive di prenotazioni dirette e di fiducia: al piccolo
  operatore turistico serve un sito semplice, veloce e credibile, non un gestionale.
- **Soluzione:** Abbiamo realizzato ukrinitsy.ru come sito vetrina essenziale: foto che vendono la
  struttura, contatti e richiesta di prenotazione a portata di mano, caricamento rapido anche da
  mobile. Lo stesso approccio «piccolo, ma fatto bene» che portiamo a ristoranti, studi e attività locali.
- **Stack e tempi:** `[ПРОВЕРИТЬ: sito vetrina · mobile-first · modulo contatti/prenotazione] · [ПРОВЕРИТЬ: N settimane]`
- **Risultato (с цифрами — основной):** Dopo il lancio le prenotazioni sono cresciute del
  **450%**: **18 prenotazioni in una stagione** arrivate dal sito — per una piccola struttura,
  la differenza tra stagione piena e stanze vuote.
- **Risultato (без цифр — fallback):** Una piccola attività che online si presenta con la cura di una grande:
  foto, contatti e prenotazione a portata di mano, veloce da mobile.
- **Alt скриншота:** `Sito vetrina della guest house ukrinitsy.ru, versione mobile`
- **CTA:** `Un sito vetrina per la vostra attività → /servizi/siti-aziendali/`  *(вилка: раздел «vetrina» покрывается страницей siti-aziendali/прайсом)*

---

### Card 9 — moscowtrans.ru + techperevod.com (пара, один кейс)
`data-cat="restyling"` · **Categoria chip:** `Design · Restyling`

- **Titolo:** `Due siti d'agenzia "belli e veloci" per un mercato esigente`
- **URL проектов:** https://moscowtrans.ru · https://techperevod.com · **label:** `moscowtrans.ru · techperevod.com`
- **Problema:** Sul mercato competitivo delle agenzie di traduzione un sito deve essere insieme
  bello e velocissimo: l'estetica costruisce fiducia, la velocità la mantiene. Riuscirci su due
  siti diversi, con la stessa qualità, è una prova di metodo.
- **Soluzione:** Abbiamo progettato moscowtrans.ru e techperevod.com come coppia di siti d'agenzia
  curati nel design e ottimizzati nella performance: gerarchia visiva chiara, immagini leggere,
  struttura dei servizi pensata per la conversione. È il nostro lato «design + restyling» applicato
  a un settore in cui i concorrenti si somigliano tutti.
- **Stack e tempi:** `[ПРОВЕРИТЬ: design custom · ottimizzazione performance · 2 siti] · design e funzionalità rinnovati nel 2026`
- **Risultato (с цифрами — основной):** Dopo il rinnovo di design e funzionalità del 2026, le
  conversioni sono cresciute di **oltre il 300%** negli ultimi mesi: due siti che si distinguono
  in un settore dove tutti si somigliano.
- **Risultato (без цифр — fallback):** Due siti d'agenzia che si distinguono in un settore dove tutti si
  somigliano: design curato e caricamento rapido, la stessa mano su entrambi.
- **Alt скриншота:** `Home page dei siti d'agenzia moscowtrans.ru e techperevod.com affiancate`
- **CTA:** `Restyling e nuovo design per il vostro sito → /servizi/restyling-migrazione/`

---

### Card 10 — Sistema di test dei traduttori / moscowtrans.ru/test-perevodchika  ⭐ (NEW, HR-tech + E-E-A-T)
`data-cat="webapp"` · **Categoria chip:** `Web app · HR-tech`

- **Titolo:** `La piattaforma che decide chi traduce i vostri testi`
- **URL проекта:** https://moscowtrans.ru/test-perevodchika/ · **label:** `moscowtrans.ru/test-perevodchika`
- **Problema:** La promessa «redattori madrelingua per specializzazione» che leggete sulle nostre
  pagine di servizio vale solo se dietro c'è un modo serio per selezionare chi traduce. Scegliere i
  traduttori a occhio non è un metodo.
- **Soluzione:** Abbiamo costruito una **piattaforma di valutazione e test dei traduttori** —
  un sistema di selezione progressivo usato in **tutti i progetti del gruppo**: prove a difficoltà
  crescente, valutazione strutturata, filtro automatico dei candidati. È il prodotto interno che
  **tiene la qualità delle nostre traduzioni**: è esattamente questo sistema a stare dietro alla
  garanzia «redattori madrelingua per profilo» dei siti multilingue che vi consegniamo.
- **Stack e tempi:** `[ПРОВЕРИТЬ: web app custom · test a più livelli · scoring automatico] · progetto interno, in uso su tutti i progetti`
- **Risultato (с цифрами — основной):** **Oltre 400 traduttori testati — e solo l'8% supera la
  selezione.** Ogni traduttore che lavora sui vostri testi è dentro quell'8%: la qualità decisa
  da un sistema, non a intuito. Dietro la promessa «redattori madrelingua per profilo» c'è una
  selezione che passa solo l'8% dei candidati.
- **Risultato (fallback, компактный):** La qualità della traduzione decisa da un sistema, non a
  intuito: la selezione la supera **solo l'8% dei candidati**, e chi lavora sui vostri testi è
  tra quelli. È la garanzia «madrelingua per profilo» resa verificabile.
- **Alt скриншота:** `Piattaforma di test e valutazione dei traduttori del gruppo Remarka`
- **CTA:** `Una web app su misura per il vostro processo → /servizi/web-app/`  *(перелинк E-E-A-T: /servizi/siti-multilingue/)*

---

### Card 11 — 1russian.com  (NEW — решение оркестратора 15.07)
`data-cat="seo"` · **Categoria chip:** `SEO · Contenuti`

- **Titolo:** `Un progetto internazionale, scritto in inglese per il mondo`
- **URL проекта:** https://1russian.com · **label:** `1russian.com`
- **Problema:** Un progetto pensato per un pubblico globale vive o muore sulla lingua e sulla
  ricerca: contenuti in inglese che un anglofono legge come propri, e una base tecnica che Google
  indicizza senza attriti. Non basta tradurre — bisogna scrivere per quel pubblico.
- **Soluzione:** Abbiamo costruito 1russian.com come progetto internazionale in lingua inglese:
  contenuti pensati per chi cerca in inglese, non tradotti dal russo, con struttura e SEO tecnica
  curate dalla base (WordPress con flusso di deploy controllato). È anche il banco di prova dei
  nostri strumenti interni di audit SEO `[ПРОВЕРИТЬ: статус SiteLens — упоминать ли]`: sul nostro
  progetto testiamo prima quello che poi applichiamo ai vostri.
- **Stack e tempi:** `WordPress (hosting REG.RU, deploy controllato da repository) · contenuti EN · SEO tecnica` · `[ПРОВЕРИТЬ: N settimane / progetto continuativo]`
- **Risultato (с цифрами — основной):** **Oltre 10.000 visitatori al mese da 80 Paesi**: un
  progetto che parla inglese a un pubblico realmente globale.
- **Risultato (без цифр — fallback):** Un progetto che parla al pubblico globale nella
  sua lingua: contenuti in inglese scritti come nativi e una base tecnica pensata per la ricerca.
- **Alt скриншота:** `Home page del progetto internazionale in inglese 1russian.com`
- **CTA:** `Contenuti nativi in più lingue per il vostro sito → /servizi/siti-multilingue/`
  *(перелинк: /servizi/seo-tecnica/ — выбрал multilingue: текст карточки держится на «писать
  на языке аудитории, а не переводить», это ось услуги multilingue; SEO-услуга уже получает
  3 CTA от карточек 4, 5, 7)*

---

## 2.4. Финальный CTA-блок страницы IT (dark, замена текущего)

- **H2:** `Il prossimo sistema possiamo costruirlo per voi<span class="sr-accent-dot">.</span>`
- **Sub:** `Prima misuriamo cosa avete oggi, poi vi diciamo — con numeri e con una data in contratto — cosa possiamo fare.`
- **CTA 1:** `Richiedi un preventivo in 24 ore → /#contatti`
- **CTA 2 (link):** `Guarda tutti i servizi → /servizi/`

---

# 3. EN — `/en/case-studies/` (зеркало IT, native English)

## 3.1. Intro

- **Eyebrow:** `Case studies`
- **H1:** `Not a client portfolio. The systems we built for ourselves<span class="sr-accent-dot">.</span>`
- **Lead:**

  > Most web agencies show off client logos. The Remarka group has worked with languages since
  > 2001 — and has been **building websites since that same year**: as early as 2002–2003 it was
  > delivering sites for outside companies, some still online today (directindustry.com.ru ·
  > ivextrans.eu · beltran.by `[VERIFY: 2002–2003 sites still live]`). Since then: **over 160
  > projects** delivered, **28** currently under our continuous maintenance. Studio Remarka is
  > this work's new storefront, not its beginning.

  > Below are the systems the group built **for itself**: to run our own operations, rank our own
  > services on Google, sell in several languages. We use them every day, with our own money and
  > reputation on the line — and when you work with us you get **the same engineering**. Every
  > case links to the **live project**: open it, test it, measure it yourself. No invented
  > clients, no numbers you can't check.

- **Intro caption (mono):** `Every card opens the live project. Scores and metrics are verifiable on the spot.`

## 3.2. Filter labels (EN)

| Key | Label EN |
|---|---|
| `all` | `All projects` |
| `siti` | `Business & brochure sites` |
| `webapp` | `Web apps & products` |
| `seo` | `Technical SEO & content` |
| `restyling` | `Redesign & marketing` |

Micro-caption: `11 group projects · filter by type of work`

## 3.3. Cards (EN) — 11

---

### Card 1 — ATT / traduzione.tech · `siti` · chip `Business website`
- **Title:** `A translation agency's website, built by translators`
- **Link:** https://www.traduzione.tech · `traduzione.tech`
- **Problem:** A translation agency with over twenty years of history needed a site that spoke the
  language of the Italian B2B buyer: fast quotes, clear services, instant trust. The old site held
  up on neither load time nor service structure.
- **Solution:** We rebuilt the ATT (Technical Translation Agency) site as a complete business
  website: services architected by field and by language, a quote request in a few steps, copy
  written by the people who actually do the translating. Technical SEO and structured data from
  line one. It's our own calling card — if it didn't work, we'd be the first to know.
- **Stack & timeline:** `[VERIFY: e.g. WordPress + custom theme · technical SEO · IT/EN] · live since 2022 · [VERIFY: N weeks]`
- **Result (with numbers — primary):** Live since 2022, the site brings the agency **around 20
  orders a month** across **more than 40 language pairs and directions**. It's the channel ATT
  wins clients with today.
- **Result (no numbers — fallback):** The site the agency wins clients with today: services readable in seconds,
  a quote a click away, live and verifiable online.
- **Alt:** `Home page of the translation agency site traduzione.tech, services in focus`
- **CTA:** `A business website like this one → /en/services/business-websites/`

---

### Card 2 — TMS / tms.perevod4.ru ⭐ FLAGSHIP · `webapp` · chip `Web app`
- **Title:** `The web app that runs a translation agency`
- **Link:** https://tms.perevod4.ru · `tms.perevod4.ru`
- **Problem:** Running hundreds of translation orders — clients, translators, deadlines, quotes,
  invoices — on spreadsheets and email is a bottleneck that breaks deliveries. We needed one system,
  not ten disconnected tools.
- **Solution:** We built a full TMS (Translation Management System): a dashboard where every order
  has a status, every client a record, every translator a workload, and every job its invoice. Order
  board, contacts, quotes and accounting in a single web app. It's the group's internal operating
  system — we use it every day so no delivery slips through. **This is our flagship:** the same
  engineering we put into custom web apps for you.
- **Stack & timeline:** `[VERIFY: e.g. custom web app (PHP/JS) · secure area · user roles] · in production for 2 years, continuous development`
- **Result (with numbers — primary):** In production for 2 years: the system handles **180 orders a
  month, over 2,000 a year**. Inside it work **2 administrators, 8 project managers and 4 partner
  agencies** with their own client base — and orders no longer get lost in email.
- **Result (no numbers — fallback):** One place for orders, clients, translators and invoices: no more work lost
  between spreadsheets and inboxes. The system we run on every day.
- **Alt:** `Dashboard of the TMS at tms.perevod4.ru showing the translation order board`
- **CTA:** `A custom web app for your company → /en/services/custom-web-apps/`

**TMS screenshot captions (EN, 5–6 — capture from real screens; ⚠️ unverified, adjust to real sections):**
1. `Order board: every translation with status, deadline and owner at a glance.`
2. `Client record: profile, order history and agreed rates in one view.`
3. `Translator management: who's free, who's loaded, with which languages and specialisms.`
4. `Quotes: from word count to client price in a few steps.`
5. `Invoicing & accounting: from "delivered" to invoice without re-entering data.`
6. `Glossaries & translation memory: the client's terminology stays and gets reused.`

---

### Card 3 — Telegram Mini App / @massimoalefBot · `webapp` · chip `Mini App / PWA`
- **Title:** `The Telegram Mini App almost nobody in Italy builds yet`
- **Link:** https://t.me/massimoalefBot · `@massimoalefBot`
- **Problem:** Translators and clients live inside chats, not at desks. Opening a browser dashboard
  just to check an order is too much. We needed access to the TMS **inside Telegram**, with nothing to install.
- **Solution:** We brought the TMS's key functions into a **Telegram Mini App**: orders, statuses and
  notifications right in the chat, with the same logic as the web dashboard. Telegram Mini Apps are
  still rare among Italian SMBs — exactly the kind of product we know how to build when the interface
  has to live where people already are.
- **Stack & timeline:** `[VERIFY: Telegram Mini App (Web App API) · TMS integration] · built in 2 weeks`
- **Result (with numbers — primary):** Built in **2 weeks**, the Mini App now handles **over 10
  users and orders a day**: the back office in your pocket, nothing to install.
- **Result (no numbers — fallback):** The back office in your pocket, inside Telegram: no app to install, no
  browser login. Orders and alerts where the team already works.
- **Alt:** `Telegram Mini App of the TMS open inside the chat, showing the order list`
- **CTA:** `A Mini App or PWA for your audience → /en/services/custom-web-apps/` *(alt /en/services/progressive-web-apps/)*

---

### Card 4 — ai.perevod4.ru · `seo` · chip `Technical SEO · Multilingual`
- **Title:** `A multilingual AI project, Italian included`
- **Link:** https://ai.perevod4.ru · `ai.perevod4.ru`
- **Problem:** An AI-powered project only matters if the right person finds it, in their own
  language. Building a multilingual AI site whose technical SEO holds up in every version — Italian
  included — is engineering, not a translation plugin.
- **Solution:** We built ai.perevod4.ru as a multilingual project with a **native Italian version**:
  a clean technical structure, structured data, and content written for search in each language
  rather than machine-translated. The Italian version exists because we can serve the Italian market
  from the technical base up to the language.
- **Stack & timeline:** `[VERIFY: AI platform · multilingual technical SEO · IT + other languages] · [VERIFY: N weeks]`
- **Result (with numbers — primary):** **Over 60 working languages** and **more than 10,000
  requests processed a month**: an AI project that gets found — and used — across markets.
- **Result (no numbers — fallback):** An AI project that gets found in several languages, with the Italian version
  built as native rather than auto-translated.
- **Alt:** `Italian version of the multilingual AI project ai.perevod4.ru`
- **CTA:** `Technical SEO and multilingual sites → /en/services/technical-seo/` *(cross-link /en/services/multilingual-websites/)*

---

### Card 5 — perevod4.ru · `seo` · chip `SEO · Content`
- **Title:** `The catalogue that indexes an entire industry`
- **Link:** https://perevod4.ru · `perevod4.ru`
- **Problem:** A catalogue portal covering an entire industry — agencies, cities, specialisms —
  lives or dies on technical SEO: if the structure doesn't hold, Google won't index it and the
  content doesn't exist.
- **Solution:** We built perevod4.ru as an editorial/SEO catalogue portal: translation agencies
  listed by city and specialism, with a consistent structure, structured data and speed kept under
  control across the whole volume. It's proof we can make technical SEO hold when the pages number
  in the hundreds, not the dozens.
- **Stack & timeline:** `[VERIFY: CMS/portal · large-scale SEO architecture · catalogue content] · multi-year project`
- **Result (with numbers — primary):** **Over 200 translation agencies** listed in the catalogue:
  an entire industry made navigable and indexable, with technical SEO tested at scale, not on a demo.
- **Result (no numbers — fallback):** An entire industry in one catalogue, made navigable and
  indexable: technical SEO tested at scale, not on a demo.
- **Alt:** `perevod4.ru catalogue portal listing translation agencies by city`
- **CTA:** `Technical SEO for content projects → /en/services/technical-seo/`

---

### Card 6 — Game «Translation Empire» / traduzione.tech/gioco · `restyling` · chip `Marketing · Gamification`
- **Title:** `A game to talk about translation (in Italian)`
- **Link:** https://traduzione.tech/gioco/ · `traduzione.tech/gioco`
- **Problem:** A "serious" B2B service like translation struggles to be memorable. We wanted a way to
  keep people on the site and tell our story without a boring brochure.
- **Solution:** We created "Translation Empire", a browser game in Italian inside the agency site:
  gamification in the service of marketing — content that entertains while it explains what we do.
  It's the creative side of the same team that handles your redesign: when the job is to keep the
  user around, we know how to entertain them too.
- **Stack & timeline:** `[VERIFY: browser game (JS/HTML5) · embedded in site] · [VERIFY: N weeks]`
- **Result (with number):** 984 games played and over 200 hours spent on the agency site
  (12,086 minutes) — content that genuinely holds attention and gets the brand talked about. *(owner numbers, 15.07)*
- **Result (no number — publishable):** Content that keeps people on the site and gives the brand something to talk
  about: gamification used as a marketing tool, not a gadget.
- **Alt:** `Screen of the browser game "Translation Empire" in Italian on traduzione.tech`
- **CTA:** `Redesign and marketing ideas for your site → /en/services/redesign-migration/`

---

### Card 7 — пере.рф · `seo` · chip `Technical SEO`
- **Title:** `A two-letter domain, a masterclass in technical SEO`
- **Link:** https://пере.рф · `пере.рф`
- **Problem:** A very short domain on a non-Latin alphabet (IDN/punycode) is an edge case: ranking it
  well takes flawless technical SEO, because you can't lean on the name.
- **Solution:** We took пере.рф to the top positions with purely technical work: structure, speed,
  structured data, correct handling of the internationalised domain. It's one of our strongest SEO
  cases precisely because the result comes from engineering, not branding.
- **Stack & timeline:** `[VERIFY: technical SEO · IDN/punycode domain · speed optimisation] · ongoing SEO project`
- **Result (with numbers — primary):** **Position no. 1 on Yandex** — Russia's leading search
  engine — for the industry queries "notarised translation" and "manual translation" (SERP links
  available), **9,000–10,000 visitors a month**, at the top **for over 1,000 days**. Top positions
  won with technique, not with the name.
- **Result (no numbers — fallback):** Top positions reached with technical SEO alone on an edge-case domain: proof
  that the result is made by engineering, not by a lucky name.
- **Alt:** `The пере.рф site, a technical SEO case on an internationalised domain`
- **CTA:** `Technical SEO that delivers → /en/services/technical-seo/`

---

### Card 8 — ukrinitsy.ru · `siti` · chip `Brochure site`
- **Title:** `A brochure site for a small hospitality business`
- **Link:** https://ukrinitsy.ru · `ukrinitsy.ru`
- **Problem:** A guest house lives on direct bookings and trust: a small tourism operator needs a
  simple, fast, credible site — not a back-office system.
- **Solution:** We built ukrinitsy.ru as an essential brochure site: photos that sell the place,
  contact and booking request within reach, fast loading even on mobile. The same "small but done
  right" approach we bring to restaurants, studios and local businesses.
- **Stack & timeline:** `[VERIFY: brochure site · mobile-first · contact/booking form] · [VERIFY: N weeks]`
- **Result (with numbers — primary):** Bookings grew **450%** after launch: **18 bookings in a
  season** straight from the site — for a small guest house, the difference between a full season
  and empty rooms.
- **Result (no numbers — fallback):** A small business that shows up online with the care of a big one: photos,
  contacts and booking within reach, fast on mobile.
- **Alt:** `Brochure site of the ukrinitsy.ru guest house, mobile version`
- **CTA:** `A brochure site for your business → /en/services/business-websites/`

---

### Card 9 — moscowtrans.ru + techperevod.com (pair) · `restyling` · chip `Design · Redesign`
- **Title:** `Two "beautiful and fast" agency sites for a demanding market`
- **Link:** https://moscowtrans.ru · https://techperevod.com · `moscowtrans.ru · techperevod.com`
- **Problem:** In the competitive translation-agency market a site has to be both beautiful and very
  fast: looks build trust, speed keeps it. Pulling that off on two different sites, at the same
  quality, is a test of method.
- **Solution:** We designed moscowtrans.ru and techperevod.com as a pair of agency sites — careful in
  design, optimised in performance: clear visual hierarchy, light images, a service structure built
  for conversion. It's our "design + redesign" side applied to an industry where competitors all look alike.
- **Stack & timeline:** `[VERIFY: custom design · performance optimisation · 2 sites] · design and functionality renewed in 2026`
- **Result (with numbers — primary):** After the 2026 redesign of both look and functionality,
  conversions grew by **over 300%** in recent months: two sites that stand out in a sector where
  everyone looks alike.
- **Result (no numbers — fallback):** Two agency sites that stand out where everyone looks the same: careful design
  and fast loading, the same hand on both.
- **Alt:** `Home pages of the agency sites moscowtrans.ru and techperevod.com side by side`
- **CTA:** `Redesign and new design for your site → /en/services/redesign-migration/`

---

### Card 10 — Translator testing platform / moscowtrans.ru/test-perevodchika ⭐ (HR-tech + E-E-A-T) · `webapp` · chip `Web app · HR-tech`
- **Title:** `The platform that decides who translates your copy`
- **Link:** https://moscowtrans.ru/test-perevodchika/ · `moscowtrans.ru/test-perevodchika`
- **Problem:** The "native editors by specialism" promise you read on our service pages only holds if
  there's a serious way to select who translates. Picking translators by gut feeling is not a method.
- **Solution:** We built a **translator testing and evaluation platform** — a progressive selection
  system used across **every project in the group**: tests of increasing difficulty, structured
  scoring, automatic candidate filtering. It's the internal product that **holds our translation
  quality**: this is exactly the system behind the "native editors by profile" guarantee on the
  multilingual sites we deliver.
- **Stack & timeline:** `[VERIFY: custom web app · multi-level testing · automatic scoring] · internal project, used across all projects`
- **Result (with numbers — primary):** **Over 400 translators tested — and only 8% pass the
  selection.** Every translator who works on your copy is inside that 8%: quality decided by a
  system, not a hunch. Behind the "native editors by profile" promise stands a selection only 8%
  of candidates get through.
- **Result (fallback, compact):** Translation quality decided by a system, not a hunch: **only 8%
  of candidates pass the selection**, and everyone who works on your copy is among them. It's the
  "native by profile" guarantee made verifiable.
- **Alt:** `Remarka group's translator testing and evaluation platform`
- **CTA:** `A custom web app for your process → /en/services/custom-web-apps/` *(E-E-A-T cross-link /en/services/multilingual-websites/)*

---

### Card 11 — 1russian.com (NEW — orchestrator decision 15.07) · `seo` · chip `SEO · Content`
- **Title:** `An international project, written in English for the world`
- **Link:** https://1russian.com · `1russian.com`
- **Problem:** A project aimed at a global audience lives or dies on language and search: English
  copy a native speaker reads as their own, and a technical base Google indexes without friction.
  Translating isn't enough — you have to write for that audience.
- **Solution:** We built 1russian.com as an international, English-language project: content
  written for people who search in English, not translated from Russian, with structure and
  technical SEO handled from the ground up (WordPress with a controlled deploy pipeline). It's
  also the proving ground for our in-house SEO audit tooling `[VERIFY: SiteLens status — whether to mention]`:
  we test on our own project first what we then apply to yours.
- **Stack & timeline:** `WordPress (REG.RU hosting, repository-controlled deploys) · EN content · technical SEO` · `[VERIFY: N weeks / ongoing project]`
- **Result (with numbers — primary):** **Over 10,000 visitors a month from 80 countries**: a
  project that speaks English to a genuinely global audience.
- **Result (no numbers — fallback):** A project that speaks to a global audience in its own language: English
  content written as native and a technical base built for search.
- **Alt:** `Home page of the international English-language project 1russian.com`
- **CTA:** `Native content in several languages for your site → /en/services/multilingual-websites/`
  *(cross-link: /en/services/technical-seo/ — multilingue chosen: the card's axis is "write in the
  audience's language, don't translate", which is the multilingual service's promise; the SEO
  service already receives 3 CTAs from cards 4, 5, 7)*

---

## 3.4. EN final CTA block (dark)
- **H2:** `The next system, we can build for you<span class="sr-accent-dot">.</span>`
- **Sub:** `First we measure what you have today, then we tell you — with numbers and a date in the contract — what we can do.`
- **CTA 1:** `Get a quote in 24 hours → /en/#contatti`
- **CTA 2:** `See all services → /en/services/`

---

# 4. RU — `/ru/kejsy/` (страница-история, не каталог)

> Совсем другая подача: нарратив «мы сами прошли путь на европейский рынок». Пары
> «русский проект ↔ европейский проект». Самодостаточный текст — доказательная база
> лендинга `/ru/uslugi/sajt-dlya-evropy/`. Форма «вы» со строчной, деньги `€ N NNN`,
> без превосходных степеней. Формат — секции нарратива, а не сетка карточек.

## Блок 0 — Hero

- **Eyebrow:** `Кейсы · Путь, который мы прошли сами`
- **H1:** `Мы не показываем чужие логотипы. Мы показываем путь, который прошли сами<span class="sr-accent-dot">.</span>`
- **Подзаголовок:** Прежде чем выводить ваш бизнес на рынок Италии и Европы, мы вывели туда
  собственные проекты. Группа Remarka работает с языками с 2001 года — и с того же года строит
  сайты: за это время создано больше 160 проектов, 28 из них сейчас у нас на постоянном
  обслуживании. Studio Remarka — новая витрина этой работы, а не её начало. За каждой строкой
  ниже — живая ссылка.
- **Микрокопия (mono):** `Русский рынок мы знаем. В Европу — уже вышли. Ниже — чем именно.`

## Блок 1 — «Мы знаем русский рынок» (пере.рф · perevod4.ru · moscowtrans/techperevod)

- **Eyebrow:** `Откуда мы вышли`
- **H2:** `Сначала мы стали заметными на русском рынке<span class="sr-accent-dot">.</span>`
- **Текст:**

  > Группа Remarka выросла из бюро переводов, работающего с 2001 года, — и сайты мы строим с
  > того же года: уже в 2002–2003 сделали ряд сайтов сторонним компаниям, и некоторые живы до
  > сих пор — directindustry.com.ru, ivextrans.eu, beltran.by `[ПРОВЕРИТЬ: сайты 2002–2003 живы]`.
  > Тренировались мы на самом требовательном для себя рынке — русскоязычном, где конкуренция за
  > поиск жёсткая, а клиент не прощает медленных сайтов.

  > Мы построили **perevod4.ru** — каталог, в котором собрано больше 200 российских бюро
  > переводов: проверка SEO не на демо, а на целой отрасли. Мы вывели в топ **пере.рф** — домен
  > из двух букв на кириллице, где нельзя опереться на имя, только на чистую техническую SEO:
  > первое место в Яндексе по запросам «нотариальный перевод» и «перевод инструкций»,
  > 9 000–10 000 посетителей в месяц, и в топе он держится уже больше 1 000 дней. А
  > **moscowtrans.ru** и **techperevod.com** — два «красивых и быстрых» сайта бюро — после
  > обновления дизайна и функционала в 2026-м прибавили больше 300% в конверсиях.

- **Живые ссылки (строкой, mono):** `perevod4.ru · пере.рф · moscowtrans.ru · techperevod.com`
- **Вывод (fallback без цифр — если решат публиковать без чисел):** Эти проекты научили нас
  держать скорость, структуру и поиск там, где конкуренция максимальная. Тот же метод мы теперь
  применяем к вашему сайту.

## Блок 2 — «Мы вывели эти проекты в Европу» (traduzione.tech · 1russian.com · ai.perevod4.ru)

- **Eyebrow:** `Куда мы пришли`
- **H2:** `А потом вывели свои проекты на рынок Италии и Европы<span class="sr-accent-dot">.</span>`
- **Текст:**

  > Знать русский рынок мало — на европейском действуют другие правила: другой дизайн,
  > другой язык доверия, другая юридическая база. Мы прошли это на себе.

  > **traduzione.tech** — сайт итальянского бюро переводов ATT: сделан для итальянского
  > B2B-клиента, на его языке, с его логикой выбора подрядчика. Он работает с 2022 года и
  > приносит бюро около 20 заказов в месяц — по более чем 40 языковым парам и направлениям.
  > **1russian.com** — наш международный проект на английском: больше 10 000 посетителей в
  > месяц из 80 стран мира. **ai.perevod4.ru** — многоязычный AI-проект с полноценной
  > **итальянской версией**, написанной как родная: больше 60 языков и свыше 10 000
  > обрабатываемых запросов в месяц.

  > Это и есть то, что мы предлагаем вам: не «перевод вашего сайта», а сайт, который в Италии и
  > ЕС читается как местный — от дизайна до последней юридической страницы.

- **Живые ссылки (mono):** `traduzione.tech · 1russian.com · ai.perevod4.ru`
- **Вывод (fallback без цифр):** Мы не изучали европейский рынок по учебнику — мы вывели туда
  собственные сайты. Ваш будет следующим.

## Блок 3 — «Мы умеем не только сайты, но и продукты» (TMS · Mini App · система тестов)

- **Eyebrow:** `Что у нас под капотом`
- **H2:** `Мы строим не только сайты — мы строим продукты<span class="sr-accent-dot">.</span>`
- **Текст:**

  > Сайт — это витрина. За витриной у серьёзного бизнеса стоят системы, и их мы тоже делаем сами.

  > **TMS** (`tms.perevod4.ru`) — система управления бюро переводов: заказы, клиенты, переводчики,
  > счета в одном веб-приложении. Это наш флагманский продукт и операционная система всей группы:
  > два года в эксплуатации, 180 заказов в месяц — больше 2 000 в год, внутри работают 2
  > администратора, 8 менеджеров и 4 партнёрских бюро со своей базой. Для той же системы мы
  > сделали **мини-приложение в Telegram** (`@massimoalefBot`) — доступ к заказам прямо в чате,
  > без установки; собрали его за 2 недели, и сегодня через него проходит больше 10 пользователей
  > и заказов в день. В Италии такие Telegram Mini App почти никто ещё не делает. И третий продукт
  > линейки — **прогрессивная система тестирования переводчиков**
  > (`moscowtrans.ru/test-perevodchika`): больше 400 переводчиков протестировано, а тест
  > проходят лишь 8 из 100 — так отбираются исполнители для всех проектов группы.

  > Если вашему бизнесу нужен не просто сайт, а рабочая система — личный кабинет, каталог,
  > расчётный модуль, — мы уже такие строили. Для себя.

- **Живые ссылки (mono):** `tms.perevod4.ru · @massimoalefBot · moscowtrans.ru/test-perevodchika`

## Блок 4 — «Почему это гарантия качества именно для вашего перевода»

- **Eyebrow:** `Про качество перевода`
- **H2:** `Качество ваших текстов держит не обещание, а система<span class="sr-accent-dot">.</span>`
- **Текст:**

  > Когда мы обещаем, что иностранную версию вашего сайта напишут редакторы-носители по профилю,
  > за этим стоит не честное слово, а отбор, который проходят лишь 8 из 100. Качество переводов
  > для ваших европейских сайтов держит **та же система, что отбирает переводчиков во всех наших
  > бюро**: прогрессивные тесты, структурная оценка, автоматический отсев — больше 400
  > переводчиков протестировано. Переводчик, который возьмётся за ваш текст, — из тех восьми,
  > как и все остальные в группе с 2001 года.

- **Публикуемый вывод без цифр:** Локализация носителями — это у нас не строчка в прайсе, а
  выстроенный процесс с собственным инструментом отбора.

## Блок 5 — «Игра и малый бизнес» (gioco · ukrinitsy) — по желанию, лёгкий блок

- **Eyebrow:** `И два штриха к портрету`
- **H2:** `Мы умеем и развлекать, и работать по-маленькому<span class="sr-accent-dot">.</span>`
- **Текст:**

  > Не каждый проект — это большая система. Для сайта ATT мы сделали браузерную игру
  > **«Империя переводов»** по-итальянски — геймификацию как инструмент маркетинга, чтобы
  > посетитель остался: 984 сыгранные партии и больше 200 часов, проведённых за игрой
  > на сайте бюро, говорят сами за себя. А для гостевого дома **ukrinitsy.ru** — простой быстрый сайт-визитку:
  > малому бизнесу в туризме нужны фото, контакты и бронь под рукой, а не тяжёлый портал.
  > После запуска бронирований стало на 450% больше — 18 за сезон, напрямую с сайта; для
  > маленького гостевого дома это разница между полным сезоном и пустыми комнатами.
  > Мы делаем и то, и другое с одинаковым вниманием.

- **Живые ссылки (mono):** `traduzione.tech/gioco · ukrinitsy.ru`

## Блок 6 — Мост к воронке (что это значит для вас)

- **Eyebrow:** `Что это значит для вас`
- **H2:** `Мы уже прошли путь, который предстоит вам<span class="sr-accent-dot">.</span>`
- **Текст:**

  > Вы выходите на рынок Италии или Европы — или уже работаете там и хотите расти. Мы прошли
  > этот путь на собственных проектах: от русскоязычного рынка до итальянского сайта, от простой
  > визитки до веб-приложения. Одна команда держит обе стороны — Милан, где ваши клиенты, и
  > русскоязычная команда, которая понимает вас с полуслова.

- **CTA-блок:**
  - **H2:** `Расскажите, куда выходите — посчитаем за 24 часа<span class="sr-accent-dot">.</span>`
  - **Sub:** Опишите бизнес и рынок назначения. Пришлём фиксированную смету и срок в течение суток.
  - **CTA 1:** `Обсудить проект → /ru/#contatti`
  - **CTA 2 (outline):** `Как мы выводим сайт в Европу → /ru/uslugi/sajt-dlya-evropy/`
  - **CTA 3 (текст-ссылка):** `Продвижение в Google Италии и ЕС → /ru/uslugi/seo-prodvizhenie/`

## RU-мета `/ru/kejsy/`
- **Focus Keyword:** `портфолио веб-студии`
- **Title (≤60):** `Кейсы: как мы сами вышли на рынок Европы | Studio Remarka`  *(57 зн.)*
- **Description (≤160):** `Мы сами прошли путь на рынок Италии и Европы: свои проекты от бюро переводов с 2001 года до веб-приложений. Портфолио с живыми ссылками, а не логотипами.`  *(156 зн.)*

---

# 5. E-E-A-T — что держим во всех языках

- **Experience/Authoritativeness:** каждый кейс — реальный проект группы Remarka, с **живой
  ссылкой**; ни одного выдуманного клиента, отзыва или числа. Прямо проговорено, что это
  «наши собственные системы» — сильнее, чем чужие логотипы.
- **Годы:** группа Remarka в языках и цифре **с 2001 года** — упоминать в интро каждого языка
  (IT `dal 2001`, EN `since 2001`, RU `с 2001 года`).
- **Trustworthiness:** «откройте, проверьте, измерьте сами»; цифры — только реальные (владелец)
  или честные диапазоны; SEO-результаты без гарантий позиций.
- **Без превосходных степеней:** не «лучший/№1», а «один из наших сильнейших SEO-кейсов»,
  «редкая на рынке компетенция» — фактические, проверяемые формулировки.
- **Связка кейс↔услуга↔инструмент:** каждый IT/EN-кейс ведёт на свою услугу; кейс TMS/tester
  дополнительно подпирает обещание качества перевода на страницах `siti-multilingue`.

---

# 6. ДЛЯ ИМПЛЕМЕНТАТОРА

> RU — **руками**. `translate_pages.py ru` запускать НЕЛЬЗЯ (см. `piano-implementazione-fase-A.md` §0.2).
> RU-страница кейсов — это НЕ перевод IT-каталога, а самостоятельный нарратив (Часть 4) — верстать отдельно.

## 6.1. Структура паттернов (как собран текущий раздел)

- **Индекс IT:** `patterns/pages/casi-studio-index.php` — сейчас сетка 2×2 (`layout:grid`,
  `--sr-grid-min:280px`) из карточек-`sr-browser` (бар браузера + `<figure><img>`), под каждой
  `<h3>` со ссылкой, mono-строка категории, mono-число результата, две полоски `.sr-barra`
  (prima/dopo) и `.sr-card-link`. Финальная секция `.sr-dark` с CTA. EN — `en-casi-studio-index.php`,
  RU — `ru-casi-studio-index.php` (идентичная структура, локализованные строки).
- **Отдельная страница кейса IT:** `patterns/pages/caso-<slug>.php` — hero (`sr-hero`, eyebrow
  «Casi studio / …», H1, mono-строка «SETTORE · SEDE · INTERVENTO · ANNO»), секция со скриншотом
  `.sr-browser`, три главы `.sr-chapter` (01 Problema / 02 Soluzione / 03 Risultati) с `.sr-stat`,
  `.sr-barra-row`, `.sr-list-rows`, `.sr-pull-quote`, финальный `.sr-dark` CTA + «Altri casi studio →».
  EN/RU — `en-caso-*.php` / `ru-caso-*.php`.
- **Текущие кейсы фиктивные** (Arredamenti Colombo, Cantina Serralta, TecnoIdraulica, Studio Legale
  Fontana) — по новой концепции они **заменяются** реальными проектами группы. Это касается и
  `data.py` (SERVICES → `mini_caso`), и `citta-*.php` (в них тоже вшиты эти кейсы — см. ниже).

## 6.2. Что менять в `data.py` vs руками

- **⚠️ ЖИРНОЕ ПРЕДУПРЕЖДЕНИЕ — ссылки из услуг и городов на кейсы.** `mini_caso` в **6 услугах**
  (`data.py` → `SERVICES[*].mini_caso.link_slug`: tecnoidraulica ×1, cantina-serralta ×2,
  arredamenti-colombo ×2, studio-legale-fontana ×1) и `case_slug` в **5 городах** (`data.py` →
  CITIES / `citta-*.php`: milano, monza, bergamo, brescia, como) ссылаются на текущие якоря/слаги
  кейсов. **При переработке раздела сохранить или обновить эти якоря так, чтобы ни одна ссылка не
  сломалась** (перепривязать на новые карточки-якоря вида `/casi-studio/#tms-perevod4` или на
  релевантный новый кейс), и **прогнать греп по всем слагам якорей** до и после деплоя:
  `grep -rn -e 'arredamenti-colombo' -e 'cantina-serralta' -e 'tecnoidraulica' -e 'studio-legale-fontana' patterns/ build-tools/`
  — в выдаче не должно остаться ссылок на удалённые страницы.
- **Формат утверждён (оркестратор, 15.07): ОДИН каталог с развёрнутыми карточками.** Отдельные
  страницы `caso-*.php` под новые кейсы НЕ создаются, `CASES_SLUGS` в `lang.py` НЕ расширяется.
  Карточки живут внутри `casi-studio-index.php` / `en-…` (RU — нарративная страница, см. Часть 4).
  Для фильтра и перелинковки карточкам дать **якоря** (`id` на обёртке карточки), IT=EN:
  `#att-traduzione-tech`, `#tms-perevod4`, `#mini-app-telegram`, `#ai-perevod4`,
  `#perevod4-catalogo`, `#gioco-impero-traduzioni`, `#pere-rf`, `#ukrinitsy`,
  `#moscowtrans-techperevod`, `#test-traduttori`, `#1russian`.
- **`deploy-import.php`:** слаги `home/en/ru` защищены от orphan-sweep; при добавлении новых
  страниц кейсов пополнить `$current_slugs` (см. §0.4 плана). Контент `patterns/**` живёт в БД →
  после правок нужен `REMARKA_FORCE=1 wp eval-file deploy-import.php`.

## 6.3. Какие скриншоты снять (URL + что в кадре · десктоп/мобайл)

> Все — реальные экраны живых проектов. Формат как у текущих кейсов: AVIF/JPG, кладутся в
> `assets/img/`, показываются в `.sr-browser` (десктоп) или в мобильной рамке.

| # | Проект | URL | Что в кадре | Устройство |
|---|---|---|---|---|
| 1 | ATT | https://www.traduzione.tech | Главная с блоком услуг | Десктоп 1440 |
| 2 | TMS | https://tms.perevod4.ru | Доска заказов (главный экран) + 5 доп. экранов под подписи §2.3 | Десктоп 1440 |
| 3 | Mini App | https://t.me/massimoalefBot | Mini App внутри Telegram, список заказов | Мобайл 390 |
| 4 | ai.perevod4 | https://ai.perevod4.ru (IT-версия) | Итальянская версия, первый экран | Десктоп + мобайл |
| 5 | perevod4 | https://perevod4.ru | Каталог бюро по городам | Десктоп 1440 |
| 6 | Gioco | https://traduzione.tech/gioco/ | Экран игры | Десктоп 1440 |
| 7 | пере.рф | https://пере.рф | Главная | Десктоп + мобайл |
| 8 | ukrinitsy | https://ukrinitsy.ru | Первый экран, мобильная версия (акцент mobile-first) | Мобайл 390 |
| 9 | moscowtrans+techperevod | https://moscowtrans.ru · https://techperevod.com | Две главные рядом (композит) | Десктоп 1440 |
| 10 | Tester | https://moscowtrans.ru/test-perevodchika/ | Экран прохождения теста / панель оценки | Десктоп 1440 |
| 11 | 1russian | https://1russian.com | Главная, англоязычный первый экран | Десктоп 1440 |

**Mobile-first:** скриншоты 3 и 8 — обязательно мобильные (Mini App и туризм смотрят с телефона);
для остальных — десктоп 1440 + опц. мобильная версия. Все `<img>` — `max-width:100%`, `loading="lazy"`.

## 6.4. Строки для `docs/seo-meta.md`

Добавить/обновить (сейчас `/casi-studio/` помечен «брендовый — фокус-ключ не задавать»; по новой
концепции задаём):

```
| /casi-studio/ · /en/case-studies/ | portfolio siti web | web design portfolio | ✅ (H1, intro, alt, chip-фильтр) |
| /ru/kejsy/ | портфолио веб-студии | ✅ (H1, hero-sub, нарратив) |
```
Title/Description — из §1.2–1.4 этого дека (все длины проверены: Title ≤60, Description ≤160).

## 6.5. Перелинковка (кейсы ↔ услуги ↔ инструменты)

- **Кейс → услуга** (CTA каждой карточки, IT/EN-слаги — см. карточки; RU — на лендинги воронки):
  ATT→siti-aziendali/business-websites · TMS→web-app/custom-web-apps · MiniApp→web-app (alt siti-pwa) ·
  ai.perevod4→seo-tecnica (+ multilingue) · perevod4→seo-tecnica · gioco→restyling-migrazione ·
  пере.рф→seo-tecnica · ukrinitsy→siti-aziendali (vetrina, утверждено) ·
  moscowtrans+techperevod→restyling-migrazione · tester→web-app (+ E-E-A-T-линк на siti-multilingue) ·
  1russian→siti-multilingue/multilingual-websites (перелинк seo-tecnica).
- **Услуга → кейс (обратная связь):** на страницах услуг заменить битые `mini_caso` на релевантный
  новый кейс (напр. `siti-multilingue` → tester/ai.perevod4; `web-app` → TMS; `seo-tecnica` → пере.рф).
- **Кейс ↔ инструмент:** в финальном dark-CTA каталога вести на `/strumenti/test-velocita/` («измерьте
  свой сайт»), как в текущей версии; RU — на `/ru/instrumenty/test-skorosti/`.
- **RU-нарратив → воронка:** блок 6 линкует `/ru/uslugi/sajt-dlya-evropy/` и `/ru/uslugi/seo-prodvizhenie/`
  (лендинги фазы B) — это и есть цель «доказательная база лендинга».

## 6.6. Напоминания

- **RU — руками**, `translate_pages.py ru` НЕ запускать. RU-кейсы — это отдельный нарратив, не перевод.
- Строить секции на `.sr-section` / `.sr-section--bianco` (у них свой фолбэк центрирования/паддингов).
- `[hidden]` перебивается `.wp-block-button__link` — учитывать в новых компонентах.
- Цифры результатов проставлены владельцем 15.07 (§7) — публиковать «вариант с цифрами»;
  «вариант без цифр» остаётся fallback (и единственный публикуемый для gioco).
- Стек и оставшиеся сроки в карточках помечены `[ПРОВЕРИТЬ: …]` — сверить с живыми сайтами перед публикацией.
- Проверить живость сайтов 2002–2003 из интро (directindustry.com.ru · ivextrans.eu · beltran.by) —
  если какой-то мёртв, убрать его из строки, не заменяя.

---

# 7. ЦИФРЫ ВЛАДЕЛЬЦА — ПОЛУЧЕНЫ И ПРОСТАВЛЕНЫ (15.07)

Все плейсхолдеры `[ЦИФРА ВЛАДЕЛЬЦА]` заменены реальными цифрами владельца (кроме gioco — см. ниже).
Варианты «без цифр» сохранены в каждой карточке как **fallback**. Что использовано и что опущено:

| Кейс | Использовано | Опущено (почему) |
|---|---|---|
| пере.рф | № 1 в Яндексе по «нотариальный перевод» и «перевод инструкций»; 9–10 тыс. посет./мес; в топе >1 000 дней | — (ссылки на выдачу упомянуты как «disponibili») |
| ATT | ~20 заказов/мес; >40 языковых пар; онлайн с 2022 | — |
| TMS | 180 заказов/мес; >2 000/год; 2 админа + 8 менеджеров + 4 партнёрских бюро; 2 года в проде | — |
| Mini App | разработка за 2 недели (акцент — скорость); >10 пользователей/заказов в день | — |
| Tester | >400 переводчиков протестировано; **тест проходят только 8%** (уточнение владельца 15.07: ранее цифра ошибочно передана как «отсев ≤8%» и была опущена; в правильном смысле — сильная, используется в ОБОИХ вариантах карточки IT/EN и в RU-блоках 3 и 4, включая связку с гарантией «носители по профилю») | — |
| perevod4.ru | >200 бюро в каталоге | **Трафик 1 200/мес — опущен** (слабая цифра рядом с 10 000 у соседних кейсов); формулировки «тысячи страниц» заменены на «сотни/целая отрасль» |
| ai.perevod4 | >60 языков; >10 000 запросов/мес | **120 зарегистрированных пользователей — опущено** (запросы сильнее; 120 рядом с 10 000 занижает) |
| 1russian | >10 000 посет./мес из 80 стран | — |
| ukrinitsy | +450% бронирований; 18 за сезон (подано с контекстом «для маленького дома это полный сезон») | — |
| moscowtrans+techperevod | обновление дизайна и функционала в 2026; конверсии +300% за последние месяцы | PageSpeed не присылался — не упоминаем |
| Gioco | 984 сыгранные партии; 12 086 минут (>200 часов) за игрой (цифры владельца, 15.07) — проставлено в IT/EN-карточках и RU-блоке 5 | — |

**Рамка интро (проставлена во всех трёх языках):** >160 проектов создано · 28 на постоянном
обслуживании · сайты строим с 2001 года · примеры 2002–2003: directindustry.com.ru,
ivextrans.eu, beltran.by `[ПРОВЕРИТЬ: сайты 2002–2003 живы — из песочницы не проверить]`.

**Остаётся владельцу/имплементатору:** `[ПРОВЕРИТЬ: стек]` и `[ПРОВЕРИТЬ: срок]` в карточках
(кроме уже известных: MiniApp — 2 недели, ATT — с 2022, TMS — 2 года, moscowtrans/techperevod —
2026); `[ПРОВЕРИТЬ: SiteLens]` в карточке 1russian; подписи TMS-экранов; живость сайтов 2002–2003.

---

# 8. СПОРНЫЕ МЕСТА — СТАТУС ПОСЛЕ РЕШЕНИЙ ОРКЕСТРАТОРА (15.07)

1. ✅ **РЕШЕНО: 1russian.com добавлен 11-й карточкой в IT/EN** (категория `SEO · Contenuti`,
   угол «progetto internazionale in lingua inglese», CTA → siti-multilingue — выбор обоснован в
   карточке; перелинк на seo-tecnica). В RU-нарративе был и остаётся без изменений (блок 2).
   Фактура из склонированного репо `/workspace/1russian.com`: WordPress на REG.RU, деплой через
   контролируемый репозиторий; рядом разрабатывается SiteLens — собственный self-hosted
   SEO-анализатор группы (Node.js/TS, Docker; аналог Screaming Frog + GSC-интеграции). Упоминание
   SiteLens в карточке помечено `[ПРОВЕРИТЬ]` — статус запуска не подтверждён.
2. ✅ **РЕШЕНО: фокус-ключи утверждены** — `portfolio siti web` / `web design portfolio` /
   `портфолио веб-студии` (portfolio-интент, не брендовый «casi studio»).
3. ✅ **РЕШЕНО: формат IT/EN — один каталог с развёрнутыми карточками.** Отдельные `caso-*.php`
   не планируются, `CASES_SLUGS` не расширяется; карточкам даны якоря (см. §6.2).
4. ✅ **РЕШЕНО: ukrinitsy CTA → siti-aziendali** (утверждено).
5. ⚠️ **ОТКРЫТО (передано имплементатору жирным в §6.2):** `mini_caso` в 6 услугах и `case_slug`
   в 5 городах ссылаются на текущие якоря кейсов — при переработке сохранить/обновить якоря без
   единой битой ссылки и прогнать греп по слагам (команда в §6.2).
6. ⚠️ **ОТКРЫТО (владелец):** стек/сроки во всех карточках — неподтверждённые (сайты недоступны
   из окружения; для 1russian стек частично подтверждён репозиторием). Помечены `[ПРОВЕРИТЬ]`;
   публикуемые «варианты без цифр» их не используют как факт.
7. ⚠️ **ОТКРЫТО (владелец):** подписи скриншотов TMS — по типовой структуре TMS, а не по реальному
   интерфейсу (решение оркестратора: оставить так, с обязательной сверкой владельцем перед публикацией).

---

*Файл: `scratchpad/copy-casi-studio.md`. Репозиторий не редактировался, git-команды не выполнялись.*
