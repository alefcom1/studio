# Check-up completo del sito — modello di scoring + copy deck (M1)

> Data: 14.07.2026 · Etapa **M1** del piano `docs/piano-checkup-sito.md`.
> Base: decisione del titolare (un test unico in home, risultati ampi gratis a
> schermo, report più completo in PDF via e-mail, livello premium visibile dai
> primi blocchi). Regole trasversali: `docs/piano-implementazione-fase-A.md` §0
> (commit atomici in inglese senza ID modelli, protocollo di verifica, tono:
> numeri al posto degli aggettivi, «voi», disclaimer onesti). Motori dei 7
> strumenti: `docs/piano-strumenti-lab.md` §0–§1 (GDPR = euristica senza
> browser headless; AI = 4 segnali; CO₂ = modello SWD dai byte del PSI).
>
> **Onestà delle promesse (vincolante):** non promettiamo mai un «audit legale
> GDPR completo» (è una verifica indicativa a 4 segnali) né posizioni su Google.
> Ogni misura dichiara il proprio motore e i propri limiti.
>
> Questo documento è la fonte unica per **M2** (orchestratore + schermata
> risultati + pagina + blocco home IT) e **M3** (endpoint report + PDF + form
> e-mail). RU è testo autonomo, non traduzione dell'italiano.

---

## PARTE 1 — Modello di scoring «Salute del sito» (0–100)

### 1.1. Pesi delle 7 dimensioni

| # | Dimensione | Motore / fonte | Peso | Natura |
|---|---|---|---|---|
| 1 | Prestazioni (performance) | PSI/Lighthouse `performance` | **25** | Google, reale |
| 2 | SEO | PSI/Lighthouse `seo` | **20** | Google, reale |
| 3 | Accessibilità | PSI/Lighthouse `accessibility` | **15** | Google, reale |
| 4 | Privacy e cookie (GDPR) | euristica `remarka_tool_fetch` (4 segnali) | **15** | nostra, indicativa |
| 5 | Best practice | PSI/Lighthouse `best-practices` | **10** | Google, reale |
| 6 | Pronto per l'AI | fetch llms.txt / robots / JSON-LD / sitemap | **10** | nostra, 4 segnali |
| 7 | Impatto CO₂ | modello SWD sui byte del PSI | **5** | derivata dal PSI |
| | **Totale** | | **100** | |

