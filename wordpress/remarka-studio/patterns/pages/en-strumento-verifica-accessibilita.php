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
<p class="sr-eyebrow">The method</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">What this website accessibility test actually checks<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">The engine is Lighthouse’s Accessibility category, called through the PageSpeed API: the same automatic checks Google makes available to developers. In a few seconds the page is examined against dozens of technical rules — contrast between text and background, image alt text, form field labels, heading order, correct use of ARIA attributes — producing a 0–100 score with the list of barriers found.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">It’s worth being clear about the limits, because it’s easy to fool yourself here. An automatic check only catches part of the WCAG 2.1 AA criteria: it captures what a machine can measure, not what a person needs to test. It doesn’t check keyboard navigation, the experience with a screen reader, or how clear your content is for people with cognitive difficulties. It’s the first step toward the compliance required by the European Accessibility Act, not the final certificate.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-section--bianco","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-section--bianco"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Reading the result</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">How to read the score and the barriers found<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">The 0–100 number tells you how well the page passes the automatic checks: the higher it is, the fewer obvious obstacles remain. But the score matters less than the list that comes with it. Each entry is a concrete barrier for a real person — contrast too weak for someone with low vision, a button with no label for someone using a screen reader. Start from those, not from the total.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">A warning against false confidence: even a perfect 100 doesn’t mean “compliant website”. It means you’ve passed the tests a machine can run, which cover roughly a third of the possible issues. The rest — keyboard, screen readers, content — has to be checked by hand. So treat a high score as a good foundation, not as a finish line already crossed.</p>
<!-- /wp:paragraph -->
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
<!-- wp:group {"tagName":"section","className":"sr-section sr-section--bianco","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-section--bianco"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">How to improve</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">How to make your website accessible to everyone<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"base"} -->
<p class="has-grigio-color has-text-color has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:12px">Many barriers fall with simple fixes that improve the experience for everyone, not just for people with disabilities.</p>
<!-- /wp:paragraph -->
<!-- wp:group {"className":"","layout":{"type":"grid","minimumColumnWidth":"240px"}} -->
<div class="wp-block-group is-layout-grid" style="--sr-grid-min:240px"><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">01</p><p style="font-weight:500;margin-top:8px">Increase your contrast</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Text and background need a contrast ratio of at least 4.5:1: the elegant light grey that looks fine on a designer’s screen becomes unreadable in sunlight or for people with low vision.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">02</p><p style="font-weight:500;margin-top:8px">Describe your images</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Every informative image needs alt text describing its content: it’s what a screen reader reads out to someone who can’t see it.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">03</p><p style="font-weight:500;margin-top:8px">Label your forms</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Every field needs an explicit, properly linked label — “Name”, “Email”, “Message” — not just grey placeholder text that vanishes as soon as you start typing.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">04</p><p style="font-weight:500;margin-top:8px">Put your headings and focus order in order</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">A consistent heading hierarchy and a keyboard-navigable path, with focus always visible, make the page usable even without a mouse.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">05</p><p style="font-weight:500;margin-top:8px">Don’t rely on colour alone</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">An error flagged only in red is invisible to someone who can’t distinguish colours: always pair it with an icon or text explaining what’s happening.</p></div></div>
<!-- /wp:group -->
<!-- wp:html -->
<div style="margin-top:24px;display:flex;flex-direction:column;gap:8px;align-items:flex-start"><p class="sr-card-link" style="margin-top:12px"><a href="/en/services/eaa-compliance/">Want us to fix them for you? Audit, fixes and statement — our EAA compliance service →</a></p><p class="sr-card-link" style="margin-top:12px"><a href="/en/blog/eaa-ecommerce-risks/">Read more: EAA 2026, what your e-commerce site really risks →</a></p><p class="sr-card-link" style="margin-top:12px"><a href="/en/blog/accessibility-statement-guide-2026/">Practical guide: the accessibility statement in 2026 →</a></p></div>
<!-- /wp:html -->
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
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/en/services/eaa-compliance/">Discover the EAA compliance service</a></div>
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
<div class="sr-servizi-rows"><div><span class="sr-mono" style="color:var(--sr-oltremare)">/00</span><a href="/en/tools/full-site-checkup/" style="color:var(--sr-inchiostro);font-size:15.5px">Full check-up</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/01</span><a href="/en/tools/speed-test/" style="color:var(--sr-inchiostro);font-size:15.5px">Speed test</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/02</span><a href="/en/tools/seo-audit/" style="color:var(--sr-inchiostro);font-size:15.5px">On-page SEO analysis</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/03</span><a href="/en/tools/gdpr-check/" style="color:var(--sr-inchiostro);font-size:15.5px">GDPR and cookie check</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/04</span><a href="/en/tools/localization-roi/" style="color:var(--sr-inchiostro);font-size:15.5px">Localization ROI</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/06</span><a href="/en/tools/ai-readiness/" style="color:var(--sr-inchiostro);font-size:15.5px">AI readiness check</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/07</span><a href="/en/tools/website-carbon/" style="color:var(--sr-inchiostro);font-size:15.5px">CO₂ impact</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/08</span><a href="/en/tools/eeat-signals/" style="color:var(--sr-inchiostro);font-size:15.5px">E-E-A-T signals</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div></div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
