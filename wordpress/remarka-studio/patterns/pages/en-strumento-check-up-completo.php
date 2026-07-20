<?php
/**
 * Title: Pagina — Strumento: Check-up completo
 * Slug: remarka-studio/en-strumento-check-up-completo
 * Categories: remarka-pagine
 * Description: Strumento gratuito Check-up completo: widget interattivo, come funziona, FAQ, CTA.
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","className":"sr-section sr-hero","layout":{"type":"constrained","contentSize":"1440px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-hero"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Full check-up · free</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"level":1,"style":{"typography":{"fontSize":"clamp(34px,4vw,52px)"}}} -->
<h1 class="wp-block-heading" style="font-size:clamp(34px,4vw,52px)">The complete check-up for your website<span class="sr-accent-dot">.</span></h1>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="max-width:100%">Seven free tools in a single analysis. Paste your address: in under a minute you get a 0–100 health score, the seven traffic lights behind it and the three most urgent fixes. The measurement is the real one from Google PageSpeed Insights, alongside our own privacy and AI-readiness checks. The full report, page by page, we send you as a PDF.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1440px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:html -->

<div class="sr-tool-widget sr-card sr-checkup" data-sr-tool="checkup" data-sr-locale="en"
     data-word-0="Excellent" data-word-1="Good" data-word-2="Needs work" data-word-3="Critical"
     data-composite-0="Excellent site health" data-composite-1="Good site health"
     data-composite-2="Site needs work" data-composite-3="Site at risk"
     data-label-suffix="— mobile analysis"
     data-calc-note="Calculated on {n} of 7 measurements."
     data-na-text="We couldn’t measure this aspect: the website refused automated reading, or Google’s service was overloaded."
     data-err="We couldn’t complete the check-up. Please try again in a few minutes."
     data-ai-suffix=" / 4 signals"
     data-more-label="See the full test →">
  <form data-sr-tool-form>
    <div class="sr-tool-row">
      <input type="text" placeholder="www.ilvostrosito.it" class="sr-text-input" required />
      <button type="submit" class="wp-block-button__link" style="padding:17px 30px">Analyse the site — free</button>
    </div>
  </form>
  <p class="sr-tool-pending sr-mono" data-sr-tool-pending hidden>Analysis in progress on seven fronts — this can take up to 30 seconds<span class="sr-blink">…</span></p>

  <div class="sr-tool-result" data-sr-tool-result hidden>

    <div class="sr-checkup-incomplete" data-sr-checkup-incomplete hidden>
      <h3 class="wp-block-heading">Check-up incomplete</h3>
      <p>Try again in a few minutes: some measures didn’t respond (Google’s service may be overloaded, or the website refused the reading).</p>
      <button type="button" class="wp-block-button__link" data-sr-checkup-retry>Retry</button>
    </div>

    <div data-sr-checkup-composite>
      <p class="sr-eyebrow">Site health</p>
      <div class="sr-checkup-composite">
        <div class="sr-gauge" data-sr-gauge>
          <div class="sr-gauge__num"><span class="sr-gauge__num-value" data-sr-gauge-num>0</span><span class="sr-gauge__num-suffix">/100</span></div>
        </div>
        <div>
          <p class="sr-mono sr-checkup-url" data-sr-checkup-url></p>
          <h2 class="wp-block-heading sr-checkup-label" data-sr-checkup-label></h2>
          <p class="sr-checkup-method-note">Weighted average of 7 measures. Performance, SEO, accessibility and best practices from Google PageSpeed; privacy, AI and CO₂ from Studio Remarka checks.</p>
          <p class="sr-mono sr-checkup-calc" data-sr-checkup-calc></p>
        </div>
      </div>
    </div>

    <!-- Priorità PRIMA dei sette semafori (feedback lancio Product Hunt,
         19.07.2026: «a prioritized action list instead of dumping all results»
         — chi non è tecnico deve vedere subito da dove partire). -->
    <div data-sr-checkup-priorities-wrap style="margin-top:32px">
      <p class="sr-eyebrow">Where to start</p>
      <h2 class="wp-block-heading" style="font-size:clamp(24px,2.4vw,32px)">The 3 fixes that matter most</h2>
      <p style="margin:8px 0 20px;color:var(--sr-grigio);font-size:15.5px">Ranked by impact on your score: how much you’d gain by fixing them.</p>
      <div class="sr-priorities" data-sr-checkup-priorities></div>
    </div>

    <div style="margin-top:32px">
      <p class="sr-eyebrow">The seven measures</p>
      <h2 class="wp-block-heading" style="font-size:clamp(24px,2.4vw,32px)">Seven traffic lights, one score</h2>
      <div class="sr-dim-grid" style="margin-top:24px"><div class="sr-card sr-dim-card" data-sr-dim="perf" data-verdict-0="Fast on mobile: meets Google’s standards." data-verdict-1="Good speed; measurable room on some pages." data-verdict-2="Average for the web, but far from the recommended standards." data-verdict-3="Slow on mobile: most visitors leave before it loads.">
  <div class="sr-dim-card__head"><p class="sr-eyebrow" style="margin:0">Performance</p><span class="sr-dim-card__weight">Weight 25</span></div>
  <div class="sr-dim-card__score"><span class="sr-dim-card__score-value" data-sr-tool-score>—</span><span class="sr-dim-card__score-suffix">/100</span></div>
  <div class="sr-barra" style="height:8px;margin-top:12px"><div class="sr-barra__fill" data-sr-tool-fill style="width:0%"></div></div>
  <p class="sr-dim-card__word" data-sr-dim-word></p>
  <p class="sr-dim-card__findings" data-sr-tool-verdict></p>
  <p class="sr-dim-card__engine sr-mono">Google PageSpeed</p>
  <p class="sr-dim-card__more"><a data-sr-dim-more hidden target="_self">See the full test →</a></p>
</div><div class="sr-card sr-dim-card" data-sr-dim="seo" data-verdict-0="On-page foundations in order: no barrier to indexing." data-verdict-1="Solid structure; a few fixes to finish the basics." data-verdict-2="Some on-page elements are missing or duplicated." data-verdict-3="Something blocks indexing: fix this first.">
  <div class="sr-dim-card__head"><p class="sr-eyebrow" style="margin:0">SEO</p><span class="sr-dim-card__weight">Weight 20</span></div>
  <div class="sr-dim-card__score"><span class="sr-dim-card__score-value" data-sr-tool-score>—</span><span class="sr-dim-card__score-suffix">/100</span></div>
  <div class="sr-barra" style="height:8px;margin-top:12px"><div class="sr-barra__fill" data-sr-tool-fill style="width:0%"></div></div>
  <p class="sr-dim-card__word" data-sr-dim-word></p>
  <p class="sr-dim-card__findings" data-sr-tool-verdict></p>
  <p class="sr-dim-card__engine sr-mono">Google PageSpeed</p>
  <p class="sr-dim-card__more"><a data-sr-dim-more hidden target="_self">See the full test →</a></p>
</div><div class="sr-card sr-dim-card" data-sr-dim="a11y" data-verdict-0="Few or no barriers: usable under WCAG 2.1 AA." data-verdict-1="Good level; minor barriers left to remove." data-verdict-2="Several barriers found: contrast, labels, navigation." data-verdict-3="Serious barriers: hard to use for many people (EAA obligation).">
  <div class="sr-dim-card__head"><p class="sr-eyebrow" style="margin:0">Accessibility</p><span class="sr-dim-card__weight">Weight 15</span></div>
  <div class="sr-dim-card__score"><span class="sr-dim-card__score-value" data-sr-tool-score>—</span><span class="sr-dim-card__score-suffix">/100</span></div>
  <div class="sr-barra" style="height:8px;margin-top:12px"><div class="sr-barra__fill" data-sr-tool-fill style="width:0%"></div></div>
  <p class="sr-dim-card__word" data-sr-dim-word></p>
  <p class="sr-dim-card__findings" data-sr-tool-verdict></p>
  <p class="sr-dim-card__engine sr-mono">WCAG 2.1 / EAA</p>
  <p class="sr-dim-card__more"><a data-sr-dim-more hidden target="_self">See the full test →</a></p>
</div><div class="sr-card sr-dim-card" data-sr-dim="gdpr" data-verdict-0="Banner, policies and trackers in order in the initial HTML." data-verdict-1="Framework in place; a couple of points to check by hand." data-verdict-2="Elements missing or some trackers poorly governed." data-verdict-3="Trackers active without a banner, or policies missing: real regulatory risk.">
  <div class="sr-dim-card__head"><p class="sr-eyebrow" style="margin:0">Privacy & cookies</p><span class="sr-dim-card__weight">Weight 15</span></div>
  <div class="sr-dim-card__score"><span class="sr-dim-card__score-value" data-sr-tool-score>—</span><span class="sr-dim-card__score-suffix">/100</span></div>
  <div class="sr-barra" style="height:8px;margin-top:12px"><div class="sr-barra__fill" data-sr-tool-fill style="width:0%"></div></div>
  <p class="sr-dim-card__word" data-sr-dim-word></p>
  <p class="sr-dim-card__findings" data-sr-tool-verdict></p>
  <p class="sr-dim-card__engine sr-mono">Indicative check · not legal advice</p>
  <p class="sr-dim-card__more"><a data-sr-dim-more hidden target="_self">See the full test →</a></p>
</div><div class="sr-card sr-dim-card" data-sr-dim="bp" data-verdict-0="Technically clean: HTTPS, no console errors, up-to-date libraries." data-verdict-1="Good technical level; a few warnings to close." data-verdict-2="Several technical warnings: security, console errors, images." data-verdict-3="Widespread technical issues weakening reliability and security.">
  <div class="sr-dim-card__head"><p class="sr-eyebrow" style="margin:0">Best practices</p><span class="sr-dim-card__weight">Weight 10</span></div>
  <div class="sr-dim-card__score"><span class="sr-dim-card__score-value" data-sr-tool-score>—</span><span class="sr-dim-card__score-suffix">/100</span></div>
  <div class="sr-barra" style="height:8px;margin-top:12px"><div class="sr-barra__fill" data-sr-tool-fill style="width:0%"></div></div>
  <p class="sr-dim-card__word" data-sr-dim-word></p>
  <p class="sr-dim-card__findings" data-sr-tool-verdict></p>
  <p class="sr-dim-card__engine sr-mono">Google PageSpeed</p>
</div><div class="sr-card sr-dim-card" data-sr-dim="ai" data-verdict-0="4 of 4 signals: readable and citable by AI models." data-verdict-1="3 of 4 signals: nearly fully AI-ready." data-verdict-2="2 of 4 signals: structured data or sitemap to complete." data-verdict-3="0–1 signals: AI models struggle to read and cite the site.">
  <div class="sr-dim-card__head"><p class="sr-eyebrow" style="margin:0">AI-readiness</p><span class="sr-dim-card__weight">Weight 10</span></div>
  <div class="sr-dim-card__score"><span class="sr-dim-card__score-value" data-sr-tool-score>—</span><span class="sr-dim-card__score-suffix">/100</span><span class="sr-dim-card__extra" data-sr-dim-extra></span></div>
  <div class="sr-barra" style="height:8px;margin-top:12px"><div class="sr-barra__fill" data-sr-tool-fill style="width:0%"></div></div>
  <p class="sr-dim-card__word" data-sr-dim-word></p>
  <p class="sr-dim-card__findings" data-sr-tool-verdict></p>
  <p class="sr-dim-card__engine sr-mono">4 technical signals</p>
  <p class="sr-dim-card__more"><a data-sr-dim-more hidden target="_self">See the full test →</a></p>
</div><div class="sr-card sr-dim-card" data-sr-dim="co2" data-verdict-0="Light page: emissions below the web average." data-verdict-1="Near the average; room to slim down." data-verdict-2="Above average: the page is heavy to load." data-verdict-3="Well above average: heavy page, an environmental and speed cost.">
  <div class="sr-dim-card__head"><p class="sr-eyebrow" style="margin:0">CO₂ impact</p><span class="sr-dim-card__weight">Weight 5</span></div>
  <div class="sr-dim-card__score"><span class="sr-dim-card__score-value" data-sr-tool-score>—</span><span class="sr-dim-card__score-suffix">/100</span></div>
  <div class="sr-barra" style="height:8px;margin-top:12px"><div class="sr-barra__fill" data-sr-tool-fill style="width:0%"></div></div>
  <p class="sr-dim-card__word" data-sr-dim-word></p>
  <p class="sr-dim-card__findings" data-sr-tool-verdict></p>
  <p class="sr-dim-card__engine sr-mono">SWD model</p>
  <p class="sr-dim-card__more"><a data-sr-dim-more hidden target="_self">See the full test →</a></p>
</div></div>
    </div>

    <div data-sr-checkup-form-wrap style="margin-top:32px">
      <div class="sr-card sr-checkup-lead">
        <p class="sr-eyebrow">Full report</p>
        <h2 class="wp-block-heading" style="font-size:clamp(22px,2.6vw,28px)">The full report, as a PDF</h2>
        <p style="margin-top:10px;color:var(--sr-grigio);font-size:15.5px;line-height:1.6">We send you the complete analysis: one page per dimension, every issue found and the fixes ranked by impact.</p>
        <ul class="sr-tool-audits" style="margin-top:18px">
          <li>The health score with the seven traffic lights</li>
          <li>A page per dimension: score, what we found, what to do</li>
          <li>The three priority fixes with countermeasures</li>
          <li>«What we would do» and Studio Remarka’s details</li>
        </ul>
        <form data-sr-checkup-report-form style="margin-top:24px">
          <p class="sr-hp-field" aria-hidden="true"><label>Website<input type="text" name="sr_checkup_hp" tabindex="-1" autocomplete="off"></label></p>
          <div class="sr-tool-row">
            <input type="email" placeholder="name@yourcompany.com" class="sr-text-input" required />
            <button type="submit" class="wp-block-button__link" style="padding:15px 26px">Send me the PDF report</button>
          </div>
          <label class="sr-consent"><input type="checkbox" data-sr-checkup-consent required /><span>I have read the <a href="/en/privacy/">privacy policy</a> and consent to receiving the report and being contacted.</span></label>
          <label class="sr-consent"><input type="checkbox" data-sr-checkup-consent-monthly /><span>Send me the monthly Core Web Vitals monitoring for this site.</span></label>
          <p class="sr-mono" data-sr-checkup-success hidden style="margin-top:16px;color:var(--sr-verde)">Done. The report is on its way to your inbox: if it doesn’t arrive within a few minutes, check spam or drop us a line.</p>
          <p class="sr-form-error" data-sr-checkup-error hidden>We couldn’t send the report. Try again shortly, or write to us and we’ll send it by hand.</p>
        </form>
        <div class="sr-checkup-dl">
          <span class="sr-mono sr-checkup-dl__or">or</span>
          <button type="button" class="sr-feedback__btn sr-checkup-dl__btn" data-sr-checkup-download data-dl-pending="Preparing your PDF…">Download the PDF now — no e-mail needed</button>
        </div>
        <p class="sr-mono" style="margin-top:20px;font-size:11px;color:var(--sr-grigio);opacity:.85">No spam. We use your address only for the report and possible follow-up. Studio Remarka S.r.l., VAT GE 302230994.</p>
      </div>
    </div>

  </div>
</div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-section--bianco","layout":{"type":"constrained","contentSize":"1440px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-section--bianco"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">How it works</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">Three steps, no sign-up<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:group {"className":"","layout":{"type":"grid","minimumColumnWidth":"240px"}} -->
<div class="wp-block-group is-layout-grid" style="--sr-grid-min:240px"><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">01</p><p style="font-weight:500;margin-top:8px">Paste in the address</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Your home page or the page that brings the most traffic. No sign-up, no payment details.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">02</p><p style="font-weight:500;margin-top:8px">We analyse on seven fronts</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">A single Google PageSpeed API call (performance, SEO, accessibility, best practices) plus our own privacy/cookie and AI-readiness checks, read from our server the way a visitor would see the page.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">03</p><p style="font-weight:500;margin-top:8px">Read the score and priorities</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Health 0–100, the seven traffic lights in plain English and the three fixes that matter most. The full report follows as a PDF.</p></div></div>
<!-- /wp:group -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1440px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">The method</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">What the full check-up actually measures<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">There’s no black box behind the score. Four of the seven dimensions — performance, SEO, accessibility and best practices — come from Google’s PageSpeed Insights API, the same engine behind pagespeed.web.dev: we query Lighthouse in mobile strategy, because that’s the version Google uses to rank you. The other three we compute ourselves: privacy compliance we read from the page’s HTML (banner, policies, trackers before consent), AI-readiness from four technical signals — llms.txt, crawler access, structured data, sitemap — and the CO₂ footprint from the page’s real weight, using the Sustainable Web Design model.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Each dimension enters the score with a stated weight: performance counts most (25 of 100), CO₂ least (5). It’s fair to know what the check-up does not do: it’s not a legal opinion on privacy — it’s an indicative, four-signal check — and it never promises a Google ranking. It’s a precise technical snapshot of your site, not a sales promise.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-section--bianco","layout":{"type":"constrained","contentSize":"1440px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-section--bianco"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Reading the result</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">How to read your site’s health score<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">The health score is the weighted average of the seven traffic lights, not a gut-feel grade. Read it like a traffic light: 90 and up is green (excellent), 75–89 is good, 50–74 leaves real room, below 50 is critical and becomes the priority. Every dimension carries the same colour code, so you see at a glance where the site is solid and where it loses points.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Two readings to avoid. A high score doesn’t mean «number one on Google»: it means the technical foundations are sound. And if a measure shows «N/A» it’s not your site failing: sometimes Google is overloaded, sometimes a site refuses automated reading. In that case we compute health on the successful measures and tell you so clearly.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-section--bianco","layout":{"type":"constrained","contentSize":"1440px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-section--bianco"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">From the community</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">What people who tried them say<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="max-width:70ch">The first reviews from our Product Hunt launch — quoted verbatim, with the authors’ permission.</p>
<!-- /wp:paragraph -->
<!-- wp:group {"className":"","layout":{"type":"grid","minimumColumnWidth":"300px"}} -->
<div class="wp-block-group is-layout-grid" style="--sr-grid-min:300px"><!-- wp:group {"className":"sr-card sr-card--carta","layout":{"type":"constrained"}} -->
<div class="wp-block-group is-layout-constrained sr-card sr-card--carta"><!-- wp:html -->
<p class="sr-recensione__testo">«A solid free checker especially for GDPR and AI readiness, those get overlooked a lot.»</p><p class="sr-mono sr-recensione__firma">Şengül Akkoca · <a href="https://www.producthunt.com/products/studio-remarka" target="_blank" rel="noopener">Product Hunt ↗</a></p>
<!-- /wp:html -->
</div>
<!-- /wp:group -->
<!-- wp:group {"className":"sr-card sr-card--carta","layout":{"type":"constrained"}} -->
<div class="wp-block-group is-layout-constrained sr-card sr-card--carta"><!-- wp:html -->
<p class="sr-recensione__testo">«Ran the GDPR and speed tests on my blog and the results page broke things down in plain language instead of jargon, which I appreciated more than expected.»</p><p class="sr-mono sr-recensione__firma">Ercan · <a href="https://www.producthunt.com/products/studio-remarka" target="_blank" rel="noopener">Product Hunt ↗</a></p>
<!-- /wp:html -->
</div>
<!-- /wp:group -->
<!-- wp:group {"className":"sr-card sr-card--carta","layout":{"type":"constrained"}} -->
<div class="wp-block-group is-layout-constrained sr-card sr-card--carta"><!-- wp:html -->
<p class="sr-recensione__testo">«Ran the GDPR and accessibility checks on my portfolio site and the accessibility report actually pointed out color contrast issues I had missed for years. Solid free tool, will keep using it.»</p><p class="sr-mono sr-recensione__firma">Demet · <a href="https://www.producthunt.com/products/studio-remarka" target="_blank" rel="noopener">Product Hunt ↗</a></p>
<!-- /wp:html -->
</div>
<!-- /wp:group -->
<!-- wp:group {"className":"sr-card sr-card--carta","layout":{"type":"constrained"}} -->
<div class="wp-block-group is-layout-constrained sr-card sr-card--carta"><!-- wp:html -->
<p class="sr-recensione__testo">«ran it on my portfolio site and the accessibility check actually flagged stuff i never noticed before, super useful. the speed results matched what i already knew from lighthouse so feels legit.»</p><p class="sr-mono sr-recensione__firma">Mihriban · <a href="https://www.producthunt.com/products/studio-remarka" target="_blank" rel="noopener">Product Hunt ↗</a></p>
<!-- /wp:html -->
</div>
<!-- /wp:group -->
</div>
<!-- /wp:group -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1440px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Three common questions</p>
<!-- /wp:paragraph -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Is this Google’s real score?</summary><!-- wp:paragraph -->
<p>For performance, SEO, accessibility and best practices, yes — it comes from the official PageSpeed Insights API, mobile strategy. Privacy, AI-readiness and CO₂ are our own checks, with the method stated in each section.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Does the GDPR check replace a privacy consultant?</summary><!-- wp:paragraph -->
<p>No. It’s an indicative, four-signal technical check: it catches the obvious problems — missing banner, trackers before consent — but it’s not a legal opinion and doesn’t replace a consultant.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
<!-- wp:details -->
<details class="wp-block-details"><summary>What’s in the PDF that I don’t already see on screen?</summary><!-- wp:paragraph -->
<p>On screen you see the score, the seven traffic lights and the three priorities. The PDF gives you a page per dimension with every issue found, the fixes ranked by impact, and what we would do, with our company details.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-cta-band","layout":{"type":"constrained","contentSize":"1440px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-cta-band"><!-- wp:heading -->
<h2 class="wp-block-heading">Want us to fix the priorities<span class="sr-accent-dot">?</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="margin-top:12px">From score to quote: we review the report together and hand you a fixed-price action plan, with PageSpeed 90+ guaranteed by contract.</p>
<!-- /wp:paragraph -->
<!-- wp:buttons {"style":{"spacing":{"blockGap":"14px","margin":{"top":"28px"}}},"layout":{"type":"flex","justifyContent":"center"}} -->
<div class="wp-block-buttons" style="margin-top:28px"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/en/#contatti">Book a free consultation</a></div>
<!-- /wp:button -->
<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/en/tools/">See all tools</a></div>
<!-- /wp:button -->
</div>
<!-- /wp:buttons -->
<!-- wp:html -->
<div class="sr-cta-band__trust"><div class="sr-cta-band__trust-item"><strong>100% free</strong><span>No obligation</span></div><div class="sr-cta-band__trust-item"><strong>Response within 24 hours</strong><span>Detailed quote</span></div><div class="sr-cta-band__trust-item"><strong>Your data, protected</strong><span>Full confidentiality</span></div></div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-section--bianco","layout":{"type":"constrained","contentSize":"1440px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-section--bianco"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">The other free tools</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<div class="sr-servizi-rows"><div><span class="sr-mono" style="color:var(--sr-oltremare)">/01</span><a href="/en/tools/speed-test/" style="color:var(--sr-inchiostro);font-size:15.5px">Speed test</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/02</span><a href="/en/tools/seo-audit/" style="color:var(--sr-inchiostro);font-size:15.5px">On-page SEO analysis</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/03</span><a href="/en/tools/gdpr-check/" style="color:var(--sr-inchiostro);font-size:15.5px">GDPR and cookie check</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/04</span><a href="/en/tools/localization-roi/" style="color:var(--sr-inchiostro);font-size:15.5px">Localization ROI</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/05</span><a href="/en/tools/accessibility-check/" style="color:var(--sr-inchiostro);font-size:15.5px">Accessibility check</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/06</span><a href="/en/tools/ai-readiness/" style="color:var(--sr-inchiostro);font-size:15.5px">AI readiness check</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/07</span><a href="/en/tools/website-carbon/" style="color:var(--sr-inchiostro);font-size:15.5px">CO₂ impact</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/08</span><a href="/en/tools/eeat-signals/" style="color:var(--sr-inchiostro);font-size:15.5px">E-E-A-T signals</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/09</span><a href="/en/tools/read-by-ai/" style="color:var(--sr-inchiostro);font-size:15.5px">Your website, read by AI</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/10</span><a href="/en/tools/does-it-sound-native/" style="color:var(--sr-inchiostro);font-size:15.5px">Does it sound native?</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/11</span><a href="/en/tools/llms-txt-generator/" style="color:var(--sr-inchiostro);font-size:15.5px">llms.txt generator</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div></div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
