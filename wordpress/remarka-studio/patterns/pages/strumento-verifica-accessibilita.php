<?php
/**
 * Title: Pagina — Strumento: Verifica accessibilità
 * Slug: remarka-studio/strumento-verifica-accessibilita
 * Categories: remarka-pagine
 * Description: Strumento gratuito Verifica accessibilità: widget interattivo, come funziona, FAQ, CTA.
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","className":"sr-section sr-hero","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-hero"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Strumento gratuito /05</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"level":1,"style":{"typography":{"fontSize":"clamp(34px,4vw,52px)"}}} -->
<h1 class="wp-block-heading" style="font-size:clamp(34px,4vw,52px)">Verifica accessibilità: il vostro sito è usabile da tutti?<span class="sr-accent-dot">.</span></h1>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="max-width:100%">Controlliamo con Google le barriere di accessibilità più comuni — contrasti, etichette, struttura. Dal 28 giugno 2025 l’European Accessibility Act rende l’accessibilità un obbligo per molti siti. Senza registrazione.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:html -->

<div class="sr-tool-widget sr-card" data-sr-tool="a11y" data-sr-locale="it"
     data-label-suffix=" — accessibilità"
     data-verdict-good="Ottimo: le barriere principali sono già rimosse."
     data-verdict-mid="Accessibilità nella media: alcune barriere restano."
     data-verdict-poor="Accessibilità carente: barriere importanti per gli utenti."
     data-audits-empty="Nessuna barriera rilevante rilevata."
     data-err="Non siamo riusciti a completare l’analisi. Riprovate tra qualche minuto.">
  <form data-sr-tool-form>
    <div class="sr-tool-row"><input type="text" placeholder="www.tuosito.it" class="sr-text-input" required /><button type="submit" class="wp-block-button__link" style="padding:17px 30px">Verifica l’accessibilità</button></div>
  </form>
  <p class="sr-tool-pending sr-mono" data-sr-tool-pending hidden>Analisi in corso<span class="sr-blink">…</span></p>
  <div class="sr-tool-result" data-sr-tool-result hidden>
    <p style="margin:0;font-size:14px;color:var(--sr-grigio)" data-sr-tool-url></p>
    <div class="sr-tool-result__score">
      <span class="sr-mono" data-sr-tool-score>0</span><span class="sr-mono" style="font-size:18px;color:var(--sr-grigio)">/100</span>
    </div>
    <div class="sr-barra" style="height:10px"><div class="sr-barra__fill" data-sr-tool-fill style="width:0%"></div><span class="sr-barra__tick" style="left:90%"></span></div>
    <p style="margin-top:20px;font-size:15.5px;color:var(--sr-grigio)" data-sr-tool-verdict></p>
    <ul class="sr-tool-audits" data-sr-tool-audits></ul>
      <p class="sr-disclaimer">Controllo automatico (Lighthouse): copre parte dei criteri WCAG 2.1 AA. La conformità EAA richiede anche verifica manuale.</p>
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
<div class="wp-block-group is-layout-grid" style="--sr-grid-min:240px"><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">01</p><p style="font-weight:500;margin-top:8px">Inserite l’indirizzo</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">La pagina da controllare: la home o una pagina di servizio, dove passano più utenti.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">02</p><p style="font-weight:500;margin-top:8px">Analisi Lighthouse</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Usiamo la categoria Accessibilità di Lighthouse via API PageSpeed: contrasti, testi alternativi, etichette dei moduli, struttura dei titoli.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">03</p><p style="font-weight:500;margin-top:8px">Vedete le barriere da rimuovere</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Punteggio 0–100 e la lista dei problemi rilevati, in italiano. Un controllo automatico copre parte dei criteri WCAG, non tutti.</p></div></div>
<!-- /wp:group -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Il metodo</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">Cosa controlla davvero questo test di accessibilità<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Il motore è la categoria Accessibilità di Lighthouse, richiamata via API PageSpeed: gli stessi controlli automatici che Google mette a disposizione degli sviluppatori. In pochi secondi la pagina viene esaminata su decine di regole tecniche — contrasto tra testo e sfondo, testi alternativi delle immagini, etichette dei campi nei moduli, ordine dei titoli, uso corretto degli attributi ARIA — e ne esce un punteggio da 0 a 100 con l’elenco delle barriere rilevate.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Serve chiarezza sui limiti, perché qui è facile illudersi. Un controllo automatico intercetta soltanto una parte dei criteri WCAG 2.1 AA: cattura ciò che una macchina sa misurare, non ciò che va provato da una persona. Non verifica la navigazione da tastiera, l’esperienza con uno screen reader, la chiarezza dei contenuti per chi ha difficoltà cognitive. È il primo gradino verso la conformità richiesta dall’European Accessibility Act, non il certificato finale.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-section--bianco","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-section--bianco"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Leggere il risultato</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">Come leggere il punteggio e le barriere rilevate<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Il numero da 0 a 100 dice quanto la pagina supera i controlli automatici: più è alto, meno ostacoli evidenti restano. Ma il punteggio conta meno dell’elenco che lo accompagna. Ogni voce è una barriera concreta per una persona reale — un contrasto troppo debole per chi ci vede poco, un pulsante senza etichetta per chi usa uno screen reader. Partite da quelle, non dal totale.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Un avvertimento sui falsi sensi di sicurezza: anche un 100 pieno non significa «sito conforme». Vuol dire che avete superato i test che una macchina può fare, e sono circa un terzo dei problemi possibili. Il resto — tastiera, lettori di schermo, contenuti — si verifica a mano. Prendete quindi un punteggio alto come una buona base, non come un traguardo raggiunto.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Tre domande tipiche</p>
<!-- /wp:paragraph -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Cos’è l’European Accessibility Act?</summary><!-- wp:paragraph -->
<p>Una direttiva europea (EAA) applicata in Italia dal 28 giugno 2025: molti siti di aziende che vendono a consumatori devono essere accessibili secondo lo standard WCAG 2.1 livello AA. È un obbligo, con alcune esenzioni per le microimprese.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Questo test basta per essere conformi?</summary><!-- wp:paragraph -->
<p>No: un controllo automatico intercetta una parte dei criteri WCAG. La conformità piena richiede anche verifica manuale — navigazione da tastiera, screen reader, contenuti. È un ottimo punto di partenza, non un certificato.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Riguarda anche la mia azienda?</summary><!-- wp:paragraph -->
<p>Se vendete beni o servizi a consumatori online (e-commerce, banche, trasporti, servizi), con ogni probabilità sì. Le microimprese che offrono servizi hanno esenzioni: meglio verificare caso per caso.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-section--bianco","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-section--bianco"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Come migliorare</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">Come rendere il sito accessibile a tutti<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"base"} -->
<p class="has-grigio-color has-text-color has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:12px">Molte barriere cadono con correzioni semplici, che migliorano l’esperienza di chiunque, non solo di chi ha una disabilità.</p>
<!-- /wp:paragraph -->
<!-- wp:group {"className":"","layout":{"type":"grid","minimumColumnWidth":"240px"}} -->
<div class="wp-block-group is-layout-grid" style="--sr-grid-min:240px"><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">01</p><p style="font-weight:500;margin-top:8px">Aumentate il contrasto</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Testo e sfondo devono avere un rapporto di contrasto di almeno 4,5:1: il grigio chiaro elegante sullo schermo del designer diventa illeggibile al sole o per chi ci vede poco.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">02</p><p style="font-weight:500;margin-top:8px">Descrivete le immagini</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Ogni immagine informativa ha bisogno di un testo alternativo che ne racconti il contenuto: è ciò che uno screen reader legge a chi non può vederla.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">03</p><p style="font-weight:500;margin-top:8px">Etichettate i moduli</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Ogni campo deve avere un’etichetta esplicita e collegata: «Nome», «Email», «Messaggio», non solo un testo grigio che sparisce appena si scrive.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">04</p><p style="font-weight:500;margin-top:8px">Ordinate titoli e focus</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Una gerarchia di titoli coerente e un percorso navigabile da tastiera, con il focus sempre visibile, rendono la pagina usabile anche senza mouse.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">05</p><p style="font-weight:500;margin-top:8px">Non affidatevi solo al colore</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Un errore segnalato solo in rosso è invisibile a chi non distingue i colori: affiancate sempre un’icona o un testo che spieghi cosa succede.</p></div></div>
<!-- /wp:group -->
<!-- wp:html -->
<div style="margin-top:24px;display:flex;flex-direction:column;gap:8px;align-items:flex-start"><p class="sr-card-link" style="margin-top:12px"><a href="/servizi/adeguamento-eaa/">Vogliamo sistemarle noi: audit, correzioni e dichiarazione — servizio Adeguamento EAA →</a></p><p class="sr-card-link" style="margin-top:12px"><a href="/blog/european-accessibility-act-ecommerce/">Approfondisci: EAA 2026, cosa rischia davvero il vostro e-commerce →</a></p><p class="sr-card-link" style="margin-top:12px"><a href="/blog/dichiarazione-di-accessibilita-guida-2026/">Guida pratica: la dichiarazione di accessibilità nel 2026 →</a></p></div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-cta-band","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-cta-band"><!-- wp:heading -->
<h2 class="wp-block-heading">Vogliamo rendere il sito accessibile<span class="sr-accent-dot">?</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="margin-top:12px">Verifichiamo le barriere una per una — automatiche e manuali — e le sistemiamo secondo lo standard WCAG 2.1 AA.</p>
<!-- /wp:paragraph -->
<!-- wp:buttons {"style":{"spacing":{"blockGap":"14px","margin":{"top":"28px"}}},"layout":{"type":"flex","justifyContent":"center"}} -->
<div class="wp-block-buttons" style="margin-top:28px"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/#contatti">Richiedi una verifica di accessibilità</a></div>
<!-- /wp:button -->
<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/servizi/adeguamento-eaa/">Scopri il servizio Adeguamento EAA</a></div>
<!-- /wp:button -->
</div>
<!-- /wp:buttons -->
<!-- wp:html -->
<div class="sr-cta-band__trust"><div class="sr-cta-band__trust-item"><strong>100% gratuito</strong><span>Nessun impegno</span></div><div class="sr-cta-band__trust-item"><strong>Risposta in 24 ore</strong><span>Preventivo dettagliato</span></div><div class="sr-cta-band__trust-item"><strong>Dati al sicuro</strong><span>Massima riservatezza</span></div></div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-section--bianco","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-section--bianco"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Gli altri strumenti gratuiti</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<div class="sr-servizi-rows"><div><span class="sr-mono" style="color:var(--sr-oltremare)">/00</span><a href="/strumenti/check-up-completo/" style="color:var(--sr-inchiostro);font-size:15.5px">Check-up completo</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/01</span><a href="/strumenti/test-velocita/" style="color:var(--sr-inchiostro);font-size:15.5px">Test velocità</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/02</span><a href="/strumenti/analisi-seo/" style="color:var(--sr-inchiostro);font-size:15.5px">Analisi SEO on-page</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/03</span><a href="/strumenti/check-gdpr/" style="color:var(--sr-inchiostro);font-size:15.5px">Check GDPR e cookie</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/04</span><a href="/strumenti/roi-localizzazione/" style="color:var(--sr-inchiostro);font-size:15.5px">ROI localizzazione</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/06</span><a href="/strumenti/sito-pronto-ai/" style="color:var(--sr-inchiostro);font-size:15.5px">Sito pronto per l’AI</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/07</span><a href="/strumenti/impatto-co2/" style="color:var(--sr-inchiostro);font-size:15.5px">Impatto CO₂</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/08</span><a href="/strumenti/segnali-eeat/" style="color:var(--sr-inchiostro);font-size:15.5px">Segnali E-E-A-T</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/09</span><a href="/strumenti/sito-letto-dallai/" style="color:var(--sr-inchiostro);font-size:15.5px">Il vostro sito, letto dall’AI</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/10</span><a href="/strumenti/suona-madrelingua/" style="color:var(--sr-inchiostro);font-size:15.5px">Suona madrelingua?</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/11</span><a href="/strumenti/generatore-llms-txt/" style="color:var(--sr-inchiostro);font-size:15.5px">Generatore di llms.txt</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div></div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
