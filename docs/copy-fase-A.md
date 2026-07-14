# Fase A — copy deck definitivo (IT + EN)

> Data: 14.07.2026 · Pacchetto WP-1 · Base: `piano-implementazione-fase-A.md` §1,
> `strategia-riposizionamento.md` (Д-1…Д-5).
> Regole di tono: **numeri al posto degli aggettivi**, forma **«voi»** in italiano,
> nessun anglicismo evitabile in IT, nessun pathos commerciale. In EN numeri in
> **formato US** (`€ 3,900–5,800`, virgola come separatore delle migliaia).
> Le tabelle qui sotto sono la fonte unica per WP-4 (IT) e WP-6 (EN).

---

## 1. Hero (`patterns/hero-home.php` · `lang-en/hero-home.php`)

| Elemento | IT | EN |
|---|---|---|
| Eyebrow | Studio di sviluppo web | Web development studio |
| H1 | Il sito nuovo in 3 settimane. A prezzo chiuso. | Your new website in 3 weeks. At a fixed price. |
| Sottotitolo | Consegna a data fissa con penale in contratto, prezzo bloccato alla firma, PageSpeed 90+ garantito. Siti in quattro lingue con redattori madrelingua, dal 2001. | Fixed delivery date with a contractual penalty, price locked at signing, PageSpeed 90+ guaranteed. Websites in four languages with native-speaking editors, since 2001. |
| CTA 1 (invariata) | Analizza il vostro sito — gratis | Test your site — free |
| CTA 2 (invariata) | Preventivo in 24 ore | Quote in 24 hours |
| Microcopy sotto i bottoni (nuova) | 3 settimane: sito aziendale. Vetrina: 2. E-commerce: 6. | 3 weeks: business website. Brochure site: 2. E-commerce: 6. |

**Note.** H1 e sottotitolo tenuti quasi identici alla bozza: già rispettano la
regola dei numeri. L'H1 chiude con `<span class="sr-accent-dot">.</span>` come gli
altri titoli. La microcopy è una riga sola, mono/eyebrow, che disinnesca l'obiezione
«3 settimane per qualsiasi sito?» nominando le tre linee di prodotto.

---

## 2. Widget hero destro — timeline «21 giorni» (`.sr-timeline`, sostituisce il widget PageSpeed)

| Elemento | IT | EN |
|---|---|---|
| Titolo (mono) | DALLA FIRMA ALL'ONLINE — 21 GIORNI | FROM SIGNATURE TO LIVE — 21 DAYS |
| Riga 1 (barra 33%) | Settimana 1 — Analisi e design | Week 1 — Analysis & design |
| Riga 2 (barra 66%) | Settimana 2 — Sviluppo | Week 2 — Development |
| Riga 3 (barra 100%) | Settimana 3 — Contenuti, test, online | Week 3 — Content, testing, go-live |
| Didascalia | La data è nel contratto: ogni giorno lavorativo di ritardo vale l'1% di sconto. | The date is in the contract: every working day of delay is 1% off. |

**Note.** Le tre righe usano il componente `.sr-barra` + `data-sr-target` (33/66/100%),
riempimento animato come la barra dei cento. Il widget PageSpeed esce dall'hero;
lo strumento resta su `/strumenti/test-velocita/` (EN `/en/tools/speed-test/`).
«go-live» in EN è preferito a «live» come sostantivo tecnico più naturale nel
contesto «content, testing, …».

---

## 3. Tre numeri (`patterns/tre-numeri.php`)

| # | Numero | Didascalia IT | Spiegazione IT |
|---|---|---|---|
| 1 | `3 settimane` | Dalla firma al sito online | Sito aziendale completo. La media di mercato è di 6–10 settimane. |
| 2 | `±0 giorni` | Di ritardo sulle consegne | Data fissa in contratto, penale dell'1% per ogni giorno lavorativo. |
| 3 | `4` | Lingue native in ogni progetto | Italiano, inglese, tedesco e francese — redattori madrelingua, non un plugin. |

| # | Number | Caption EN | Explanation EN |
|---|---|---|---|
| 1 | `3 weeks` | From signature to live site | A complete business website. The market average is 6–10 weeks. |
| 2 | `±0 days` | Of delay on deliveries | Fixed date in the contract, a 1% penalty for every working day. |
| 3 | `4` | Native languages in every project | Italian, English, German and French — native-speaking editors, not a plugin. |

