<?php
/**
 * Title: Prezzi — tabella teaser noi vs mercato
 * Slug: remarka-studio/prezzi-teaser
 * Categories: remarka
 * Description: Tabella compatta mercato/Remarka (prezzo+tempi), nota sul prezzo chiuso e CTA.
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group sr-section"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Prezzi</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Prezzi e tempi, accanto al mercato<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->

<!-- wp:html -->
{{lancio}}<div class="sr-lancio-badge sr-mono" style="margin-top:20px">PREZZO LANCIO — PRIMI 5 PROGETTI</div><p class="sr-lancio-line">Prezzo lancio sui primi 5 progetti: stesso contratto, stesse garanzie. Listino pieno dal 2027.</p><p class="sr-lancio-counter sr-mono">Ne restano {{lancio_slots}} su 5.</p>{{/lancio}}
<!-- /wp:html -->

<!-- wp:group {"className":"sr-market-table sr-market-table--compact","style":{"spacing":{"margin":{"top":"28px"}}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group sr-market-table sr-market-table--compact" style="margin-top:28px"><!-- wp:html -->
<table>
<thead><tr>
<th>Prodotto</th>
<th>Mercato</th>
<th class="sr-market-table__uscol">Remarka</th>
</tr></thead>
<tbody>
<tr>
<td class="sr-market-table__prod">Sito vetrina</td>
<td>€ 1.000–3.000<span class="sr-market-table__sub">2–4 settimane</span></td>
<td class="sr-market-table__us sr-market-table__us--lancio">{{listino}}€ 1.900–2.800{{/listino}}{{lancio}}<s class="sr-lancio-listino">€ 1.900–2.800</s><span class="sr-lancio-price">€ 950–1.400</span>{{/lancio}}<span class="sr-market-table__sub">2 settimane</span></td>
</tr>
<tr>
<td class="sr-market-table__prod">Sito aziendale</td>
<td>€ 2.500–8.000<span class="sr-market-table__sub">6–10 settimane</span></td>
<td class="sr-market-table__us sr-market-table__us--lancio">{{listino}}€ 3.900–5.800{{/listino}}{{lancio}}<s class="sr-lancio-listino">€ 3.900–5.800</s><span class="sr-lancio-price">€ 1.950–2.900</span>{{/lancio}}<span class="sr-market-table__sub">3 settimane</span></td>
</tr>
<tr>
<td class="sr-market-table__prod">E-commerce</td>
<td>€ 6.000–25.000<span class="sr-market-table__sub">8–14 settimane</span></td>
<td class="sr-market-table__us sr-market-table__us--lancio">{{listino}}€ 7.500–14.000{{/listino}}{{lancio}}<s class="sr-lancio-listino">€ 7.500–14.000</s><span class="sr-lancio-price">€ 3.750–7.000</span>{{/lancio}}<span class="sr-market-table__sub">6 settimane</span></td>
</tr>
</tbody>
</table>
<!-- /wp:html --></div>
<!-- /wp:group -->

<!-- wp:columns {"verticalAlignment":"center","style":{"spacing":{"margin":{"top":"28px"}}}} -->
<div class="wp-block-columns are-vertically-aligned-center" style="margin-top:28px"><!-- wp:column {"verticalAlignment":"center","width":"60%"} -->
<div class="wp-block-column is-vertically-aligned-center" style="flex-basis:60%"><!-- wp:paragraph {"fontSize":"small","textColor":"grigio"} -->
<p class="has-grigio-color has-text-color has-small-font-size">I prezzi Remarka sono chiusi: quello che firmate è quello che pagate.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->

<!-- wp:column {"verticalAlignment":"center","width":"40%"} -->
<div class="wp-block-column is-vertically-aligned-center" style="flex-basis:40%"><!-- wp:buttons {"layout":{"type":"flex","justifyContent":"right"}} -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="#contatti">Richiedi preventivo dettagliato</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></section>
<!-- /wp:group -->