**Razionale dei pesi.** I segnali verificati da Google pesano per il 70 %
(prestazioni + SEO + accessibilità + best practice): sono misurabili, ripetibili
e cross-verificabili su pagespeed.web.dev, quindi reggono il punteggio. Le
prestazioni restano la voce dominante (25) perché determinano abbandono e resa
delle campagne; la SEO tecnica on-page vale 20 perché è la seconda leva di
business più diretta. Il GDPR pesa 15 — quanto l'accessibilità — non perché la
nostra sia una misura «forte» (è un'euristica a 4 segnali), ma perché per una
PMI italiana/UE il rischio legale è esistenziale: un semaforo rosso qui vale più
di due punti di PageSpeed. AI-readiness (10) e impatto CO₂ (5) sono i
differenziali che rendono il check-up «premium e in anticipo sui tempi» senza
gonfiare il voto: insieme pesano 15, abbastanza da spostare l'ago ma non da
falsare la fotografia. **M2 deve estendere `psiFetch` alla 4ª categoria**
`BEST_PRACTICES` (oggi ne chiede 3) e restituire `scores.bp`.

### 1.2. Normalizzazione delle dimensioni non-Google su 0–100

Le 4 categorie Lighthouse arrivano già in scala 0–100: si usano tal quali.
Le 3 dimensioni non-Google vanno normalizzate.

**GDPR (euristica 4 segnali → 0–100).** Ogni segnale ha un flag `good|warn|bad`
prodotto dal modulo JS (vedi `remarka.js` `initGdprTool`). Punti per flag:
`good = 1,0 · warn = 0,5 · bad = 0,0`, moltiplicati per il peso del segnale:

| Segnale | Peso interno | good | warn | bad |
|---|---|---|---|---|
| Cookie banner / CMP rilevata | 35 | banner presente | — | assente |
| Tracker prima del consenso | 30 | nessun tracker | tracker **con** banner | tracker **senza** banner |
| Link a privacy/cookie policy | 20 | presente | — | assente |
| Domini esterni che caricano script | 15 | 0 domini | ≤ 5 domini | > 5 domini |

`GDPR = 35·f(cmp) + 30·f(tracker) + 20·f(policy) + 15·f(esterni)` → 0–100.
Il peso maggiore al CMP e ai tracker riflette ciò che il Garante sanziona più
spesso. **Resta una verifica indicativa, non un parere legale** (disclaimer
obbligatorio a schermo e nel PDF).

**AI-readiness (4 segnali → 0–100).** Segnali: llms.txt valido · crawler AI non
bloccati in robots.txt · JSON-LD presente · sitemap.xml valida. Pesi interni
non uniformi, per non affossare il voto di un sito solo perché privo di un file
molto recente:

| Segnale | Peso interno |
|---|---|
| Dati strutturati JSON-LD | 30 |
| Sitemap.xml valida | 25 |
| Crawler AI non bloccati (robots) | 25 |
| llms.txt valido | 20 |

`AI = Σ pesi dei segnali positivi` → 0–100. A schermo mostriamo **sia** il
punteggio normalizzato **sia** il conteggio grezzo «N segnali su 4», per
trasparenza (llms.txt è uno standard emergente: la sua assenza non è un guasto).

**CO₂ (grammi/visita → 0–100).** Più leggero è meglio. Ancoriamo alla media del
web (0,8 g/visita, la stessa del modulo `co2`) con una rampa lineare:

`CO₂score = clamp( round( 100 · (1,6 − g) / 1,2 ), 0, 100 )`

cioè: **≤ 0,4 g → 100** (metà della media, eccellente) · **0,8 g → 67** (media) ·
**≥ 1,6 g → 0** (doppio della media, pesante). Sotto 0,4 g si satura a 100, sopra
1,6 g si azzera. La rampa è dichiarata come stima del modello Sustainable Web
Design, non una misura di laboratorio.

### 1.3. Calcolo del punteggio composito

`Salute = Σ (peso_i · score_i) / Σ (peso_i)` sulle sole dimensioni **disponibili**
(vedi degrado, 1.5). Con tutte e 7 attive il denominatore è 100.

### 1.4. Soglie dei semafori (verdetti a 4 livelli)

Valgono **identiche** per ogni dimensione (0–100) e per il composito. Tre colori
di pallino (riuso di `[data-sr-flag]` esistente: `good`/`warn`/`bad` =
verde/ambra/rosso), quattro etichette di verdetto:

| Punteggio | Verdetto | Pallino |
|---|---|---|
| 90–100 | **Eccellente** | 🟢 `good` |
| 75–89 | **Buono** | 🟢 `good` |
| 50–74 | **Da migliorare** | 🟡 `warn` |
| 0–49 | **Critico** | 🔴 `bad` |

Il pallino è verde già da 75 (soglia «premium», più severa del semplice
sufficiente); il rosso sotto 50 resta allineato alla soglia «poor» di Lighthouse,
così chi verifica su pagespeed.web.dev ritrova gli stessi colori. La parola del
verdetto distingue *eccellente* da *buono* dentro il verde.

**Etichetta del composito** (stesse soglie, testo dedicato):

| Salute | Etichetta composito |
|---|---|
| 90–100 | Sito in salute eccellente |
| 75–89 | Sito in buona salute |
| 50–74 | Sito da migliorare |
| 0–49 | Sito a rischio |

*(Nota UX: se in M2 si vorrà una 4ª tinta per la fascia «Buono», introdurre
`[data-sr-flag="ok"]` verde-lime — vedi §Nuove classi CSS. Non obbligatoria: i
mock M1 funzionano con i 3 colori esistenti.)*

### 1.5. Regola di degrado (una misura non risponde)

Se una dimensione non completa (timeout PSI, il sito blocca il nostro fetch,
quota esaurita) ritorna `null`:

1. Il **composito si calcola sulle sole dimensioni disponibili**, rinormalizzando
   i pesi: `Salute = Σ(peso·score disponibili) / Σ(peso disponibili)`.
2. La dimensione mancante mostra **«N/D»** con pallino neutro (grigio: è già il
   default di `[data-sr-flag]` senza valore) e una riga onesta («Non siamo
   riusciti a misurare questo aspetto: il sito ha rifiutato la lettura / il
   servizio Google era saturo»). **Non conta come 0** e non affossa il voto.
3. Sotto il composito compare la nota «Calcolato su **N misurazioni su 7**».
4. **Guardia di validità:** il composito si mostra solo se sono disponibili
   **almeno 4 dimensioni su 7 E almeno una fra Prestazioni e SEO** (le due voci
   Google più pesanti). Altrimenti niente numero: schermata «Check-up incompleto
   — riprovate tra qualche minuto», con il dettaglio delle misure riuscite già
   visibile e il pulsante «Riprova».
5. Nel PDF la pagina della dimensione N/D resta, con la spiegazione del perché e
   l'invito a rilanciare il test; il badge del composito riporta «su N di 7».

---

## PARTE 2 — Copy deck ITALIANO

> Tono: sobrio, premium, numeri concreti, «voi». Nessun punto esclamativo nei
> titoli. Segnali E-E-A-T espliciti: chi misura (Studio Remarka, parte del
> gruppo Remarka, nel settore linguistico e digitale dal 2001), con quali motori
> (Google PageSpeed Insights/Lighthouse, modello Sustainable Web Design), con
> quali limiti dichiarati.

### 2.1. Blocco HOME (subito dopo l'hero — l'hero **non si tocca**)

| Elemento | Testo IT |
|---|---|
| Eyebrow (mono) | Check-up completo · gratuito |
| H2 | Lo stato di salute del vostro sito, in un numero<span class="sr-accent-dot">.</span> |
| Sottotitolo | Un test unico raccoglie sette analisi — velocità, SEO, accessibilità, privacy, best practice, prontezza AI e impatto ambientale — e restituisce un punteggio da 0 a 100 con i problemi da risolvere per primi. Motore Google PageSpeed e nostre verifiche, spiegati in italiano. |
| Placeholder campo URL | www.ilvostrosito.it |
| Bottone | Analizza il sito — gratis |
| Riga di fiducia (mono) | 7 test in uno · gratis · senza registrazione |
| Micro-etichette misure (mono, sotto la riga) | Velocità · SEO · Accessibilità · Privacy · Best practice · AI · CO₂ |
| Nota E-E-A-T (small, sotto il form) | Lo fa Studio Remarka, nel settore linguistico e digitale dal 2001. Dati reali dall'API di Google, nessun numero simulato. |

Il submit porta a `/strumenti/check-up-completo/?url=…&autostart=1`.

### 2.2. Pagina `/strumenti/check-up-completo/`

**SEO (per M2 → Rank Math; cfr. `docs/seo-meta.md`)**

- **Focus keyword:** `check up sito web`
- **Title (≤60):** `Check-up completo del sito web, gratis | Studio Remarka` (54)
- **Description (≤160):** `Un solo test: velocità, SEO, accessibilità, privacy, best practice, AI e CO₂. Punteggio di salute 0–100 e report PDF completo. Gratis, senza registrazione.` (157)
- **H1:** `Il check-up completo del vostro sito web`
- **Varianti chiave negli H2:** «analisi completa del sito», «check up del sito web», «stato di salute del sito».

**Intro (sotto l'H1)**
> Sette strumenti gratuiti in una sola analisi. Incollate l'indirizzo: in meno
> di un minuto vedete un punteggio di salute da 0 a 100, i sette semafori che lo
> compongono e i tre interventi più urgenti. La misura è quella vera di Google
> PageSpeed Insights, affiancata dalle nostre verifiche su privacy e prontezza
> AI. Il report completo, pagina per pagina, ve lo inviamo in PDF.

**Come funziona — 3 passi** *(riuso griglia `.sr-step`)*

1. **Incollate l'indirizzo** — La home o la pagina che porta più visite. Nessuna registrazione, nessun dato di pagamento.
2. **Analizziamo su sette fronti** — Un'unica interrogazione all'API Google PageSpeed (prestazioni, SEO, accessibilità, best practice) più le nostre verifiche su privacy/cookie e prontezza AI, letti dal nostro server come farebbe un visitatore.
3. **Leggete il punteggio e le priorità** — Salute 0–100, i sette semafori spiegati in italiano e i tre interventi che pesano di più. Il report completo arriva in PDF.

**Sezione «Il metodo»** *(eyebrow «Il metodo», tono dei testi L1 in `data.py`)*
> H2: **Che cosa misura davvero il check-up completo**
>
> Dietro il punteggio non c'è una scatola nera. Quattro delle sette dimensioni —
> prestazioni, SEO, accessibilità e best practice — arrivano dall'API PageSpeed
> Insights di Google, la stessa che alimenta pagespeed.web.dev: interroghiamo
> Lighthouse in strategia mobile, perché è la versione del sito che Google usa
> per posizionarvi. Le altre tre le calcoliamo noi: la conformità privacy la
> leggiamo dall'HTML della pagina (banner, informative, tracker prima del
> consenso), la prontezza AI da quattro segnali tecnici — llms.txt, accesso ai
> crawler, dati strutturati, sitemap — e l'impronta di CO₂ dal peso reale della
> pagina, con il modello Sustainable Web Design.
>
> Ogni dimensione entra nel voto con un peso dichiarato: le prestazioni valgono
> di più (25 su 100), la CO₂ di meno (5). È giusto sapere anche cosa il check-up
> non fa: non è un parere legale sulla privacy — è una verifica indicativa a
> quattro segnali — e non promette una posizione su Google. È la fotografia
> tecnica precisa del vostro sito, non una promessa di vendita.

**Sezione «Come leggere»** *(eyebrow «Come leggere il punteggio»)*
> H2: **Come si legge lo stato di salute del sito**
>
> Il punteggio di salute è la media pesata dei sette semafori, non un voto a
> sensazione. Si legge come un semaforo: da 90 in su siete in fascia verde
> (eccellente), da 75 a 89 è buono, tra 50 e 74 c'è margine concreto, sotto 50 è
> critico e diventa la priorità. Ogni dimensione porta lo stesso codice colore,
> così capite in un colpo d'occhio dove il sito è solido e dove perde punti.
>
> Due letture da evitare. Un voto alto non significa «primi su Google»: significa
> che le fondamenta tecniche sono sane. E se una misura risulta «N/D» non è un
> guasto del vostro sito: a volte Google è saturo, a volte il sito rifiuta la
> lettura automatica. In quel caso calcoliamo la salute sulle misure riuscite e
> ve lo diciamo con chiarezza.

**FAQ (3)** *(riuso `details_faq`)*

1. **Il punteggio è quello vero di Google?**
   Per prestazioni, SEO, accessibilità e best practice sì: arrivano dall'API
   ufficiale PageSpeed Insights, strategia mobile. Privacy, prontezza AI e CO₂
   sono nostre verifiche, con il metodo dichiarato in ogni sezione.
2. **Il check-up GDPR sostituisce un consulente privacy?**
   No. È una verifica tecnica indicativa a quattro segnali: intercetta i problemi
   evidenti — banner assente, tracker prima del consenso — ma non è un parere
   legale e non sostituisce un consulente.
3. **Cosa ricevo nel report PDF che non vedo già a schermo?**
   A schermo vedete il punteggio, i sette semafori e le tre priorità. Nel PDF
   trovate una pagina per dimensione con tutte le criticità rilevate, le
   raccomandazioni operative in ordine di impatto e cosa faremmo noi, con i nostri
   riferimenti aziendali.

**CTA finale** *(sezione `sr-dark`)*
> H2: **Vogliamo sistemare noi le priorità?**
> Testo: Dal punteggio al preventivo: analizziamo il report insieme e vi diamo un
> piano d'intervento a prezzo chiuso, con PageSpeed 90+ garantito da contratto.
> Bottoni: `Richiedi la consulenza — gratis` → `/#contatti` · `Vedi tutti gli strumenti` → `/strumenti/` (outline)

### 2.3. Schermata dei RISULTATI

**Titolo del punteggio composito**
- Occhiello (mono): `Salute del sito`
- Numero grande: `68` `/100`
- Etichetta (dal composito): `Sito da migliorare`
- Riga URL (mono, small): `ilvostrosito.it — analisi mobile · 14.07.2026`
- Nota metodo (small): `Media pesata di 7 misure. Prestazioni, SEO, accessibilità e best practice da Google PageSpeed; privacy, AI e CO₂ da verifiche Studio Remarka.`

**Etichette delle 7 dimensioni** (occhiello di ogni card)

| # | Etichetta IT | Sotto-riga (peso) |
|---|---|---|
| 1 | Prestazioni | Peso 25 · Google PageSpeed |
| 2 | SEO | Peso 20 · Google PageSpeed |
| 3 | Accessibilità | Peso 15 · WCAG 2.1 / EAA |
| 4 | Privacy e cookie | Peso 15 · verifica indicativa |
| 5 | Best practice | Peso 10 · Google PageSpeed |
| 6 | Pronto per l'AI | Peso 10 · 4 segnali |
| 7 | Impatto CO₂ | Peso 5 · modello SWD |

**Formulazioni dei verdetti per dimensione** (una frase per livello)

- **Prestazioni**
  - Eccellente: «Il sito è rapido su mobile: rispetta gli standard Google.»
  - Buono: «Velocità buona; restano margini misurabili su qualche pagina.»
  - Da migliorare: «Nella media del web, ma lontano dagli standard consigliati.»
  - Critico: «Il sito è lento su mobile: gran parte dei visitatori abbandona prima del caricamento.»
- **SEO**
  - Eccellente: «Basi tecniche on-page in ordine: nessun ostacolo all'indicizzazione.»
  - Buono: «Struttura solida; poche correzioni per completare le basi.»
  - Da migliorare: «Alcuni elementi on-page mancano o sono duplicati.»
  - Critico: «Qualcosa ostacola l'indicizzazione: da sistemare prima di tutto.»
- **Accessibilità**
  - Eccellente: «Poche o nessuna barriera: sito fruibile secondo WCAG 2.1 AA.»
  - Buono: «Buon livello; restano barriere minori da rimuovere.»
  - Da migliorare: «Diverse barriere rilevate: contrasti, etichette, navigazione.»
  - Critico: «Barriere gravi: il sito è difficile da usare per molte persone (obbligo EAA).»
- **Privacy e cookie**
  - Eccellente: «Banner, informative e tracker in ordine nell'HTML iniziale.»
  - Buono: «Impianto presente; un paio di punti da verificare a mano.»
  - Da migliorare: «Mancano elementi o alcuni tracker vanno governati meglio.»
  - Critico: «Tracker attivi senza banner o policy assenti: rischio concreto col Garante.»
- **Best practice**
  - Eccellente: «Sito tecnicamente pulito: HTTPS, console senza errori, librerie aggiornate.»
  - Buono: «Buon livello tecnico; qualche avviso da chiudere.»
  - Da migliorare: «Diversi avvisi tecnici: sicurezza, errori console, immagini.»
  - Critico: «Problemi tecnici diffusi che indeboliscono affidabilità e sicurezza.»
- **Pronto per l'AI**
  - Eccellente: «4 segnali su 4: il sito è leggibile e citabile dai modelli AI.»
  - Buono: «3 segnali su 4: manca poco alla piena prontezza AI.»
  - Da migliorare: «2 segnali su 4: dati strutturati o sitemap da completare.»
  - Critico: «0–1 segnali: i modelli AI faticano a leggere e citare il sito.»
- **Impatto CO₂**
  - Eccellente: «Pagina leggera: emissioni sotto la media del web.»
  - Buono: «Vicino alla media; c'è margine per alleggerire.»
  - Da migliorare: «Sopra la media: la pagina è pesante da caricare.»
  - Critico: «Molto sopra la media: pagina pesante, costo ambientale e di velocità.»

**Blocco «I 3 interventi più urgenti»**
- Occhiello: `Le priorità`
- H3: `I 3 interventi che pesano di più`
- Intro: `Ordinati per impatto sul punteggio: quanto guadagnereste sistemandoli.`
- Voci demo (punteggio 68):
  1. **Prestazioni · Critico** — «Il sito è lento su mobile. È l'intervento con il maggior peso sul voto: alleggerire immagini e attivare la cache è il primo passo.»
  2. **Privacy e cookie · Critico** — «Rilevati tracker prima del consenso. A norma del Garante vanno caricati solo dopo il sì: rischio legale, non solo tecnico.»
  3. **Pronto per l'AI · Da migliorare** — «Mancano dati strutturati e sitemap completa: due segnali che rendono il sito leggibile ai modelli AI.»

**Form e-mail — «Il report completo, in PDF»**
- H3: `Il report completo, in PDF`
- Testo: `Vi inviamo l'analisi integrale: una pagina per ognuna delle sette dimensioni, tutte le criticità rilevate e le raccomandazioni in ordine di impatto.`
- Cosa contiene il PDF (elenco):
  - Il punteggio di salute con i sette semafori
  - Una pagina per dimensione: punteggio, cosa abbiamo trovato, cosa fare
  - I tre interventi prioritari con le contromisure
  - «Cosa faremmo noi» e i riferimenti di Studio Remarka
- Placeholder campo e-mail: `nome@vostraazienda.it`
- Checkbox consenso (obbligatorio): `Ho letto la privacy policy e acconsento all'invio del report e a essere ricontattato.` (link «privacy policy» → `/privacy/`)
- Checkbox facoltativo (monitoraggio futuro): `Inviatemi ogni mese il monitoraggio dei Core Web Vitals di questo sito.`
- Bottone: `Inviatemi il report PDF`
- Messaggio di successo: `Fatto. Il report è in viaggio verso la vostra casella: se non arriva entro qualche minuto, controllate lo spam o scriveteci.`
- Messaggio di errore: `Non siamo riusciti a inviare il report. Riprovate tra poco o scriveteci: ve lo mandiamo a mano.`
- Nota (small): `Niente spam. Usiamo l'indirizzo solo per inviarvi il report ed eventualmente ricontattarvi. Studio Remarka S.r.l., P.IVA GE 302230994.`

### 2.4. E-mail di consegna del PDF

- **Oggetto:** `Il check-up completo di {dominio} — report in PDF`
- **Corpo:**
> Buongiorno,
>
> in allegato trovate il report completo del check-up di **{dominio}**: punteggio
> di salute {punteggio}/100, i sette semafori e le raccomandazioni in ordine di
> impatto.
>
> Le prestazioni, la SEO, l'accessibilità e le best practice sono misurate con
> l'API Google PageSpeed Insights; privacy, prontezza AI e impatto CO₂ con le
> nostre verifiche, tutte con i limiti dichiarati nel report.
>
> Se volete, guardiamo insieme le priorità e vi diamo un piano d'intervento a
> prezzo chiuso — la consulenza è gratuita.
>
> [**Richiedi la consulenza gratuita →**]
>
> Studio Remarka — nel settore linguistico e digitale dal 2001
> info@remarka.biz · +39 347 83 11141

### 2.5. Struttura del PDF (pagina per pagina)

Testi statici in italiano; i valori fra `{…}` sono dinamici (M3).

1. **Copertina** — logo Studio Remarka · `Check-up completo del sito` · dominio
   `{dominio}` · data `{data}` · badge grande `Salute {punteggio}/100 —
   {etichetta}` · riga «su {N} misurazioni di 7» se in degrado.
2. **Riepilogo** — H1 «Lo stato di salute in un colpo d'occhio» · i 7 semafori in
   tabella (dimensione · peso · punteggio · verdetto · pallino) · frase di sintesi
   `{sintesi}`.
3–9. **Una pagina per dimensione** (nell'ordine dei pesi) — titolo dimensione ·
   `{punteggio}/100` + verdetto · «Cosa abbiamo trovato»: `{criticità}` · «Cosa
   fare»: 3 raccomandazioni `{consigli}` · riga-metodo statica (es. Prestazioni:
   «Misura: Google PageSpeed Insights, Lighthouse mobile»; GDPR: «Verifica
   indicativa Studio Remarka su 4 segnali — non è un parere legale»; CO₂: «Stima
   con il modello Sustainable Web Design»).
10. **I 3 interventi prioritari** — H1 «Da dove partire» · le 3 voci con impatto e
    contromisura `{priorità}`.
11. **Cosa faremmo noi** — H1 «Cosa faremmo noi, e con quali garanzie» · testo:
    «Trasformiamo questo report in un piano a prezzo chiuso: consegna a data
    fissa con penale, PageSpeed 90+ garantito, 12 mesi di assistenza. Prima di
    ogni intervento, un preventivo chiuso in 24 ore.» · CTA «Richiedi la
    consulenza gratuita».
12. **Chi ha preparato questo report** *(E-E-A-T)* — «Studio Remarka S.r.l., parte
    del gruppo Remarka, nel settore linguistico e digitale dal 2001. Siti
    aziendali, e-commerce e localizzazione con redattori madrelingua.» · Sedi:
    Milano, Vicolo Privato Lavandai 2a · Torino, Corso Regina Margherita 94 ·
    Roma, Via Flaminia 122 · P.IVA GE 302230994 · info@remarka.biz · +39 347 83
    11141. **Nota metodologica:** motori usati (Google PageSpeed Insights /
    Lighthouse; modello Sustainable Web Design; verifiche proprietarie su privacy
    e AI) e limiti (il GDPR è indicativo, non un parere legale; nessuna promessa
    di posizione su Google; l'accessibilità segue lo standard WCAG 2.1 AA
    richiesto dall'European Accessibility Act).

---

## PARTE 3 — Copy deck ENGLISH

> Native-level EN, «you» form, US number format where numbers occur. Same E-E-A-T
> signals: Studio Remarka, part of the Remarka group, in language and digital
> services since 2001; Google PageSpeed Insights/Lighthouse + Sustainable Web
> Design model + our own checks with stated limits.

### 3.1. HOME block (right after the hero — hero untouched)

| Element | EN |
|---|---|
| Eyebrow (mono) | Full check-up · free |
| H2 | Your website's health, in a single number<span class="sr-accent-dot">.</span> |
| Subtitle | One test runs seven analyses — speed, SEO, accessibility, privacy, best practices, AI-readiness and environmental impact — and returns a 0–100 health score with the issues to fix first. Google PageSpeed engine plus our own checks, in plain English. |
| URL placeholder | www.yoursite.com |
| Button | Analyse the site — free |
| Trust row (mono) | 7 tests in one · free · no sign-up |
| Micro-labels (mono) | Speed · SEO · Accessibility · Privacy · Best practices · AI · CO₂ |
| E-E-A-T note (small) | Run by Studio Remarka, in language and digital services since 2001. Real data from Google's API — never simulated numbers. |

### 3.2. Page `/en/tools/full-site-checkup/`

- **Focus keyword:** `website check up`
- **Title (≤60):** `Full website check-up, free — 7 tests in one | Studio Remarka` (59)
- **Description (≤160):** `One test: speed, SEO, accessibility, privacy, best practices, AI and CO₂. A 0–100 health score and a full PDF report. Free, no sign-up required.` (146)
- **H1:** `The complete check-up for your website`
- **H2 key variants:** «complete website analysis», «website check up», «site health score».

**Intro**
> Seven free tools in a single analysis. Paste your address: in under a minute you
> get a 0–100 health score, the seven traffic lights behind it and the three most
> urgent fixes. The measurement is the real one from Google PageSpeed Insights,
> alongside our own privacy and AI-readiness checks. The full report, page by
> page, we send you as a PDF.

**How it works — 3 steps**
1. **Paste your address** — Your home page or the page that brings the most traffic. No sign-up, no payment details.
2. **We analyse on seven fronts** — A single Google PageSpeed API call (performance, SEO, accessibility, best practices) plus our own privacy/cookie and AI-readiness checks, read from our server the way a visitor would see the page.
3. **Read the score and priorities** — Health 0–100, the seven traffic lights in plain English and the three fixes that matter most. The full report follows as a PDF.

**«The method»**
> H2: **What the full check-up actually measures**
>
> There's no black box behind the score. Four of the seven dimensions —
> performance, SEO, accessibility and best practices — come from Google's
> PageSpeed Insights API, the same engine behind pagespeed.web.dev: we query
> Lighthouse in mobile strategy, because that's the version Google uses to rank
> you. The other three we compute ourselves: privacy compliance we read from the
> page's HTML (banner, policies, trackers before consent), AI-readiness from four
> technical signals — llms.txt, crawler access, structured data, sitemap — and the
> CO₂ footprint from the page's real weight, using the Sustainable Web Design
> model.
>
> Each dimension enters the score with a stated weight: performance counts most
> (25 of 100), CO₂ least (5). It's fair to know what the check-up does not do:
> it's not a legal opinion on privacy — it's an indicative, four-signal check —
> and it never promises a Google ranking. It's a precise technical snapshot of
> your site, not a sales promise.

**«How to read it»**
> H2: **How to read your site's health score**
>
> The health score is the weighted average of the seven traffic lights, not a
> gut-feel grade. Read it like a traffic light: 90 and up is green (excellent),
> 75–89 is good, 50–74 leaves real room, below 50 is critical and becomes the
> priority. Every dimension carries the same colour code, so you see at a glance
> where the site is solid and where it loses points.
>
> Two readings to avoid. A high score doesn't mean «number one on Google»: it
> means the technical foundations are sound. And if a measure shows «N/A» it's not
> your site failing: sometimes Google is overloaded, sometimes a site refuses
> automated reading. In that case we compute health on the successful measures and
> tell you so clearly.

**FAQ (3)**
1. **Is the score the real Google one?** For performance, SEO, accessibility and best practices, yes — it comes from the official PageSpeed Insights API, mobile strategy. Privacy, AI-readiness and CO₂ are our own checks, with the method stated in each section.
2. **Does the GDPR check replace a privacy consultant?** No. It's an indicative, four-signal technical check: it catches the obvious problems — missing banner, trackers before consent — but it's not a legal opinion and doesn't replace a consultant.
3. **What's in the PDF that I don't already see on screen?** On screen you see the score, the seven traffic lights and the three priorities. The PDF gives you a page per dimension with every issue found, the fixes ranked by impact, and what we would do, with our company details.

**Final CTA** (`sr-dark`)
> H2: **Want us to fix the priorities?**
> Text: From score to quote: we review the report together and hand you a fixed-price action plan, with PageSpeed 90+ guaranteed by contract.
> Buttons: `Book a free consultation` → `/en/#contatti` · `See all tools` → `/en/tools/` (outline)

### 3.3. RESULTS screen

- Eyebrow (mono): `Site health`
- Big number: `68` `/100`
- Label: `Site needs work`
- URL row: `yoursite.com — mobile analysis · 14 Jul 2026`
- Method note: `Weighted average of 7 measures. Performance, SEO, accessibility and best practices from Google PageSpeed; privacy, AI and CO₂ from Studio Remarka checks.`

**7 dimension labels:** Performance (Weight 25 · Google PageSpeed) · SEO (Weight 20 · Google PageSpeed) · Accessibility (Weight 15 · WCAG 2.1 / EAA) · Privacy & cookies (Weight 15 · indicative check) · Best practices (Weight 10 · Google PageSpeed) · AI-readiness (Weight 10 · 4 signals) · CO₂ impact (Weight 5 · SWD model).

**Verdicts per dimension** (Excellent / Good / Needs work / Critical)
- **Performance:** «Fast on mobile: meets Google's standards.» / «Good speed; measurable room on some pages.» / «Average for the web, but far from the recommended standards.» / «Slow on mobile: most visitors leave before it loads.»
- **SEO:** «On-page foundations in order: no barrier to indexing.» / «Solid structure; a few fixes to finish the basics.» / «Some on-page elements are missing or duplicated.» / «Something blocks indexing: fix this first.»
- **Accessibility:** «Few or no barriers: usable under WCAG 2.1 AA.» / «Good level; minor barriers left to remove.» / «Several barriers found: contrast, labels, navigation.» / «Serious barriers: hard to use for many people (EAA obligation).»
- **Privacy & cookies:** «Banner, policies and trackers in order in the initial HTML.» / «Framework in place; a couple of points to check by hand.» / «Elements missing or some trackers poorly governed.» / «Trackers active without a banner, or policies missing: real regulatory risk.»
- **Best practices:** «Technically clean: HTTPS, no console errors, up-to-date libraries.» / «Good technical level; a few warnings to close.» / «Several technical warnings: security, console errors, images.» / «Widespread technical issues weakening reliability and security.»
- **AI-readiness:** «4 of 4 signals: readable and citable by AI models.» / «3 of 4 signals: nearly fully AI-ready.» / «2 of 4 signals: structured data or sitemap to complete.» / «0–1 signals: AI models struggle to read and cite the site.»
- **CO₂ impact:** «Light page: emissions below the web average.» / «Near the average; room to slim down.» / «Above average: the page is heavy to load.» / «Well above average: heavy page, an environmental and speed cost.»

**«Top 3 fixes»**
- Eyebrow: `Priorities` · H3: `The 3 fixes that matter most` · Intro: `Ranked by impact on your score: how much you'd gain by fixing them.`
- Demo: 1) **Performance · Critical** — «The site is slow on mobile. It's the fix with the biggest weight on the score: lighter images and caching come first.» 2) **Privacy & cookies · Critical** — «Trackers found before consent. Under EU rules they must load only after opt-in: a legal risk, not just a technical one.» 3) **AI-readiness · Needs work** — «Missing structured data and a complete sitemap: two signals that make the site readable to AI models.»

**E-mail form — «The full report, as a PDF»**
- H3: `The full report, as a PDF`
- Text: `We send you the complete analysis: one page per dimension, every issue found and the fixes ranked by impact.`
- PDF contains: The health score with the seven traffic lights · A page per dimension: score, what we found, what to do · The three priority fixes with countermeasures · «What we would do» and Studio Remarka's details.
- E-mail placeholder: `name@yourcompany.com`
- Consent (required): `I have read the privacy policy and consent to receiving the report and being contacted.` (link → `/en/privacy/`)
- Optional: `Send me the monthly Core Web Vitals monitoring for this site.`
- Button: `Send me the PDF report`
- Success: `Done. The report is on its way to your inbox: if it doesn't arrive within a few minutes, check spam or drop us a line.`
- Error: `We couldn't send the report. Try again shortly, or write to us and we'll send it by hand.`
- Note (small): `No spam. We use your address only to send the report and, if useful, to get back to you. Studio Remarka S.r.l., VAT GE 302230994.`

### 3.4. Delivery e-mail
- **Subject:** `Your full check-up for {domain} — PDF report`
- **Body:**
> Hello,
>
> attached is the complete check-up report for **{domain}**: health score
> {score}/100, the seven traffic lights and the recommendations ranked by impact.
>
> Performance, SEO, accessibility and best practices are measured with the Google
> PageSpeed Insights API; privacy, AI-readiness and CO₂ impact with our own checks,
> all with the limits stated in the report.
>
> If you'd like, we'll go through the priorities together and hand you a
> fixed-price action plan — the consultation is free.
>
> [**Book your free consultation →**]
>
> Studio Remarka — in language and digital services since 2001
> info@remarka.biz · +39 347 83 11141

### 3.5. PDF structure (EN)
Same 12-page structure as IT (§2.5), static text in English. Cover: `Full website
check-up`. Closing E-E-A-T page: «Studio Remarka S.r.l., part of the Remarka
group, in language and digital services since 2001.» Offices: Milan, Turin, Rome ·
VAT GE 302230994 · info@remarka.biz · +39 347 83 11141. Methodology note: engines
used (Google PageSpeed Insights / Lighthouse; Sustainable Web Design model; our
own privacy and AI checks) and limits (GDPR is indicative, not a legal opinion; no
Google ranking promise; accessibility follows WCAG 2.1 AA as required by the EAA).

---

## PARTE 4 — Copy deck РУССКИЙ

> Литературный русский, форма «вы» со строчной, числа вместо прилагательных, без
> кальки с итальянского. Аудитория — русскоязычный бизнес в Европе (см.
> `docs/copy-fase-B.md`). Формат евро — с пробелом-тысячником: `€ 3 900`. Сигналы
> E-E-A-T: тест проводит Студия Ремарка, в языковой и цифровой сфере с 2001 года;
> движки — Google PageSpeed Insights/Lighthouse и модель Sustainable Web Design,
> плюс наши собственные проверки с честно указанными границами.

### 4.1. Блок ГЛАВНОЙ (сразу после hero — hero не трогаем)

| Элемент | RU |
|---|---|
| Eyebrow (mono) | Полная проверка · бесплатно |
| H2 | Состояние вашего сайта — одним числом<span class="sr-accent-dot">.</span> |
| Подзаголовок | Один тест объединяет семь проверок — скорость, SEO, доступность, приватность, технические стандарты, готовность к ИИ и экологичность — и выдаёт оценку от 0 до 100 с задачами, которые стоит решить первыми. Движок Google PageSpeed и наши проверки, объяснённые по-русски. |
| Плейсхолдер URL | www.vashsajt.ru |
| Кнопка | Проверить сайт — бесплатно |
| Строка доверия (mono) | 7 тестов в одном · бесплатно · без регистрации |
| Микроподписи (mono) | Скорость · SEO · Доступность · Приватность · Стандарты · ИИ · CO₂ |
| Заметка E-E-A-T (small) | Проверку проводит Студия Ремарка — в языковой и цифровой сфере с 2001 года. Реальные данные Google, без выдуманных цифр. |

Сабмит ведёт на `/ru/instrumenty/polnaya-proverka-sajta/?url=…&autostart=1`.

### 4.2. Страница `/ru/instrumenty/polnaya-proverka-sajta/`

- **Фокус-ключ:** `полная проверка сайта`
- **Title (≤60):** `Полная проверка сайта: 7 тестов в одном | Studio Remarka` (56)
- **Description (≤160):** `Один тест: скорость, SEO, доступность, приватность, стандарты, ИИ и CO₂. Оценка здоровья сайта 0–100 и полный отчёт в PDF. Бесплатно, без регистрации.` (150)
- **H1:** `Полная проверка вашего сайта`
- **Варианты ключа в H2:** «комплексный анализ сайта», «проверка сайта онлайн», «оценка состояния сайта».

**Интро**
> Семь бесплатных инструментов в одном анализе. Вставьте адрес — меньше чем за
> минуту вы увидите оценку здоровья от 0 до 100, семь светофоров за ней и три
> самые срочные задачи. Скорость, SEO, доступность и технические стандарты
> измеряет Google PageSpeed Insights; приватность и готовность к ИИ проверяем мы.
> Полный отчёт, страница за страницей, пришлём в PDF.

**Как это работает — 3 шага**
1. **Вставьте адрес** — Главная или страница, которая приносит больше всего визитов. Без регистрации и без платёжных данных.
2. **Анализируем по семи направлениям** — Один запрос к API Google PageSpeed (скорость, SEO, доступность, стандарты) плюс наши проверки приватности и готовности к ИИ: сайт мы читаем со своего сервера, как его увидел бы посетитель.
3. **Читаете оценку и приоритеты** — Здоровье 0–100, семь светофоров по-русски и три задачи, которые весят больше всего. Полный отчёт придёт в PDF.

**Раздел «Метод»**
> H2: **Что на самом деле измеряет полная проверка**
>
> За оценкой нет чёрного ящика. Четыре из семи измерений — скорость, SEO,
> доступность и технические стандарты — приходят из API Google PageSpeed
> Insights, того же, что стоит за pagespeed.web.dev: мы опрашиваем Lighthouse в
> мобильной стратегии, потому что именно эту версию сайта Google использует для
> ранжирования. Остальные три считаем мы: приватность читаем из HTML страницы
> (баннер, политики, трекеры до согласия), готовность к ИИ — по четырём
> техническим сигналам (llms.txt, доступ краулеров, структурированные данные,
> sitemap), а углеродный след — по реальному весу страницы, по модели
> Sustainable Web Design.
>
> Каждое измерение входит в оценку со своим весом: скорость весит больше всего
> (25 из 100), CO₂ — меньше всего (5). Стоит знать и то, чего проверка не делает:
> это не юридическое заключение по GDPR — это ориентировочная проверка по четырём
> сигналам — и она не обещает позиций в Google. Это точный технический снимок
> сайта, а не обещание продаж.

**Раздел «Как читать»**
> H2: **Как читать оценку состояния сайта**
>
> Оценка здоровья — это взвешенное среднее семи светофоров, а не отметка «на
> глаз». Читается как светофор: от 90 и выше — зелёная зона (отлично), 75–89 —
> хорошо, 50–74 — есть реальный запас, ниже 50 — критично и становится
> приоритетом. У каждого измерения один и тот же цветовой код, поэтому сразу
> видно, где сайт крепок, а где теряет баллы.
>
> Два неверных прочтения. Высокая оценка не значит «первые в Google»: она значит,
> что технический фундамент здоров. А если измерение показывает «Н/Д», это не
> поломка вашего сайта: иногда Google перегружен, иногда сайт отказывает в
> автоматическом чтении. В этом случае мы считаем здоровье по удавшимся
> измерениям и честно об этом сообщаем.

**FAQ (3)**
1. **Оценка — настоящая от Google?** Для скорости, SEO, доступности и стандартов — да: она из официального API PageSpeed Insights, мобильная стратегия. Приватность, готовность к ИИ и CO₂ — наши проверки, метод описан в каждом разделе.
2. **Проверка GDPR заменяет консультанта по приватности?** Нет. Это ориентировочная техническая проверка по четырём сигналам: она ловит очевидные проблемы — нет баннера, трекеры до согласия, — но это не юридическое заключение и не замена консультанту.
3. **Что в PDF-отчёте, чего нет на экране?** На экране — оценка, семь светофоров и три приоритета. В PDF — по странице на каждое из семи измерений со всеми найденными проблемами, рекомендации по степени влияния и раздел «что сделали бы мы» с нашими реквизитами.

**Финальный CTA** (`sr-dark`)
> H2: **Хотите, чтобы приоритеты закрыли мы?**
> Текст: От оценки — к смете: разберём отчёт вместе и дадим план работ по
> фиксированной цене, со скоростью PageSpeed 90+ по договору.
> Кнопки: `Бесплатная консультация` → `/ru/#contatti` · `Все инструменты` → `/ru/instrumenty/` (outline)

### 4.3. Экран РЕЗУЛЬТАТОВ

- Eyebrow (mono): `Здоровье сайта`
- Крупное число: `68` `/100`
- Метка: `Сайт требует доработки`
- Строка URL: `vashsajt.ru — мобильный анализ · 14.07.2026`
- Заметка о методе: `Взвешенное среднее 7 измерений. Скорость, SEO, доступность и стандарты — из Google PageSpeed; приватность, ИИ и CO₂ — проверки Студии Ремарка.`

**Подписи 7 измерений:** Скорость (Вес 25 · Google PageSpeed) · SEO (Вес 20 · Google PageSpeed) · Доступность (Вес 15 · WCAG 2.1 / EAA) · Приватность и cookie (Вес 15 · ориентировочная проверка) · Технические стандарты (Вес 10 · Google PageSpeed) · Готовность к ИИ (Вес 10 · 4 сигнала) · Углеродный след (Вес 5 · модель SWD).

**Вердикты по измерениям** (Отлично / Хорошо / Внимание / Критично)
- **Скорость:** «Сайт быстрый на мобильном: соответствует стандартам Google.» / «Скорость хорошая; на части страниц есть измеримый запас.» / «В среднем по вебу, но далеко от рекомендуемых стандартов.» / «Сайт медленный на мобильном: большинство уходит до загрузки.»
- **SEO:** «Технические основы страницы в порядке: ничто не мешает индексации.» / «Структура крепкая; несколько правок, чтобы завершить основы.» / «Часть элементов страницы отсутствует или дублируется.» / «Что-то мешает индексации: исправить в первую очередь.»
- **Доступность:** «Барьеров мало или нет: сайт пригоден по WCAG 2.1 AA.» / «Хороший уровень; остались мелкие барьеры.» / «Найдено несколько барьеров: контраст, подписи, навигация.» / «Серьёзные барьеры: сайтом трудно пользоваться многим (требование EAA).»
- **Приватность и cookie:** «Баннер, политики и трекеры в начальном HTML в порядке.» / «Механизм есть; пару пунктов стоит проверить вручную.» / «Не хватает элементов или трекеры управляются плохо.» / «Трекеры работают без баннера или нет политик: реальный юридический риск.»
- **Технические стандарты:** «Технически чисто: HTTPS, консоль без ошибок, актуальные библиотеки.» / «Хороший уровень; несколько предупреждений закрыть.» / «Несколько технических предупреждений: безопасность, ошибки консоли, картинки.» / «Много технических проблем, ослабляющих надёжность и безопасность.»
- **Готовность к ИИ:** «4 сигнала из 4: сайт читаем и цитируем ИИ-моделями.» / «3 сигнала из 4: до полной готовности немного.» / «2 сигнала из 4: доработать структурированные данные или sitemap.» / «0–1 сигнал: ИИ-моделям трудно читать и цитировать сайт.»
- **Углеродный след:** «Лёгкая страница: выбросы ниже среднего по вебу.» / «Около среднего; есть запас, чтобы облегчить.» / «Выше среднего: страница тяжёлая при загрузке.» / «Заметно выше среднего: тяжёлая страница, цена для экологии и скорости.»

**Блок «3 самых срочных действия»**
- Eyebrow: `Приоритеты` · H3: `3 задачи, которые весят больше всего` · Интро: `По степени влияния на оценку: сколько вы выиграете, решив их.`
- Демо: 1) **Скорость · Критично** — «Сайт медленный на мобильном. Это действие с наибольшим весом на оценку: начать стоит с облегчения изображений и кэша.» 2) **Приватность и cookie · Критично** — «Найдены трекеры до согласия. По правилам ЕС они должны загружаться только после «да»: это юридический риск, а не только технический.» 3) **Готовность к ИИ · Внимание** — «Нет структурированных данных и полной sitemap: два сигнала, которые делают сайт читаемым для ИИ-моделей.»

