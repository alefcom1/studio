<?php
/**
 * Title: Pagina — Articolo: INP, la nuova metrica dei Core Web Vitals: cosa misura e come si risolve
 * Slug: remarka-studio/en-blog-inp-metrica-core-web-vitals
 * Categories: remarka-pagine
 * Description: Articolo blog: INP, la nuova metrica dei Core Web Vitals: cosa misura e come si risolve
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1440px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:html -->
<p class="sr-mono" style="color:var(--sr-grigio);font-size:13px">23 JUL 2026</p>
<!-- /wp:html -->
<!-- wp:heading {"level":1,"style":{"typography":{"fontSize":"clamp(32px,4vw,48px)"}}} -->
<h1 class="wp-block-heading" style="font-size:clamp(32px,4vw,48px)">INP, the new Core Web Vitals metric: what it measures and how to fix it</h1>
<!-- /wp:heading -->
<!-- wp:html -->
<figure class="wp-block-image size-large" style="margin:8px 0 8px"><img src="/wp-content/themes/remarka-studio/assets/img/blog/inp-cover.svg" alt="INP, the new Core Web Vitals metric: what it measures about a site’s responsiveness" width="1200" height="630" loading="lazy" style="max-width:100%;height:auto;display:block;border:1px solid var(--sr-bordo)"/></figure>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1440px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:18px;line-height:1.75;max-width:75ch">Since March 2024 there’s one more acronym to keep an eye on: INP. It has taken the place of another metric, FID, among Google’s Core Web Vitals — the three parameters the engine uses to measure the real experience of people browsing. The change isn’t cosmetic: many sites that passed the test with FID now find themselves struggling with INP, because the new metric is stricter and catches problems that used to stay invisible. Let’s look at what INP actually measures, why your site can seem fast and still fail it, and the concrete steps to get back into good values.</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">What INP is and why it replaced FID<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">INP stands for Interaction to Next Paint. In plain terms, it measures responsiveness: when you tap a button, open a menu or type in a field, how long it takes before the screen responds by showing the result. It’s one of the three Core Web Vitals metrics, alongside LCP (loading speed) and CLS (visual stability).</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Until March 2024, responsiveness was measured with FID, which however only looked at the delay of the very first interaction — and, worse, only the initial wait, not the full response. INP is more honest: it looks at every interaction during the visit and takes the slowest one, from the start of the tap to when the page actually shows the change. That’s why many sites “passed” by FID now find themselves slow under INP: the new metric measures what the user actually feels.</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">What it really measures, and Google’s thresholds<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">The thresholds are clear. An INP under 200 milliseconds is considered good: the page responds in a way the user perceives as instant. Between 200 and 500 milliseconds there’s room for improvement; above 500 milliseconds the experience is poor and noticeable — that annoying micro-delay between the click and the reaction. Google evaluates the 75th percentile: it’s not enough to be fast “on average”, it has to be fast for the vast majority of real interactions.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">And here’s the point: real. Google judges Core Web Vitals on “field” data, collected from real Chrome users (the Chrome UX Report), not on one-off lab tests run from your brand-new computer on a great connection. That’s why an honest test looks at field numbers: it’s the experience of your visitors with their phones and their networks, not the ideal one.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<p class="sr-card-link" style="margin-top:14px"><a href="/en/tools/speed-test/">Measure your site’s real Core Web Vitals for free →</a></p>
<!-- /wp:html -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Why a site can “seem” fast and still fail INP<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">A site can load in a flash and then freeze up at the very first tap. The culprit is almost always the same: too much JavaScript keeping the browser’s “main thread” busy — the same thread that also has to respond to your clicks. If a piece of code runs for a long time without a break, the interaction sits queued up waiting — and that wait is exactly what INP measures. Loading finished a while ago, but the page “isn’t responding”.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">The typical causes are well known: heavy third-party scripts (chat widgets, banners, trackers, widgets), themes and plugins that load huge libraries even where they aren’t needed, event handlers that do too much work on every click. These are things that classic speed tests, all focused on loading, never surfaced. INP brings them out into the open: it measures the moment the user tries to use the site, not just the moment they watch it appear.</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">How to fix INP<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">There’s one strategy: lighten and break up the browser’s workload. Cut unnecessary JavaScript and defer loading what isn’t needed right away; split long operations into short chunks, so the browser can respond to taps in between them; keep third-party scripts in check, since they often weigh more than the site itself. These are technical interventions, but everyone feels the effect: the page reacts instantly.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">The right method is to measure before and after, always on real data. You start by identifying the slowest interactions on smartphones (where processors are weaker and problems show up more clearly), fix the code that slows them down, and verify that INP at the 75th percentile drops below the good threshold. It isn’t magic: it’s removing weight until the page responds the way it should.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<figure class="wp-block-image size-large" style="margin:36px 0 8px"><img src="/wp-content/themes/remarka-studio/assets/img/blog/inp-schema.svg" alt="The three INP thresholds in Core Web Vitals: good under 200 ms, needs improvement 200–500 ms, poor over 500 ms" width="1200" height="500" loading="lazy" style="max-width:100%;height:auto;display:block;border:1px solid var(--sr-bordo)"/><figcaption class="sr-mono" style="margin-top:12px;font-size:12.5px;letter-spacing:0.04em;color:var(--sr-grigio);max-width:75ch">INP (Interaction to Next Paint) thresholds, measured at the 75th percentile on real users: good under 200 ms, needs improvement between 200 and 500 ms, poor above 500 ms. INP measures the delay between the tap and the page’s visible response — the responsiveness the user actually feels. The most common brake is JavaScript keeping the browser’s main thread busy.</figcaption></figure>
<!-- /wp:html -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Responsiveness is an investment, not a detail<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">INP isn’t just another acronym to keep Google happy: it measures a very concrete frustration, that half-second where the site “does nothing” after you’ve tapped it. On mobile, where most visits happen these days, it’s the difference between a site that feels like an app and one that feels broken. And since it counts toward Core Web Vitals, it also affects rankings: responsiveness and visibility travel together.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">In our projects, responsiveness isn’t a last-minute patch: it comes from technical choices — less unnecessary code and third-party scripts kept in check — from day one. A site that loads fast but responds slowly is a promise kept only halfway — and INP, finally, puts that in black and white.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<p class="sr-card-link" style="margin-top:14px"><a href="/en/services/technical-seo/">Technical SEO that starts from real speed →</a></p><p class="sr-card-link" style="margin-top:14px"><a href="/en/blog/core-web-vitals-2026/">Read also: Core Web Vitals in 2026, what Google measures →</a></p><p class="sr-card-link" style="margin-top:14px"><a href="/en/blog/image-optimization-webp-lazy-load/">Read also: images and speed, WebP and lazy-load →</a></p>
<!-- /wp:html -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Sources<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:16px;line-height:1.7;max-width:75ch;margin-top:8px">The figures and claims in this article come from here. These are primary sources, not summaries: open them and check for yourself.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<ul style="list-style:none;padding:0;margin:20px 0 0;border-top:1px solid var(--sr-bordo)"><li style="margin-top:16px;line-height:1.55"><a href="https://web.dev/articles/inp" target="_blank" rel="noopener">web.dev — Interaction to Next Paint (INP)</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">The official definition of the metric and its thresholds, explaining the shift from FID to INP in 2024.</span></li><li style="margin-top:16px;line-height:1.55"><a href="https://web.dev/articles/optimize-inp" target="_blank" rel="noopener">web.dev — optimizing INP</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">The practical guide to improving responsiveness: reducing and splitting main-thread work, managing event handlers.</span></li><li style="margin-top:16px;line-height:1.55"><a href="https://web.dev/articles/vitals" target="_blank" rel="noopener">web.dev — Core Web Vitals (Google)</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">The three metrics (LCP, INP, CLS), their thresholds and why they matter: the real experience, not lab numbers.</span></li><li style="margin-top:16px;line-height:1.55"><a href="https://developer.chrome.com/docs/crux" target="_blank" rel="noopener">Chrome UX Report (CrUX) — documentation</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">The source of “field” data: real Chrome users, on whom Google evaluates Core Web Vitals at the 75th percentile.</span></li></ul>
<!-- /wp:html -->
<!-- wp:html -->
<p class="sr-card-link" style="margin-top:32px"><a href="/en/tools/speed-test/">Measure your site’s Core Web Vitals for free →</a></p>
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
