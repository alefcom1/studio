<?php
/**
 * Title: Full check-up — home block
 * Slug: remarka-studio/en-checkup-home
 * Categories: remarka
 * Description: Block right after the hero: full site check-up (7 tests in one), URL field, submits to /en/tools/full-site-checkup/?url=…&autostart=1.
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","className":"sr-section sr-section--bianco sr-rule-top","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group sr-section sr-section--bianco sr-rule-top"><!-- wp:columns {"verticalAlignment":"center","className":"sr-cascade","style":{"spacing":{"blockGap":{"left":"56px"}}}} -->
<div class="wp-block-columns are-vertically-aligned-center sr-cascade"><!-- wp:column {"verticalAlignment":"center","width":"55%"} -->
<div class="wp-block-column is-vertically-aligned-center" style="flex-basis:55%"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Full check-up · free</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(30px, 3.2vw, 44px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(30px, 3.2vw, 44px)">Your website’s health, in a single number<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"fontSize":"medium","textColor":"grigio","style":{"spacing":{"margin":{"top":"18px"}}}} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="margin-top:18px;max-width:52ch">One test runs seven analyses — speed, SEO, accessibility, privacy, best practices, AI-readiness and environmental impact — and returns a 0–100 health score with the issues to fix first. Google PageSpeed engine plus our own checks, in plain English.</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<div style="display:flex;flex-wrap:wrap;gap:8px;margin-top:24px">
<span class="sr-week-chip">Speed</span>
<span class="sr-week-chip">SEO</span>
<span class="sr-week-chip">Accessibility</span>
<span class="sr-week-chip">Privacy</span>
<span class="sr-week-chip">Best practices</span>
<span class="sr-week-chip">AI</span>
<span class="sr-week-chip">CO₂</span>
</div>
<!-- /wp:html --></div>
<!-- /wp:column -->

<!-- wp:column {"verticalAlignment":"center","width":"45%"} -->
<div class="wp-block-column is-vertically-aligned-center" style="flex-basis:45%"><!-- wp:html -->
<div class="sr-tool-widget sr-card">
  <p class="sr-mono" style="font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--sr-grigio);margin:0 0 14px">Your website, tested in 60 seconds</p>
  <form data-sr-checkup-home data-sr-locale="en">
    <div class="sr-tool-row">
      <input type="text" placeholder="www.yoursite.com" class="sr-text-input" required />
      <button type="submit" class="wp-block-button__link" style="padding:15px 26px">Analyse the site — free</button>
    </div>
  </form>
  <p class="sr-mono" style="font-size:12.5px;color:var(--sr-grigio);margin:18px 0 0">7 tests in one · free · no sign-up</p>
  <p style="font-size:12.5px;color:var(--sr-grigio);opacity:.85;margin:14px 0 0;line-height:1.55">Run by <strong style="color:var(--sr-inchiostro);font-weight:500">Studio Remarka</strong>, in language and digital services since 2001. Real data from Google’s API — never simulated numbers.</p>
</div>
<!-- /wp:html --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></section>
<!-- /wp:group -->