**Форма e-mail — «Полный отчёт в PDF»**
- H3: `Полный отчёт в PDF`
- Текст: `Пришлём анализ целиком: по странице на каждое из семи измерений, все найденные проблемы и рекомендации по степени влияния.`
- Что внутри PDF: Оценка здоровья с семью светофорами · Страница на каждое измерение: балл, что нашли, что делать · Три приоритетные задачи с мерами · «Что сделали бы мы» и реквизиты Студии Ремарка.
- Плейсхолдер e-mail: `imya@vashakompaniya.ru`
- Согласие (обязательно): `Я прочитал политику конфиденциальности и согласен на отправку отчёта и на обратную связь.` (ссылка → `/ru/privacy/`)
- Необязательно: `Присылайте мне ежемесячный мониторинг Core Web Vitals этого сайта.`
- Кнопка: `Прислать отчёт в PDF`
- Успех: `Готово. Отчёт уже в пути к вашей почте: если не придёт за пару минут, проверьте спам или напишите нам.`
- Ошибка: `Не удалось отправить отчёт. Попробуйте ещё раз или напишите нам — пришлём вручную.`
- Заметка (small): `Без спама. Адрес используем только для отправки отчёта и, при необходимости, обратной связи. Студия Ремарка, ИНН 231149349191.`

