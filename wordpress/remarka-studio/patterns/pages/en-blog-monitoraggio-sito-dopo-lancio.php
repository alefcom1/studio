<?php
/**
 * Title: Pagina — Articolo: Monitoraggio del sito dopo il lancio: cosa misurare ogni mese
 * Slug: remarka-studio/en-blog-monitoraggio-sito-dopo-lancio
 * Categories: remarka-pagine
 * Description: Articolo blog: Monitoraggio del sito dopo il lancio: cosa misurare ogni mese
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1440px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:html -->
<p class="sr-mono" style="color:var(--sr-grigio);font-size:13px">19 JUL 2026</p>
<!-- /wp:html -->
<!-- wp:heading {"level":1,"style":{"typography":{"fontSize":"clamp(32px,4vw,48px)"}}} -->
<h1 class="wp-block-heading" style="font-size:clamp(32px,4vw,48px)">Website monitoring after launch: what to measure every month</h1>
<!-- /wp:heading -->
<!-- wp:html -->
<figure class="wp-block-image size-large" style="margin:8px 0 8px"><img src="/wp-content/themes/remarka-studio/assets/img/blog/monitoraggio-cover.svg" alt="Website monitoring after launch: a score wearing down over twelve unwatched months, and the Core Web Vitals thresholds" width="1200" height="630" loading="lazy" style="max-width:100%;height:auto;display:block;border:1px solid var(--sr-bordo)"/></figure>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1440px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:18px;line-height:1.75;max-width:75ch">On delivery day your website was a perfect scorecard: PageSpeed 94, all green, handshakes. Twelve months later it takes five seconds to load, one form no longer sends anything, and nobody noticed — because nobody was watching. Websites don’t break with a bang: they wear out in silence, one plugin update at a time, one 8 MB photo at a time. Website monitoring is the craft of noticing before your customers do. Here’s what to measure every month, with which tools, and when it makes sense to delegate.</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Why a fast website stops being fast<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">A website is a living system: the CMS and plugins update themselves, the team uploads photos straight off the phone, marketing adds a tracking script “just for one campaign” that stays forever, the shared hosting fills up with neighbours. Each change is small; the sum is not. It’s the same reason a car gets serviced: not because it broke, but because it’s been used.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">And a second clock is ticking: Google’s. The metrics change — in 2024 INP replaced FID among the Core Web Vitals — and a site frozen at two-year-old standards slides backwards even if nobody touches a thing. The delivery-day score isn’t a diploma on the wall: it’s a photograph, and photographs age.</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">The four measures of serious website monitoring<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Four measures, in this order: first “does it exist?”, then “does it work for real people?”, then “does it sell?”, finally “can it be found?”. Monitoring that watches only the speed score is a dashboard with just the fuel light: useful, but it won’t tell you a wheel has come off.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<div class="sr-list-rows"><div><span class="sr-mono">a</span><span>Uptime: does the site respond? Sounds trivial, until you find out it was down on the very night of your campaign. You need an automatic check every few minutes, with an immediate alert.</span></div><div><span class="sr-mono">b</span><span>Core Web Vitals in the field: LCP under 2.5 seconds, INP under 200 milliseconds, CLS under 0.1 — measured on real users (CrUX data aggregated over 28 days), not just in the lab.</span></div><div><span class="sr-mono">c</span><span>Critical functions: forms, cart, bookings. The real damage isn’t “the site is slow” — it’s “the form hasn’t been sending for three weeks”.</span></div><div><span class="sr-mono">d</span><span>Visibility: the pages in the index, the errors flagged by Search Console, your positions on the searches that bring you customers.</span></div></div>
<!-- /wp:html -->
<!-- wp:html -->
<figure class="wp-block-image size-large" style="margin:36px 0 8px"><img src="/wp-content/themes/remarka-studio/assets/img/blog/monitoraggio-quattro-misure.svg" alt="The four measures of website monitoring: uptime, real-user Core Web Vitals, critical functions and visibility on Google" width="1200" height="500" loading="lazy" style="max-width:100%;height:auto;display:block;border:1px solid var(--sr-bordo)"/><figcaption class="sr-mono" style="margin-top:12px;font-size:12.5px;letter-spacing:0.04em;color:var(--sr-grigio);max-width:75ch">The four measures, in order: first “does it exist?” (uptime), then “does it work for real users?” (field Core Web Vitals, CrUX over 28 days), then “does it sell?” (forms and cart), finally “can it be found?” (index and rankings). Sources: web.dev and the CrUX documentation (Google).</figcaption></figure>
<!-- /wp:html -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Lab and real world: why the two numbers don’t match<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Lighthouse — the engine behind PageSpeed Insights — measures the site under controlled conditions: same simulated network, same device. It’s invaluable for diagnosing, but it’s still a lab. Field Core Web Vitals come instead from the Chrome UX Report: real users, real networks, real phones, aggregated over 28 days. The two numbers can diverge — the lab passing and the field failing, or the other way round — and when they diverge, the field is right: that’s where your customers are.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">The practical consequence: a one-off check tells you how the site is doing today, in the lab. Only a monthly series tells you whether it’s getting better or worse for the people who actually use it. It’s the difference between a photo and an electrocardiogram.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<p class="sr-card-link" style="margin-top:14px"><a href="/en/blog/core-web-vitals-2026/">Core Web Vitals in 2026: what Google actually measures →</a></p>
<!-- /wp:html -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">The monthly ritual, in twenty minutes<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:html -->
<div class="sr-list-rows"><div><span class="sr-mono">a</span><span>Run a full check-up and save the score next to last month’s: what counts is the direction, not the number of the day.</span></div><div><span class="sr-mono">b</span><span>Open Search Console: index coverage, new errors, the searches that bring clicks.</span></div><div><span class="sr-mono">c</span><span>Look at the month’s uptime report: how many minutes of downtime, and at what hours.</span></div><div><span class="sr-mono">d</span><span>Walk the path that brings you money by hand — form, quote request, cart — from a phone, not from your desk.</span></div><div><span class="sr-mono">e</span><span>Check that the latest backup exists and opens: a backup never tested is a hope, not a backup.</span></div></div>
<!-- /wp:html -->
<!-- wp:html -->
<p class="sr-card-link" style="margin-top:14px"><a href="/en/tools/full-site-checkup/">Full site check-up: 7 measures in one minute, free →</a></p>
<!-- /wp:html -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">When to delegate (and what to demand from whoever does it for you)<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">The twenty-minute ritual works — as long as someone actually does it. Experience says that after the third month the appointment slips, and the site goes back to wearing out unseen. Google’s reliability engineering formalised a principle that holds at small scale too: systems are kept safe by automatic checks and alerts, not by good intentions.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">That’s why monitoring is included in our projects with a maintenance plan: our platform keeps an eye on uptime, periodic checks and the real-user Core Web Vitals of the sites we look after, and when a value slips we see it — before you hear about it from customers. The report arrives every month, in human language. If you prefer DIY, the ritual above is yours: what matters is that someone is watching.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<p class="sr-card-link" style="margin-top:14px"><a href="https://lab.remarka.biz/showcase" target="_blank" rel="noopener">Our Monitor live — and try it on a site of yours, free →</a></p><p class="sr-card-link" style="margin-top:14px"><a href="/strumenti/#monitor">Free today, under watch tomorrow: monitoring for clients →</a></p><p class="sr-card-link" style="margin-top:14px"><a href="/en/services/redesign-migration/">Technical redesign: when the numbers say it’s time →</a></p>
<!-- /wp:html -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Sources<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:16px;line-height:1.7;max-width:75ch;margin-top:8px">The figures and claims in this article come from here. These are primary sources, not summaries: open them and check for yourself.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<ul style="list-style:none;padding:0;margin:20px 0 0;border-top:1px solid var(--sr-bordo)"><li style="margin-top:16px;line-height:1.55"><a href="https://web.dev/articles/vitals" target="_blank" rel="noopener">web.dev — Core Web Vitals (Google)</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">The official definitions and thresholds of LCP, INP and CLS cited in this article, including the switch from FID to INP in 2024.</span></li><li style="margin-top:16px;line-height:1.55"><a href="https://developer.chrome.com/docs/crux" target="_blank" rel="noopener">Chrome UX Report (CrUX) — documentation</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">The source of field data: real Chrome users, aggregated over a rolling 28-day window.</span></li><li style="margin-top:16px;line-height:1.55"><a href="https://sre.google/sre-book/monitoring-distributed-systems/" target="_blank" rel="noopener">Google SRE — Monitoring Distributed Systems</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">The Site Reliability Engineering book’s chapter on keeping systems safe: automatic checks and alerts, not good intentions.</span></li></ul>
<!-- /wp:html -->
<!-- wp:html -->
<p class="sr-card-link" style="margin-top:32px"><a href="/en/tools/full-site-checkup/">Run the full check-up of your website — free →</a></p>
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
