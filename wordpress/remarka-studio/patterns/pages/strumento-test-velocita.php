<?php
/**
 * Title: Pagina — Strumento: Test velocità
 * Slug: remarka-studio/strumento-test-velocita
 * Categories: remarka-pagine
 * Description: Strumento gratuito Test velocità: widget interattivo, come funziona, FAQ, CTA.
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","className":"sr-section sr-hero","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-hero"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Strumento gratuito /01</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"level":1,"style":{"typography":{"fontSize":"clamp(34px,4vw,52px)"}}} -->
<h1 class="wp-block-heading" style="font-size:clamp(34px,4vw,52px)">Test velocità sito web: il punteggio reale di Google<span class="sr-accent-dot">.</span></h1>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="max-width:100%">Punteggio Google PageSpeed e le tre metriche che lo determinano — LCP, INP, CLS — spiegate in italiano. Strategia mobile, dati reali dall’API di Google. Senza registrazione.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:html -->

<div class="sr-tool-widget sr-card" data-sr-tool="speed" data-sr-locale="it">
  <form data-sr-tool-form>
    <div class="sr-tool-row">
      <input type="text" placeholder="www.tuosito.it" class="sr-text-input" required />
      <button type="submit" class="wp-block-button__link" style="padding:17px 30px">Avvia il test</button>
    </div>
  <p class="sr-tool-pending sr-mono" data-sr-tool-pending hidden>Rilevazione Google in corso — mobile, può richiedere fino a 30 secondi<span class="sr-blink">…</span></p>
  <div class="sr-tool-result" data-sr-tool-result hidden>
    <p style="margin:0;font-size:14px;color:var(--sr-grigio)" data-sr-tool-url></p>
    <div class="sr-tool-result__score">
      <span class="sr-mono" data-sr-tool-score>0</span><span class="sr-mono" style="font-size:18px;color:var(--sr-grigio)">/100</span>
    </div>
    <div class="sr-barra" style="height:10px">
      <div class="sr-barra__fill" data-sr-tool-fill style="width:0%"></div>
      <span class="sr-barra__tick" style="left:90%"></span>
    </div>
    <div style="display:flex;justify-content:space-between;margin-top:8px;font-family:var(--sr-font-mono);font-size:11px;color:var(--sr-grigio)"><span>0</span><span>50</span><span>90</span><span>100</span></div>
    <p style="margin-top:20px;font-size:15.5px;color:var(--sr-grigio)" data-sr-tool-verdict></p>
    <div class="sr-tool-cwv">
      <div><p class="sr-eyebrow" style="margin-bottom:8px">LCP</p><p class="sr-tool-cwv-value sr-mono" data-sr-tool-lcp></p><p style="font-size:13.5px;color:var(--sr-grigio)">Tempo di caricamento del contenuto principale. Sotto i 2,5 s è considerato buono.</p></div>
      <div><p class="sr-eyebrow" style="margin-bottom:8px">INP</p><p class="sr-tool-cwv-value sr-mono" data-sr-tool-inp></p><p style="font-size:13.5px;color:var(--sr-grigio)">Reattività del sito al tocco. Sotto i 200 ms è considerato buono.</p></div>
      <div><p class="sr-eyebrow" style="margin-bottom:8px">CLS</p><p class="sr-tool-cwv-value sr-mono" data-sr-tool-cls></p><p style="font-size:13.5px;color:var(--sr-grigio)">Stabilità visiva durante il caricamento. Sotto 0,1 è considerato buono.</p></div>
    </div>
    <p class="sr-tool-caption sr-mono">Dati reali da Google PageSpeed Insights API — strategia mobile. LCP e CLS da analisi Lighthouse; INP da dati di campo Chrome UX quando disponibili.</p>
  </div>
  </form>
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
<div class="wp-block-group is-layout-grid" style="--sr-grid-min:240px"><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">01</p><p style="font-weight:500;margin-top:8px">Incollate l’indirizzo</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Scrivete l’URL del sito: la home o la pagina interna che porta più visite.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">02</p><p style="font-weight:500;margin-top:8px">Misuriamo con Google</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Interroghiamo l’API PageSpeed Insights in strategia mobile — gli stessi dati che Google usa per il posizionamento.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">03</p><p style="font-weight:500;margin-top:8px">Leggete cosa frena il sito</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Punteggio 0–100 e le tre metriche Core Web Vitals spiegate in italiano, senza gergo tecnico.</p></div></div>
<!-- /wp:group -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Il metodo</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">Cosa misura davvero questo test dei tempi di caricamento<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Dietro il punteggio c’è un motore solo: l’API PageSpeed Insights di Google, la stessa che alimenta pagespeed.web.dev. Interroghiamo Lighthouse in strategia mobile, perché è la versione del sito che Google usa per posizionarvi. Il numero da 0 a 100 nasce in laboratorio, con un telefono e una connessione simulati e standardizzati: così due misurazioni della stessa pagina restano confrontabili nel tempo. Dove il vostro sito riceve abbastanza traffico reale, aggiungiamo anche i Core Web Vitals raccolti sul campo dagli utenti veri di Chrome.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">È giusto sapere cosa questo test non guarda. Non giudica la qualità dei testi, non conta i link in entrata, non misura la sicurezza del server né quanto vendete: pesa solo l’esperienza di caricamento di una singola pagina. Un punteggio alto non è la promessa di un primo posto su Google, ma una base tecnica sana su cui tutto il resto lavora meglio. Preferiamo dirlo chiaro: è la fotografia precisa di un aspetto, non la diagnosi completa del sito.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-section--bianco","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-section--bianco"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Leggere il risultato</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">Come leggere il punteggio delle prestazioni del sito<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Il risultato si legge come un semaforo. Da 90 a 100 siete in fascia verde: la pagina compare in fretta anche in mobilità, sul 4G di città come ai bordi della copertura. Tra 50 e 89 la velocità è nella media del web italiano, con margini concreti di guadagno. Sotto 50 siete nel rosso: buona parte dei visitatori da smartphone se ne va prima che appaia la prima riga, e ogni euro investito in pubblicità rende molto meno.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Due falsi allarmi ricorrenti. Il valore oscilla di qualche punto tra una prova e l’altra: è normale, dipende dai server di misura di Google, non dal vostro sito — contano i grandi salti, non i due punti di scarto. E non spaventatevi se il desktop segna 95 e il mobile 40: quasi tutti i siti hanno questo divario, ma è il mobile a decidere la classifica. Guardate sempre quel numero.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Tre domande tipiche</p>
<!-- /wp:paragraph -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Il punteggio è quello vero di Google?</summary><!-- wp:paragraph -->
<p>Sì: arriva dall’API ufficiale PageSpeed Insights, strategia mobile. È lo stesso motore che trovate su pagespeed.web.dev.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Perché misurate solo il mobile?</summary><!-- wp:paragraph -->
<p>Perché Google indicizza e classifica in base alla versione mobile del sito. Il punteggio desktop, più alto quasi ovunque, conta poco per il posizionamento.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Un punteggio basso danneggia le vendite?</summary><!-- wp:paragraph -->
<p>Sotto i 50, gran parte dei visitatori da mobile abbandona prima del caricamento completo: le campagne portano clic che non diventano richieste.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-section--bianco","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-section--bianco"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Come migliorare</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">Come velocizzare il sito web: cinque interventi concreti<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"base"} -->
<p class="has-grigio-color has-text-color has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:12px">Un punteggio basso nasce quasi sempre dalle stesse cause, e le prime sono anche le più economiche da correggere.</p>
<!-- /wp:paragraph -->
<!-- wp:group {"className":"","layout":{"type":"grid","minimumColumnWidth":"240px"}} -->
<div class="wp-block-group is-layout-grid" style="--sr-grid-min:240px"><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">01</p><p style="font-weight:500;margin-top:8px">Alleggerite le immagini</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Convertite le fotografie in WebP o AVIF e attivate il caricamento differito: è la causa numero uno della lentezza e spesso, da sola, dimezza i tempi di attesa.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">02</p><p style="font-weight:500;margin-top:8px">Attivate la cache</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Una cache di pagina e del browser evita al server di ricostruire tutto a ogni visita: mezza giornata di lavoro, risultato misurabile da subito.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">03</p><p style="font-weight:500;margin-top:8px">Sfoltite CSS e JavaScript</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Portate in linea il CSS critico, rimandate il resto e togliete gli script di terze parti che non servono: meno codice da eseguire, prima visualizzazione più rapida.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">04</p><p style="font-weight:500;margin-top:8px">Scegliete un hosting all’altezza</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Un server condiviso e sovraffollato risponde in un secondo prima ancora di iniziare: un hosting adeguato, con una CDN davanti, taglia quell’attesa iniziale.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">05</p><p style="font-weight:500;margin-top:8px">Controllate i font</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Limitate le famiglie di caratteri, precaricate quelle essenziali e usate font-display swap, così il testo appare subito invece di restare invisibile.</p></div></div>
<!-- /wp:group -->
<!-- wp:html -->
<div style="margin-top:24px;display:flex;flex-direction:column;gap:8px;align-items:flex-start"><p class="sr-card-link" style="margin-top:12px"><a href="/servizi/restyling-migrazione/">Vogliamo intervenire noi: scopri il restyling tecnico →</a></p><p class="sr-card-link" style="margin-top:12px"><a href="/blog/sito-lento-cause-costi/">Approfondisci: le 7 cause reali di un sito lento →</a></p></div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-dark","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-dark"><!-- wp:heading -->
<h2 class="wp-block-heading">Vogliamo sistemare noi questi problemi<span class="sr-accent-dot">?</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="margin-top:12px">Report gratuito con le cause, le priorità e un preventivo chiuso: PageSpeed 90+ garantito da contratto.</p>
<!-- /wp:paragraph -->
<!-- wp:buttons {"style":{"spacing":{"blockGap":"14px","margin":{"top":"28px"}}},"layout":{"type":"flex","justifyContent":"center"}} -->
<div class="wp-block-buttons" style="margin-top:28px"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/#contatti">Richiedi l’analisi completa</a></div>
<!-- /wp:button -->
<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/servizi/seo-tecnica/">Scopri la SEO tecnica</a></div>
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
<div class="sr-servizi-rows"><div><span class="sr-mono" style="color:var(--sr-oltremare)">/02</span><a href="/strumenti/analisi-seo/" style="color:var(--sr-inchiostro);font-size:15.5px">Analisi SEO on-page</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/03</span><a href="/strumenti/check-gdpr/" style="color:var(--sr-inchiostro);font-size:15.5px">Check GDPR e cookie</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/04</span><a href="/strumenti/roi-localizzazione/" style="color:var(--sr-inchiostro);font-size:15.5px">ROI localizzazione</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/05</span><a href="/strumenti/verifica-accessibilita/" style="color:var(--sr-inchiostro);font-size:15.5px">Verifica accessibilità</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/06</span><a href="/strumenti/sito-pronto-ai/" style="color:var(--sr-inchiostro);font-size:15.5px">Sito pronto per l’AI</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/07</span><a href="/strumenti/impatto-co2/" style="color:var(--sr-inchiostro);font-size:15.5px">Impatto CO₂</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div></div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