### 4.4. Письмо с PDF
- **Тема:** `Полная проверка {домен} — отчёт в PDF`
- **Тело:**
> Здравствуйте,
>
> во вложении — полный отчёт проверки **{домен}**: оценка здоровья {оценка}/100,
> семь светофоров и рекомендации по степени влияния.
>
> Скорость, SEO, доступность и стандарты измерены через API Google PageSpeed
> Insights; приватность, готовность к ИИ и углеродный след — нашими проверками,
> все с границами, указанными в отчёте.
>
> Если хотите, разберём приоритеты вместе и дадим план работ по фиксированной
> цене — консультация бесплатная.
>
> [**Записаться на бесплатную консультацию →**]
>
> Студия Ремарка — в языковой и цифровой сфере с 2001 года
> info@remarka.biz · +7 918 263 00 13

### 4.5. Структура PDF (RU)
Те же 12 страниц, что в IT (§2.5), статический текст по-русски. Обложка:
`Полная проверка сайта`. Финальная страница E-E-A-T: «Студия Ремарка — часть
группы Remarka, в языковой и цифровой сфере с 2001 года. Сайты, интернет-магазины
и локализация носителями языка.» Реквизиты: Москва, Глинищевский пер., 6 ·
Краснодар, ул. Кузнечная, 6 · ИНН 231149349191 · ОГРНИП 323237500359402 ·
info@remarka.biz · +7 918 263 00 13. Методологическая заметка: движки (Google
PageSpeed Insights / Lighthouse; модель Sustainable Web Design; наши проверки
приватности и ИИ) и границы (GDPR — ориентировочно, не юридическое заключение;
без обещаний позиций в Google; доступность — по стандарту WCAG 2.1 AA,
обязательному по European Accessibility Act).

