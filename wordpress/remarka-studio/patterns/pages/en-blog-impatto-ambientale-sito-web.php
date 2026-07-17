<?php
/**
 * Title: Pagina — Articolo: Quanto pesa il vostro sito sull’ambiente (e sul portafoglio)
 * Slug: remarka-studio/en-blog-impatto-ambientale-sito-web
 * Categories: remarka-pagine
 * Description: Articolo blog: Quanto pesa il vostro sito sull’ambiente (e sul portafoglio)
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:html -->
<p class="sr-mono" style="color:var(--sr-grigio);font-size:13px">16 JUL 2026</p>
<!-- /wp:html -->
<!-- wp:heading {"level":1,"style":{"typography":{"fontSize":"clamp(32px,4vw,48px)"}}} -->
<h1 class="wp-block-heading" style="font-size:clamp(32px,4vw,48px)">How much your site weighs on the environment (and on your wallet)</h1>
<!-- /wp:heading -->
<!-- wp:html -->
<figure class="wp-block-image size-large" style="margin:8px 0 8px"><img src="/wp-content/themes/remarka-studio/assets/img/blog/impatto-cover.svg" alt="Website environmental impact: from page weight in bytes to energy consumed and grams of CO₂ per visit" loading="lazy" style="max-width:100%;height:auto;display:block;border:1px solid var(--sr-bordo)"/></figure>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:18px;line-height:1.75;max-width:75ch">A website seems immaterial, but it isn’t: every time someone opens it, bytes travel from a data center to their screen, and that journey consumes energy. Multiply by tens of thousands of visits a month and the “immaterial” becomes a bill and a bit of carbon dioxide. The good news is that a website’s environmental impact can be estimated, and that reducing it almost always coincides with making it faster and cheaper. Let’s see how it’s measured, what it has to do with your accounts and the new European reporting rules, and what you can do in an afternoon.</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">A site has a weight, and the weight has a cost<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">A page’s weight is the sum of everything the browser has to download to show it: images, fonts, scripts, video. The heavier it is, the more energy it takes to transfer and display — in the data center, along the network, on the viewer’s device. That energy has two parallel prices: an environmental one, in grams of CO₂, and an economic one, in more expensive servers, campaigns that bring visits that flee, and customers who leave before seeing the first line because the phone is struggling.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">That’s why we talk about the environment and the wallet in the same breath: they aren’t two conversations, it’s the same conversation. The page that pollutes most is, almost always, the same one that loads more slowly and costs more to maintain.</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">How to estimate a website’s environmental impact<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">It isn’t a feeling, it’s a calculation. You start from a measurable figure — the page weight in bytes — and apply a model that turns the transferred bytes into energy and then into grams of CO₂ equivalent. The most widely used model is Sustainable Web Design, made available by the Green Web Foundation in the open-source library co2.js: the same tools behind the web’s emission calculators. The handy reference is the average: a web page produces around 0.8 grams of CO₂ per visit. Below that threshold you’re light; noticeably above, there’s room to lighten.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Some honesty about the limits is in order, because it’s easy to sell smoke here. It’s an estimate with global average coefficients: it doesn’t know your hosting’s real energy or every visitor’s behavior. It isn’t a certified footprint, it’s a reliable, comparable order of magnitude — and its merit is precisely that it hangs on a technical fact you can actually act on: weight.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<figure class="wp-block-image size-large" style="margin:36px 0 8px"><img src="/wp-content/themes/remarka-studio/assets/img/blog/impatto-peso.svg" alt="From page weight to grams of CO₂: transferred bytes, energy consumed, emissions per visit and yearly estimate with the Sustainable Web Design model" loading="lazy" style="max-width:100%;height:auto;display:block;border:1px solid var(--sr-bordo)"/><figcaption class="sr-mono" style="margin-top:12px;font-size:12.5px;letter-spacing:0.04em;color:var(--sr-grigio);max-width:75ch">From weight to grams: the transferred bytes become energy and then CO₂ per visit, which multiplied by traffic gives the yearly estimate. Reference: web average ≈ 0.8 g per visit. Model: Sustainable Web Design (co2.js, Green Web Foundation).</figcaption></figure>
<!-- /wp:html -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Why light means fast and cheaper<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Lightening a page and speeding it up are the same operation seen from two sides. Every byte removed is less energy transferred — so less CO₂ — and at the same time less loading time, so more visits that stay. Unoptimized photos are almost always the heaviest item: converting them to modern formats can cut them by 80% at the same visible quality, and with them cuts emissions, bandwidth costs and seconds of waiting. You don’t have to choose between doing right by the planet and doing right by the accounts: it’s the same lever.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">A typical example from an audit: a homepage of 6 megabytes, almost all in uncompressed photos, brought down to just over 1 megabyte without removing a single image — just modern formats and lazy loading. The result is threefold: a page several seconds faster on a phone, bandwidth saved every month, and a CO₂ footprint per visit more than halved. One intervention, three benefits — environment, speed and cost — that always pull in the same direction.</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">CO₂ enters the balance sheets too: the CSRD<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Until yesterday a site’s environmental impact was a matter of sensibility. Recently it’s also an item that can end up in a balance sheet. The European directive on sustainability reporting — the CSRD — greatly widens the pool of companies that must report their environmental impacts, and those under the obligation extend it to their suppliers. If you work with or inside companies subject to the CSRD, a measurable, light site stops being a nicety and becomes a figure someone will ask you for. Better to get there with a number in hand than with a shrug.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Let’s say it honestly, as always: our tool gives an indicative estimate, not a certified audit for official reporting. But it’s the right first step — it tells you where you are and how much room you have, even before you talk to a consultant.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<p class="sr-card-link" style="margin-top:14px"><a href="https://eur-lex.europa.eu/eli/dir/2022/2464/oj" target="_blank" rel="noopener">The CSRD directive on sustainability reporting (EUR-Lex) →</a></p>
<!-- /wp:html -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">What you can do in an afternoon<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">You don’t have to redo everything to see the number drop. The first moves are simple and pay off right away.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<div class="sr-list-rows"><div><span class="sr-mono">a</span><span>Lighten the images: convert them to WebP or AVIF with lazy loading. It’s almost always the intervention with the highest cost/benefit ratio.</span></div><div><span class="sr-mono">b</span><span>Trim superfluous scripts and fonts: every third-party library and every extra font family is energy transferred on every visit.</span></div><div><span class="sr-mono">c</span><span>Use cache and a CDN: they avoid re-transferring the same content a thousand times — less repeated traffic and less consumption.</span></div><div><span class="sr-mono">d</span><span>Choose hosting powered by renewables: it lowers the carbon intensity of every byte served, with immediate effect.</span></div></div>
<!-- /wp:html -->
<!-- wp:html -->
<p class="sr-card-link" style="margin-top:14px"><a href="/en/tools/website-carbon/">Measure your site’s CO₂ footprint for free →</a></p><p class="sr-card-link" style="margin-top:14px"><a href="/en/services/redesign-migration/">Vogliamo alleggerirlo noi: restyling e migrazione →</a></p><p class="sr-card-link" style="margin-top:14px"><a href="/en/blog/slow-website-causes-fixes/">Read also: a slow site, the 7 real causes (and what it costs to fix them) →</a></p>
<!-- /wp:html -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Sources<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:16px;line-height:1.7;max-width:75ch;margin-top:8px">The figures and claims in this article come from here. These are primary sources, not summaries: open them and check for yourself.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<ul style="list-style:none;padding:0;margin:20px 0 0;border-top:1px solid var(--sr-bordo)"><li style="margin-top:16px;line-height:1.55"><a href="https://sustainablewebdesign.org/estimating-digital-emissions/" target="_blank" rel="noopener">Sustainable Web Design — emissions estimate</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">The model used to calculate the CO₂ footprint from the page’s real weight.</span></li><li style="margin-top:16px;line-height:1.55"><a href="https://www.thegreenwebfoundation.org/co2-js/" target="_blank" rel="noopener">Green Web Foundation — CO2.js</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">The open-source library that turns transferred bytes into grams of CO₂ equivalent.</span></li><li style="margin-top:16px;line-height:1.55"><a href="https://eur-lex.europa.eu/eli/dir/2022/2464/oj" target="_blank" rel="noopener">Direttiva (UE) 2022/2464 — CSRD (EUR-Lex)</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">The official text of the sustainability reporting rules that extend environmental obligations to businesses.</span></li><li style="margin-top:16px;line-height:1.55"><a href="https://almanac.httparchive.org/en/2024/" target="_blank" rel="noopener">HTTP Archive — Web Almanac 2024</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">Real data on page weights: where the web’s consumption really concentrates.</span></li><li style="margin-top:16px;line-height:1.55"><a href="https://web.dev/articles/vitals" target="_blank" rel="noopener">web.dev — Web Vitals</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">Why a light site is also a fast one: the metrics that link weight, speed and experience.</span></li></ul>
<!-- /wp:html -->
<!-- wp:html -->
<p class="sr-card-link" style="margin-top:32px"><a href="/en/tools/website-carbon/">Measure your site’s CO₂ footprint now — free →</a></p>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-cta-band","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-cta-band"><!-- wp:heading -->
<h2 class="wp-block-heading">Let’s talk about your website<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="margin-top:12px">Free analysis of your current website; a fixed quote within 24 hours of the call.</p>
<!-- /wp:paragraph -->
<!-- wp:buttons {"style":{"spacing":{"blockGap":"14px","margin":{"top":"28px"}}},"layout":{"type":"flex","justifyContent":"center"}} -->
<div class="wp-block-buttons" style="margin-top:28px"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/en/#contatti">Get a quote in 24 hours</a></div>
<!-- /wp:button -->
<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/en/tools/full-site-checkup/">Test your website — free</a></div>
<!-- /wp:button -->
</div>
<!-- /wp:buttons -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:buttons {"style":{"spacing":{"blockGap":"14px"}},"layout":{"type":"flex","justifyContent":"center"}} -->
<div class="wp-block-buttons"><!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/en/blog/">← All articles</a></div>
<!-- /wp:button -->
</div>
<!-- /wp:buttons -->
</section>
<!-- /wp:group -->
