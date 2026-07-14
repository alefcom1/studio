<?php
/**
 * Title: Pagina — Strumento: Verifica accessibilità
 * Slug: remarka-studio/en-strumento-verifica-accessibilita
 * Categories: remarka-pagine
 * Description: Strumento gratuito Verifica accessibilità: widget interattivo, come funziona, FAQ, CTA.
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","className":"sr-section sr-hero","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-hero"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Free tool /05</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"level":1,"style":{"typography":{"fontSize":"clamp(34px,4vw,52px)"}}} -->
<h1 class="wp-block-heading" style="font-size:clamp(34px,4vw,52px)">Accessibility check: is your website usable by everyone?<span class="sr-accent-dot">.</span></h1>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="max-width:100%">We use Google to check the most common accessibility barriers — contrast, labels, structure. Since 28 June 2025 the European Accessibility Act makes accessibility a legal duty for many websites. No sign-up.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:html -->

<div class="sr-tool-widget sr-card" data-sr-tool="a11y" data-sr-locale="en"
     data-label-suffix=" — accessibility"
     data-verdict-good="Great: the main barriers are already removed."
     data-verdict-mid="Average accessibility: some barriers remain."
     data-verdict-poor="Poor accessibility: significant barriers for users."
     data-audits-empty="No significant barriers found."
     data-err="We couldn’t complete the analysis. Please try again in a few minutes.">
  <form data-sr-tool-form>
    <div class="sr-tool-row"><input type="text" placeholder="www.tuosito.it" class="sr-text-input" required /><button type="submit" class="wp-block-button__link" style="padding:17px 30px">Check accessibility</button></div>
  </form>
  <p class="sr-tool-pending sr-mono" data-sr-tool-pending hidden>Analyzing<span class="sr-blink">…</span></p>
  <div class="sr-tool-result" data-sr-tool-result hidden>
    <p style="margin:0;font-size:14px;color:var(--sr-grigio)" data-sr-tool-url></p>
    <div class="sr-tool-result__score">
      <span class="sr-mono" data-sr-tool-score>0</span><span class="sr-mono" style="font-size:18px;color:var(--sr-grigio)">/100</span>
    </div>
    <div class="sr-barra" style="height:10px"><div class="sr-barra__fill" data-sr-tool-fill style="width:0%"></div><span class="sr-barra__tick" style="left:90%"></span></div>
    <p style="margin-top:20px;font-size:15.5px;color:var(--sr-grigio)" data-sr-tool-verdict></p>
    <ul class="sr-tool-audits" data-sr-tool-audits></ul>
      <p class="sr-disclaimer">Automatic check (Lighthouse): it covers part of the WCAG 2.1 AA criteria. Full EAA compliance also requires a manual review.</p>
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
<div class="wp-block-group is-layout-grid" style="--sr-grid-min:240px"><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">01</p><p style="font-weight:500;margin-top:8px">Enter the address</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">The page to check: the homepage or a service page, wherever most users land.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">02</p><p style="font-weight:500;margin-top:8px">Lighthouse analysis</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">We use Lighthouse’s Accessibility category via the PageSpeed API: contrast, alt text, form labels, heading structure.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">03</p><p style="font-weight:500;margin-top:8px">See the barriers to remove</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">A 0–100 score and the list of issues found, explained in plain English. An automatic check covers part of the WCAG criteria, not all of them.</p></div></div>
<!-- /wp:group -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Three common questions</p>
<!-- /wp:paragraph -->
<!-- wp:details -->
<details class="wp-block-details"><summary>What is the European Accessibility Act?</summary><!-- wp:paragraph -->
<p>A European directive (EAA), in force in Italy since 28 June 2025: many websites of businesses selling to consumers must be accessible to the WCAG 2.1 level AA standard. It’s a legal duty, with some exemptions for microenterprises.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Is this test enough to be compliant?</summary><!-- wp:paragraph -->
<p>No: an automatic check catches only part of the WCAG criteria. Full compliance also requires manual testing — keyboard navigation, screen readers, content. It’s a great starting point, not a certificate.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Does this apply to my business too?</summary><!-- wp:paragraph -->
<p>If you sell goods or services to consumers online (e-commerce, banking, transport, services), most likely yes. Microenterprises offering services have exemptions: it’s best to check case by case.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-dark","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-dark"><!-- wp:heading -->
<h2 class="wp-block-heading">Want to make the website accessible<span class="sr-accent-dot">?</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="margin-top:12px">We check the barriers one by one — automatic and manual — and fix them to the WCAG 2.1 AA standard.</p>
<!-- /wp:paragraph -->
<!-- wp:buttons {"style":{"spacing":{"blockGap":"14px","margin":{"top":"28px"}}},"layout":{"type":"flex","justifyContent":"center"}} -->
<div class="wp-block-buttons" style="margin-top:28px"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/en/#contatti">Request an accessibility check</a></div>
<!-- /wp:button -->
<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/en/services/business-websites/">See business websites</a></div>
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
<div class="sr-servizi-rows"><div><span class="sr-mono" style="color:var(--sr-oltremare)">/01</span><a href="/en/tools/speed-test/" style="color:var(--sr-inchiostro);font-size:15.5px">Speed test</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/02</span><a href="/en/tools/seo-audit/" style="color:var(--sr-inchiostro);font-size:15.5px">On-page SEO analysis</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/03</span><a href="/en/tools/gdpr-check/" style="color:var(--sr-inchiostro);font-size:15.5px">GDPR and cookie check</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/04</span><a href="/en/tools/localization-roi/" style="color:var(--sr-inchiostro);font-size:15.5px">Localization ROI</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/06</span><a href="/en/tools/ai-readiness/" style="color:var(--sr-inchiostro);font-size:15.5px">AI readiness check</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/07</span><a href="/en/tools/website-carbon/" style="color:var(--sr-inchiostro);font-size:15.5px">CO₂ impact</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div></div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
