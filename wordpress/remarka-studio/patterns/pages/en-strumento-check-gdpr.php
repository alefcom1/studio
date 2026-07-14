<?php
/**
 * Title: Pagina — Strumento: Check GDPR e cookie
 * Slug: remarka-studio/en-strumento-check-gdpr
 * Categories: remarka-pagine
 * Description: Strumento gratuito Check GDPR e cookie: widget interattivo, come funziona, FAQ, CTA.
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","className":"sr-section sr-hero","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-hero"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Free tool /03</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"level":1,"style":{"typography":{"fontSize":"clamp(34px,4vw,52px)"}}} -->
<h1 class="wp-block-heading" style="font-size:clamp(34px,4vw,52px)">Is your website GDPR compliant?<span class="sr-accent-dot">.</span></h1>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="max-width:100%">We check the cookie banner, privacy notices and trackers active before consent: four checks to see what’s missing. It’s an indicative check, not legal advice.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:html -->

<div class="sr-tool-widget sr-card" data-sr-tool="gdpr" data-sr-locale="en"
     data-label-cmp-yes="Cookie banner detected" data-label-cmp-no="No cookie banner detected"
     data-label-policy-yes="Link to a privacy/cookie policy present" data-label-policy-no="No link to a privacy/cookie policy"
     data-label-trackers-clean="No trackers in the initial HTML"
     data-label-trackers-flag="Active trackers without a banner"
     data-label-trackers-ok="Trackers present (with banner)"
     data-label-external="{n} external domains load scripts"
     data-err="We couldn’t read the website. Please try again in a few minutes.">
  <form data-sr-tool-form>
    <div class="sr-tool-row">
      <input type="text" placeholder="www.tuosito.it" class="sr-text-input" required />
      <button type="submit" class="wp-block-button__link" style="padding:17px 30px">Check the website</button>
    </div>
  </form>
  <p class="sr-tool-pending sr-mono" data-sr-tool-pending hidden>Reading the website<span class="sr-blink">…</span></p>
  <div class="sr-tool-result" data-sr-tool-result hidden>
    <ul class="sr-gdpr-rows">
      <li><span class="sr-gdpr-key">Cookie banner</span><span data-sr-tool-cmp data-sr-flag></span></li>
      <li><span class="sr-gdpr-key">Policy</span><span data-sr-tool-policy data-sr-flag></span></li>
      <li><span class="sr-gdpr-key">Trackers</span><span data-sr-tool-trackers data-sr-flag></span></li>
      <li><span class="sr-gdpr-key">External scripts</span><span data-sr-tool-external data-sr-flag></span></li>
    </ul>
    <p class="sr-disclaimer" data-sr-tool-disclaimer>An indicative check, not legal advice. A full GDPR audit requires a manual review of cookies, purposes and legal bases.</p>
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
<div class="wp-block-group is-layout-grid" style="--sr-grid-min:240px"><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">01</p><p style="font-weight:500;margin-top:8px">Enter the website address</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">We read the homepage from our server, the way a first-time visitor would.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">02</p><p style="font-weight:500;margin-top:8px">Four automatic checks</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">We look for the cookie banner (CMP), links to the privacy and cookie policy, trackers loaded before consent, and external domains.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">03</p><p style="font-weight:500;margin-top:8px">A traffic light, not a verdict</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Each point is green, yellow or red: we flag the obvious issues, not a full legal audit.</p></div></div>
<!-- /wp:group -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Three common questions</p>
<!-- /wp:paragraph -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Is this legal advice?</summary><!-- wp:paragraph -->
<p>No, and it’s important to say so: this is an indicative automatic check, not legal advice. It flags the obvious technical issues; full compliance should be assessed by a privacy consultant.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
<!-- wp:details -->
<details class="wp-block-details"><summary>What does “trackers without a banner” mean?</summary><!-- wp:paragraph -->
<p>That the page’s initial HTML already contains tracking tools (Google Analytics, Meta Pixel and similar) active before the user consents. It’s the most common red flag on Italian websites.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Why is Italy’s data protection authority so strict on cookies?</summary><!-- wp:paragraph -->
<p>Because consent must be free, informed and provable: refusing must be as easy as accepting, and no advertising tracker can fire before the user says yes.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-dark","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-dark"><!-- wp:heading -->
<h2 class="wp-block-heading">Want us to bring the website into compliance<span class="sr-accent-dot">?</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="margin-top:12px">A compliant banner, notices and consent flow, included in every business website we deliver.</p>
<!-- /wp:paragraph -->
<!-- wp:buttons {"style":{"spacing":{"blockGap":"14px","margin":{"top":"28px"}}},"layout":{"type":"flex","justifyContent":"center"}} -->
<div class="wp-block-buttons" style="margin-top:28px"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/en/services/business-websites/">See business websites</a></div>
<!-- /wp:button -->
<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/en/#contatti">Request an analysis</a></div>
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
<div class="sr-servizi-rows"><div><span class="sr-mono" style="color:var(--sr-oltremare)">/01</span><a href="/en/tools/speed-test/" style="color:var(--sr-inchiostro);font-size:15.5px">Speed test</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/02</span><a href="/en/tools/seo-audit/" style="color:var(--sr-inchiostro);font-size:15.5px">On-page SEO analysis</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/04</span><a href="/en/tools/localization-roi/" style="color:var(--sr-inchiostro);font-size:15.5px">Localization ROI</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/05</span><a href="/en/tools/accessibility-check/" style="color:var(--sr-inchiostro);font-size:15.5px">Accessibility check</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/06</span><a href="/en/tools/ai-readiness/" style="color:var(--sr-inchiostro);font-size:15.5px">AI readiness check</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/07</span><a href="/en/tools/website-carbon/" style="color:var(--sr-inchiostro);font-size:15.5px">CO₂ impact</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div></div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