---

## PARTE 5 — Nota per M2/M3: nuove classi CSS e dati strutturati

### 5.1. Classi CSS da aggiungere in `assets/css/remarka.css` (M2)

I mock M1 usano stili inline dove serve, per **non** toccare `remarka.css`. In M2
vanno estratte queste classi (in coda alle sezioni pertinenti):

| Classe | Scopo | Note |
|---|---|---|
| `.sr-checkup` | wrapper della schermata risultati | contenitore, gap verticale |
| `.sr-gauge` | indicatore circolare del composito | `conic-gradient` sul punteggio; fallback: numero grande + `.sr-barra` (già esistente). Su 390px il gauge scende a ~120px |
| `.sr-gauge__num` | numero dentro il gauge | riuso `--sr-font-mono`, `clamp()` |
| `.sr-dim-grid` | griglia delle 7 dimensioni | `repeat(auto-fit, minmax(280px,1fr))`; **su ≤520px → 1 colonna**; 640–860px → 2 colonne |
| `.sr-dim-card` | card singola dimensione | può estendere `.sr-card`; header con occhiello + punteggio mono + pallino `[data-sr-flag]` |
| `.sr-dim-card__score` | numero /100 della card | mono, ~34px |
| `.sr-dim-card__findings` | 2–3 rilievi | riuso stile `.sr-tool-audits li` |
| `.sr-priorities` | blocco «3 interventi» | lista numerata con pallino di stato |
| `.sr-checkup-lead` | form e-mail PDF | riuso `.sr-card` + `.sr-text-input`; checkbox come `.sr-consent` |
| `.sr-consent` | riga checkbox consenso | allineamento checkbox+label, link inline |
| `[data-sr-flag="ok"]` *(opzionale)* | 4ª tinta «Buono» (verde-lime) | solo se si vuole distinguere 75–89 da 90+ nel pallino; **non necessaria** per M1 |

