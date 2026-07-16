<?php
/**
 * Title: Pagina — Strumento: Impatto CO₂
 * Slug: remarka-studio/strumento-impatto-co2
 * Categories: remarka-pagine
 * Description: Strumento gratuito Impatto CO₂: widget interattivo, come funziona, FAQ, CTA.
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","className":"sr-section sr-hero","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-hero"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Strumento gratuito /07</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"level":1,"style":{"typography":{"fontSize":"clamp(34px,4vw,52px)"}}} -->
<h1 class="wp-block-heading" style="font-size:clamp(34px,4vw,52px)">Impatto CO₂ del vostro sito web<span class="sr-accent-dot">.</span></h1>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="max-width:100%">Ogni visita al sito consuma energia e produce CO₂. Misuriamo il peso della vostra pagina e stimiamo le emissioni per visita e all’anno, con il modello Sustainable Web Design. Un sito leggero è anche un sito veloce.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:html -->

<div class="sr-tool-widget sr-card" data-sr-tool="co2" data-sr-locale="it"
     data-co2-average="0.8" data-co2-visits="10000"
     data-label-unit-year="kg CO₂e / anno"
     data-verdict-good="Sotto la media del web: pagina leggera, bene così."
     data-verdict-mid="Vicino alla media del web: c’è margine per alleggerire."
     data-verdict-poor="Sopra la media del web: pagina pesante, conviene ottimizzare."
     data-err="Non siamo riusciti a misurare il peso della pagina. Riprovate.">
  <form data-sr-tool-form>
    <div class="sr-tool-row">
      <input type="text" placeholder="www.tuosito.it" class="sr-text-input" required />
      <button type="submit" class="wp-block-button__link" style="padding:17px 30px">Misura l’impatto</button>
    </div>
  </form>
  <p class="sr-tool-pending sr-mono" data-sr-tool-pending hidden>Misurazione in corso<span class="sr-blink">…</span></p>
  <div class="sr-tool-result" data-sr-tool-result hidden>
    <p style="margin:0;font-size:14px;color:var(--sr-grigio)" data-sr-tool-url></p>
    <div class="sr-tool-result__score">
      <span class="sr-mono" data-sr-tool-grams>0 g</span>
    </div>
    <div class="sr-barra" style="height:10px;margin-top:8px"><div class="sr-barra__fill" data-sr-tool-fill style="width:0%"></div><span class="sr-barra__tick" style="left:50%"></span></div>
    <p style="margin-top:20px;font-size:15.5px;color:var(--sr-grigio)" data-sr-tool-verdict></p>
    <div class="sr-tool-cwv">
      <div><p class="sr-eyebrow" style="margin-bottom:8px">Peso pagina</p><p class="sr-tool-cwv-value sr-mono" data-sr-tool-weight></p></div>
      <div><p class="sr-eyebrow" style="margin-bottom:8px">Stima annua</p><p class="sr-tool-cwv-value sr-mono" data-sr-tool-year></p></div>
    </div>
    <p class="sr-tool-caption sr-mono">Modello Sustainable Web Design (co2.js, Apache-2.0). Stima per visita; anno calcolato su 10.000 visite/mese.</p>
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
<div class="wp-block-group is-layout-grid" style="--sr-grid-min:240px"><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">01</p><p style="font-weight:500;margin-top:8px">Inserite l’indirizzo</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">La pagina da misurare: di solito la home, la più visitata.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">02</p><p style="font-weight:500;margin-top:8px">Pesiamo la pagina</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Con l’API PageSpeed misuriamo i byte totali che il browser deve scaricare per mostrare la pagina.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">03</p><p style="font-weight:500;margin-top:8px">Stima delle emissioni</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Applichiamo il modello Sustainable Web Design (co2.js) e otteniamo i grammi di CO₂e per visita, il confronto con la media del web e la stima annua.</p></div></div>
<!-- /wp:group -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Il metodo</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">Come stimiamo davvero le emissioni della pagina<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Il calcolo parte da un dato concreto e misurabile: con l’API PageSpeed pesiamo tutti i byte che il browser deve scaricare per mostrare la vostra pagina. Su quel peso applichiamo il modello Sustainable Web Design della Green Web Foundation — le stesse formule della libreria open source co2.js — che traduce i byte trasferiti in energia consumata lungo la catena (data center, rete, dispositivo) e infine in grammi di CO₂ equivalente per visita.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">È una stima, ed è giusto trattarla come tale. Il modello usa coefficienti medi mondiali per l’intensità energetica e per il mix elettrico: non conosce l’energia reale del vostro hosting né il comportamento esatto di ogni visitatore. Non è una misura certificata di impronta ambientale, ma un ordine di grandezza affidabile e confrontabile. Il pregio è che si lega a un fatto tecnico — il peso — su cui potete davvero intervenire.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-section--bianco","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-section--bianco"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Leggere il risultato</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">Come leggere i grammi di CO₂ per visita<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Il numero chiave è la CO₂ equivalente per singola visita, che confrontiamo con la media del web, intorno agli 0,8 grammi. Sotto quella soglia siete tra i siti leggeri; sensibilmente sopra, la pagina è più pesante della media e c’è margine per alleggerirla. La stima annua moltiplica quel valore per un traffico di riferimento: cambiando le visite reali del vostro sito, l’impatto cresce o cala in proporzione.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Il confronto conta più del valore assoluto. Pochi grammi per visita sembrano nulla, ma moltiplicati per decine di migliaia di visite al mese diventano una cifra concreta, e soprattutto sono lo specchio di una pagina pesante: quasi sempre chi inquina di più è anche chi carica più lentamente. Leggete quindi l’impatto come un secondo indicatore delle prestazioni, non solo come una questione ambientale.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Tre domande tipiche</p>
<!-- /wp:paragraph -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Come calcolate le emissioni?</summary><!-- wp:paragraph -->
<p>Con il modello Sustainable Web Design della Green Web Foundation (libreria co2.js, Apache-2.0): dal peso della pagina all’energia consumata, fino ai grammi di CO₂e. È una stima con coefficienti medi mondiali.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Perché un sito leggero inquina meno?</summary><!-- wp:paragraph -->
<p>Perché ogni byte trasferito consuma energia — nel data center, nella rete, sul vostro dispositivo. Meno peso significa meno energia, meno emissioni e, come effetto collaterale, un sito più veloce.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
<!-- wp:details -->
<details class="wp-block-details"><summary>La stima annua da dove viene?</summary><!-- wp:paragraph -->
<p>Moltiplichiamo le emissioni per visita per un traffico di riferimento di 10.000 visite al mese. Cambiando il traffico reale del vostro sito, cambia la stima proporzionalmente.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-section--bianco","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-section--bianco"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Come migliorare</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">Come ridurre l’impronta di carbonio del sito<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"base"} -->
<p class="has-grigio-color has-text-color has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:12px">Ridurre le emissioni e velocizzare il sito sono la stessa cosa: entrambe passano dal tagliare peso inutile.</p>
<!-- /wp:paragraph -->
<!-- wp:group {"className":"","layout":{"type":"grid","minimumColumnWidth":"240px"}} -->
<div class="wp-block-group is-layout-grid" style="--sr-grid-min:240px"><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">01</p><p style="font-weight:500;margin-top:8px">Alleggerite le immagini</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Le fotografie sono quasi sempre la voce più pesante: convertitele in WebP o AVIF con caricamento differito e taglierete gran parte dei byte, e quindi delle emissioni.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">02</p><p style="font-weight:500;margin-top:8px">Riducete script e font</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Ogni libreria di terze parti e ogni famiglia di caratteri in più è energia trasferita a ogni visita: tenete solo ciò che serve davvero.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">03</p><p style="font-weight:500;margin-top:8px">Sfruttate cache e CDN</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Una buona cache e una rete di distribuzione evitano di trasferire gli stessi contenuti mille volte: meno traffico ripetuto, meno consumo.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">04</p><p style="font-weight:500;margin-top:8px">Scegliete un hosting verde</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Un provider alimentato da energia rinnovabile abbassa l’intensità di carbonio di ogni byte servito: è la leva più semplice per un effetto immediato.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">05</p><p style="font-weight:500;margin-top:8px">Preferite un design sobrio</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Niente video in riproduzione automatica o animazioni pesanti dove non servono: un’estetica pulita consuma meno e, spesso, comunica meglio.</p></div></div>
<!-- /wp:group -->
<!-- wp:html -->
<div style="margin-top:24px;display:flex;flex-direction:column;gap:8px;align-items:flex-start"><p class="sr-card-link" style="margin-top:12px"><a href="/servizi/restyling-migrazione/">Vogliamo alleggerirlo noi: scopri il restyling tecnico →</a></p><p class="sr-card-link" style="margin-top:12px"><a href="/blog/sito-lento-cause-costi/">Approfondisci: le 7 cause di un sito lento →</a></p><p class="sr-card-link" style="margin-top:12px"><a href="/blog/impatto-ambientale-sito-web/">Guida: quanto pesa il vostro sito sull’ambiente (e sul portafoglio) →</a></p></div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-dark","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-dark"><!-- wp:heading -->
<h2 class="wp-block-heading">Vogliamo alleggerire il sito<span class="sr-accent-dot">?</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="margin-top:12px">Immagini ottimizzate, base tecnica pulita, meno peso a parità di contenuti: meno CO₂ e PageSpeed 90+ da contratto.</p>
<!-- /wp:paragraph -->
<!-- wp:buttons {"style":{"spacing":{"blockGap":"14px","margin":{"top":"28px"}}},"layout":{"type":"flex","justifyContent":"center"}} -->
<div class="wp-block-buttons" style="margin-top:28px"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/servizi/restyling-migrazione/">Restyling e migrazione</a></div>
<!-- /wp:button -->
<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/strumenti/test-velocita/">Misura la velocità</a></div>
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
<div class="sr-servizi-rows"><div><span class="sr-mono" style="color:var(--sr-oltremare)">/00</span><a href="/strumenti/check-up-completo/" style="color:var(--sr-inchiostro);font-size:15.5px">Check-up completo</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/01</span><a href="/strumenti/test-velocita/" style="color:var(--sr-inchiostro);font-size:15.5px">Test velocità</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/02</span><a href="/strumenti/analisi-seo/" style="color:var(--sr-inchiostro);font-size:15.5px">Analisi SEO on-page</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/03</span><a href="/strumenti/check-gdpr/" style="color:var(--sr-inchiostro);font-size:15.5px">Check GDPR e cookie</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/04</span><a href="/strumenti/roi-localizzazione/" style="color:var(--sr-inchiostro);font-size:15.5px">ROI localizzazione</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/05</span><a href="/strumenti/verifica-accessibilita/" style="color:var(--sr-inchiostro);font-size:15.5px">Verifica accessibilità</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/06</span><a href="/strumenti/sito-pronto-ai/" style="color:var(--sr-inchiostro);font-size:15.5px">Sito pronto per l’AI</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/08</span><a href="/strumenti/segnali-eeat/" style="color:var(--sr-inchiostro);font-size:15.5px">Segnali E-E-A-T</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div></div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
