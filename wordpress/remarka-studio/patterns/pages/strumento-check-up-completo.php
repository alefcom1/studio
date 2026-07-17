<?php
/**
 * Title: Pagina — Strumento: Check-up completo
 * Slug: remarka-studio/strumento-check-up-completo
 * Categories: remarka-pagine
 * Description: Strumento gratuito Check-up completo: widget interattivo, come funziona, FAQ, CTA.
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","className":"sr-section sr-hero","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-hero"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Check-up completo · gratuito</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"level":1,"style":{"typography":{"fontSize":"clamp(34px,4vw,52px)"}}} -->
<h1 class="wp-block-heading" style="font-size:clamp(34px,4vw,52px)">Il check-up completo del vostro sito web<span class="sr-accent-dot">.</span></h1>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="max-width:100%">Sette strumenti gratuiti in una sola analisi. Incollate l’indirizzo: in meno di un minuto vedete un punteggio di salute da 0 a 100, i sette semafori che lo compongono e i tre interventi più urgenti. La misura è quella vera di Google PageSpeed Insights, affiancata dalle nostre verifiche su privacy e prontezza AI. Il report completo, pagina per pagina, ve lo inviamo in PDF.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:html -->

<div class="sr-tool-widget sr-card sr-checkup" data-sr-tool="checkup" data-sr-locale="it"
     data-word-0="Eccellente" data-word-1="Buono" data-word-2="Da migliorare" data-word-3="Critico"
     data-composite-0="Sito in salute eccellente" data-composite-1="Sito in buona salute"
     data-composite-2="Sito da migliorare" data-composite-3="Sito a rischio"
     data-label-suffix=" — analisi mobile"
     data-calc-note="Calcolato su {n} misurazioni su 7."
     data-na-text="Non siamo riusciti a misurare questo aspetto: il sito ha rifiutato la lettura o il servizio Google era saturo."
     data-err="Non siamo riusciti a completare il check-up. Riprovate tra qualche minuto."
     data-ai-suffix=" / 4 segnali"
     data-more-label="Approfondisci →">
  <form data-sr-tool-form>
    <div class="sr-tool-row">
      <input type="text" placeholder="www.ilvostrosito.it" class="sr-text-input" required />
      <button type="submit" class="wp-block-button__link" style="padding:17px 30px">Analizza il sito — gratis</button>
    </div>
  </form>
  <p class="sr-tool-pending sr-mono" data-sr-tool-pending hidden>Analisi in corso su sette fronti — può richiedere fino a 30 secondi<span class="sr-blink">…</span></p>

  <div class="sr-tool-result" data-sr-tool-result hidden>

    <div class="sr-checkup-incomplete" data-sr-checkup-incomplete hidden>
      <h3 class="wp-block-heading">Check-up incompleto</h3>
      <p>Riprovate tra qualche minuto: alcune misure non hanno risposto (il servizio Google potrebbe essere saturo, oppure il sito ha rifiutato la lettura).</p>
      <button type="button" class="wp-block-button__link" data-sr-checkup-retry>Riprova</button>
    </div>

    <div data-sr-checkup-composite>
      <p class="sr-eyebrow">Salute del sito</p>
      <div class="sr-checkup-composite">
        <div class="sr-gauge" data-sr-gauge>
          <div class="sr-gauge__num"><span class="sr-gauge__num-value" data-sr-gauge-num>0</span><span class="sr-gauge__num-suffix">/100</span></div>
        </div>
        <div>
          <p class="sr-mono sr-checkup-url" data-sr-checkup-url></p>
          <h2 class="wp-block-heading sr-checkup-label" data-sr-checkup-label></h2>
          <p class="sr-checkup-method-note">Media pesata di 7 misure. Prestazioni, SEO, accessibilità e best practice arrivano da Google PageSpeed Insights; privacy, prontezza AI e impatto CO₂ dalle verifiche di Studio Remarka.</p>
          <p class="sr-mono sr-checkup-calc" data-sr-checkup-calc></p>
        </div>
      </div>
    </div>

    <div style="margin-top:32px">
      <p class="sr-eyebrow">Le sette misure</p>
      <h2 class="wp-block-heading" style="font-size:clamp(24px,2.4vw,32px)">Sette semafori, un punteggio</h2>
      <div class="sr-dim-grid" style="margin-top:24px"><div class="sr-card sr-dim-card" data-sr-dim="perf" data-verdict-0="Il sito è rapido su mobile: rispetta gli standard Google." data-verdict-1="Velocità buona; restano margini misurabili su qualche pagina." data-verdict-2="Nella media del web, ma lontano dagli standard consigliati." data-verdict-3="Il sito è lento su mobile: gran parte dei visitatori abbandona prima del caricamento.">
  <div class="sr-dim-card__head"><p class="sr-eyebrow" style="margin:0">Prestazioni</p><span class="sr-dim-card__weight">Peso 25</span></div>
  <div class="sr-dim-card__score"><span class="sr-dim-card__score-value" data-sr-tool-score>—</span><span class="sr-dim-card__score-suffix">/100</span></div>
  <div class="sr-barra" style="height:8px;margin-top:12px"><div class="sr-barra__fill" data-sr-tool-fill style="width:0%"></div></div>
  <p class="sr-dim-card__word" data-sr-dim-word></p>
  <p class="sr-dim-card__findings" data-sr-tool-verdict></p>
  <p class="sr-dim-card__engine sr-mono">Google PageSpeed</p>
  <p class="sr-dim-card__more"><a data-sr-dim-more hidden target="_self">Approfondisci →</a></p>
</div><div class="sr-card sr-dim-card" data-sr-dim="seo" data-verdict-0="Basi tecniche on-page in ordine: nessun ostacolo all’indicizzazione." data-verdict-1="Struttura solida; poche correzioni per completare le basi." data-verdict-2="Alcuni elementi on-page mancano o sono duplicati." data-verdict-3="Qualcosa ostacola l’indicizzazione: da sistemare prima di tutto.">
  <div class="sr-dim-card__head"><p class="sr-eyebrow" style="margin:0">SEO</p><span class="sr-dim-card__weight">Peso 20</span></div>
  <div class="sr-dim-card__score"><span class="sr-dim-card__score-value" data-sr-tool-score>—</span><span class="sr-dim-card__score-suffix">/100</span></div>
  <div class="sr-barra" style="height:8px;margin-top:12px"><div class="sr-barra__fill" data-sr-tool-fill style="width:0%"></div></div>
  <p class="sr-dim-card__word" data-sr-dim-word></p>
  <p class="sr-dim-card__findings" data-sr-tool-verdict></p>
  <p class="sr-dim-card__engine sr-mono">Google PageSpeed</p>
  <p class="sr-dim-card__more"><a data-sr-dim-more hidden target="_self">Approfondisci →</a></p>
</div><div class="sr-card sr-dim-card" data-sr-dim="a11y" data-verdict-0="Poche o nessuna barriera: sito fruibile secondo WCAG 2.1 AA." data-verdict-1="Buon livello; restano barriere minori da rimuovere." data-verdict-2="Diverse barriere rilevate: contrasti, etichette, navigazione." data-verdict-3="Barriere gravi: il sito è difficile da usare per molte persone (obbligo EAA).">
  <div class="sr-dim-card__head"><p class="sr-eyebrow" style="margin:0">Accessibilità</p><span class="sr-dim-card__weight">Peso 15</span></div>
  <div class="sr-dim-card__score"><span class="sr-dim-card__score-value" data-sr-tool-score>—</span><span class="sr-dim-card__score-suffix">/100</span></div>
  <div class="sr-barra" style="height:8px;margin-top:12px"><div class="sr-barra__fill" data-sr-tool-fill style="width:0%"></div></div>
  <p class="sr-dim-card__word" data-sr-dim-word></p>
  <p class="sr-dim-card__findings" data-sr-tool-verdict></p>
  <p class="sr-dim-card__engine sr-mono">WCAG 2.1 / EAA</p>
  <p class="sr-dim-card__more"><a data-sr-dim-more hidden target="_self">Approfondisci →</a></p>
</div><div class="sr-card sr-dim-card" data-sr-dim="gdpr" data-verdict-0="Banner, informative e tracker in ordine nell’HTML iniziale." data-verdict-1="Impianto presente; un paio di punti da verificare a mano." data-verdict-2="Mancano elementi o alcuni tracker vanno governati meglio." data-verdict-3="Tracker attivi senza banner o policy assenti: rischio concreto col Garante.">
  <div class="sr-dim-card__head"><p class="sr-eyebrow" style="margin:0">Privacy e cookie</p><span class="sr-dim-card__weight">Peso 15</span></div>
  <div class="sr-dim-card__score"><span class="sr-dim-card__score-value" data-sr-tool-score>—</span><span class="sr-dim-card__score-suffix">/100</span></div>
  <div class="sr-barra" style="height:8px;margin-top:12px"><div class="sr-barra__fill" data-sr-tool-fill style="width:0%"></div></div>
  <p class="sr-dim-card__word" data-sr-dim-word></p>
  <p class="sr-dim-card__findings" data-sr-tool-verdict></p>
  <p class="sr-dim-card__engine sr-mono">Verifica indicativa · non legale</p>
  <p class="sr-dim-card__more"><a data-sr-dim-more hidden target="_self">Approfondisci →</a></p>
</div><div class="sr-card sr-dim-card" data-sr-dim="bp" data-verdict-0="Sito tecnicamente pulito: HTTPS, console senza errori, librerie aggiornate." data-verdict-1="Buon livello tecnico; qualche avviso da chiudere." data-verdict-2="Diversi avvisi tecnici: sicurezza, errori console, immagini." data-verdict-3="Problemi tecnici diffusi che indeboliscono affidabilità e sicurezza.">
  <div class="sr-dim-card__head"><p class="sr-eyebrow" style="margin:0">Best practice</p><span class="sr-dim-card__weight">Peso 10</span></div>
  <div class="sr-dim-card__score"><span class="sr-dim-card__score-value" data-sr-tool-score>—</span><span class="sr-dim-card__score-suffix">/100</span></div>
  <div class="sr-barra" style="height:8px;margin-top:12px"><div class="sr-barra__fill" data-sr-tool-fill style="width:0%"></div></div>
  <p class="sr-dim-card__word" data-sr-dim-word></p>
  <p class="sr-dim-card__findings" data-sr-tool-verdict></p>
  <p class="sr-dim-card__engine sr-mono">Google PageSpeed</p>
</div><div class="sr-card sr-dim-card" data-sr-dim="ai" data-verdict-0="4 segnali su 4: il sito è leggibile e citabile dai modelli AI." data-verdict-1="3 segnali su 4: manca poco alla piena prontezza AI." data-verdict-2="2 segnali su 4: dati strutturati o sitemap da completare." data-verdict-3="0–1 segnali: i modelli AI faticano a leggere e citare il sito.">
  <div class="sr-dim-card__head"><p class="sr-eyebrow" style="margin:0">Pronto per l’AI</p><span class="sr-dim-card__weight">Peso 10</span></div>
  <div class="sr-dim-card__score"><span class="sr-dim-card__score-value" data-sr-tool-score>—</span><span class="sr-dim-card__score-suffix">/100</span><span class="sr-dim-card__extra" data-sr-dim-extra></span></div>
  <div class="sr-barra" style="height:8px;margin-top:12px"><div class="sr-barra__fill" data-sr-tool-fill style="width:0%"></div></div>
  <p class="sr-dim-card__word" data-sr-dim-word></p>
  <p class="sr-dim-card__findings" data-sr-tool-verdict></p>
  <p class="sr-dim-card__engine sr-mono">4 segnali tecnici</p>
  <p class="sr-dim-card__more"><a data-sr-dim-more hidden target="_self">Approfondisci →</a></p>
</div><div class="sr-card sr-dim-card" data-sr-dim="co2" data-verdict-0="Pagina leggera: emissioni sotto la media del web." data-verdict-1="Vicino alla media; c’è margine per alleggerire." data-verdict-2="Sopra la media: la pagina è pesante da caricare." data-verdict-3="Molto sopra la media: pagina pesante, costo ambientale e di velocità.">
  <div class="sr-dim-card__head"><p class="sr-eyebrow" style="margin:0">Impatto CO₂</p><span class="sr-dim-card__weight">Peso 5</span></div>
  <div class="sr-dim-card__score"><span class="sr-dim-card__score-value" data-sr-tool-score>—</span><span class="sr-dim-card__score-suffix">/100</span></div>
  <div class="sr-barra" style="height:8px;margin-top:12px"><div class="sr-barra__fill" data-sr-tool-fill style="width:0%"></div></div>
  <p class="sr-dim-card__word" data-sr-dim-word></p>
  <p class="sr-dim-card__findings" data-sr-tool-verdict></p>
  <p class="sr-dim-card__engine sr-mono">Modello SWD</p>
  <p class="sr-dim-card__more"><a data-sr-dim-more hidden target="_self">Approfondisci →</a></p>
</div></div>
    </div>

    <div data-sr-checkup-priorities-wrap style="margin-top:32px">
      <p class="sr-eyebrow">Le priorità</p>
      <h2 class="wp-block-heading" style="font-size:clamp(24px,2.4vw,32px)">I 3 interventi che pesano di più</h2>
      <p style="margin:8px 0 20px;color:var(--sr-grigio);font-size:15.5px">Ordinati per impatto sul punteggio: quanto guadagnereste sistemandoli.</p>
      <div class="sr-priorities" data-sr-checkup-priorities></div>
    </div>

    <div data-sr-checkup-form-wrap style="margin-top:32px">
      <div class="sr-card sr-checkup-lead">
        <p class="sr-eyebrow">Report completo</p>
        <h2 class="wp-block-heading" style="font-size:clamp(22px,2.6vw,28px)">Il report completo, in PDF</h2>
        <p style="margin-top:10px;color:var(--sr-grigio);font-size:15.5px;line-height:1.6">Vi inviamo l’analisi integrale: una pagina per ognuna delle sette dimensioni, tutte le criticità rilevate e le raccomandazioni in ordine di impatto.</p>
        <ul class="sr-tool-audits" style="margin-top:18px">
          <li>Il punteggio di salute con i sette semafori</li>
          <li>Una pagina per dimensione: punteggio, cosa abbiamo trovato, cosa fare</li>
          <li>I tre interventi prioritari con le contromisure</li>
          <li>«Cosa faremmo noi» e i riferimenti di Studio Remarka</li>
        </ul>
        <form data-sr-checkup-report-form style="margin-top:24px">
          <p class="sr-hp-field" aria-hidden="true"><label>Sito web<input type="text" name="sr_checkup_hp" tabindex="-1" autocomplete="off"></label></p>
          <div class="sr-tool-row">
            <input type="email" placeholder="nome@vostraazienda.it" class="sr-text-input" required />
            <button type="submit" class="wp-block-button__link" style="padding:15px 26px">Inviatemi il report PDF</button>
          </div>
          <label class="sr-consent"><input type="checkbox" data-sr-checkup-consent required /><span>Ho letto la <a href="/privacy/">privacy policy</a> e acconsento all’invio del report e a essere ricontattato.</span></label>
          <label class="sr-consent"><input type="checkbox" data-sr-checkup-consent-monthly /><span>Inviatemi ogni mese il monitoraggio dei Core Web Vitals di questo sito.</span></label>
          <p class="sr-mono" data-sr-checkup-success hidden style="margin-top:16px;color:var(--sr-verde)">Fatto. Il report è in viaggio verso la vostra casella: se non arriva entro qualche minuto, controllate lo spam o scriveteci.</p>
          <p class="sr-form-error" data-sr-checkup-error hidden>Non siamo riusciti a inviare il report. Riprovate tra poco o scriveteci: ve lo mandiamo a mano.</p>
        </form>
        <p class="sr-mono" style="margin-top:20px;font-size:11px;color:var(--sr-grigio);opacity:.85">Niente spam. Usiamo l’indirizzo solo per il report ed eventuale ricontatto. Studio Remarka S.r.l., P.IVA GE 302230994.</p>
      </div>
    </div>

  </div>
</div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-section--bianco","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-section--bianco"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Come funziona</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">Tre passaggi, nessuna registrazione<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:group {"className":"","layout":{"type":"grid","minimumColumnWidth":"240px"}} -->
<div class="wp-block-group is-layout-grid" style="--sr-grid-min:240px"><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">01</p><p style="font-weight:500;margin-top:8px">Incollate l’indirizzo</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">La home o la pagina che porta più visite. Nessuna registrazione, nessun dato di pagamento.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">02</p><p style="font-weight:500;margin-top:8px">Analizziamo su sette fronti</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Un’unica interrogazione all’API Google PageSpeed (prestazioni, SEO, accessibilità, best practice) più le nostre verifiche su privacy/cookie e prontezza AI, letti dal nostro server come farebbe un visitatore.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">03</p><p style="font-weight:500;margin-top:8px">Leggete il punteggio e le priorità</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Salute 0–100, i sette semafori spiegati in italiano e i tre interventi che pesano di più. Il report completo arriva in PDF.</p></div></div>
<!-- /wp:group -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Il metodo</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">Che cosa misura davvero il check-up completo<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Dietro il punteggio non c’è una scatola nera. Quattro delle sette dimensioni — prestazioni, SEO, accessibilità e best practice — arrivano dall’API PageSpeed Insights di Google, la stessa che alimenta pagespeed.web.dev: interroghiamo Lighthouse in strategia mobile, perché è la versione del sito che Google usa per posizionarvi. Le altre tre le calcoliamo noi: la conformità privacy la leggiamo dall’HTML della pagina (banner, informative, tracker prima del consenso), la prontezza AI da quattro segnali tecnici — llms.txt, accesso ai crawler, dati strutturati, sitemap — e l’impronta di CO₂ dal peso reale della pagina, con il modello Sustainable Web Design.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Ogni dimensione entra nel voto con un peso dichiarato: le prestazioni valgono di più (25 su 100), la CO₂ di meno (5). È giusto sapere anche cosa il check-up non fa: non è un parere legale sulla privacy — è una verifica indicativa a quattro segnali — e non promette una posizione su Google. È la fotografia tecnica precisa del vostro sito, non una promessa di vendita.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-section--bianco","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-section--bianco"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Leggere il risultato</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">Come si legge lo stato di salute del sito<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Il punteggio di salute è la media pesata dei sette semafori, non un voto a sensazione. Si legge come un semaforo: da 90 in su siete in fascia verde (eccellente), da 75 a 89 è buono, tra 50 e 74 c’è margine concreto, sotto 50 è critico e diventa la priorità. Ogni dimensione porta lo stesso codice colore, così capite in un colpo d’occhio dove il sito è solido e dove perde punti.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Due letture da evitare. Un voto alto non significa «primi su Google»: significa che le fondamenta tecniche sono sane. E se una misura risulta «N/D» non è un guasto del vostro sito: a volte Google è saturo, a volte il sito rifiuta la lettura automatica. In quel caso calcoliamo la salute sulle misure riuscite e ve lo diciamo con chiarezza.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Tre domande tipiche</p>
<!-- /wp:paragraph -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Il punteggio è quello vero di Google?</summary><!-- wp:paragraph -->
<p>Per prestazioni, SEO, accessibilità e best practice sì: arrivano dall’API ufficiale PageSpeed Insights, strategia mobile. Privacy, prontezza AI e CO₂ sono nostre verifiche, con il metodo dichiarato in ogni sezione.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Il check-up GDPR sostituisce un consulente privacy?</summary><!-- wp:paragraph -->
<p>No. È una verifica tecnica indicativa a quattro segnali: intercetta i problemi evidenti — banner assente, tracker prima del consenso — ma non è un parere legale e non sostituisce un consulente.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Cosa ricevo nel report PDF che non vedo già a schermo?</summary><!-- wp:paragraph -->
<p>A schermo vedete il punteggio, i sette semafori e le tre priorità. Nel PDF trovate una pagina per dimensione con tutte le criticità rilevate, le raccomandazioni operative in ordine di impatto e cosa faremmo noi, con i nostri riferimenti aziendali.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-cta-band","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-cta-band"><!-- wp:heading -->
<h2 class="wp-block-heading">Vogliamo sistemare noi le priorità<span class="sr-accent-dot">?</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="margin-top:12px">Dal punteggio al preventivo: analizziamo il report insieme e vi diamo un piano d’intervento a prezzo chiuso, con PageSpeed 90+ garantito da contratto.</p>
<!-- /wp:paragraph -->
<!-- wp:buttons {"style":{"spacing":{"blockGap":"14px","margin":{"top":"28px"}}},"layout":{"type":"flex","justifyContent":"center"}} -->
<div class="wp-block-buttons" style="margin-top:28px"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/#contatti">Richiedi la consulenza — gratis</a></div>
<!-- /wp:button -->
<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/strumenti/">Vedi tutti gli strumenti</a></div>
<!-- /wp:button -->
</div>
<!-- /wp:buttons -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-section--bianco","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-section--bianco"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Gli altri strumenti gratuiti</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<div class="sr-servizi-rows"><div><span class="sr-mono" style="color:var(--sr-oltremare)">/01</span><a href="/strumenti/test-velocita/" style="color:var(--sr-inchiostro);font-size:15.5px">Test velocità</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/02</span><a href="/strumenti/analisi-seo/" style="color:var(--sr-inchiostro);font-size:15.5px">Analisi SEO on-page</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/03</span><a href="/strumenti/check-gdpr/" style="color:var(--sr-inchiostro);font-size:15.5px">Check GDPR e cookie</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/04</span><a href="/strumenti/roi-localizzazione/" style="color:var(--sr-inchiostro);font-size:15.5px">ROI localizzazione</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/05</span><a href="/strumenti/verifica-accessibilita/" style="color:var(--sr-inchiostro);font-size:15.5px">Verifica accessibilità</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/06</span><a href="/strumenti/sito-pronto-ai/" style="color:var(--sr-inchiostro);font-size:15.5px">Sito pronto per l’AI</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/07</span><a href="/strumenti/impatto-co2/" style="color:var(--sr-inchiostro);font-size:15.5px">Impatto CO₂</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/08</span><a href="/strumenti/segnali-eeat/" style="color:var(--sr-inchiostro);font-size:15.5px">Segnali E-E-A-T</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/09</span><a href="/strumenti/sito-letto-dallai/" style="color:var(--sr-inchiostro);font-size:15.5px">Il vostro sito, letto dall’AI</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/10</span><a href="/strumenti/suona-madrelingua/" style="color:var(--sr-inchiostro);font-size:15.5px">Suona madrelingua?</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/11</span><a href="/strumenti/generatore-llms-txt/" style="color:var(--sr-inchiostro);font-size:15.5px">Generatore di llms.txt</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div></div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
