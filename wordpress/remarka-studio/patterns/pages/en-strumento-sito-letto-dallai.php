<?php
/**
 * Title: Pagina — Strumento: Il vostro sito, letto dall’AI
 * Slug: remarka-studio/en-strumento-sito-letto-dallai
 * Categories: remarka-pagine
 * Description: Strumento gratuito Il vostro sito, letto dall’AI: widget interattivo, come funziona, FAQ, CTA.
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","className":"sr-section sr-hero","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-hero"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Strumento gratuito /09</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"level":1,"style":{"typography":{"fontSize":"clamp(34px,4vw,52px)"}}} -->
<h1 class="wp-block-heading" style="font-size:clamp(34px,4vw,52px)">Your website, read by AI<span class="sr-accent-dot">.</span></h1>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="max-width:100%">Paste your address: an artificial intelligence reads your homepage the way ChatGPT or an AI assistant would, and tells you what it understood. What you do, who for, and how easy it is — for an AI — to cite you in an answer. In under a minute, a verdict and the three moves that matter. This isn’t the technical check from «Ready for AI»: here the AI actually reads you.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:html -->

<div class="sr-tool-widget sr-card" data-sr-tool="ai-read" data-sr-locale="en"
     data-ai-loading="The AI is reading your site…"
     data-ai-maintenance="Tool under maintenance."
     data-ai-limit="You’ve reached today’s limit. Please try again tomorrow."
     data-ai-err="The tool isn’t available right now. Please try again shortly.">
  <form data-sr-tool-form>
    <div class="sr-tool-row">
      <input type="text" placeholder="www.tuosito.it" class="sr-text-input" required />
      <button type="submit" class="wp-block-button__link" style="padding:17px 30px">Analyze</button>
    </div>
  </form>
  <p class="sr-tool-pending sr-mono" data-sr-tool-pending hidden>The AI is reading your site…<span class="sr-blink">…</span></p>
  <div class="sr-tool-result" data-sr-tool-result hidden>
    <p style="margin:0;font-size:17px;font-weight:500" data-sr-tool-verdict></p>
    <p class="sr-eyebrow" style="margin-top:24px">AI citability</p>
    <div class="sr-tool-result__score">
      <span class="sr-mono" data-ai-citabilita>0</span><span class="sr-mono" style="font-size:18px;color:var(--sr-grigio)">/100</span>
    </div>
    <div class="sr-barra" style="height:10px"><div class="sr-barra__fill" data-ai-citabilita-fill style="width:0%"></div><span class="sr-barra__tick" style="left:75%"></span><span class="sr-barra__tick" style="left:50%"></span></div>
    <p class="sr-eyebrow" style="margin-top:28px">The 3 moves</p>
    <div data-ai-azioni>
      <template><div class="ai-azione"><span class="ai-azione-fai"></span><span class="ai-azione-arrow">→</span><span class="ai-azione-effetto"></span></div></template>
    </div>
    <p class="sr-disclaimer">We don’t store the content: it’s an AI reading, not a certified audit.</p>

    <div class="sr-ai-lead">
      <p class="sr-eyebrow">Get the full analysis by e-mail</p>
      <form data-ai-lead-form>
        <div class="sr-tool-row">
          <input type="email" class="sr-text-input" placeholder="Your e-mail" required />
          <button type="submit" class="wp-block-button__link" style="padding:15px 26px">Send me the full analysis</button>
        </div>
        <p style="margin-top:12px;font-size:13.5px"><label><input type="checkbox" data-ai-lead-consent required> I agree to be contacted by Studio Remarka.</label></p>
        <input type="text" name="sr_ai_hp" class="sr-hp-field" tabindex="-1" autocomplete="off">
      </form>
      <p data-ai-lead-success hidden>Done — check your inbox.</p>
      <p class="sr-form-error" data-ai-lead-error hidden>The tool isn’t available right now. Please try again shortly.</p>
    </div>
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
<div class="wp-block-group is-layout-grid" style="--sr-grid-min:240px"><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">01</p><p style="font-weight:500;margin-top:8px">Paste in the address</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Your homepage or the page that represents you. No sign-up, no payment details.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">02</p><p style="font-weight:500;margin-top:8px">The AI reads like an assistant</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">Our server takes the text, headings, structured data, llms.txt and robots.txt of the page and passes them to an AI model — the same information an AI assistant sees when it comes across you.</p></div><div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">03</p><p style="font-weight:500;margin-top:8px">See what it understood</p><p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">What you do and who for, according to the AI; a «citability» score from 0 to 100; and three concrete moves, in the form «do X → get Y». We send you the rest of the analysis by e-mail.</p></div></div>
<!-- /wp:group -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">The method</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">What the AI sees when it reads your site<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">An AI assistant doesn’t «look at» a site the way a visitor does: it reads the text, the headings, the meta description, the structured data and — if there are any — the llms.txt and the rules for its crawlers. From those signals it reconstructs who you are and what you offer. We pass a model exactly that material and ask it three simple things: what this site does, who it’s for, and how confident it would be citing it in an answer. That’s where the citability score comes from: it isn’t your ranking on ChatGPT, it’s how well your site explains itself.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">It’s only fair to say what this tool doesn’t do. It doesn’t promise ChatGPT will name you, it doesn’t count how many times you’re already cited, it isn’t a page-by-page technical audit. It’s a qualitative reading: a mirror of how a machine interprets your words. If the AI misunderstands, it’s usually the site that isn’t speaking clearly — and that’s something you can fix.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-section--bianco","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-section--bianco"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Reading the result</p>
<!-- /wp:paragraph -->
<!-- wp:heading -->
<h2 class="wp-block-heading">How to read the verdict and the citability score<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Start with the verdict and the three moves: they’re already ranked by impact and written as actions, «do this → that happens». Then look at the citability score. From 75 up, the AI understands you and would gladly cite you: the site presents itself well. Between 50 and 74, the sense is there but something is confusing — a generic title, a homepage that doesn’t say straight away what you sell. Below 50, the AI struggles to say what you do: that’s the first thing to fix, before any tactic.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Two readings to avoid. A high score doesn’t mean «first on ChatGPT»: it means you explain yourselves well, which is the precondition, not the guarantee. And if «what it understood» doesn’t sound like you, that isn’t the AI’s mistake: it’s a sign that your site, read from the outside, tells a different story from the one in your head.</p>
<!-- /wp:paragraph -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"className":"sr-eyebrow"} -->
<p class="sr-eyebrow">Three common questions</p>
<!-- /wp:paragraph -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Is this the same as «Is your site ready for AI?»</summary><!-- wp:paragraph -->
<p>No, they’re complementary. «Ready for AI» checks the technical signals — llms.txt, crawler access, structured data, sitemap — and gives a score out of 4. Here the AI actually reads your content and tells you what it understood. One measures the gears, the other the result.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Do you store my site’s text?</summary><!-- wp:paragraph -->
<p>No. The page content is read once to generate the analysis and we don’t save it. We only cache the result, for 24 hours, so a second run on the same site is instant.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
<!-- wp:details -->
<details class="wp-block-details"><summary>Why does the full analysis arrive by e-mail?</summary><!-- wp:paragraph -->
<p>On screen you get the verdict and the three moves right away. We send you the rest — what the AI understood, who it thinks you’re for, why that score — by e-mail, so it stays handy when you talk about it with us or your team.</p>
<!-- /wp:paragraph --></details>
<!-- /wp:details -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-dark","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section sr-dark"><!-- wp:heading -->
<h2 class="wp-block-heading">Want the AI to understand you on the first try<span class="sr-accent-dot">?</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"textColor":"grigio","fontSize":"medium"} -->
<p class="has-grigio-color has-text-color has-medium-font-size" style="margin-top:12px">From verdict to work: we make your site readable by AI assistants and search engines — clear content, structured data, llms.txt. At a fixed price, with PageSpeed 90+ guaranteed by contract.</p>
<!-- /wp:paragraph -->
<!-- wp:buttons {"style":{"spacing":{"blockGap":"14px","margin":{"top":"28px"}}},"layout":{"type":"flex","justifyContent":"center"}} -->
<div class="wp-block-buttons" style="margin-top:28px"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/en/services/technical-seo/">Discover technical SEO</a></div>
<!-- /wp:button -->
<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/en/tools/ai-readiness/">Is your site ready for AI?</a></div>
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
<div class="sr-servizi-rows"><div><span class="sr-mono" style="color:var(--sr-oltremare)">/00</span><a href="/en/tools/full-site-checkup/" style="color:var(--sr-inchiostro);font-size:15.5px">Full check-up</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/01</span><a href="/en/tools/speed-test/" style="color:var(--sr-inchiostro);font-size:15.5px">Speed test</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/02</span><a href="/en/tools/seo-audit/" style="color:var(--sr-inchiostro);font-size:15.5px">On-page SEO analysis</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/03</span><a href="/en/tools/gdpr-check/" style="color:var(--sr-inchiostro);font-size:15.5px">GDPR and cookie check</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/04</span><a href="/en/tools/localization-roi/" style="color:var(--sr-inchiostro);font-size:15.5px">Localization ROI</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/05</span><a href="/en/tools/accessibility-check/" style="color:var(--sr-inchiostro);font-size:15.5px">Accessibility check</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/06</span><a href="/en/tools/ai-readiness/" style="color:var(--sr-inchiostro);font-size:15.5px">AI readiness check</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/07</span><a href="/en/tools/website-carbon/" style="color:var(--sr-inchiostro);font-size:15.5px">CO₂ impact</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/08</span><a href="/en/tools/eeat-signals/" style="color:var(--sr-inchiostro);font-size:15.5px">E-E-A-T signals</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/10</span><a href="/en/tools/does-it-sound-native/" style="color:var(--sr-inchiostro);font-size:15.5px">Does it sound native?</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div><div><span class="sr-mono" style="color:var(--sr-oltremare)">/11</span><a href="/en/tools/llms-txt-generator/" style="color:var(--sr-inchiostro);font-size:15.5px">llms.txt generator</a><span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div></div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
