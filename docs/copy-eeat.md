# Copy deck — 8° strumento Lab: «Segnali E-E-A-T» (IT + EN + RU)

> Data: 15.07.2026 · Autore: Opus (strategia + copy). Base di lettura:
> `docs/piano-strumenti-lab.md` §0–§1, `wordpress/build-tools/data.py` (TOOLS),
> `wordpress/remarka-studio/assets/js/remarka.js` (moduli `initGdprTool`/`initAiTool`),
> `wordpress/build-tools/lang.py`, `docs/seo-meta.md`, `docs/copy-fase-B.md`,
> `docs/piano-implementazione-fase-A.md` §0.
>
> **Nome onesto (cornice del proprietario, non modificare):** misuriamo **segnali
> on-page verificabili nel codice della pagina**, NON la reputazione o la competenza
> reale. Il disclaimer è obbligatorio in pagina e nei verdetti.
>
> **Motore:** solo `remarka_tool_fetch` esistente. Tutti i segnali si estraggono da
> **un** fetch `mode:html` della home (≤512 KB) + schema dell'URL. Nessun codice
> server nuovo. Il modulo JS `eeat` è più leggero di `ai` (un solo fetch).
>
> **Slug finali (verificati contro `lang.py`):**
> IT `strumenti/segnali-eeat` · EN `en/tools/eeat-signals` · RU `ru/instrumenty/signaly-eeat`.
>
> **Questo file è l'unico output. Nessuna modifica al repo, nessun comando git
> eseguito (altro agente lavora in parallelo). L'orchestratore importa il file.**

---

# PARTE 0 — DECISIONI CHE RICHIEDONO IL PROPRIETARIO

1. **Slug** — confermare la terna proposta (sopra). Coerente col pattern `TOOLS_SLUGS`.
2. **Peso degli assi** — proposta: Affidabilità 42 / Esperienza 22 / Competenza 20 /
   Autorevolezza 16 (motivazione in §1.3). Trust pesa di più perché nelle linee guida
   Google è il pilastro centrale. Se il proprietario preferisce un profilo più
   «bilanciato» (25/25/25/25) va deciso qui — cambia solo i numeri, non la struttura.
3. **Competenza su un solo segnale** (dati strutturati) — scelta onesta: la competenza
   è il pilastro più difficile da provare via HTML. Se si vuole irrobustire, l'unica
   aggiunta possibile senza server nuovo è spezzare il segnale schema in
   «Organization/Person» + «author/datePublished». Decisione del proprietario.
4. **Ingresso nel check-up sintetico** — per ora NO (da mandato). Confermato.
5. **P.IVA reale** — in tutto il sito la P.IVA è ancora un dato fittizio
   («Sostituire i dati fittizi prima del lancio», `trust-strip.php`). Il copy usa la
   formula esistente «P.IVA verificabile», non un numero inventato.

---

# PARTE 1 — MODELLO DI SCORING

## 1.1. Gli 8 segnali (tutti da HTML home + schema URL)

| # | Segnale | Come lo rileviamo (tecnico, JS su HTML ≤512 KB) | Asse | Peso | good / warn / bad |
|---|---|---|---|---|---|
| 1 | **HTTPS** | Schema dell'URL finale della risposta = `https` (protocollo servito, nessun downgrade). Binario. | Affidabilità | 8 | good: `https` · bad: `http` |
| 2 | **Contatti verificabili** | Presenza nel DOM di `href^="tel:"` o `href^="mailto:"`; oppure indirizzo postale in chiaro: regex `/(via|viale|piazza|corso|str\.)\s+[^,<]{2,}/i` seguita da CAP `/\b\d{5}\b/`. | Affidabilità | 12 | good: `tel:` **o** indirizzo con CAP · warn: solo `mailto:`/email · bad: nessuno |
| 3 | **Identità legale** | Regex `/(p\.?\s?iva|partita\s+iva|\bvat\b|\brea\b|c\.?f\.?|cod(?:ice)?\s+fisc)/i` o sequenza di 11 cifre nel footer. Binario. | Affidabilità | 12 | good: trovata · bad: assente |
| 4 | **Privacy & cookie policy** | `href` o testo àncora con `/(privacy|cookie|informativa)/i`. | Affidabilità | 10 | good: **entrambe** (privacy + cookie) · warn: una sola · bad: nessuna |
| 5 | **Pagina «Chi siamo»** | `href` o testo àncora con `/(chi[-\s]siamo\|about(?:-us)?\|su-di-noi\|azienda\|team\|storia)/i`. Binario. | Esperienza | 12 | good: trovata · bad: assente |
| 6 | **Portfolio / casi studio** | `href` o testo àncora con `/(casi[-\s]studio\|case[-\s]stud\|portfolio\|referenze\|lavori\|progetti\|testimonial)/i`. Binario. | Esperienza | 10 | good: trovato · bad: assente |
| 7 | **Dati strutturati JSON-LD** | Parsing di `<script type="application/ld+json">` (già presente in `initAiTool`); leggo gli `@type`. | Competenza | 20 | good: presente un `@type` d'identità (`Organization`/`LocalBusiness`/`Person`) · warn: JSON-LD presente ma solo generico (`WebSite`/`WebPage`) o malformato · bad: nessun JSON-LD |
| 8 | **Profili esterni (sameAs)** | Array `sameAs` nel JSON-LD, oppure link a domini social: `/(linkedin\|facebook\|instagram\|youtube\|x\.com\|twitter\|t\.me)/i`. | Autorevolezza | 16 | good: ≥2 profili o `sameAs` · warn: 1 profilo · bad: nessuno |

