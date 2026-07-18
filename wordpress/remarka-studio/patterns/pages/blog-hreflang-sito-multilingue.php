<?php
/**
 * Title: Pagina — Articolo: Sito multilingue: hreflang senza mal di testa
 * Slug: remarka-studio/blog-hreflang-sito-multilingue
 * Categories: remarka-pagine
 * Description: Articolo blog: Sito multilingue: hreflang senza mal di testa
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1440px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:html -->
<p class="sr-mono" style="color:var(--sr-grigio);font-size:13px">18 LUG 2026</p>
<!-- /wp:html -->
<!-- wp:heading {"level":1,"style":{"typography":{"fontSize":"clamp(32px,4vw,48px)"}}} -->
<h1 class="wp-block-heading" style="font-size:clamp(32px,4vw,48px)">Sito multilingue: hreflang senza mal di testa</h1>
<!-- /wp:heading -->
<!-- wp:html -->
<figure class="wp-block-image size-large" style="margin:8px 0 8px"><img src="/wp-content/themes/remarka-studio/assets/img/blog/hreflang-cover.svg" alt="Hreflang per un sito multilingue: le versioni italiana, inglese e tedesca collegate così che Google serva la lingua giusta" width="1200" height="630" loading="lazy" style="max-width:100%;height:auto;display:block;border:1px solid var(--sr-bordo)"/></figure>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1440px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:18px;line-height:1.75;max-width:75ch">Avete tradotto il sito in inglese e tedesco, giustamente. Ma ora un cliente italiano cerca su Google e si ritrova la pagina inglese; un tedesco atterra sulla versione italiana; e le vostre due pagine — stesso contenuto, lingue diverse — si fanno concorrenza a vicenda nei risultati. Il colpevole è quasi sempre lo stesso: manca, o è sbagliato, l’hreflang. È l’attributo con cui si dice a Google «questa pagina è la versione italiana, quest’altra l’inglese, servile alla persona giusta». Si sente parlare di hreflang per un sito multilingue come di qualcosa di ostico: lo è, se lo si tratta come un plugin da attivare. Vediamo cos’è davvero, come si imposta senza errori e perché è ingegneria, non fortuna.</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Cos’è l’hreflang (in parole vostre)<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Immaginate di avere la stessa pagina in tre lingue: italiano, inglese, tedesco. Per un motore di ricerca sono tre indirizzi diversi con contenuti che si somigliano molto — e senza un’indicazione esplicita, Google deve indovinare quale mostrare a chi, rischiando di sbagliare o di considerarle contenuti duplicati. L’hreflang è quell’indicazione esplicita: un piccolo segnale, presente su ogni versione, che dice «esisto in queste lingue, ecco gli indirizzi di tutte, e io sono quella per l’italiano».</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">La regola d’oro è la reciprocità: se la pagina italiana punta all’inglese, l’inglese deve puntare all’italiano, e ogni versione deve elencare tutte le altre — sé stessa compresa. Google, nella sua documentazione ufficiale sulle versioni localizzate, insiste proprio su questo: i riferimenti devono essere bidirezionali e completi, altrimenti li ignora. È qui che nascono la maggior parte dei mal di testa: non nel concetto, ma nella coerenza da mantenere su decine di pagine.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<figure class="wp-block-image size-large" style="margin:36px 0 8px"><img src="/wp-content/themes/remarka-studio/assets/img/blog/hreflang-versioni.svg" alt="Come funziona l’hreflang in un sito multilingue: le versioni italiana, inglese e tedesca si citano a vicenda in modo reciproco" width="1200" height="500" loading="lazy" style="max-width:100%;height:auto;display:block;border:1px solid var(--sr-bordo)"/><figcaption class="sr-mono" style="margin-top:12px;font-size:12.5px;letter-spacing:0.04em;color:var(--sr-grigio);max-width:75ch">L’hreflang collega le versioni di una pagina: ognuna dichiara sé stessa e tutte le altre, in modo reciproco (se IT punta a EN, EN deve puntare a IT). Così Google serve la lingua giusta e non le tratta come contenuti duplicati. Fonte: Google Search Central, versioni localizzate.</figcaption></figure>
<!-- /wp:html -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Gli errori che rompono un sito multilingue<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Quasi tutti i problemi di hreflang nascono da pochi errori ricorrenti. Conoscerli è metà del lavoro, perché sono quasi sempre gli stessi.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<div class="sr-list-rows"><div><span class="sr-mono">a</span><span>Riferimenti non reciproci: la pagina IT cita la EN, ma la EN non ricambia. Google scarta l’intera coppia e torna a indovinare.</span></div><div><span class="sr-mono">b</span><span>Codici lingua sbagliati: «en-UK» non esiste (è «en-GB»), e un codice inventato viene ignorato in silenzio.</span></div><div><span class="sr-mono">c</span><span>URL relativi o pagine che rimandano a versioni in «noindex»: l’hreflang deve puntare a indirizzi assoluti e indicizzabili, o non serve a nulla.</span></div><div><span class="sr-mono">d</span><span>Manca l’autoreferenza: ogni versione deve elencare anche sé stessa. Dimenticarlo è l’errore più comune e più silenzioso.</span></div></div>
<!-- /wp:html -->
<!-- wp:html -->
<p class="sr-card-link" style="margin-top:14px"><a href="https://developers.google.com/search/docs/specialty/international/localized-versions" target="_blank" rel="noopener">Google — dire a Google le versioni localizzate (hreflang) →</a></p>
<!-- /wp:html -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Hreflang non è tutto: la lingua deve suonare vera<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">C’è un equivoco da smontare: l’hreflang risolve il «quale versione mostrare», non il «la versione è buona». Potete avere l’hreflang perfetto e perdere comunque il cliente, se la traduzione suona finta. Una scheda prodotto tradotta a macchina, con un registro sbagliato, allontana chi la legge nella propria lingua — e nessun attributo tecnico lo compensa. La ricerca di CSA («Can’t Read, Won’t Buy») lo dice da anni: le persone comprano molto più volentieri nella propria lingua, e diffidano dei testi che suonano stranieri.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Per questo, da noi, il multilingue è due mestieri in uno: l’ingegneria che collega le versioni (hreflang, sitemap, struttura degli URL) e i redattori madrelingua che scrivono, non traducono a macchina. Le lingue le curano madrelingua del gruppo Remarka, nel settore dal 2001, selezionati da una piattaforma di test interna che scarta la stragrande maggioranza dei candidati — la stessa che tiene la qualità di ogni nostro progetto multilingue. E se un mercato ha regole proprie — per la Germania, l’Austria — la parte tecnica va oltre l’hreflang: è la gestione dei siti multi-regionali.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<p class="sr-card-link" style="margin-top:14px"><a href="/servizi/siti-multilingue/">Siti multilingue con redattori madrelingua →</a></p><p class="sr-card-link" style="margin-top:14px"><a href="https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites" target="_blank" rel="noopener">Google — gestire i siti multi-regionali e multilingue →</a></p><p class="sr-card-link" style="margin-top:14px"><a href="/casi-studio/">La piattaforma che seleziona chi traduce (solo l’8% passa) →</a></p>
<!-- /wp:html -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Come si tiene in ordine, senza impazzire<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Il segreto per non impazzire con l’hreflang è non gestirlo a mano. Su decine di pagine e tre lingue, mantenere a mano i riferimenti reciproci è una fonte inesauribile di errori. La soluzione è generare l’hreflang da un’unica mappa delle corrispondenze — una fonte di verità sola, da cui ogni pagina eredita i propri collegamenti — così che aggiungere una pagina non significhi aggiornarne trenta. È esattamente l’approccio con cui è costruito questo sito: italiano alla radice, inglese e russo come alberi coerenti, collegati da una mappa che non si tocca a mano.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">In pratica, prima di aggiungere lingue conviene verificare come Google legge già il vostro sito: se le versioni esistenti si citano correttamente, se ci sono codici sbagliati, se qualcosa finisce fuori indice. Un’analisi SEO on-page fa emergere questi problemi prima che costino posizioni. E se state pensando non solo a tradurre ma ad aprire un mercato estero per davvero, l’hreflang è solo il primo pezzo di un discorso più grande: quello dell’export digitale.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<p class="sr-card-link" style="margin-top:14px"><a href="/strumenti/analisi-seo/">Analizza gratis la SEO on-page della vostra pagina →</a></p><p class="sr-card-link" style="margin-top:14px"><a href="/servizi/siti-multilingue/">Progettiamo il vostro sito multilingue a prezzo chiuso →</a></p><p class="sr-card-link" style="margin-top:14px"><a href="/blog/sito-per-export/">Leggi anche: export digitale, il sito che apre mercati esteri →</a></p>
<!-- /wp:html -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Fonti<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:16px;line-height:1.7;max-width:75ch;margin-top:8px">Le cifre e le affermazioni di questo articolo vengono da qui. Sono prime fonti, non riassunti: apritele e verificate.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<ul style="list-style:none;padding:0;margin:20px 0 0;border-top:1px solid var(--sr-bordo)"><li style="margin-top:16px;line-height:1.55"><a href="https://developers.google.com/search/docs/specialty/international/localized-versions" target="_blank" rel="noopener">Google Search Central — versioni localizzate (hreflang)</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">La documentazione ufficiale: come dichiarare le versioni per lingua, con riferimenti reciproci e completi.</span></li><li style="margin-top:16px;line-height:1.55"><a href="https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites" target="_blank" rel="noopener">Google Search Central — siti multi-regionali e multilingue</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">Come gestire lingua e Paese insieme: struttura degli URL, targeting e insidie da evitare.</span></li><li style="margin-top:16px;line-height:1.55"><a href="https://csa-research.com/Featured-Content/Global-Growth/CRWB-Series/CRWB-B2C" target="_blank" rel="noopener">CSA Research — «Can’t Read, Won’t Buy»</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">La ricerca sul comportamento d’acquisto: le persone comprano molto più volentieri nella propria lingua.</span></li></ul>
<!-- /wp:html -->
<!-- wp:html -->
<p class="sr-card-link" style="margin-top:32px"><a href="/servizi/siti-multilingue/">Siti multilingue con hreflang e madrelingua, a prezzo chiuso →</a></p>
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
