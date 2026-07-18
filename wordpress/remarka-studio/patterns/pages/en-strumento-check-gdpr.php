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
<div class="wp-block-group is-layout-grid" style="--sr-grid-min:240px"><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">01</p><p style="font-weight:500;margin-top:8px">Enter the site address</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">We read the homepage from our server, the way a first-time visitor would.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">02</p><p style="font-weight:500;margin-top:8px">Four automatic checks</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">We look for the cookie banner (CMP), links to the privacy and cookie policy, trackers loaded before consent, and external domains.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">03</p><p style="font-weight:500;margin-top:8px">A traffic light, not a verdict</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Each point is green, yellow or red: we flag the obvious issues, not a full legal audit.</p></div></div>
<!-- /wp:group -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">The method</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">What this cookie compliance check actually verifies<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Unlike the Google-based tests, here it’s our own server that reads your website’s home page, exactly as a visitor would see it on first landing, before any click. On that HTML we run four automatic checks: we look for the cookie banner (the CMP: Iubenda, Cookiebot, Complianz and similar tools), links to the privacy and cookie policies, tracking tools that fire before consent, and the external domains the page calls.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Let’s say it upfront, because it matters: this is not legal advice. It’s an indicative technical check that catches the obvious problems — the ones Italy’s Data Protection Authority challenges most often — but it doesn’t replace a privacy consultant. It doesn’t see what happens after the user accepts, doesn’t evaluate your consent records, and doesn’t examine your policies line by line. It’s a great starting point to see where to act, not a certificate of compliance.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-section--bianco","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-section--bianco"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Reading the result</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">How to read your compliance traffic light<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Every checkpoint gets a colour, and the colour should be read for exactly what it is. Green: the signal is present and correct. Yellow: something is there but needs a manual check — a policy that exists but might be incomplete, for instance. Red: an important element is missing or, worse, there are active trackers with no banner governing them. The overall picture matters more than any single dot.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">The most common red flag on Italian websites is “trackers without a banner”: Google Analytics or the Meta Pixel firing in the initial HTML, before the user has said yes. It’s also the mistake Italy’s Data Protection Authority penalises most decisively. A yellow, on the other hand, is usually not an emergency: often it just takes completing or updating a policy that’s already there.</p>
<!-- /wp:paragraph -->
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
<!-- wp:group {"tagName":"section","className":"sr-section sr-section--bianco","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-section--bianco"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">How to improve</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">How to bring your consent and cookies up to standard<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"base"} -->
<p class="has-grigio-color has-text-color has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:12px">Practical compliance is built from a handful of measures, but every one of them has to be respected.</p>
<!-- /wp:paragraph -->
<!-- wp:group {"className":"","layout":{"type":"grid","minimumColumnWidth":"240px"}} -->
<div class="wp-block-group is-layout-grid" style="--sr-grid-min:240px"><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">01</p><p style="font-weight:500;margin-top:8px">Install a CMP that actually blocks trackers</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">A proper banner shouldn’t just appear: it has to stop trackers from firing until the user has accepted. That’s the difference between looking compliant and being compliant.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">02</p><p style="font-weight:500;margin-top:8px">Make refusing as easy as accepting</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">The “Reject” button must carry the same visual weight as “Accept”, on the same screen: no cookie walls, no obstacle course for saying no.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">03</p><p style="font-weight:500;margin-top:8px">Publish complete policies</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Clear, up-to-date privacy and cookie policies that are easy to find: they need to state what you collect, why, and who you share it with.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">04</p><p style="font-weight:500;margin-top:8px">Make consent provable</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Keep a record of every consent — when, for what — so you can show it if asked: the yes has to be freely given, informed and traceable.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">05</p><p style="font-weight:500;margin-top:8px">Load trackers only after the yes</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Analytics, pixels and heatmaps should only activate after acceptance, conditionally: before consent, the page has to stay clean.</p></div></div>
<!-- /wp:group -->
<!-- wp:html -->
<div style="margin-top:24px;display:flex;flex-direction:column;gap:8px;align-items:flex-start"><p class="sr-card-link" style="margin-top:12px"><a href="/en/services/business-websites/">We include it in every business website we deliver →</a></p><p class="sr-card-link" style="margin-top:12px"><a href="/en/blog/cookie-banner-compliance-italy-2026/">Read more: the 2026 cookie checklist from Italy’s Data Protection Authority →</a></p></div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-cta-band","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-cta-band"><!-- wp:heading -->
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
<!-- wp:html -->
<div class="sr-cta-band__trust"><div class="sr-cta-band__trust-item"><strong>100% free</strong><span>No obligation</span></div><div class="sr-cta-band__trust-item"><strong>Response within 24 hours</strong><span>Detailed quote</span></div><div class="sr-cta-band__trust-item"><strong>Your data, protected</strong><span>Full confidentiality</span></div></div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-section--bianco","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-section--bianco"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">The other free tools</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<div class="sr-servizi-rows"><div><span class="sr-mono" style="color:var(--sr-oltremare)">/00</span><a href="/en/tools/full-site-checkup/" style="color:var(--sr-inchiostro);font-size:15.5px">Full check-up</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/01</span><a href="/en/tools/speed-test/" style="color:var(--sr-inchiostro);font-size:15.5px">Speed test</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/02</span><a href="/en/tools/seo-audit/" style="color:var(--sr-inchiostro);font-size:15.5px">On-page SEO analysis</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/04</span><a href="/en/tools/localization-roi/" style="color:var(--sr-inchiostro);font-size:15.5px">Localization ROI</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/05</span><a href="/en/tools/accessibility-check/" style="color:var(--sr-inchiostro);font-size:15.5px">Accessibility check</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/06</span><a href="/en/tools/ai-readiness/" style="color:var(--sr-inchiostro);font-size:15.5px">AI readiness check</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/07</span><a href="/en/tools/website-carbon/" style="color:var(--sr-inchiostro);font-size:15.5px">CO₂ impact</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/08</span><a href="/en/tools/eeat-signals/" style="color:var(--sr-inchiostro);font-size:15.5px">E-E-A-T signals</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/09</span><a href="/en/tools/read-by-ai/" style="color:var(--sr-inchiostro);font-size:15.5px">Your website, read by AI</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/10</span><a href="/en/tools/does-it-sound-native/" style="color:var(--sr-inchiostro);font-size:15.5px">Does it sound native?</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/11</span><a href="/en/tools/llms-txt-generator/" style="color:var(--sr-inchiostro);font-size:15.5px">llms.txt generator</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div></div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
