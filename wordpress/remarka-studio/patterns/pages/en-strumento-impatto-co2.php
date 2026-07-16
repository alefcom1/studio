<?php
/**
 * Title: Pagina — Strumento: Impatto CO₂
 * Slug: remarka-studio/en-strumento-impatto-co2
 * Categories: remarka-pagine
 * Description: Strumento gratuito Impatto CO₂: widget interattivo, come funziona, FAQ, CTA.
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","className":"sr-section sr-hero","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-hero"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Free tool /07</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"level":1,"style":{"typography":{"fontSize":"clamp(34px,4vw,52px)"}}} -->
<h1 class="wp-block-heading" style="font-size:clamp(34px,4vw,52px)">Your website’s CO₂ impact<span class="sr-accent-dot">.</span></h1>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="max-width:100%">Every website visit consumes energy and produces CO₂. We measure your page weight and estimate emissions per visit and per year, using the Sustainable Web Design model. A lighter website is also a faster one.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:html -->

<div class="sr-tool-widget sr-card" data-sr-tool="co2" data-sr-locale="en"
     data-co2-average="0.8" data-co2-visits="10000"
     data-label-unit-year="kg CO₂e / year"
     data-verdict-good="Below the web average: a light page, well done."
     data-verdict-mid="Close to the web average: there’s room to trim it down."
     data-verdict-poor="Above the web average: a heavy page, worth optimizing."
     data-err="We couldn’t measure the page weight. Please try again.">
  <form data-sr-tool-form>
    <div class="sr-tool-row">
      <input type="text" placeholder="www.tuosito.it" class="sr-text-input" required />
      <button type="submit" class="wp-block-button__link" style="padding:17px 30px">Measure the impact</button>
    </div>
  </form>
  <p class="sr-tool-pending sr-mono" data-sr-tool-pending hidden>Measuring<span class="sr-blink">…</span></p>
  <div class="sr-tool-result" data-sr-tool-result hidden>
    <p style="margin:0;font-size:14px;color:var(--sr-grigio)" data-sr-tool-url></p>
    <div class="sr-tool-result__score">
      <span class="sr-mono" data-sr-tool-grams>0 g</span>
    </div>
    <div class="sr-barra" style="height:10px;margin-top:8px"><div class="sr-barra__fill" data-sr-tool-fill style="width:0%"></div><span class="sr-barra__tick" style="left:50%"></span></div>
    <p style="margin-top:20px;font-size:15.5px;color:var(--sr-grigio)" data-sr-tool-verdict></p>
    <div class="sr-tool-cwv">
      <div><p class="sr-eyebrow" style="margin-bottom:8px">Page weight</p><p class="sr-tool-cwv-value sr-mono" data-sr-tool-weight></p></div>
      <div><p class="sr-eyebrow" style="margin-bottom:8px">Annual estimate</p><p class="sr-tool-cwv-value sr-mono" data-sr-tool-year></p></div>
    </div>
    <p class="sr-tool-caption sr-mono">Sustainable Web Design model (co2.js, Apache-2.0). Per-visit estimate; the annual figure is based on 10,000 visits/month.</p>
  </div>
</div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-section--bianco","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-section--bianco"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">How it works</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">Three steps, no sign-up<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:group {"className":"","layout":{"type":"grid","minimumColumnWidth":"240px"}} -->
<div class="wp-block-group is-layout-grid" style="--sr-grid-min:240px"><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">01</p><p style="font-weight:500;margin-top:8px">Enter the address</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">The page to measure: usually the homepage, the most visited one.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">02</p><p style="font-weight:500;margin-top:8px">We weigh the page</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Using the PageSpeed API we measure the total bytes the browser must download to show the page.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">03</p><p style="font-weight:500;margin-top:8px">Emissions estimate</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">We apply the Sustainable Web Design model (co2.js) and get the grams of CO₂e per visit, a comparison with the web average, and the annual estimate.</p></div></div>
<!-- /wp:group -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">The method</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">How we actually estimate your website’s carbon emissions<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">The calculation starts from a concrete, measurable figure: with the PageSpeed API we weigh every byte the browser has to download to show your page. On that weight we apply the Green Web Foundation’s Sustainable Web Design model — the same formulas as the open-source co2.js library — which translates transferred bytes into energy consumed along the chain (data centre, network, device) and finally into grams of CO₂ equivalent per visit.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">It’s an estimate, and it’s only fair to treat it as one. The model uses global average coefficients for energy intensity and the electricity mix: it doesn’t know the real energy source of your hosting or the exact behaviour of each visitor. It isn’t a certified measurement of environmental footprint, but a reliable, comparable order of magnitude. Its strength is that it ties back to a technical fact — page weight — that you can genuinely act on.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-section--bianco","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-section--bianco"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Reading the result</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">How to read your website’s CO₂ grams per visit<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">The key number is the CO₂ equivalent per single visit, which we compare against the web average, around 0.8 grams. Below that threshold you’re among the lighter sites; noticeably above it, your page is heavier than average and there’s room to lighten it. The annual estimate multiplies that value by a reference traffic figure: change it to your site’s real visits, and the impact grows or shrinks proportionally.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">The comparison matters more than the absolute value. A few grams per visit look like nothing, but multiplied by tens of thousands of visits a month they become a real figure — and above all, they mirror a heavy page: the sites that pollute more are almost always the ones that load more slowly, too. So read the impact as a second performance indicator, not only as an environmental issue.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Three common questions</p>
<!-- /wp:paragraph -->
<!-- wp:details -->
<details class="wp-block-details"><summary>How do you calculate emissions?</summary><!-- wp:paragraph -->
<p>With the Green Web Foundation’s Sustainable Web Design model (the co2.js library, Apache-2.0): from page weight to energy consumed, down to grams of CO₂e. It’s an estimate using global average coefficients.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Why does a lighter website pollute less?</summary><!-- wp:paragraph -->
<p>Because every byte transferred consumes energy — in the data center, on the network, on your device. Less weight means less energy, fewer emissions and, as a side effect, a faster website.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Where does the annual estimate come from?</summary><!-- wp:paragraph -->
<p>We multiply the per-visit emissions by a reference traffic of 10,000 visits a month. Change it to your website’s real traffic and the estimate scales proportionally.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-section--bianco","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-section--bianco"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">How to improve</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">How to reduce your website’s carbon footprint<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"base"} -->
<p class="has-grigio-color has-text-color has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:12px">Cutting emissions and speeding up your site are the same job: both come down to trimming unnecessary weight.</p>
<!-- /wp:paragraph -->
<!-- wp:group {"className":"","layout":{"type":"grid","minimumColumnWidth":"240px"}} -->
<div class="wp-block-group is-layout-grid" style="--sr-grid-min:240px"><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">01</p><p style="font-weight:500;margin-top:8px">Lighten your images</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Photos are almost always the heaviest line item: convert them to WebP or AVIF with lazy loading, and you’ll cut most of the bytes — and the emissions — right there.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">02</p><p style="font-weight:500;margin-top:8px">Cut down scripts and fonts</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Every extra third-party library and every additional typeface is energy transferred on every visit: keep only what you truly need.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">03</p><p style="font-weight:500;margin-top:8px">Make the most of caching and a CDN</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Good caching and a content delivery network avoid transferring the same content a thousand times over: less repeated traffic, less consumption.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">04</p><p style="font-weight:500;margin-top:8px">Choose green hosting</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">A provider running on renewable energy lowers the carbon intensity of every byte served: it’s the simplest lever for an immediate effect.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">05</p><p style="font-weight:500;margin-top:8px">Favour a sober design</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">No autoplaying video or heavy animation where it isn’t needed: a clean aesthetic consumes less and, often, communicates better.</p></div></div>
<!-- /wp:group -->
<!-- wp:html -->
<div style="margin-top:24px;display:flex;flex-direction:column;gap:8px;align-items:flex-start"><p class="sr-card-link" style="margin-top:12px"><a href="/en/services/redesign-migration/">Want us to lighten it for you? See our technical redesign service →</a></p><p class="sr-card-link" style="margin-top:12px"><a href="/en/blog/slow-website-causes-fixes/">Read more: the 7 causes of a slow website →</a></p><p class="sr-card-link" style="margin-top:12px"><a href="/en/blog/website-environmental-impact/">Guide: how much your site weighs on the environment (and on your wallet) →</a></p></div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-dark","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-dark"><!-- wp:heading -->
<h2 class="wp-block-heading">Want to lighten up the website<span class="sr-accent-dot">?</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="margin-top:12px">Optimized images, a clean technical foundation, less weight for the same content: less CO₂ and PageSpeed 90+ by contract.</p>
<!-- /wp:paragraph -->
<!-- wp:buttons {"style":{"spacing":{"blockGap":"14px","margin":{"top":"28px"}}},"layout":{"type":"flex","justifyContent":"center"}} -->
<div class="wp-block-buttons" style="margin-top:28px"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/en/services/redesign-migration/">Rebuild and migration</a></div>
<!-- /wp:button -->
<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/en/tools/speed-test/">Measure your speed</a></div>
<!-- /wp:button -->
</div>
<!-- /wp:buttons -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-section--bianco","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-section--bianco"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">The other free tools</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<div class="sr-servizi-rows"><div><span class="sr-mono" style="color:var(--sr-oltremare)">/00</span><a href="/en/tools/full-site-checkup/" style="color:var(--sr-inchiostro);font-size:15.5px">Full check-up</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/01</span><a href="/en/tools/speed-test/" style="color:var(--sr-inchiostro);font-size:15.5px">Speed test</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/02</span><a href="/en/tools/seo-audit/" style="color:var(--sr-inchiostro);font-size:15.5px">On-page SEO analysis</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/03</span><a href="/en/tools/gdpr-check/" style="color:var(--sr-inchiostro);font-size:15.5px">GDPR and cookie check</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/04</span><a href="/en/tools/localization-roi/" style="color:var(--sr-inchiostro);font-size:15.5px">Localization ROI</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/05</span><a href="/en/tools/accessibility-check/" style="color:var(--sr-inchiostro);font-size:15.5px">Accessibility check</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/06</span><a href="/en/tools/ai-readiness/" style="color:var(--sr-inchiostro);font-size:15.5px">AI readiness check</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/08</span><a href="/en/tools/eeat-signals/" style="color:var(--sr-inchiostro);font-size:15.5px">E-E-A-T signals</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div></div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