**Note / scostamento dalla bozza.** Il primo numero `97` (PageSpeed) esce da
questa sezione — resta in «Nero su bianco» dove c'è già `90+`, per non ripetere il
punteggio due volte in home. Il secondo numero passa da `−38%` (velocità post
restyling, dato 2025 non più centrale all'offerta) a `±0 giorni`, che parla di
puntualità: coerente con il gancio n. 1 «tempi». Terzo numero invariato.
`±0` è scritto attaccato per uniformità con `±0 gg` di «Nero su bianco».

---

## 4. «Nero su bianco» — quarta garanzia (`patterns/garanzie-dark.php`)

| Elemento | IT | EN |
|---|---|---|
| Intro sezione (era «Tre clausole…») | Quattro clausole del nostro contratto standard. Non promesse commerciali: obblighi firmati. | Four clauses from our standard contract. Not marketing promises: signed obligations. |
| Numero tassello 4 | `€ 0` | `€ 0` |
| Titolo tassello 4 | Sorprese in fattura | Invoice surprises |
| Testo tassello 4 | Il prezzo firmato è il prezzo finale. Ogni extra si concorda per iscritto prima — o è a carico nostro. | The signed price is the final price. Any extra is agreed in writing first — or it's on us. |
| Didascalia di chiusura (aggiornata) | Estratto dagli artt. 4–7 del contratto standard — copia su richiesta | Excerpt from arts. 4–7 of the standard contract — copy on request |

**Ordine dei quattro tasselli:** `90+` PageSpeed · `±0 gg` Consegna a data fissa ·
`€ 0` Sorprese in fattura · `12 mesi` Assistenza inclusa.

**Note.** L'intro passa da «Tre» a «Quattro» e la didascalia da «artt. 4–6» a
«artt. 4–7» (una clausola in più). Testi dei primi tre tasselli invariati.

---

## 5. Come lavoriamo → «Le 3 settimane, giorno per giorno» (`patterns/come-lavoriamo.php`)

| Elemento | IT | EN |
|---|---|---|
| Eyebrow | Come lavoriamo | How we work |
| H2 | Le 3 settimane, giorno per giorno. | The 3 weeks, day by day. |
| Chip settimana 1 (`.sr-week-chip`) | SETTIMANA 1 | WEEK 1 |
| Chip settimana 2 | SETTIMANA 2 | WEEK 2 |
| Chip settimana 3 | SETTIMANA 3 | WEEK 3 |
| Nota a piè di sezione | Tempi del sito aziendale. Vetrina: 2 settimane. E-commerce: 6. | Business-website timeline. Brochure site: 2 weeks. E-commerce: 6. |

**Raggruppamento dei cinque passaggi (invariati come contenuto) sotto i chip:**

| Settimana | Passaggio | Tag durata IT | Tag durata EN | Testo (invariato dalla versione attuale) |
|---|---|---|---|---|
| SETTIMANA 1 | 01 Analisi | GIORNI 1–2 | DAYS 1–2 | Report tecnico del sito attuale, con priorità e obiettivi misurabili. |
| SETTIMANA 1 | 02 Preventivo fisso | 24 ORE | 24 HOURS | Prezzo chiuso e data di consegna, scritti nel contratto. |
| SETTIMANA 1 | 03 Design | GIORNI 3–5 | DAYS 3–5 | Prototipo navigabile da approvare pagina per pagina, non PDF statici. |
| SETTIMANA 2 | 04 Sviluppo | GIORNI 6–10 | DAYS 6–10 | Sito su ambiente di prova, avanzamento visibile ogni venerdì. |
| SETTIMANA 3 | 05 Consegna e assistenza | GIORNI 11–15 · 12 MESI | DAYS 11–15 · 12 MONTHS | Formazione all'uso, misurazioni mensili e assistenza inclusa. |

**Note / scostamento.** I tag durata attuali (`1–2 SETTIMANE`, `2–4 SETTIMANE`)
contraddicono la promessa «3 settimane» e sono stati ricalibrati in giorni lavorativi
dentro le tre settimane. Il testo dei passaggi resta identico. La nota a piè chiarisce
che il calendario mostrato è quello del sito aziendale.

---

## 6. Tabella «noi vs mercato» (`/prezzi/` completa + teaser home in `prezzi-teaser.php`)

### 6.1 Versione completa (pagina Prezzi) — `.sr-market-table`

| Elemento | IT | EN |
|---|---|---|
| H2 | Prezzi e tempi, accanto a quelli di mercato. | Prices and timelines, next to the market's. |
| Introduzione | Le forbici di mercato vengono dai listini pubblici delle web agency italiane (2026). Le nostre cifre sono quelle del contratto. | The market ranges come from the public price lists of Italian web agencies (2026). Our figures are the ones in the contract. |

Intestazioni colonne — IT: `Prodotto` · `Prezzo di mercato` · `Prezzo Remarka` · `Tempi di mercato` · `Tempi Remarka`
EN: `Product` · `Market price` · `Remarka price` · `Market timeline` · `Remarka timeline`

| Prodotto (IT / EN) | Prezzo di mercato / Market price | **Prezzo Remarka / Remarka price** | Tempi di mercato / Market timeline | **Tempi Remarka / Remarka timeline** |
|---|---|---|---|---|
| Sito vetrina / Brochure site | € 1.000–3.000 · € 1,000–3,000 | **€ 1.900–2.800 · € 1,900–2,800** | 2–4 settimane · 2–4 weeks | **2 settimane · 2 weeks** |
| Sito aziendale / Business website | € 2.500–8.000 · € 2,500–8,000 | **€ 3.900–5.800 · € 3,900–5,800** | 6–10 settimane · 6–10 weeks | **3 settimane · 3 weeks** |
| E-commerce / E-commerce | € 6.000–25.000 · € 6,000–25,000 | **€ 7.500–14.000 · € 7,500–14,000** | 8–14 settimane · 8–14 weeks | **6 settimane · 6 weeks** |

Nota-fonte:
- IT: `Forbici di mercato dai listini pubblici delle web agency italiane, 2026. Analisi completa con le fonti nel nostro blog: «Quanto costa un sito aziendale in Italia».` → link `/blog/quanto-costa-sito-aziendale-italia/`
- EN: `Market ranges from the public price lists of Italian web agencies, 2026. Full breakdown with sources on our blog: "How much a business website costs in Italy".` → link `/en/blog/business-website-cost-italy/` *(slug EN da confermare in WP-6)*

### 6.2 Teaser home compatto (`prezzi-teaser.php`) — `.sr-market-table--compact`

Tre righe, tre colonne: `Prodotto` · `Mercato` · `Remarka` (la colonna Remarka unisce prezzo e tempi).

| Elemento | IT | EN |
|---|---|---|
| Eyebrow | Prezzi | Prices |
| H2 | Prezzi e tempi, accanto al mercato. | Prices and timelines, next to the market. |
| Intestazioni | Prodotto · Mercato · Remarka | Product · Market · Remarka |
| Riga vetrina — Mercato | € 1.000–3.000 · 2–4 sett. | € 1,000–3,000 · 2–4 wks |
| Riga vetrina — Remarka | **€ 1.900–2.800 · 2 sett.** | **€ 1,900–2,800 · 2 wks** |
| Riga aziendale — Mercato | € 2.500–8.000 · 6–10 sett. | € 2,500–8,000 · 6–10 wks |
| Riga aziendale — Remarka | **€ 3.900–5.800 · 3 sett.** | **€ 3,900–5,800 · 3 wks** |
| Riga e-commerce — Mercato | € 6.000–25.000 · 8–14 sett. | € 6,000–25,000 · 8–14 wks |
| Riga e-commerce — Remarka | **€ 7.500–14.000 · 6 sett.** | **€ 7,500–14,000 · 6 wks** |
| Nota | I prezzi Remarka sono chiusi: quello che firmate è quello che pagate. | Remarka prices are fixed: what you sign is what you pay. |
| CTA (invariata) | Richiedi preventivo dettagliato | Request a detailed quote |

**Note / scostamento.** La tabella teaser attuale (Tariffa / Per chi / Tempi /
Prezzo) viene sostituita dal confronto mercato↔Remarka: è il gancio n. 2 della
strategia (Д-2, «trasparente e sotto la media, con garanzie che il mercato non dà»).
I tempi del teaser attuale (`3 sett.` vetrina, `5–7 sett.` aziendale, `8–10 sett.`
e-commerce) erano incoerenti con la nuova offerta e sono allineati ai valori di
contratto (2 / 3 / 6 settimane).

---

## 7. Nuovo blocco «Lingue e mercati» (`patterns/lingue-mercati.php`, nuovo) — `.sr-langs`

| Elemento | IT | EN |
|---|---|---|
| Eyebrow | Lingue | Languages |
| H2 | Ogni lingua ha il suo redattore madrelingua. | Every language has its own native editor. |
| Introduzione | Dal 2001 il gruppo Remarka lavora con la traduzione professionale: la versione estera del vostro sito non è un plugin, è un deliverable con nome e cognome. | Since 2001 the Remarka group has worked in professional translation: the foreign version of your site isn't a plugin, it's a deliverable with a name attached. |
| Gruppo 1 — mercato | UE | EU |
| Gruppo 1 — codici | EN · DE · FR · ES | EN · DE · FR · ES |
| Gruppo 2 — mercato | Nord America | North America |
| Gruppo 2 — codici | EN-US | EN-US |
| Gruppo 3 — mercato | CSI e Caucaso | CIS & Caucasus |
| Gruppo 3 — codici | RU · UK · KA · HY · KK | RU · UK · KA · HY · KK |
| CTA | Scopri i siti multilingue → | Explore multilingual websites → |
| CTA link | `/servizi/siti-multilingue/` | `/en/services/multilingual-websites/` *(slug EN da confermare in WP-6)* |

**Note.** Niente bandiere (rumore visivo e politica): solo tipografia mono, come
da strategia §3.3. I codici sono ISO 639-1: `KA` georgiano, `HY` armeno, `KK` kazako,
`UK` ucraino, `RU` russo. Il gruppo «CSI e Caucaso» presenta la competenza sui
mercati vicini **come fatto**, dentro l'imbuto italiano, senza landing dedicate
(Д-5). Posizione in home: dopo il Manifesto, prima delle card servizi.
</content>
