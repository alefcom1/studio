<?php
/**
 * Title: Pagina — Articolo: Sito multilingue: hreflang senza mal di testa
 * Slug: remarka-studio/en-blog-hreflang-sito-multilingue
 * Categories: remarka-pagine
 * Description: Articolo blog: Sito multilingue: hreflang senza mal di testa
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1440px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:html -->
<p class="sr-mono" style="color:var(--sr-grigio);font-size:13px">18 JUL 2026</p>
<!-- /wp:html -->
<!-- wp:heading {"level":1,"style":{"typography":{"fontSize":"clamp(32px,4vw,48px)"}}} -->
<h1 class="wp-block-heading" style="font-size:clamp(32px,4vw,48px)">Multilingual website: hreflang without the headache</h1>
<!-- /wp:heading -->
<!-- wp:html -->
<figure class="wp-block-image size-large" style="margin:8px 0 8px"><img src="/wp-content/themes/remarka-studio/assets/img/blog/hreflang-cover.svg" alt="Hreflang for a multilingual website: the Italian, English and German versions linked so Google serves the right language" width="1200" height="630" loading="lazy" style="max-width:100%;height:auto;display:block;border:1px solid var(--sr-bordo)"/></figure>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1440px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:18px;line-height:1.75;max-width:75ch">You’ve translated the site into English and German, rightly so. But now an Italian customer searches Google and ends up on the English page; a German lands on the Italian version; and your two pages — same content, different languages — compete with each other in the results. The culprit is almost always the same: hreflang is missing or wrong. It’s the attribute that tells Google “this page is the Italian version, that one is English, serve each to the right person.” People talk about hreflang for a multilingual website as something forbidding: it is, if you treat it as a plugin to switch on. Let’s see what it really is, how to set it up without errors and why it’s engineering, not luck.</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">What hreflang is (in plain terms)<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Imagine you have the same page in three languages: Italian, English, German. To a search engine they’re three different addresses with contents that look very much alike — and without an explicit signal, Google has to guess which to show to whom, risking mistakes or treating them as duplicate content. Hreflang is that explicit signal: a small marker, present on every version, that says “I exist in these languages, here are the addresses of all of them, and I’m the one for Italian.”</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">The golden rule is reciprocity: if the Italian page points to the English one, the English must point back to the Italian, and every version must list all the others — itself included. Google, in its official documentation on localised versions, insists on exactly this: the references must be bidirectional and complete, or it ignores them. This is where most of the headaches come from: not in the concept, but in the consistency to maintain across dozens of pages.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<figure class="wp-block-image size-large" style="margin:36px 0 8px"><img src="/wp-content/themes/remarka-studio/assets/img/blog/hreflang-versioni.svg" alt="How hreflang works in a multilingual website: the Italian, English and German versions cite each other reciprocally" width="1200" height="500" loading="lazy" style="max-width:100%;height:auto;display:block;border:1px solid var(--sr-bordo)"/><figcaption class="sr-mono" style="margin-top:12px;font-size:12.5px;letter-spacing:0.04em;color:var(--sr-grigio);max-width:75ch">Hreflang links the versions of a page: each declares itself and all the others, reciprocally (if IT points to EN, EN must point to IT). This way Google serves the right language and doesn’t treat them as duplicate content. Source: Google Search Central, localised versions.</figcaption></figure>
<!-- /wp:html -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">The mistakes that break a multilingual website<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Almost every hreflang problem comes from a few recurring mistakes. Knowing them is half the job, because they’re almost always the same ones.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<div class="sr-list-rows"><div><span class="sr-mono">a</span><span>Non-reciprocal references: the IT page cites the EN one, but the EN doesn’t reciprocate. Google discards the whole pair and goes back to guessing.</span></div><div><span class="sr-mono">b</span><span>Wrong language codes: “en-UK” doesn’t exist (it’s “en-GB”), and a made-up code is silently ignored.</span></div><div><span class="sr-mono">c</span><span>Relative URLs or pages pointing to “noindex” versions: hreflang must point to absolute, indexable addresses, or it’s useless.</span></div><div><span class="sr-mono">d</span><span>The self-reference is missing: every version must also list itself. Forgetting it is the most common and most silent mistake.</span></div></div>
<!-- /wp:html -->
<!-- wp:html -->
<p class="sr-card-link" style="margin-top:14px"><a href="https://developers.google.com/search/docs/specialty/international/localized-versions" target="_blank" rel="noopener">Google — tell Google about localised versions (hreflang) →</a></p>
<!-- /wp:html -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Hreflang isn’t everything: the language has to ring true<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">There’s a misconception to dismantle: hreflang solves “which version to show,” not “the version is any good.” You can have perfect hreflang and still lose the customer if the translation sounds fake. A machine-translated product page with the wrong register drives away the person reading it in their own language — and no technical attribute makes up for that. CSA’s research (“Can’t Read, Won’t Buy”) has said it for years: people buy far more willingly in their own language, and distrust text that sounds foreign.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">That’s why, for us, multilingual is two crafts in one: the engineering that links the versions (hreflang, sitemap, URL structure) and the native-speaking editors who write, rather than machine-translate. The languages are handled by native speakers of the Remarka group, in the field since 2001, selected by an internal testing platform that rejects the vast majority of candidates — the same one that holds the quality of every multilingual project of ours. And if a market has its own rules — for Germany, Austria — the technical part goes beyond hreflang: it’s the handling of multi-regional sites.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<p class="sr-card-link" style="margin-top:14px"><a href="/en/services/multilingual-websites/">Multilingual websites with native-speaking editors →</a></p><p class="sr-card-link" style="margin-top:14px"><a href="https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites" target="_blank" rel="noopener">Google — managing multi-regional and multilingual sites →</a></p><p class="sr-card-link" style="margin-top:14px"><a href="/en/case-studies/">The platform that selects who translates (only 8% pass) →</a></p>
<!-- /wp:html -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">How to keep it in order, without losing your mind<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">The secret to not losing your mind over hreflang is not managing it by hand. Across dozens of pages and three languages, keeping reciprocal references by hand is an endless source of errors. The solution is to generate hreflang from a single map of correspondences — one source of truth, from which every page inherits its own links — so that adding a page doesn’t mean updating thirty. It’s exactly the approach this site is built on: Italian at the root, English and Russian as coherent trees, linked by a map that’s never touched by hand.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">In practice, before adding languages it’s worth checking how Google already reads your site: whether the existing versions cite each other correctly, whether there are wrong codes, whether something ends up out of the index. An on-page SEO analysis surfaces these problems before they cost you positions. And if you’re thinking not just of translating but of opening a foreign market for real, hreflang is only the first piece of a bigger picture: digital export.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<p class="sr-card-link" style="margin-top:14px"><a href="/en/tools/seo-audit/">Analyse your page’s on-page SEO for free →</a></p><p class="sr-card-link" style="margin-top:14px"><a href="/en/services/multilingual-websites/">We design your multilingual site at a fixed price →</a></p><p class="sr-card-link" style="margin-top:14px"><a href="/en/blog/website-for-export/">Read also: digital export, the site that opens foreign markets →</a></p>
<!-- /wp:html -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Sources<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:16px;line-height:1.7;max-width:75ch;margin-top:8px">The figures and claims in this article come from here. These are primary sources, not summaries: open them and check for yourself.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<ul style="list-style:none;padding:0;margin:20px 0 0;border-top:1px solid var(--sr-bordo)"><li style="margin-top:16px;line-height:1.55"><a href="https://developers.google.com/search/docs/specialty/international/localized-versions" target="_blank" rel="noopener">Google Search Central — localised versions (hreflang)</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">The official documentation: how to declare versions by language, with reciprocal and complete references.</span></li><li style="margin-top:16px;line-height:1.55"><a href="https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites" target="_blank" rel="noopener">Google Search Central — multi-regional and multilingual sites</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">How to handle language and country together: URL structure, targeting and pitfalls to avoid.</span></li><li style="margin-top:16px;line-height:1.55"><a href="https://csa-research.com/Featured-Content/Global-Growth/CRWB-Series/CRWB-B2C" target="_blank" rel="noopener">CSA Research — “Can’t Read, Won’t Buy”</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">The research on buying behaviour: people buy far more willingly in their own language.</span></li></ul>
<!-- /wp:html -->
<!-- wp:html -->
<p class="sr-card-link" style="margin-top:32px"><a href="/en/services/multilingual-websites/">Multilingual sites with hreflang and native speakers, at a fixed price →</a></p>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-cta-band","layout":{"type":"constrained","contentSize":"1440px"}} -->
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
<!-- wp:html -->
<div class="sr-cta-band__trust"><div class="sr-cta-band__trust-item"><strong>100% free</strong><span>No obligation</span></div><div class="sr-cta-band__trust-item"><strong>Response within 24 hours</strong><span>Detailed quote</span></div><div class="sr-cta-band__trust-item"><strong>Your data, protected</strong><span>Full confidentiality</span></div></div>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1440px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:buttons {"style":{"spacing":{"blockGap":"14px"}},"layout":{"type":"flex","justifyContent":"center"}} -->
<div class="wp-block-buttons"><!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/en/blog/">← All articles</a></div>
<!-- /wp:button -->
</div>
<!-- /wp:buttons -->
</section>
<!-- /wp:group -->
