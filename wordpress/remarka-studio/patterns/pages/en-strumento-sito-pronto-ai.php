<?php
/**
 * Title: Pagina — Strumento: Sito pronto per l’AI
 * Slug: remarka-studio/en-strumento-sito-pronto-ai
 * Categories: remarka-pagine
 * Description: Strumento gratuito Sito pronto per l’AI: widget interattivo, come funziona, FAQ, CTA.
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","className":"sr-section sr-hero","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-hero"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Free tool /06</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"level":1,"style":{"typography":{"fontSize":"clamp(34px,4vw,52px)"}}} -->
<h1 class="wp-block-heading" style="font-size:clamp(34px,4vw,52px)">Is your website ready for AI?<span class="sr-accent-dot">.</span></h1>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="max-width:100%">When ChatGPT, Claude or Perplexity read the web, do they find your website? We check four signals: llms.txt, AI crawler access, structured data and sitemap. No sign-up.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:html -->

<div class="sr-tool-widget sr-card" data-sr-tool="ai" data-sr-locale="en"
     data-label-yes="Yes" data-label-no="No" data-label-partial="Partial"
     data-err="We couldn’t read the website. Please try again in a few minutes.">
  <form data-sr-tool-form>
    <div class="sr-tool-row">
      <input type="text" placeholder="www.tuosito.it" class="sr-text-input" required />
      <button type="submit" class="wp-block-button__link" style="padding:17px 30px">Check AI readiness</button>
    </div>
  </form>
  <p class="sr-tool-pending sr-mono" data-sr-tool-pending hidden>Checking<span class="sr-blink">…</span></p>
  <div class="sr-tool-result" data-sr-tool-result hidden>
    <div class="sr-tool-result__score">
      <span class="sr-mono" data-sr-tool-score>0/4</span>
    </div>
    <ul class="sr-gdpr-rows">
      <li><span class="sr-gdpr-key">llms.txt</span><span data-sr-tool-llms data-sr-flag></span></li>
      <li><span class="sr-gdpr-key">AI crawlers</span><span data-sr-tool-robots data-sr-flag></span></li>
      <li><span class="sr-gdpr-key">JSON-LD</span><span data-sr-tool-jsonld data-sr-flag></span></li>
      <li><span class="sr-gdpr-key">Sitemap</span><span data-sr-tool-sitemap data-sr-flag></span></li>
    </ul>
    <p class="sr-tool-caption sr-mono">Checks llms.txt, AI crawler access (GPTBot, ClaudeBot, PerplexityBot, Google-Extended), JSON-LD structured data and the sitemap.</p>
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
<div class="wp-block-group is-layout-grid" style="--sr-grid-min:240px"><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">01</p><p style="font-weight:500;margin-top:8px">Enter the site address</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">We read a few public files and the homepage HTML from our server.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">02</p><p style="font-weight:500;margin-top:8px">Four checks</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">We look for the llms.txt file, check whether robots.txt lets AI crawlers through (GPTBot, ClaudeBot, PerplexityBot, Google-Extended), plus JSON-LD structured data and the sitemap.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">03</p><p style="font-weight:500;margin-top:8px">Score N out of 4</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">A traffic light for each signal and an overall score, with guidance on what to add to get found and cited by AI models.</p></div></div>
<!-- /wp:group -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">The method</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">What this AI-readiness check actually verifies<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">As with the GDPR check, it’s our own server that reads a few public files from your site and the HTML of your home page, without going through Google. We run four checks: we look for the llms.txt file, check whether robots.txt lets the model crawlers through (OpenAI’s GPTBot, ClaudeBot, PerplexityBot, Google-Extended), detect JSON-LD structured data on the page, and check for a sitemap. The result is a readiness score out of four.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">It’s worth knowing what this test doesn’t promise. It checks that the technical signals are there, not that ChatGPT or Perplexity will actually cite you: that also depends on the quality and authority of your content, which no tool measures automatically. And since llms.txt is a young standard, its absence isn’t yet a serious mistake: it’s one more opportunity to be read well by machines. Read the score as a list of opportunities, not as a failing grade.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-section--bianco","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-section--bianco"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Reading the result</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">How to read your readiness score out of 4<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Each signal is worth one point and has its own traffic light. Four out of four means your site gives AI models every handhold they need to understand and cite it. Two or three out of four is the most common situation: llms.txt is almost always the missing piece, sometimes structured data too. Zero or one out of four deserves attention, especially if robots.txt is blocking AI crawlers: in that case you’re left out of generated answers, possibly without having decided to be.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">One clarification to avoid needless alarm. Blocking AI crawlers isn’t a flaw in itself: it’s a legitimate choice if you want to protect your content. The test flags it so you know that door is closed, not to tell you you’re wrong. For most businesses, though, being cited by an AI assistant is extra visibility, not a risk: it’s worth weighing with open eyes.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Three common questions</p>
<!-- /wp:paragraph -->
<!-- wp:details -->
<details class="wp-block-details"><summary>What is the llms.txt file?</summary><!-- wp:paragraph -->
<p>A proposed standard: a Markdown text file that tells AI models what the website contains and how to cite it, the way robots.txt does for search engines. It’s young, but increasingly common.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Should you let AI crawlers in?</summary><!-- wp:paragraph -->
<p>It depends on your goals: blocking them protects your content, but excludes you from generated answers. For most businesses, being cited by ChatGPT or Perplexity is extra visibility.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Is structured data still worth it?</summary><!-- wp:paragraph -->
<p>Yes, more than ever: JSON-LD data (schema.org) helps both Google and AI models understand who you are, what you offer and to whom. It’s the foundation of good indexing.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-section--bianco","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-section--bianco"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">How to improve</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">How to get found and cited by AI models<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"base"} -->
<p class="has-grigio-color has-text-color has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:12px">Getting ready for AI doesn’t take an overhaul: it’s largely the same signals that help you with Google, plus a few new ones.</p>
<!-- /wp:paragraph -->
<!-- wp:group {"className":"","layout":{"type":"grid","minimumColumnWidth":"240px"}} -->
<div class="wp-block-group is-layout-grid" style="--sr-grid-min:240px"><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">01</p><p style="font-weight:500;margin-top:8px">Publish an llms.txt file</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">A simple Markdown text file at the root of your site that sums up who you are and what you offer: it’s the map that models are happy to read.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">02</p><p style="font-weight:500;margin-top:8px">Open the door to the right crawlers</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">In robots.txt, allow access to GPTBot, ClaudeBot, PerplexityBot and Google-Extended if you want to appear in generated answers.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">03</p><p style="font-weight:500;margin-top:8px">Add structured data</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">JSON-LD schema.org markup states your name, location, offer and services explicitly: it’s the foundation both Google and AI models use to understand you.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">04</p><p style="font-weight:500;margin-top:8px">Keep your sitemap up to date</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">A complete XML sitemap helps crawlers find every page; make sure your content is readable text, not just images.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">05</p><p style="font-weight:500;margin-top:8px">State facts explicitly</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">State clearly what you do, where, and for whom: models cite what they understand unambiguously, not what they have to guess at.</p></div></div>
<!-- /wp:group -->
<!-- wp:html -->
<div style="margin-top:24px;display:flex;flex-direction:column;gap:8px;align-items:flex-start"><p class="sr-card-link" style="margin-top:12px"><a href="/en/services/technical-seo/">We set it up: it’s part of technical SEO →</a></p><p class="sr-card-link" style="margin-top:12px"><a href="/en/blog/llms-txt-explained/">Read more: llms.txt, what it is and whether your site needs it →</a></p><p class="sr-card-link" style="margin-top:12px"><a href="/en/blog/get-cited-by-chatgpt-geo/">Guide: how to get found and cited by ChatGPT (GEO) →</a></p><p class="sr-card-link" style="margin-top:12px"><a href="/en/tools/eeat-signals/">Also measure your site’s E-E-A-T trust signals →</a></p><p class="sr-card-link" style="margin-top:12px"><a href="/en/tools/llms-txt-generator/">Missing an llms.txt? Create one here in a minute →</a></p><p class="sr-card-link" style="margin-top:12px"><a href="/en/tools/read-by-ai/">Want to know how AI actually reads your site? →</a></p></div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-cta-band","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-cta-band"><!-- wp:heading -->
<h2 class="wp-block-heading">Want to get the website ready for AI<span class="sr-accent-dot">?</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="margin-top:12px">Structured data, the right files and a machine-readable structure: it’s part of the technical SEO we deliver.</p>
<!-- /wp:paragraph -->
<!-- wp:buttons {"style":{"spacing":{"blockGap":"14px","margin":{"top":"28px"}}},"layout":{"type":"flex","justifyContent":"center"}} -->
<div class="wp-block-buttons" style="margin-top:28px"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/en/services/technical-seo/">Discover technical SEO</a></div>
<!-- /wp:button -->
<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/en/tools/seo-audit/">Analyze the on-page SEO</a></div>
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
<div class="sr-servizi-rows"><div><span class="sr-mono" style="color:var(--sr-oltremare)">/00</span><a href="/en/tools/full-site-checkup/" style="color:var(--sr-inchiostro);font-size:15.5px">Full check-up</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/01</span><a href="/en/tools/speed-test/" style="color:var(--sr-inchiostro);font-size:15.5px">Speed test</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/02</span><a href="/en/tools/seo-audit/" style="color:var(--sr-inchiostro);font-size:15.5px">On-page SEO analysis</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/03</span><a href="/en/tools/gdpr-check/" style="color:var(--sr-inchiostro);font-size:15.5px">GDPR and cookie check</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/04</span><a href="/en/tools/localization-roi/" style="color:var(--sr-inchiostro);font-size:15.5px">Localization ROI</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/05</span><a href="/en/tools/accessibility-check/" style="color:var(--sr-inchiostro);font-size:15.5px">Accessibility check</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/07</span><a href="/en/tools/website-carbon/" style="color:var(--sr-inchiostro);font-size:15.5px">CO₂ impact</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/08</span><a href="/en/tools/eeat-signals/" style="color:var(--sr-inchiostro);font-size:15.5px">E-E-A-T signals</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/09</span><a href="/en/tools/read-by-ai/" style="color:var(--sr-inchiostro);font-size:15.5px">Your website, read by AI</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/10</span><a href="/en/tools/does-it-sound-native/" style="color:var(--sr-inchiostro);font-size:15.5px">Does it sound native?</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/11</span><a href="/en/tools/llms-txt-generator/" style="color:var(--sr-inchiostro);font-size:15.5px">llms.txt generator</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div></div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
