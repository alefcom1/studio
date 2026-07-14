<?php
/**
 * Title: Pagina — Strumento: Check GDPR e cookie
 * Slug: remarka-studio/strumento-check-gdpr
 * Categories: remarka-pagine
 * Description: Strumento gratuito Check GDPR e cookie: widget interattivo, come funziona, FAQ, CTA.
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","className":"sr-section sr-hero","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-hero"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Strumento gratuito /03</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"level":1,"style":{"typography":{"fontSize":"clamp(34px,4vw,52px)"}}} -->
<h1 class="wp-block-heading" style="font-size:clamp(34px,4vw,52px)">Il vostro sito è a norma GDPR?<span class="sr-accent-dot">.</span></h1>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="max-width:100%">Controlliamo banner cookie, informative e tracker attivi prima del consenso: quattro verifiche per capire cosa manca. È una verifica indicativa, non una consulenza legale.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:html -->

<div class="sr-tool-widget sr-card" data-sr-tool="gdpr" data-sr-locale="it"
     data-label-cmp-yes="Cookie banner rilevato" data-label-cmp-no="Nessun cookie banner rilevato"
     data-label-policy-yes="Link a privacy/cookie policy presente" data-label-policy-no="Nessun link a privacy/cookie policy"
     data-label-trackers-clean="Nessun tracker nell’HTML iniziale"
     data-label-trackers-flag="Tracker attivi senza banner"
     data-label-trackers-ok="Tracker presenti (con banner)"
     data-label-external="{n} domini esterni caricano script"
     data-err="Non siamo riusciti a leggere il sito. Riprovate tra qualche minuto.">
  <form data-sr-tool-form>
    <div class="sr-tool-row">
      <input type="text" placeholder="www.tuosito.it" class="sr-text-input" required />
      <button type="submit" class="wp-block-button__link" style="padding:17px 30px">Controlla il sito</button>
    </div>
  </form>
  <p class="sr-tool-pending sr-mono" data-sr-tool-pending hidden>Lettura del sito in corso<span class="sr-blink">…</span></p>
  <div class="sr-tool-result" data-sr-tool-result hidden>
    <ul class="sr-gdpr-rows">
      <li><span class="sr-gdpr-key">Cookie banner</span><span data-sr-tool-cmp data-sr-flag></span></li>
      <li><span class="sr-gdpr-key">Policy</span><span data-sr-tool-policy data-sr-flag></span></li>
      <li><span class="sr-gdpr-key">Tracker</span><span data-sr-tool-trackers data-sr-flag></span></li>
      <li><span class="sr-gdpr-key">Script esterni</span><span data-sr-tool-external data-sr-flag></span></li>
    </ul>
    <p class="sr-disclaimer" data-sr-tool-disclaimer>Verifica indicativa, non una consulenza legale. Un audit GDPR completo richiede la verifica manuale di cookie, finalità e basi giuridiche.</p>
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
<div class="wp-block-group is-layout-grid" style="--sr-grid-min:240px"><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">01</p><p style="font-weight:500;margin-top:8px">Inserite l’indirizzo del sito</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Leggiamo la home page dal nostro server, come farebbe un visitatore alla prima apertura.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">02</p><p style="font-weight:500;margin-top:8px">Quattro controlli automatici</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Cerchiamo il cookie banner (CMP), i link a privacy e cookie policy, i tracker caricati prima del consenso e i domini esterni.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">03</p><p style="font-weight:500;margin-top:8px">Semaforo, non sentenza</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Ogni punto è verde, giallo o rosso: segnaliamo i problemi evidenti, non un audit legale completo.</p></div></div>
<!-- /wp:group -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Tre domande tipiche</p>
<!-- /wp:paragraph -->
<!-- wp:details -->
<details class="wp-block-details"><summary>È un parere legale?</summary><!-- wp:paragraph -->
<p>No, ed è importante dirlo: è una verifica automatica indicativa, non una consulenza legale. Segnala i problemi tecnici evidenti; la conformità piena va valutata da un consulente privacy.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Cosa vuol dire «tracker senza banner»?</summary><!-- wp:paragraph -->
<p>Che nell’HTML iniziale della pagina troviamo strumenti di tracciamento (Google Analytics, Meta Pixel e simili) attivi prima che l’utente accetti. È il segnale rosso più frequente sui siti italiani.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Perché il Garante è così severo sui cookie?</summary><!-- wp:paragraph -->
<p>Perché il consenso deve essere libero, informato e documentabile: rifiutare deve essere facile quanto accettare, e nessun tracker pubblicitario può partire prima del sì.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-dark","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-dark"><!-- wp:heading -->
<h2 class="wp-block-heading">Vogliamo mettere il sito a norma<span class="sr-accent-dot">?</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="margin-top:12px">Banner, informative e consensi conformi al Garante, inclusi in ogni sito aziendale che consegniamo.</p>
<!-- /wp:paragraph -->
<!-- wp:buttons {"style":{"spacing":{"blockGap":"14px","margin":{"top":"28px"}}},"layout":{"type":"flex","justifyContent":"center"}} -->
<div class="wp-block-buttons" style="margin-top:28px"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/servizi/siti-aziendali/">Scopri i siti aziendali</a></div>
<!-- /wp:button -->
<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/#contatti">Richiedi un’analisi</a></div>
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
<div class="sr-servizi-rows"><div><span class="sr-mono" style="color:var(--sr-oltremare)">/01</span><a href="/strumenti/test-velocita/" style="color:var(--sr-inchiostro);font-size:15.5px">Test velocità</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/02</span><a href="/strumenti/analisi-seo/" style="color:var(--sr-inchiostro);font-size:15.5px">Analisi SEO on-page</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/04</span><a href="/strumenti/roi-localizzazione/" style="color:var(--sr-inchiostro);font-size:15.5px">ROI localizzazione</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/05</span><a href="/strumenti/verifica-accessibilita/" style="color:var(--sr-inchiostro);font-size:15.5px">Verifica accessibilità</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/06</span><a href="/strumenti/sito-pronto-ai/" style="color:var(--sr-inchiostro);font-size:15.5px">Sito pronto per l’AI</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/07</span><a href="/strumenti/impatto-co2/" style="color:var(--sr-inchiostro);font-size:15.5px">Impatto CO₂</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div></div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
