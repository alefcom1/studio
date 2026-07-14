<?php
/**
 * Title: Pagina — Strumento: Sito pronto per l’AI
 * Slug: remarka-studio/strumento-sito-pronto-ai
 * Categories: remarka-pagine
 * Description: Strumento gratuito Sito pronto per l’AI: widget interattivo, come funziona, FAQ, CTA.
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","className":"sr-section sr-hero","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-hero"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Strumento gratuito /06</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"level":1,"style":{"typography":{"fontSize":"clamp(34px,4vw,52px)"}}} -->
<h1 class="wp-block-heading" style="font-size:clamp(34px,4vw,52px)">Il vostro sito è pronto per l’AI?<span class="sr-accent-dot">.</span></h1>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="max-width:100%">Quando ChatGPT, Claude o Perplexity leggono il web, trovano il vostro sito? Controlliamo quattro segnali: llms.txt, accesso dei crawler AI, dati strutturati e sitemap. Senza registrazione.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:html -->

<div class="sr-tool-widget sr-card" data-sr-tool="ai" data-sr-locale="it"
     data-label-yes="Sì" data-label-no="No" data-label-partial="Parziale"
     data-err="Non siamo riusciti a leggere il sito. Riprovate tra qualche minuto.">
  <form data-sr-tool-form>
    <div class="sr-tool-row">
      <input type="text" placeholder="www.tuosito.it" class="sr-text-input" required />
      <button type="submit" class="wp-block-button__link" style="padding:17px 30px">Verifica la prontezza AI</button>
    </div>
  </form>
  <p class="sr-tool-pending sr-mono" data-sr-tool-pending hidden>Verifica in corso<span class="sr-blink">…</span></p>
  <div class="sr-tool-result" data-sr-tool-result hidden>
    <div class="sr-tool-result__score">
      <span class="sr-mono" data-sr-tool-score>0/4</span>
    </div>
    <ul class="sr-gdpr-rows">
      <li><span class="sr-gdpr-key">llms.txt</span><span data-sr-tool-llms data-sr-flag></span></li>
      <li><span class="sr-gdpr-key">Crawler AI</span><span data-sr-tool-robots data-sr-flag></span></li>
      <li><span class="sr-gdpr-key">JSON-LD</span><span data-sr-tool-jsonld data-sr-flag></span></li>
      <li><span class="sr-gdpr-key">Sitemap</span><span data-sr-tool-sitemap data-sr-flag></span></li>
    </ul>
    <p class="sr-tool-caption sr-mono">Controlla llms.txt, l’accesso dei crawler AI (GPTBot, ClaudeBot, PerplexityBot, Google-Extended), i dati strutturati JSON-LD e la sitemap.</p>
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
<div class="wp-block-group is-layout-grid" style="--sr-grid-min:240px"><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">01</p><p style="font-weight:500;margin-top:8px">Inserite l’indirizzo del sito</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Leggiamo dal nostro server alcuni file pubblici e l’HTML della home page.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">02</p><p style="font-weight:500;margin-top:8px">Quattro verifiche</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Cerchiamo il file llms.txt, controlliamo se robots.txt lascia passare i crawler AI (GPTBot, ClaudeBot, PerplexityBot, Google-Extended), i dati strutturati JSON-LD e la sitemap.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">03</p><p style="font-weight:500;margin-top:8px">Punteggio N su 4</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Un semaforo per ogni segnale e un punteggio complessivo, con le indicazioni su cosa aggiungere per farsi trovare e citare dai modelli.</p></div></div>
<!-- /wp:group -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Tre domande tipiche</p>
<!-- /wp:paragraph -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Cos’è il file llms.txt?</summary><!-- wp:paragraph -->
<p>Una proposta di standard: un file di testo in Markdown che riassume ai modelli AI cosa contiene il sito e come citarlo, come fa robots.txt per i motori di ricerca. È giovane, ma sempre più diffuso.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Conviene far entrare i crawler AI?</summary><!-- wp:paragraph -->
<p>Dipende dagli obiettivi: bloccarli protegge i contenuti, ma vi esclude dalle risposte generate. Per la maggior parte delle aziende, essere citati da ChatGPT o Perplexity è visibilità in più.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
<!-- wp:details -->
<details class="wp-block-details"><summary>I dati strutturati servono ancora?</summary><!-- wp:paragraph -->
<p>Sì, più che mai: i dati JSON-LD (schema.org) aiutano sia Google sia i modelli AI a capire chi siete, cosa offrite e a chi. Sono la base di ogni buona indicizzazione.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-dark","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-dark"><!-- wp:heading -->
<h2 class="wp-block-heading">Vogliamo preparare il sito per l’AI<span class="sr-accent-dot">?</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="margin-top:12px">Dati strutturati, file corretti e struttura leggibile dalle macchine: fa parte della SEO tecnica che consegniamo.</p>
<!-- /wp:paragraph -->
<!-- wp:buttons {"style":{"spacing":{"blockGap":"14px","margin":{"top":"28px"}}},"layout":{"type":"flex","justifyContent":"center"}} -->
<div class="wp-block-buttons" style="margin-top:28px"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/servizi/seo-tecnica/">Scopri la SEO tecnica</a></div>
<!-- /wp:button -->
<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/strumenti/analisi-seo/">Analizza la SEO on-page</a></div>
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
<div class="sr-servizi-rows"><div><span class="sr-mono" style="color:var(--sr-oltremare)">/01</span><a href="/strumenti/test-velocita/" style="color:var(--sr-inchiostro);font-size:15.5px">Test velocità</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/02</span><a href="/strumenti/analisi-seo/" style="color:var(--sr-inchiostro);font-size:15.5px">Analisi SEO on-page</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/03</span><a href="/strumenti/check-gdpr/" style="color:var(--sr-inchiostro);font-size:15.5px">Check GDPR e cookie</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/04</span><a href="/strumenti/roi-localizzazione/" style="color:var(--sr-inchiostro);font-size:15.5px">ROI localizzazione</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/05</span><a href="/strumenti/verifica-accessibilita/" style="color:var(--sr-inchiostro);font-size:15.5px">Verifica accessibilità</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/07</span><a href="/strumenti/impatto-co2/" style="color:var(--sr-inchiostro);font-size:15.5px">Impatto CO₂</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div></div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