**Mobile-first (richiesta titolare):** il blocco home e la schermata risultati
si progettano prima a 390px. Regole minime: riga URL = **stack verticale**
(input sopra, bottone sotto a piena larghezza) sotto i ~560px; griglia dimensioni
a 1 colonna ≤520px, 2 colonne fino a ~860px; il numero del composito deve restare
leggibile senza zoom (min ~56px). Dove qualcosa non entra, decidere a favore del
mobile.

### 5.2. Dati strutturati schema.org (M2/M3, nel `<head>` della pagina check-up)

Da iniettare come JSON-LD (analogo al blocco Organization già in `functions.php`):

- **`WebApplication`** (o `SoftwareApplication`) per lo strumento:
  - `name`: «Check-up completo del sito» / «Full website check-up» / «Полная проверка сайта»
  - `applicationCategory`: `"BusinessApplication"` · `operatingSystem`: `"Web"`
  - `offers`: `{ "@type": "Offer", "price": "0", "priceCurrency": "EUR" }` (è gratis)
  - `featureList`: le 7 dimensioni · `inLanguage`: `it`/`en`/`ru`
  - `provider`: riferimento all'`Organization` (Studio Remarka)
  - `isAccessibleForFree`: `true`
- **`Organization`**: riusare i dati reali già presenti (`remarka_company_lang_data()`):
  nome, indirizzi (Milano/Torino/Roma; RU: Москва/Краснодар), P.IVA/VAT `GE 302230994`
  (RU: ИНН `231149349191`), email `info@remarka.biz`, telefono, `foundingDate` 2001.
- **`FAQPage`** con le 3 FAQ della pagina (una per lingua).

Non inventare recensioni, valutazioni (`aggregateRating`) o nomi di esperti: i
segnali E-E-A-T restano ancorati a fatti reali (heritage 2001, requisiti fiscali
verificabili, motori dichiarati).

---

## Stato

- **M1 — completato.** Modello di scoring finalizzato, copy deck IT/EN/RU, mock su
  CSS reale (blocco home + schermata risultati, 390px e 1440px). Vedi
  `piano-checkup-sito.md` §Stato.
</content>
</invoke>
