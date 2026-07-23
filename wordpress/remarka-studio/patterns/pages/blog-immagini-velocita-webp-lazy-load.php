<?php
/**
 * Title: Pagina — Articolo: Immagini e velocità: WebP, lazy-load e Core Web Vitals
 * Slug: remarka-studio/blog-immagini-velocita-webp-lazy-load
 * Categories: remarka-pagine
 * Description: Articolo blog: Immagini e velocità: WebP, lazy-load e Core Web Vitals
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1440px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:html -->
<p class="sr-mono" style="color:var(--sr-grigio);font-size:13px">23 LUG 2026</p>
<!-- /wp:html -->
<!-- wp:heading {"level":1,"style":{"typography":{"fontSize":"clamp(32px,4vw,48px)"}}} -->
<h1 class="wp-block-heading" style="font-size:clamp(32px,4vw,48px)">Immagini e velocità: WebP, lazy-load e Core Web Vitals</h1>
<!-- /wp:heading -->
<!-- wp:html -->
<figure class="wp-block-image size-large" style="margin:8px 0 8px"><img src="/wp-content/themes/remarka-studio/assets/img/blog/immagini-velocita-cover.svg" alt="Ottimizzare le immagini del sito: WebP, lazy-load e dimensioni giuste per la velocità" width="1200" height="630" loading="lazy" style="max-width:100%;height:auto;display:block;border:1px solid var(--sr-bordo)"/></figure>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1440px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:18px;line-height:1.75;max-width:75ch">Se il vostro sito è lento, con ogni probabilità la colpa più grossa ce l’hanno le immagini. Su gran parte delle pagine sono il contenuto che pesa di più, molto più del testo o del codice: una sola foto caricata a piena risoluzione può pesare quanto decine di pagine scritte. La buona notizia è che le immagini sono anche il punto dove ottimizzare rende di più e costa meno: il formato giusto, il caricamento pigro e le dimensioni corrette bastano a trasformare una pagina lenta in una svelta. Vediamo come ottimizzare le immagini del sito con WebP, lazy-load e un occhio ai Core Web Vitals.</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Perché le immagini pesano così tanto<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Aprite una pagina qualsiasi e, quasi sempre, la parte più pesante da scaricare sono le immagini. I rapporti sullo stato del web lo confermano da anni: sono in cima alla classifica dei byte trasferiti, spesso più di tutto il resto messo insieme. Il motivo è banale — una foto ricca di dettagli contiene un’enorme quantità di informazione — ma le conseguenze no: ogni megabyte in più è tempo di attesa, soprattutto per chi naviga da smartphone con una rete lenta.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Il guaio è che molte immagini sono più pesanti del necessario, per pura disattenzione. Foto caricate a 4000 pixel di larghezza e poi mostrate in un riquadro da 400; formati vecchi e ingombranti dove ne basterebbe uno moderno; nessuna compressione. È peso morto: informazione che l’utente non vedrà mai, ma che il suo telefono deve comunque scaricare. Ottimizzare le immagini vuol dire togliere questo peso inutile, senza che si veda la differenza.</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">WebP (e AVIF): il formato giusto<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Il primo intervento è cambiare formato. I vecchi JPEG e PNG funzionano, ma pesano: i formati moderni come WebP — e il più recente AVIF — offrono la stessa qualità visiva occupando molto meno spazio, spesso il 25-35% in meno rispetto a un JPEG equivalente, a volte molto di più. Per l’occhio non cambia nulla; per il tempo di caricamento è una differenza enorme. Oggi WebP è supportato da tutti i browser diffusi: non c’è più ragione di spedire file inutilmente grandi.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Il bello è che non serve rifare le foto: si convertono quelle esistenti, idealmente in modo automatico quando vengono caricate, servendo il formato moderno a chi lo supporta. È uno degli interventi con il miglior rapporto tra fatica e risultato: si tocca il file, non il design, e la pagina si alleggerisce di colpo. La compressione, dosata bene, fa il resto senza intaccare la nitidezza percepita.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<p class="sr-card-link" style="margin-top:14px"><a href="/strumenti/test-velocita/">Misura gratis peso della pagina e velocità del vostro sito →</a></p>
<!-- /wp:html -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Lazy-load: caricare solo ciò che serve<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">La seconda mossa è non caricare tutto subito. Quando aprite una pagina lunga, le immagini in fondo — quelle che vedrete solo scorrendo, se scorrerete — non servono nel primo istante. Il lazy-load («caricamento pigro») le rinvia: il browser scarica prima ciò che è visibile e carica il resto solo quando l’utente si avvicina. Il risultato è una pagina che appare pronta molto prima, perché non aspetta immagini che nessuno sta ancora guardando.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Oggi il lazy-load è quasi gratis da attivare: basta un attributo standard sull’immagine, `loading="lazy"`, e i browser fanno il resto. Attenzione a una sola cosa: non va messo sull’immagine più importante in cima alla pagina, quella che l’utente vede subito — rinviarla peggiorerebbe la velocità percepita invece di migliorarla. Il lazy-load è per ciò che sta sotto la piega, non per il protagonista.</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Dimensioni giuste e Core Web Vitals<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Terzo pilastro: servire ogni immagine nella misura in cui verrà mostrata. Non ha senso mandare una foto da 3000 pixel a uno schermo che ne mostrerà 600. Le tecniche per farlo — immagini responsive che adattano la risoluzione al dispositivo — evitano di scaricare pixel che nessuno vedrà. E vanno sempre indicate larghezza e altezza dell’immagine, così il browser riserva lo spazio in anticipo e la pagina non «salta» mentre carica: quel salto ha persino una metrica, il CLS dei Core Web Vitals.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Qui si chiude il cerchio con la velocità misurata da Google. L’immagine grande in cima, di solito, è l’elemento che decide l’LCP — la metrica che misura quanto ci mette a comparire il contenuto principale. Alleggerirla con WebP, darle le dimensioni giuste e non metterla in lazy-load è spesso il singolo intervento che fa passare una pagina dall’arancione al verde. Immagini e Core Web Vitals sono, in gran parte, lo stesso problema.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<figure class="wp-block-image size-large" style="margin:36px 0 8px"><img src="/wp-content/themes/remarka-studio/assets/img/blog/immagini-velocita-schema.svg" alt="Ottimizzare le immagini: WebP invece di JPEG, lazy-load sotto la piega, dimensioni giuste per LCP e CLS" width="1200" height="500" loading="lazy" style="max-width:100%;height:auto;display:block;border:1px solid var(--sr-bordo)"/><figcaption class="sr-mono" style="margin-top:12px;font-size:12.5px;letter-spacing:0.04em;color:var(--sr-grigio);max-width:75ch">Le tre leve per ottimizzare le immagini di un sito: il formato moderno (WebP o AVIF al posto di JPEG/PNG, fino al 25-35% in meno di peso), il lazy-load per ciò che sta sotto la piega (mai per l’immagine principale in cima), e le dimensioni giuste servite al dispositivo — con larghezza e altezza dichiarate per non far «saltare» la pagina. Insieme migliorano LCP e CLS, due dei tre Core Web Vitals.</figcaption></figure>
<!-- /wp:html -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Leggere, non pesare<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Ottimizzare le immagini non è un vezzo da tecnici: è il modo più rapido e concreto di rendere un sito veloce, e quindi più gradito ai visitatori e a Google. Formato moderno, caricamento pigro, dimensioni giuste: tre interventi che non toccano il design ma cambiano l’esperienza, soprattutto su mobile e su reti lente — cioè per la maggioranza delle persone che oggi vi visitano.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Nei siti che costruiamo le immagini vengono trattate così di serie: convertite nei formati moderni, servite nella misura giusta, con il lazy-load dove serve. Non è un extra da vendere a parte, è il minimo perché una pagina piena di foto resti leggera. Un sito bello ma pesante non è un bel sito: è una pagina che i visitatori non aspettano di vedere caricare.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<p class="sr-card-link" style="margin-top:14px"><a href="/servizi/restyling-migrazione/">Restyling e migrazione: rimettere in forma un sito lento →</a></p><p class="sr-card-link" style="margin-top:14px"><a href="/blog/inp-metrica-core-web-vitals/">Leggi anche: INP, la nuova metrica dei Core Web Vitals →</a></p>
<!-- /wp:html -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Fonti<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:16px;line-height:1.7;max-width:75ch;margin-top:8px">Le cifre e le affermazioni di questo articolo vengono da qui. Sono prime fonti, non riassunti: apritele e verificate.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<ul style="list-style:none;padding:0;margin:20px 0 0;border-top:1px solid var(--sr-bordo)"><li style="margin-top:16px;line-height:1.55"><a href="https://web.dev/learn/images/" target="_blank" rel="noopener">web.dev — Learn Images (Google)</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">Il corso ufficiale sulle immagini per il web: formati, compressione, immagini responsive. Pratico e aggiornato.</span></li><li style="margin-top:16px;line-height:1.55"><a href="https://web.dev/articles/serve-images-webp" target="_blank" rel="noopener">web.dev — servire immagini in WebP</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">Perché e come usare WebP: la stessa qualità visiva con file molto più leggeri dei vecchi JPEG e PNG.</span></li><li style="margin-top:16px;line-height:1.55"><a href="https://developer.mozilla.org/en-US/docs/Web/Performance/Lazy_loading" target="_blank" rel="noopener">MDN — Lazy loading</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">La guida di riferimento al caricamento pigro: come funziona l’attributo loading="lazy" e quando (non) usarlo.</span></li><li style="margin-top:16px;line-height:1.55"><a href="https://web.dev/articles/lcp" target="_blank" rel="noopener">web.dev — Largest Contentful Paint (LCP)</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">La metrica dei Core Web Vitals più legata alle immagini: spesso è la foto in cima a decidere il vostro LCP.</span></li></ul>
<!-- /wp:html -->
<!-- wp:html -->
<p class="sr-card-link" style="margin-top:32px"><a href="/strumenti/test-velocita/">Misura gratis peso e velocità del vostro sito →</a></p>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-cta-band","layout":{"type":"constrained","contentSize":"1440px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-cta-band"><!-- wp:heading -->
<h2 class="wp-block-heading">Parliamo del vostro sito<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="margin-top:12px">Analisi gratuita del sito attuale, preventivo chiuso entro 24 ore dalla chiamata.</p>
<!-- /wp:paragraph -->
<!-- wp:buttons {"style":{"spacing":{"blockGap":"14px","margin":{"top":"28px"}}},"layout":{"type":"flex","justifyContent":"center"}} -->
<div class="wp-block-buttons" style="margin-top:28px"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/#contatti">Richiedi preventivo in 24 ore</a></div>
<!-- /wp:button -->
<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/strumenti/check-up-completo/">Analizza il tuo sito — gratis</a></div>
<!-- /wp:button -->
</div>
<!-- /wp:buttons -->
<!-- wp:html -->
<div class="sr-cta-band__trust"><div class="sr-cta-band__trust-item"><strong>100% gratuito</strong><span>Nessun impegno</span></div><div class="sr-cta-band__trust-item"><strong>Risposta in 24 ore</strong><span>Preventivo dettagliato</span></div><div class="sr-cta-band__trust-item"><strong>Dati al sicuro</strong><span>Massima riservatezza</span></div></div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1440px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:buttons {"style":{"spacing":{"blockGap":"14px"}},"layout":{"type":"flex","justifyContent":"center"}} -->
<div class="wp-block-buttons"><!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/blog/">← Tutti gli articoli</a></div>
<!-- /wp:button -->
</div>
<!-- /wp:buttons -->
</section>
<!-- /wp:group -->
