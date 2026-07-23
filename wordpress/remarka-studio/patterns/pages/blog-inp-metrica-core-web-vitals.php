<?php
/**
 * Title: Pagina — Articolo: INP, la nuova metrica dei Core Web Vitals: cosa misura e come si risolve
 * Slug: remarka-studio/blog-inp-metrica-core-web-vitals
 * Categories: remarka-pagine
 * Description: Articolo blog: INP, la nuova metrica dei Core Web Vitals: cosa misura e come si risolve
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1440px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:html -->
<p class="sr-mono" style="color:var(--sr-grigio);font-size:13px">23 LUG 2026</p>
<!-- /wp:html -->
<!-- wp:heading {"level":1,"style":{"typography":{"fontSize":"clamp(32px,4vw,48px)"}}} -->
<h1 class="wp-block-heading" style="font-size:clamp(32px,4vw,48px)">INP, la nuova metrica dei Core Web Vitals: cosa misura e come si risolve</h1>
<!-- /wp:heading -->
<!-- wp:html -->
<figure class="wp-block-image size-large" style="margin:8px 0 8px"><img src="/wp-content/themes/remarka-studio/assets/img/blog/inp-cover.svg" alt="INP, la nuova metrica dei Core Web Vitals: cosa misura la reattività di un sito" width="1200" height="630" loading="lazy" style="max-width:100%;height:auto;display:block;border:1px solid var(--sr-bordo)"/></figure>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1440px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:18px;line-height:1.75;max-width:75ch">Da marzo 2024 c’è una sigla in più da tenere d’occhio: INP. Ha preso il posto di un’altra metrica, FID, tra i Core Web Vitals di Google — i tre parametri con cui il motore misura l’esperienza reale di chi naviga. Il cambio non è cosmetico: molti siti che passavano l’esame con FID si ritrovano ora in difficoltà con INP, perché la nuova metrica è più severa e cattura problemi che prima restavano invisibili. Vediamo cosa misura davvero INP, perché il vostro sito può sembrare veloce e non superarla, e le mosse concrete per rientrare nei valori buoni.</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Cos’è INP e perché ha sostituito FID<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">INP sta per Interaction to Next Paint, «interazione fino al prossimo disegno». In parole semplici misura la reattività: quando toccate un pulsante, aprite un menu o scrivete in un campo, quanto tempo passa prima che lo schermo risponda mostrando il risultato. È una delle tre metriche dei Core Web Vitals, insieme a LCP (velocità di caricamento) e CLS (stabilità visiva).</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Fino al marzo 2024 la reattività si misurava con FID, che però guardava solo il ritardo della primissima interazione — e per giunta solo l’attesa iniziale, non l’intera risposta. INP è più onesta: osserva tutte le interazioni durante la visita e considera la più lenta, dall’inizio del tocco fino a quando la pagina mostra davvero il cambiamento. Per questo molti siti «promossi» con FID si scoprono ora lenti con INP: la nuova metrica misura ciò che l’utente sente davvero.</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Cosa misura davvero, e le soglie di Google<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Le soglie sono chiare. Un INP sotto i 200 millisecondi è considerato buono: la pagina risponde in modo che l’utente percepisce come immediato. Tra 200 e 500 millisecondi c’è margine di miglioramento; sopra i 500 millisecondi l’esperienza è scadente e si nota, quel micro-ritardo fastidioso tra il clic e la reazione. Google valuta il 75° percentile: non basta che sia veloce «in media», deve esserlo per la grande maggioranza delle interazioni reali.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">E qui sta il punto: reali. Google giudica i Core Web Vitals sui dati «sul campo», raccolti dagli utenti veri di Chrome (il Chrome UX Report), non sulle prove di laboratorio fatte una volta sola dal vostro computer nuovo su una connessione ottima. Ecco perché un test onesto guarda ai numeri del campo: è l’esperienza dei vostri visitatori con i loro telefoni e le loro reti, non quella ideale.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<p class="sr-card-link" style="margin-top:14px"><a href="/strumenti/test-velocita/">Misura gratis i Core Web Vitals reali del vostro sito →</a></p>
<!-- /wp:html -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Perché un sito «sembra» veloce ma fallisce INP<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Un sito può caricarsi in un lampo e poi impuntarsi al primo tocco. Il colpevole quasi sempre è lo stesso: troppo JavaScript che tiene occupato il «thread principale» del browser, quello che deve anche rispondere ai vostri clic. Se un pezzo di codice lavora a lungo senza pause, l’interazione resta in coda ad aspettare — e quel millisecondo di attesa è esattamente ciò che INP misura. Il caricamento è finito da un pezzo, ma la pagina «non risponde».</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Le cause tipiche sono note: script di terze parti pesanti (chat, banner, tracker, widget), temi e plugin che caricano librerie enormi anche dove non servono, gestori di eventi che fanno troppo lavoro a ogni clic. Sono cose che nei test di velocità classici, tutti concentrati sul caricamento, non emergevano. INP le porta a galla: misura il momento in cui l’utente prova a usare il sito, non solo quello in cui lo guarda comparire.</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Come si risolve INP<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">La strategia è una: alleggerire e spezzare il lavoro del browser. Ridurre il JavaScript inutile e caricare in ritardo ciò che non serve subito; spezzare le operazioni lunghe in pezzi brevi, così tra uno e l’altro il browser può rispondere ai tocchi; tenere sotto controllo gli script di terze parti, che spesso pesano più del sito stesso. Sono interventi tecnici, ma l’effetto lo sente chiunque: la pagina reagisce all’istante.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Il metodo giusto è misurare prima e dopo, sempre sui dati reali. Si parte identificando le interazioni più lente su smartphone (dove i processori sono più deboli e i problemi si vedono meglio), si interviene sul codice che le rallenta e si verifica che l’INP al 75° percentile scenda sotto la soglia buona. Non è magia: è togliere peso finché la pagina non risponde come dovrebbe.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<figure class="wp-block-image size-large" style="margin:36px 0 8px"><img src="/wp-content/themes/remarka-studio/assets/img/blog/inp-schema.svg" alt="Le tre soglie INP dei Core Web Vitals: buono sotto 200 ms, da migliorare 200–500 ms, scadente oltre 500 ms" width="1200" height="500" loading="lazy" style="max-width:100%;height:auto;display:block;border:1px solid var(--sr-bordo)"/><figcaption class="sr-mono" style="margin-top:12px;font-size:12.5px;letter-spacing:0.04em;color:var(--sr-grigio);max-width:75ch">Le soglie di INP (Interaction to Next Paint), misurate al 75° percentile sugli utenti reali: buono sotto i 200 ms, da migliorare tra 200 e 500 ms, scadente oltre i 500 ms. INP misura il ritardo tra il tocco e la risposta visibile della pagina — la reattività che l’utente sente davvero. Il freno più comune è il JavaScript che tiene occupato il thread principale del browser.</figcaption></figure>
<!-- /wp:html -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">La reattività è un investimento, non un dettaglio<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">INP non è l’ennesima sigla per far felice Google: è la misura di una frustrazione concreta, quel mezzo secondo in cui il sito «non fa niente» dopo che l’avete toccato. Su mobile, dove ormai avviene la maggior parte delle visite, è la differenza tra un sito che sembra un’app e uno che sembra rotto. E siccome pesa sui Core Web Vitals, tocca anche il posizionamento: reattività e visibilità viaggiano insieme.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Nei nostri progetti la reattività non è una toppa dell’ultimo minuto: nasce dalle scelte tecniche, meno codice inutile e script di terze parti tenuti a bada, fin dal primo giorno. Un sito veloce a caricarsi ma lento a rispondere è una promessa mantenuta a metà — e INP, finalmente, la mette nero su bianco.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<p class="sr-card-link" style="margin-top:14px"><a href="/servizi/seo-tecnica/">La SEO tecnica che parte dalla velocità reale →</a></p><p class="sr-card-link" style="margin-top:14px"><a href="/blog/core-web-vitals-2026/">Leggi anche: Core Web Vitals nel 2026, cosa misura Google →</a></p><p class="sr-card-link" style="margin-top:14px"><a href="/blog/immagini-velocita-webp-lazy-load/">Leggi anche: immagini e velocità, WebP e lazy-load →</a></p>
<!-- /wp:html -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Fonti<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:16px;line-height:1.7;max-width:75ch;margin-top:8px">Le cifre e le affermazioni di questo articolo vengono da qui. Sono prime fonti, non riassunti: apritele e verificate.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<ul style="list-style:none;padding:0;margin:20px 0 0;border-top:1px solid var(--sr-bordo)"><li style="margin-top:16px;line-height:1.55"><a href="https://web.dev/articles/inp" target="_blank" rel="noopener">web.dev — Interaction to Next Paint (INP)</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">La definizione ufficiale della metrica e delle sue soglie, con la spiegazione del passaggio da FID a INP nel 2024.</span></li><li style="margin-top:16px;line-height:1.55"><a href="https://web.dev/articles/optimize-inp" target="_blank" rel="noopener">web.dev — ottimizzare l’INP</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">La guida pratica per migliorare la reattività: ridurre e spezzare il lavoro del thread principale, gestire i gestori di eventi.</span></li><li style="margin-top:16px;line-height:1.55"><a href="https://web.dev/articles/vitals" target="_blank" rel="noopener">web.dev — Core Web Vitals (Google)</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">Le tre metriche (LCP, INP, CLS), le soglie e perché contano: l’esperienza reale, non i numeri di laboratorio.</span></li><li style="margin-top:16px;line-height:1.55"><a href="https://developer.chrome.com/docs/crux" target="_blank" rel="noopener">Chrome UX Report (CrUX) — documentazione</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">La fonte dei dati «sul campo»: utenti reali di Chrome, su cui Google valuta i Core Web Vitals al 75° percentile.</span></li></ul>
<!-- /wp:html -->
<!-- wp:html -->
<p class="sr-card-link" style="margin-top:32px"><a href="/strumenti/test-velocita/">Misura gratis i Core Web Vitals del vostro sito →</a></p>
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