**Perché questi 8 e non altri.** Sono i soli candidati della lista del proprietario
che (a) compaiono davvero sulla **home** — non su pagine interne — e (b) si leggono
con regex/DOM sul primo HTML, senza eseguire JavaScript. Scartati di proposito:
«autore + data sui contenuti» (segnale da pagina-articolo, quasi mai in home →
falsi negativi sistematici) sostituito da «Portfolio/casi studio», più adatto alla home;
«favicon/og» tenuto fuori dal punteggio perché troppo debole come prova di fiducia
(resta eventualmente come nota d'igiene, non pesa).

## 1.2. Formula

```
punteggio_segnale = peso            se good
                  = round(peso/2)   se warn
                  = 0               se bad
                  (segnali binari: solo good=peso o bad=0)

PUNTEGGIO = Σ punteggio_segnale        → intero 0–100  (i pesi sommano a 100)
```

Sotto-punteggio per asse (mostrato nel widget, normalizzato 0–100):

```
asse% = round( Σ punti_ottenuti_asse / max_asse × 100 )
max_asse: Affidabilità 42 · Esperienza 22 · Competenza 20 · Autorevolezza 16
```

warn dei non-binari (metà peso, arrotondato): Contatti 6 · Policy 5 · Schema 10 · Profili 8.

## 1.3. Soglie dei verdetti (identiche a check-up: 90 / 75 / 50)

| Fascia | Verdetto generale | Colore |
|---|---|---|
| **90–100** | Ottimo | verde |
| **75–89** | Buona base | verde chiaro |
| **50–74** | A metà strada | giallo |
| **0–49** | Segnali deboli | rosso |

**Flag per asse** (triade CSS `data-sr-flag` già supportata `good\|warn\|bad`):
asse% ≥ 75 → `good` · 50–74 → `warn` · < 50 → `bad`.

**Motivazione dei pesi.** Nelle Search Quality Rater Guidelines di Google il **Trust
è il pilastro centrale**: «Experience, Expertise e Authoritativeness sono importanti in
quanto sostengono il Trust». Da qui Affidabilità = 42 (quattro segnali igienico-legali,
i più oggettivi da leggere nel codice). Esperienza = 22 (chi c'è dietro + track record).
Competenza = 20 (dichiarazione machine-readable dell'identità: è l'asse più difficile da
provare on-page, e lo diciamo). Autorevolezza = 16 (i profili esterni sono l'unico
appiglio di autorevolezza leggibile in home — i backlink, che la determinano davvero,
non li vediamo).

## 1.4. Regola N/D e casi limite

- **Fetch fallito** (timeout, blocco, risposta non-HTML) → nessun punteggio, messaggio
  d'errore (testi in §3, §4, §5 per lingua). Non mostriamo mai uno «0» fuorviante.
- **HTML integro ma SPA / troppo scarno** (`<body>` quasi vuoto, impronta tipo
  `<div id="root"></div>`/`<div id="app"></div>`, o testo visibile < ~2 KB) → il
  punteggio si calcola comunque, ma la pagina mostra un **avviso «analisi parziale»**:
  «Il sito rende i contenuti via JavaScript: molti segnali potrebbero esistere ma non
  essere leggibili nell'HTML iniziale.» I segnali risultati `bad` vengono annotati
  «non rilevato (possibile rendering JavaScript)». È l'unico caso in cui appare la
  dicitura **N/D** accanto a un segnale.
- **Segnale JSON-LD malformato** → contato come `warn` (presente ma non pulito), non `bad`
  (coerente con `initAiTool`, che già conta il JSON-LD malformato come presente).

## 1.5. Confini onesti (obbligatorio in pagina — disclaimer)

> **Misuriamo segnali on-page verificabili nel codice della pagina, non la vostra
> reputazione o competenza reale.** Un punteggio alto significa che i segnali di fiducia
> ci sono e sono leggibili; **non** garantisce un giudizio E-E-A-T positivo da parte di
> Google, che valuta l'intera entità con criteri umani.

Il test **non** misura: link in entrata e menzioni; recensioni e reputazione; competenza
reale degli autori; veridicità e qualità dei contenuti; l'E-E-A-T «reale» come lo giudica
un quality rater; nulla che compaia solo dopo l'esecuzione del JavaScript; pagine diverse
dalla home indicata.

---

# PARTE 2 — SEO (IT / EN / RU)

## 2.1. Focus keyword e varianti (nicchia vuota: prendiamo le query che definiscono il tema)

| Lingua | Focus keyword (Rank Math, una) | Varianti / query correlate |
|---|---|---|
| IT | **segnali E-E-A-T** | `E-E-A-T cos'è`, `test E-E-A-T`, `E-E-A-T sito`, `come migliorare E-E-A-T` |
| EN | **E-E-A-T checker** | `E-E-A-T signals`, `what is E-E-A-T`, `E-E-A-T test`, `check E-E-A-T` |
| RU | **проверка E-E-A-T** | `E-E-A-T что это`, `сигналы E-E-A-T`, `E-E-A-T сайта`, `тест E-E-A-T` |

## 2.2. Title / Description (limiti Title ≤60, Description ≤160)

**IT** — `/strumenti/segnali-eeat/`
- **Title:** `Segnali E-E-A-T: test di fiducia del sito | Studio Remarka`  *(58)*
- **Description:** `Misuriamo i segnali E-E-A-T leggibili nel codice della home: HTTPS, contatti, P.IVA, chi siamo, dati strutturati. Punteggio 0–100, gratis, senza registrazione.`  *(≈159)*

**EN** — `/en/tools/eeat-signals/`
- **Title:** `E-E-A-T Checker: your site's trust signals | Studio Remarka`  *(59)*
- **Description:** `We check the E-E-A-T signals readable in your homepage code: HTTPS, contacts, VAT, an about page, structured data. A 0–100 score, free, no sign-up.`  *(≈152)*

**RU** — `/ru/instrumenty/signaly-eeat/`
- **Title:** `Проверка E-E-A-T: сигналы доверия сайта | Studio Remarka`  *(56)*
- **Description:** `Проверяем сигналы E-E-A-T, читаемые в коде главной: HTTPS, контакты, реквизиты, страница «о нас», микроразметка. Оценка 0–100, бесплатно, без регистрации.`  *(≈153)*

## 2.3. H1 e variazioni H2 (l'H2 non ripete l'H1 alla lettera — pattern seo-meta)

| | H1 | H2 metodologia | H2 lettura | H2 migliorare |
|---|---|---|---|---|
| IT | `Segnali E-E-A-T: quanto è credibile il vostro sito?` | `Cosa misura davvero questo test dei segnali E-E-A-T` | `Come leggere il punteggio E-E-A-T e i quattro assi` | `Come rafforzare i segnali E-E-A-T del sito` |
| EN | `E-E-A-T signals: how credible does your site look?` | `What this E-E-A-T signal test actually measures` | `How to read the E-E-A-T score and the four pillars` | `How to strengthen your site's E-E-A-T signals` |
| RU | `Сигналы E-E-A-T: насколько сайт выглядит надёжным?` | `Что на самом деле проверяет этот тест сигналов E-E-A-T` | `Как читать оценку E-E-A-T и четыре оси` | `Как усилить сигналы E-E-A-T на сайте` |

---

# PARTE 3 — CONTENUTO PAGINA IT (record `data.py` TOOLS)

> Struttura campo-per-campo come le voci esistenti. `tipo='eeat'`, `idx='/08'`.

```
slug = 'segnali-eeat'
idx  = '/08'
tipo = 'eeat'
titolo = 'Segnali E-E-A-T'
has_demo = False
```

**hero_titolo:** `Segnali E-E-A-T: quanto è credibile il vostro sito?`

**hero_sub:** `Analizziamo otto segnali di fiducia leggibili nel codice della vostra home — HTTPS, contatti, P.IVA, chi siamo, dati strutturati e altri — raggruppati nei quattro pilastri E-E-A-T. Misuriamo i segnali on-page, non la vostra reputazione o competenza reale. Senza registrazione.`

**descrizione (sottotitolo card):** `Otto segnali di fiducia on-page, raggruppati nei quattro pilastri E-E-A-T.`

**come_funziona (3 passi):**
1. `('Inserite l'indirizzo del sito', 'Leggiamo la home page dal nostro server, come farebbe un visitatore alla prima apertura: analizziamo il codice HTML, non serve installare nulla.')`
2. `('Otto controlli automatici', 'Cerchiamo otto segnali di fiducia leggibili nella pagina — HTTPS, contatti, P.IVA, privacy, chi siamo, portfolio, dati strutturati, profili esterni — e li raggruppiamo nei quattro pilastri E-E-A-T.')`
3. `('Punteggio 0–100 e quattro assi', 'Un punteggio complessivo e il dettaglio per Esperienza, Competenza, Autorevolezza e Affidabilità, con il colore di ogni segnale e cosa manca.')`

**faq (3):**
1. `('Cos'è l'E-E-A-T?', 'È un concetto delle linee guida di Google per i valutatori della qualità (Search Quality Rater Guidelines): Experience, Expertise, Authoritativeness, Trust — esperienza, competenza, autorevolezza e affidabilità. Aiuta Google a stimare quanto ci si può fidare di una pagina, soprattutto sui temi che incidono su salute, denaro e sicurezza.')`
2. `('L'E-E-A-T influenza il posizionamento?', 'Non è un fattore di ranking diretto né un punteggio che Google assegna: è una cornice di qualità che i valutatori umani usano per addestrare gli algoritmi. Rafforzare i segnali di fiducia aiuta indirettamente, ma nessuno strumento — nemmeno il nostro — misura l'E-E-A-T «reale» del vostro sito.')`
3. `('Perché il test non vede la mia reputazione?', 'Perché leggiamo solo il codice della vostra pagina: possiamo verificare che i segnali di fiducia ci siano e siano dichiarati, non chi vi cita, che recensioni avete o quanto siete davvero esperti. Quella parte la giudicano le persone e il resto del web, non una scansione dell'HTML.')`

**metodologia** — h2: `Cosa misura davvero questo test dei segnali E-E-A-T`
1. `Come per il controllo GDPR e per quello di prontezza AI, è il nostro server a leggere la home page del vostro sito, senza passare da Google. Sul codice HTML cerchiamo otto segnali di fiducia che chiunque — un motore di ricerca, un modello AI, un cliente diffidente — userebbe per decidere se fidarsi: la connessione sicura (HTTPS), i contatti verificabili, l'identità legale (P.IVA e ragione sociale), i link a privacy e cookie policy, la pagina «Chi siamo», un portfolio o dei casi studio, i dati strutturati in JSON-LD e i profili esterni. Ogni segnale finisce in uno dei quattro pilastri E-E-A-T — Esperienza, Competenza, Autorevolezza, Affidabilità — e pesa sul punteggio complessivo.`
2. `Ed ecco il confine, che diciamo subito: misuriamo segnali on-page verificabili nel codice, non l'E-E-A-T reale del vostro sito. Non contiamo i link o le menzioni che ricevete, non leggiamo le recensioni né la vostra reputazione, non giudichiamo se siete davvero esperti o se i contenuti dicono il vero: quella valutazione la fanno le persone — i quality rater di Google e il resto del web — non una scansione dell'HTML. Guardiamo solo la home indicata, non l'intero sito, e non vediamo ciò che compare soltanto dopo l'esecuzione del JavaScript. Un punteggio alto significa che i segnali di fiducia ci sono e sono leggibili, non che Google vi darà un giudizio E-E-A-T positivo.`

**lettura** — h2: `Come leggere il punteggio E-E-A-T e i quattro assi`
1. `Il punteggio va da 0 a 100 e si legge come un semaforo a quattro livelli. Da 90 in su i segnali di fiducia ci sono quasi tutti e si leggono senza sforzo. Tra 75 e 89 avete una buona base, con pochi elementi da completare. Tra 50 e 74 mancano diversi segnali importanti: è la fascia più comune per i siti aziendali italiani, che spesso curano i contenuti ma dimenticano la parte tecnica. Sotto 50 la pagina espone pochi appigli di fiducia — ed è anche la situazione in cui bastano poche aggiunte per salire in fretta. Accanto al totale trovate i quattro assi, così vedete su quale pilastro conviene intervenire prima.`
2. `Due letture da evitare. La prima: un segnale in rosso non è una colpa, ma un'occasione — «nessun dato strutturato» vuol dire che, aggiungendo un blocco JSON-LD, guadagnate punti in un pomeriggio. La seconda, più importante: un 100 pieno non certifica il vostro E-E-A-T. Significa che avete dichiarato bene chi siete, non che il web vi considera autorevoli — quella fiducia si costruisce con contenuti, tempo e reputazione, che nessuno strumento legge dall'HTML. E se il punteggio vi sembra ingiustamente basso, controllate se il sito rende i contenuti via JavaScript: in quel caso molti segnali esistono ma non sono nel codice iniziale che leggiamo, e ve lo segnaliamo con un avviso.`

**migliorare** — h2: `Come rafforzare i segnali E-E-A-T del sito`
- intro: `Rafforzare la fiducia non richiede riscrivere il sito: sono aggiunte tecniche precise, quasi tutte veloci e a basso costo.`
- punti:
  1. `('Pubblicate una pagina «Chi siamo» vera', 'Con nomi, volti, storia e competenze reali del team, non un paragrafo generico: è il primo posto dove Google e i lettori cercano di capire chi c'è dietro.')`
  2. `('Rendete i contatti verificabili', 'Indirizzo completo, telefono ed email reali in chiaro, nel footer di ogni pagina, non solo dentro un modulo: un recapito tracciabile è un segnale di fiducia di base.')`
  3. `('Dichiarate l'identità legale', 'P.IVA, ragione sociale e sede nel footer: per un'azienda italiana è la prova più semplice di essere un soggetto reale e raggiungibile.')`
  4. `('Aggiungete i dati strutturati', 'Un blocco JSON-LD schema.org Organization (o LocalBusiness) con nome, logo, contatti e profili «sameAs» dice a motori e AI chi siete, in modo esplicito.')`
  5. `('Firmate e datate i contenuti', 'Autore riconoscibile, data di pubblicazione e di aggiornamento su articoli e schede: mostrano esperienza reale e contenuti curati nel tempo.')`
- links:
  - `('Vogliamo sistemarli noi: fa parte della SEO tecnica', '/servizi/seo-tecnica/')`
  - `('Chi siamo, contatti e dati strutturati sono di serie nei siti aziendali', '/servizi/siti-aziendali/')`

**cta:**
- heading: `Vogliamo rafforzare la fiducia del vostro sito?`
- testo: `Chi siamo, contatti verificabili, identità legale e dati strutturati a posto: fanno parte della SEO tecnica e di ogni sito aziendale che consegniamo.`
- buttons:
  - `('Scopri la SEO tecnica', '/servizi/seo-tecnica/', None)`
  - `('Verifica se il sito è pronto per l'AI', '/strumenti/sito-pronto-ai/', 'outline')`

---

# PARTE 3-BIS — WIDGET IT (etichette, verdetti, errori)

**Contratto data-* (per il generatore).** Wrapper `[data-sr-tool="eeat"]` con `data-sr-locale`.
Un solo fetch `html`. Campi:
- `[data-sr-tool-form]` (input url + submit) · `[data-sr-tool-pending]` · `[data-sr-tool-result]`
- `[data-sr-tool-url]` · `[data-sr-tool-score]` (0–100) · `[data-sr-tool-fill]` (barra = score%) · `[data-sr-tool-verdict]` (generale)
- 4 assi: `[data-sr-tool-axis-esperienza]` `[data-sr-tool-axis-competenza]` `[data-sr-tool-axis-autorevolezza]` `[data-sr-tool-axis-affidabilita]` (valore 0–100 + `[data-sr-flag]`)
- 8 segnali: `[data-sr-tool-https]` `[data-sr-tool-contatti]` `[data-sr-tool-legale]` `[data-sr-tool-policy]` `[data-sr-tool-chisiamo]` `[data-sr-tool-portfolio]` `[data-sr-tool-schema]` `[data-sr-tool-profili]` (ognuno con `[data-sr-flag]=good|warn|bad`)
- `[data-sr-tool-notice]` (avviso «analisi parziale» SPA, hidden di default) · `[data-sr-tool-disclaimer]` (statico)

**Etichette campi (podpisi/subtitles del widget):**
- Punteggio: `Punteggio E-E-A-T on-page` · barra: `0–100`
- Assi: `Esperienza` · `Competenza` · `Autorevolezza` · `Affidabilità`
- Righe segnali: `Connessione HTTPS` · `Contatti verificabili` · `Identità legale (P.IVA)` · `Privacy e cookie policy` · `Pagina «Chi siamo»` · `Portfolio / casi studio` · `Dati strutturati (JSON-LD)` · `Profili esterni`

**Verdetti generali (4 livelli — `data-verdict-*`):**
- good (≥90): `Ottimo: i segnali di fiducia E-E-A-T sono presenti e leggibili nel codice. Ricordate che parliamo di segnali on-page, non del vostro E-E-A-T reale.`
- buono (75–89): `Buona base: la maggior parte dei segnali di fiducia c'è. Sistemate i pochi punti in giallo o rosso per completare il quadro.`
- mid (50–74): `A metà strada: diversi segnali di fiducia mancano o non sono leggibili. La lista qui sotto indica da dove partire.`
- poor (<50): `Segnali deboli: la pagina espone pochi elementi di fiducia verificabili — che sono anche i più facili da aggiungere.`

**Etichette per segnale (good / warn / bad) — `data-label-*`:**
| Segnale | good | warn | bad |
|---|---|---|---|
| HTTPS | `Connessione sicura (HTTPS)` | — | `Nessun HTTPS: connessione non sicura` |
| Contatti | `Contatti verificabili presenti` | `Solo un'email, nessun telefono o indirizzo` | `Nessun contatto verificabile` |
| Identità legale | `P.IVA / dati fiscali presenti` | — | `Nessuna P.IVA o identità legale` |
| Policy | `Privacy e cookie policy presenti` | `Presente solo una delle due policy` | `Nessuna privacy o cookie policy` |
| Chi siamo | `Pagina «Chi siamo» presente` | — | `Nessuna pagina «Chi siamo»` |
| Portfolio | `Portfolio o casi studio presenti` | — | `Nessun portfolio o caso studio` |
| Dati strutturati | `Dati strutturati d'identità presenti` | `JSON-LD presente ma solo generico` | `Nessun dato strutturato JSON-LD` |
| Profili esterni | `Profili esterni collegati` | `Un solo profilo esterno` | `Nessun profilo esterno collegato` |

**Avviso «analisi parziale» (`data-notice`):** `Il sito rende i contenuti via JavaScript: alcuni segnali potrebbero esistere ma non essere leggibili nell'HTML iniziale. Il punteggio è indicativo.`

**Suffisso N/D per segnale non rilevato in caso SPA (`data-label-nd`):** `non rilevato (possibile rendering JavaScript)`

**Disclaimer statico (`data-sr-tool-disclaimer`):** `Misuriamo segnali on-page verificabili nel codice della pagina, non la vostra reputazione o competenza reale. Un punteggio alto non garantisce un giudizio E-E-A-T positivo da parte di Google.`

**Errore (`data-err`):** `Non siamo riusciti a leggere la pagina. Controllate l'indirizzo e riprovate tra qualche minuto.`

---

# PARTE 4 — CONTENUTO PAGINA EN (`/en/tools/eeat-signals/`)

> Per il conveyor EN: coppie CHROME (`en` only) di ogni stringa nuova → `translate_pages.py en`.
> Testi già rifiniti a livello madrelingua qui sotto (usare come traduzione di riferimento).

**hero_titolo:** `E-E-A-T signals: how credible does your site look?`

**hero_sub:** `We analyse eight trust signals readable in your homepage code — HTTPS, contacts, VAT number, an about page, structured data and more — grouped into the four E-E-A-T pillars. We measure on-page signals, not your real reputation or expertise. No sign-up.`

**descrizione:** `Eight on-page trust signals, grouped into the four E-E-A-T pillars.`

**come_funziona:**
1. `('Enter the site address', 'We read the home page from our own server, the way a first-time visitor would: we analyse the HTML, nothing to install.')`
2. `('Eight automatic checks', 'We look for eight trust signals in the page — HTTPS, contacts, VAT, privacy, about page, portfolio, structured data, external profiles — and group them into the four E-E-A-T pillars.')`
3. `('A 0–100 score and four pillars', 'An overall score plus the breakdown by Experience, Expertise, Authoritativeness and Trust, with a colour for each signal and what's missing.')`

**faq:**
1. `('What is E-E-A-T?', 'It's a concept from Google's Search Quality Rater Guidelines: Experience, Expertise, Authoritativeness and Trust. It helps Google estimate how much a page can be trusted, especially on topics that affect health, money and safety.')`
2. `('Does E-E-A-T affect rankings?', 'It's not a direct ranking factor or a score Google assigns: it's a quality framework human raters use to train the algorithms. Strengthening your trust signals helps indirectly, but no tool — ours included — measures your site's "real" E-E-A-T.')`
3. `('Why doesn't the test see my reputation?', 'Because we only read your page's code: we can confirm the trust signals are there and declared, not who cites you, what reviews you have or how expert you really are. That part is judged by people and the wider web, not by scanning HTML.')`

**metodologia** — h2: `What this E-E-A-T signal test actually measures`
1. `As with the GDPR and AI-readiness checks, it's our server that reads your home page, without going through Google. In the HTML we look for eight trust signals that anyone — a search engine, an AI model, a cautious customer — would use to decide whether to trust you: a secure connection (HTTPS), verifiable contacts, legal identity (VAT and company name), links to privacy and cookie policy, an about page, a portfolio or case studies, JSON-LD structured data, and external profiles. Each signal falls into one of the four E-E-A-T pillars — Experience, Expertise, Authoritativeness, Trust — and weighs on the overall score.`
2. `And here's the boundary, stated up front: we measure on-page signals readable in the code, not your site's real E-E-A-T. We don't count the links or mentions you receive, we don't read reviews or reputation, we don't judge whether you're genuinely expert or whether the content is true: that call is made by people — Google's quality raters and the wider web — not by scanning HTML. We look only at the home page you give us, not the whole site, and we don't see anything that appears only after JavaScript runs. A high score means the trust signals are present and readable, not that Google will give you a positive E-E-A-T judgement.`

**lettura** — h2: `How to read the E-E-A-T score and the four pillars`
1. `The score runs from 0 to 100 and reads like a four-level traffic light. From 90 up, almost all trust signals are there and easy to read. Between 75 and 89 you have a solid base, with a few items to complete. Between 50 and 74 several important signals are missing: this is the most common band for business sites that look after content but forget the technical side. Below 50 the page exposes few trust cues — which is also the situation where a handful of additions lift you quickly. Next to the total you'll find the four pillars, so you can see which one to fix first.`
2. `Two readings to avoid. First: a red signal isn't a fault, it's an opportunity — "no structured data" means that by adding a JSON-LD block you gain points in an afternoon. Second, and more important: a perfect 100 doesn't certify your E-E-A-T. It means you've declared who you are well, not that the web considers you authoritative — that trust is built with content, time and reputation, which no tool reads from HTML. And if the score seems unfairly low, check whether the site renders its content via JavaScript: in that case many signals exist but aren't in the initial code we read, and we flag it with a notice.`

**migliorare** — h2: `How to strengthen your site's E-E-A-T signals`
- intro: `Strengthening trust doesn't mean rewriting the site: these are precise technical additions, most of them quick and low-cost.`
- punti:
  1. `('Publish a real about page', 'With names, faces, history and the team's actual expertise, not a generic paragraph: it's the first place Google and readers look to understand who's behind the site.')`
  2. `('Make your contacts verifiable', 'A full address, a real phone number and email in plain sight, in every page footer, not just inside a form: a traceable contact is a baseline trust signal.')`
  3. `('Declare your legal identity', 'VAT number, company name and registered address in the footer: it's the simplest proof of being a real, reachable business.')`
  4. `('Add structured data', 'A JSON-LD schema.org Organization (or LocalBusiness) block with name, logo, contacts and "sameAs" profiles tells engines and AI who you are, explicitly.')`
  5. `('Sign and date your content', 'A named author, a publish date and a last-updated date on articles and pages: they show real experience and content kept current.')`
- links:
  - `('We can fix them for you: it's part of technical SEO', '/en/services/technical-seo/')`
  - `('About page, contacts and structured data come standard on business websites', '/en/services/business-websites/')`

**cta:**
- heading: `Want to strengthen your site's credibility?`
- testo: `About page, verifiable contacts, legal identity and structured data in place: they're part of the technical SEO and every business website we deliver.`
- buttons:
  - `('Discover technical SEO', '/en/services/technical-seo/', None)`
  - `('Check if your site is AI-ready', '/en/tools/ai-readiness/', 'outline')`

**Widget EN — verdetti generali:**
- good: `Excellent: the E-E-A-T trust signals are present and readable in the code. Remember these are on-page signals, not your real E-E-A-T.`
- buono: `Solid base: most trust signals are there. Fix the few amber or red items to complete the picture.`
- mid: `Halfway there: several trust signals are missing or unreadable. The list below shows where to start.`
- poor: `Weak signals: the page exposes few verifiable trust cues — which are also the easiest to add.`

**Etichette segnali EN (good/warn/bad):** HTTPS `Secure connection (HTTPS)` / — / `No HTTPS: insecure connection` · Contatti `Verifiable contacts present` / `Only an email, no phone or address` / `No verifiable contacts` · Legale `VAT / tax details present` / — / `No VAT or legal identity` · Policy `Privacy and cookie policy present` / `Only one of the two policies` / `No privacy or cookie policy` · Chi siamo `About page present` / — / `No about page` · Portfolio `Portfolio or case studies present` / — / `No portfolio or case studies` · Schema `Identity structured data present` / `JSON-LD present but generic only` / `No JSON-LD structured data` · Profili `External profiles linked` / `Only one external profile` / `No external profiles linked`.

**Avviso EN:** `The site renders content via JavaScript: some signals may exist but aren't readable in the initial HTML. The score is indicative.`
**N/D EN:** `not detected (possible JavaScript rendering)`
**Disclaimer EN:** `We measure on-page signals readable in the page code, not your real reputation or expertise. A high score doesn't guarantee a positive E-E-A-T judgement from Google.`
**Errore EN:** `We couldn't read the page. Check the address and try again in a few minutes.`

**Etichette campi EN:** score `On-page E-E-A-T score` · assi `Experience` / `Expertise` / `Authoritativeness` / `Trust` · righe `HTTPS connection` / `Verifiable contacts` / `Legal identity (VAT)` / `Privacy & cookie policy` / `About page` / `Portfolio / case studies` / `Structured data (JSON-LD)` / `External profiles`.

---

# PARTE 5 — CONTENUTO PAGINA RU (`/ru/instrumenty/signaly-eeat/`) — АВТОНОМНЫЙ

> RU пишется руками (носитель), НЕ через конвейер. Форма «вы» со строчной, числа
> вместо прилагательных, без кальки. Евро — «€ 3 900». Самодостаточный текст.

**hero_titolo (H1):** `Сигналы E-E-A-T: насколько сайт выглядит надёжным?`

**hero_sub:** `Разбираем восемь сигналов доверия, читаемых прямо в коде вашей главной страницы, — HTTPS, контакты, реквизиты, страница «о нас», микроразметка и другие — и раскладываем их по четырём осям E-E-A-T. Мы измеряем сигналы на странице, а не вашу реальную репутацию и экспертность. Без регистрации.`

**descrizione (подзаголовок карточки):** `Восемь сигналов доверия на странице, разложенных по четырём осям E-E-A-T.`

**come_funziona (как это работает, 3 шага):**
1. `('Введите адрес сайта', 'Мы читаем главную страницу с нашего сервера — так, как её увидит посетитель при первом заходе: анализируем HTML-код, ничего устанавливать не нужно.')`
2. `('Восемь автоматических проверок', 'Ищем на странице восемь сигналов доверия — HTTPS, контакты, реквизиты, privacy, страницу «о нас», портфолио, микроразметку, внешние профили — и группируем их по четырём осям E-E-A-T.')`
3. `('Оценка 0–100 и четыре оси', 'Общий балл и разбивка по осям: Опыт, Экспертность, Авторитетность и Надёжность — с цветом каждого сигнала и тем, чего не хватает.')`

**faq (3):**
1. `('Что такое E-E-A-T?', 'Это понятие из рекомендаций Google для асессоров качества (Search Quality Rater Guidelines): Experience, Expertise, Authoritativeness, Trust — опыт, экспертность, авторитетность и надёжность. Оно помогает Google оценить, насколько странице можно доверять, особенно в темах, которые влияют на здоровье, деньги и безопасность.')`
2. `('Влияет ли E-E-A-T на позиции?', 'Это не прямой фактор ранжирования и не балл, который выставляет Google: это рамка качества, по которой живые асессоры обучают алгоритмы. Усиление сигналов доверия помогает косвенно, но ни один инструмент — включая наш — не измеряет «настоящий» E-E-A-T вашего сайта.')`
3. `('Почему тест не видит мою репутацию?', 'Потому что мы читаем только код вашей страницы: мы можем проверить, что сигналы доверия есть и заявлены, но не то, кто вас цитирует, какие у вас отзывы и насколько вы действительно эксперт. Это оценивают люди и остальной веб, а не сканирование HTML.')`

**metodologia (metodo)** — h2: `Что на самом деле проверяет этот тест сигналов E-E-A-T`
1. `Как и в проверке GDPR и готовности к ИИ, главную страницу вашего сайта читает наш сервер — без обращения к Google. В HTML-коде мы ищем восемь сигналов доверия, по которым любой — поисковик, ИИ-модель, осторожный клиент — решает, стоит ли доверять: защищённое соединение (HTTPS), проверяемые контакты, юридические реквизиты (P.IVA/VAT и название компании), ссылки на privacy и cookie policy, страницу «о нас», портфолио или кейсы, микроразметку JSON-LD и внешние профили. Каждый сигнал попадает на одну из четырёх осей E-E-A-T — Опыт, Экспертность, Авторитетность, Надёжность — и влияет на общий балл.`
2. `И сразу о границе, честно: мы измеряем сигналы на странице, читаемые в коде, а не реальный E-E-A-T сайта. Мы не считаем ссылки и упоминания, не читаем отзывы и репутацию, не судим, эксперт вы или нет и правдив ли контент: это оценивают люди — асессоры Google и остальной веб, — а не разбор HTML. Мы смотрим только указанную главную страницу, а не весь сайт, и не видим того, что появляется лишь после выполнения JavaScript. Высокий балл значит, что сигналы доверия есть и читаются, а не то, что Google поставит вам положительную оценку E-E-A-T.`

**lettura (как читать результат)** — h2: `Как читать оценку E-E-A-T и четыре оси`
1. `Балл — от 0 до 100 и читается как четырёхуровневый светофор. От 90 и выше сигналы доверия почти все на месте и читаются без труда. От 75 до 89 — хорошая основа, осталось дополнить пару пунктов. От 50 до 74 не хватает нескольких важных сигналов: это самая частая зона для корпоративных сайтов, где занимаются контентом, но забывают о технической части. Ниже 50 страница показывает мало опор доверия — и это же тот случай, когда несколько добавлений быстро поднимают балл. Рядом с общим числом — четыре оси, чтобы видеть, с какой начать.`
2. `Две ошибки в чтении. Первая: красный сигнал — не вина, а возможность: «нет микроразметки» значит, что, добавив блок JSON-LD, вы получаете баллы за один вечер. Вторая, важнее: полные 100 не сертифицируют ваш E-E-A-T. Это значит, что вы хорошо заявили, кто вы, а не то, что веб считает вас авторитетом — такое доверие строится контентом, временем и репутацией, которые ни один инструмент не читает из HTML. А если балл кажется несправедливо низким, проверьте, не отдаёт ли сайт контент через JavaScript: тогда многие сигналы есть, но их нет в исходном коде, который мы читаем, — об этом мы предупреждаем отдельно.`

**migliorare (как улучшить)** — h2: `Как усилить сигналы E-E-A-T на сайте`
- intro: `Усилить доверие — не значит переписать сайт: это точные технические добавления, почти все быстрые и недорогие.`
- пункты:
  1. `('Сделайте настоящую страницу «о нас»', 'С именами, лицами, историей и реальными компетенциями команды, а не общим абзацем: это первое место, где Google и читатель хотят понять, кто стоит за сайтом.')`
  2. `('Сделайте контакты проверяемыми', 'Полный адрес, реальный телефон и почта — открыто, в подвале каждой страницы, а не только внутри формы: отслеживаемый контакт — базовый сигнал доверия.')`
  3. `('Укажите юридические реквизиты', 'Реквизиты компании (P.IVA/VAT, название, адрес) в подвале: для бизнеса в Европе это самое простое доказательство, что вы — реальное и досягаемое лицо.')`
  4. `('Добавьте микроразметку', 'Блок JSON-LD schema.org Organization (или LocalBusiness) с названием, логотипом, контактами и профилями «sameAs» прямо говорит поисковикам и ИИ, кто вы.')`
  5. `('Подписывайте и датируйте контент', 'Узнаваемый автор, дата публикации и обновления на статьях и страницах: они показывают реальный опыт и контент, за которым следят.')`
- links:
  - `('Настроим за вас: это часть технического SEO', '/ru/uslugi/tehnicheskoe-seo/')`
  - `('Страница «о нас», контакты и микроразметка — по умолчанию в сайте для рынка Италии и Европы', '/ru/uslugi/sajt-dlya-evropy/')`

**cta:**
- heading: `Хотите усилить доверие к сайту?`
- testo: `Страница «о нас», проверяемые контакты, реквизиты и микроразметка в порядке — это часть технического SEO и каждого сайта, который мы делаем под рынок Италии и Европы.`
- buttons:
  - `('Техническое SEO', '/ru/uslugi/tehnicheskoe-seo/', None)`
  - `('Сайт для Италии и Европы', '/ru/uslugi/sajt-dlya-evropy/', 'outline')`

**Виджет RU — подписи полей:** балл `Оценка E-E-A-T на странице` · оси `Опыт` / `Экспертность` / `Авторитетность` / `Надёжность` · строки `Соединение HTTPS` / `Проверяемые контакты` / `Юридические реквизиты` / `Privacy и cookie policy` / `Страница «о нас»` / `Портфолио / кейсы` / `Микроразметка (JSON-LD)` / `Внешние профили`.

**Виджет RU — общие вердикты (4 уровня):**
- good (≥90): `Отлично: сигналы доверия E-E-A-T есть и читаются в коде. Помните: это сигналы на странице, а не ваш реальный E-E-A-T.`
- buono (75–89): `Хорошая основа: большинство сигналов доверия на месте. Поправьте немногие жёлтые и красные пункты, чтобы закрыть картину.`
- mid (50–74): `На полпути: нескольких сигналов доверия не хватает или они не читаются. Список ниже показывает, с чего начать.`
- poor (<50): `Слабые сигналы: страница показывает мало проверяемых опор доверия — их же и проще всего добавить.`

**Этикетки сигналов RU (good / warn / bad):** HTTPS `Защищённое соединение (HTTPS)` / — / `Нет HTTPS: соединение незащищено` · Контакты `Проверяемые контакты есть` / `Только e-mail, без телефона и адреса` / `Проверяемых контактов нет` · Реквизиты `Реквизиты компании есть` / — / `Реквизитов компании нет` · Policy `Privacy и cookie policy есть` / `Есть только одна из двух политик` / `Нет privacy и cookie policy` · О нас `Страница «о нас» есть` / — / `Страницы «о нас» нет` · Портфолио `Портфолио или кейсы есть` / — / `Портфолио и кейсов нет` · Микроразметка `Микроразметка с реквизитами есть` / `JSON-LD есть, но только общий` / `Микроразметки JSON-LD нет` · Профили `Внешние профили привязаны` / `Только один внешний профиль` / `Внешних профилей нет`.

**Предупреждение RU (SPA):** `Сайт отдаёт контент через JavaScript: часть сигналов может существовать, но не читаться в исходном HTML. Балл ориентировочный.`
**N/D RU:** `не найдено (возможно, рендеринг через JavaScript)`
**Дисклеймер RU (статичный):** `Мы измеряем сигналы на странице, читаемые в её коде, а не вашу реальную репутацию и экспертность. Высокий балл не гарантирует положительной оценки E-E-A-T от Google.`
**Ошибка RU:** `Не удалось прочитать страницу. Проверьте адрес и попробуйте снова через несколько минут.`

---

# PARTE 6 — E-E-A-T DEL TESTO STESSO

- **Fonte del concetto (citare in pagina, in FAQ e/o metodologia):** *Google Search
  Quality Rater Guidelines* — è da lì che vengono Experience, Expertise,
  Authoritativeness, Trust. Il testo lo attribuisce esplicitamente («un concetto delle
  linee guida di Google per i valutatori della qualità»), senza spacciarlo per fattore
  di ranking: è la mossa di onestà che dà autorevolezza al nostro stesso testo.
- **Trasparenza P.IVA nostra:** coerente con `trust-strip.php`/`faq.php`, ribadiamo
  «S.r.l. italiana con P.IVA verificabile» — pratichiamo ciò che il tool misura. NON
  inserire un numero di P.IVA finché il proprietario non fornisce quello reale.
- **Onestà nei verdetti:** ogni fascia e il disclaimer ripetono che misuriamo segnali
  on-page, non l'E-E-A-T reale — la stessa linea «diciamo cosa NON guarda» degli altri
  strumenti (speed/gdpr/ai).

---

# PARTE 7 — PERELINKOVKA (interna)

- **Footer menu «Strumenti/Tools/Инструменты»:** già esistente (T3). Aggiungere la
  voce all'8° strumento non serve nel menu principale (regola 5+CTA); la card entra
  nell'indice `/strumenti/` e nel blocco «Gli altri strumenti gratuiti».
- **Indice `/strumenti/` (+ EN/RU):** aggiungere la card «Segnali E-E-A-T» → ora 8 card.
- **Blocco «Gli altri strumenti gratuiti»** su ogni pagina strumento: passa da 6 a 7
  vicini (il generatore lo costruisce da `TOOLS`, si aggiorna da solo aggiungendo la voce).
- **Vicini reciproci (link bidirezionali consigliati):**
  - `sito-pronto-ai` ↔ `segnali-eeat` — condividono il tema dati strutturati JSON-LD.
    Il CTA `outline` di E-E-A-T punta già a `sito-pronto-ai`; aggiungere in
    `sito-pronto-ai` un rimando a E-E-A-T (es. nel `migliorare` o come CTA outline).
  - `analisi-seo` ↔ `segnali-eeat` — la SEO on-page e i segnali di fiducia sono
    complementari; un rimando reciproco nei testi `migliorare` è coerente.
- **Servizi citati nei testi `migliorare`/CTA (uso appropriato):**
  - `seo-tecnica` — è il servizio che «sistema» dati strutturati, JSON-LD, chi siamo,
    contatti (primo link migliorare + CTA principale). IT `/servizi/seo-tecnica/` ·
    EN `/en/services/technical-seo/` · RU `/ru/uslugi/tehnicheskoe-seo/`.
  - `siti-aziendali` — chi siamo, contatti, identità legale e dati strutturati «di
    serie». IT `/servizi/siti-aziendali/` · EN `/en/services/business-websites/` ·
    RU: usare il landing `/ru/uslugi/sajt-dlya-evropy/` (in RU non c'è pagina servizio
    «siti aziendali» a sé — la voce corrispondente è `korporativnye-sajty`; per la
    voronka RU è più naturale il landing «sajt-dlya-evropy»).
- **Contestuale dai servizi verso lo strumento (facoltativo, coerente con §2.5 del
  piano):** una riga-link da `seo-tecnica` → `segnali-eeat` (IT/EN/RU) rafforza il
  tema fiducia/dati strutturati. Decisione del proprietario se aggiungerla ora.

---

# PARTE 8 — PER L'IMPLEMENTATORE (checklist)

**Dati / build**
- [ ] `wordpress/build-tools/data.py` → nuova voce `TOOLS` (dopo `impatto-co2`):
      `tipo='eeat'`, `idx='/08'`, `slug='segnali-eeat'`, `has_demo=False`, con tutti i
      campi di §3 (hero_titolo, hero_sub, descrizione, come_funziona×3, faq×3,
      metodologia, lettura, migliorare, cta). Attenzione agli apostrofi tipografici
      `'` come nelle voci esistenti.
- [ ] `wordpress/build-tools/lang.py` → `TOOLS_SLUGS`:
      `'segnali-eeat': {'en':'eeat-signals','ru':'signaly-eeat'}`.
- [ ] Rigenerare `inc/lang-map.php` con `emit_php_lang_map` (o eseguendo `lang.py` come
      `__main__`). Verificare diff: **solo +1 riga** (terna strumenti).
- [ ] Rigenerazione **puntuale** delle sole pagine: `strumento-segnali-eeat` (IT), la
      card in `strumenti-index`, e il blocco vicini negli altri 7 strumenti. `main()`
      vietato (grabli chi-siamo/citta).

**JS (`assets/js/remarka.js`)**
- [ ] Nuovo modulo `initEeatTool(root)` sul modello di `initGdprTool`/`initAiTool`:
      un solo `toolFetch(url,'html')`; riusare il parser JSON-LD già presente in
      `initAiTool`; regex dei segnali come in §1.1; `setFlag`/`setText` come i moduli
      esistenti; calcolo punteggio+assi come §1.2; verdetto a 4 livelli da `data-verdict-*`.
- [ ] Dispatcher `initToolWidgets()`: aggiungere `case 'eeat': initEeatTool(root); break;`.
- [ ] HTTPS: leggere lo schema dell'URL normalizzato / dell'eventuale URL finale della
      risposta (`data.status`/redirect già gestiti server-side). Verificare che
      `remarka_tool_fetch` esponga l'URL finale; altrimenti usare lo schema dell'input
      normalizzato (`normalizeUrl` forza già `https://` di default → in tal caso HTTPS
      va valutato sul valore digitato dall'utente, con nota all'implementatore).
- [ ] Avviso SPA: heuristica su lunghezza del testo/`<body>` e marker `id="root"|"app"`.

**Pagine / deploy**
- [ ] `patterns/pages/strumento-segnali-eeat.php` (IT, dal generatore) con markup
      widget `data-sr-tool="eeat"` e tutte le stringhe `data-*` di §3-bis.
- [ ] EN: coppie CHROME (`en` only) di tutte le stringhe nuove in `chrome_strings.py`
      → `translate_pages.py en` → exit 0, diff solo `en-strumento-eeat-signals.php` (+
      card index EN + vicini EN). Testi di riferimento in §4.
- [ ] RU **a mano** (conveyor RU vietato): `patterns/pages/ru-strumento-signaly-eeat.php`
      con i testi di §5 + card in `ru-strumenti-index` + blocco vicini nei 7 ru-strumento-*.
- [ ] `deploy-import.php` → `$page_map` +3 righe:
      `'strumento-segnali-eeat' => ['segnali-eeat','strumenti',null]` (IT),
      `'en-strumento-eeat-signals' => ['eeat-signals','en/tools',null]` (EN),
      `'ru-strumento-signaly-eeat' => ['signaly-eeat','ru/instrumenty',null]` (RU).
      Verificare i nomi-chiave contro le convenzioni già usate per gli altri strumenti.
- [ ] `$current_slugs` (orphan-sweep) in `deploy-import.php`: aggiungere i 3 nuovi slug.
- [ ] Footer «Pagine»: la voce Strumenti/Tools/Инструменты esiste già — nessuna azione.

**Docs**
- [ ] `docs/seo-meta.md`: aggiungere le righe Title/Description/Focus di §2.2 per i 3
      slug (sezione «Инструменты (Lab)»), con verifica lunghezze.
- [ ] `docs/piano-strumenti-lab.md`: aggiornare §0 (7 → 8 strumenti) e tabella stato.

**QA**
- [ ] `php -l` su ogni file toccato; parse-check JS (`new Function`); test-harness stub
      del modulo `eeat` (fixture HTML: sito «buono» ~90+, sito «SPA» → avviso, sito
      «nudo» ~<30) come i 5 node-test PSI esistenti.
- [ ] Screenshot risultato IT/EN/RU (1440/800/390).
- [ ] Link-audit: la card E-E-A-T presente in index + home-cards (se si estende) +
      blocco vicini dei 7, su 3 lingue; hreflang: la terna dà 3 lingue.

---

## Riepilogo modello (per il rapporto)

**8 segnali → 4 assi → 100 punti:**
Affidabilità 42 (HTTPS 8 · Contatti 12 · Identità legale 12 · Privacy/cookie 10) ·
Esperienza 22 (Chi siamo 12 · Portfolio/casi 10) · Competenza 20 (Dati strutturati
JSON-LD 20) · Autorevolezza 16 (Profili esterni/sameAs 16).
warn = metà peso; binari solo good/bad. Soglie verdetto **90/75/50** (4 livelli).
N/D solo su SPA/HTML scarno (avviso + annotazione). Motore: un `toolFetch('html')`.
