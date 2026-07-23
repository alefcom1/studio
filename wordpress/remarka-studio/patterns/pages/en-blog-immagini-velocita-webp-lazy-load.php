<?php
/**
 * Title: Pagina — Articolo: Immagini e velocità: WebP, lazy-load e Core Web Vitals
 * Slug: remarka-studio/en-blog-immagini-velocita-webp-lazy-load
 * Categories: remarka-pagine
 * Description: Articolo blog: Immagini e velocità: WebP, lazy-load e Core Web Vitals
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1440px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:html -->
<p class="sr-mono" style="color:var(--sr-grigio);font-size:13px">23 JUL 2026</p>
<!-- /wp:html -->
<!-- wp:heading {"level":1,"style":{"typography":{"fontSize":"clamp(32px,4vw,48px)"}}} -->
<h1 class="wp-block-heading" style="font-size:clamp(32px,4vw,48px)">Images and speed: WebP, lazy-load and Core Web Vitals</h1>
<!-- /wp:heading -->
<!-- wp:html -->
<figure class="wp-block-image size-large" style="margin:8px 0 8px"><img src="/wp-content/themes/remarka-studio/assets/img/blog/immagini-velocita-cover.svg" alt="Optimizing website images: WebP, lazy-load and the right sizes for speed" width="1200" height="630" loading="lazy" style="max-width:100%;height:auto;display:block;border:1px solid var(--sr-bordo)"/></figure>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1440px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:18px;line-height:1.75;max-width:75ch">If your site is slow, chances are images carry most of the blame. On most pages they’re the heaviest content by far, much more than text or code: a single photo loaded at full resolution can weigh as much as dozens of written pages. The good news is that images are also the point where optimizing pays off the most and costs the least: the right format, lazy loading and correct sizing are enough to turn a slow page into a fast one. Let’s look at how to optimize a site’s images with WebP, lazy-load and an eye on Core Web Vitals.</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Why images weigh so much<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Open any page and, almost always, the heaviest thing to download is the images. State-of-the-web reports have confirmed this for years: they’re at the top of the ranking for bytes transferred, often more than everything else combined. The reason is simple — a detail-rich photo contains an enormous amount of information — but the consequences aren’t: every extra megabyte is waiting time, especially for someone browsing from a smartphone on a slow network.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">The trouble is that many images are heavier than they need to be, out of pure oversight. Photos uploaded at 4000 pixels wide and then shown in a 400-pixel box; old, bulky formats where a modern one would do; no compression. It’s dead weight: information the user will never see, but that their phone still has to download. Optimizing images means removing that unnecessary weight without any visible difference.</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">WebP (and AVIF): the right format<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">The first step is changing format. Old JPEGs and PNGs work, but they’re heavy: modern formats like WebP — and the more recent AVIF — offer the same visual quality while taking up much less space, often 25-35% less than an equivalent JPEG, sometimes a lot more. To the eye, nothing changes; for loading time, it’s a huge difference. Today WebP is supported by every major browser: there’s no longer a reason to ship needlessly large files.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">The nice part is that you don’t need to redo the photos: you convert the existing ones, ideally automatically on upload, serving the modern format to whoever supports it. It’s one of the interventions with the best ratio of effort to result: you touch the file, not the design, and the page instantly gets lighter. Well-tuned compression does the rest without denting the perceived sharpness.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<p class="sr-card-link" style="margin-top:14px"><a href="/en/tools/speed-test/">Measure your page weight and site speed for free →</a></p>
<!-- /wp:html -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Lazy-load: loading only what’s needed<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">The second move is not loading everything at once. When you open a long page, the images further down — the ones you’ll only see if you scroll, and only if you do — aren’t needed in the first instant. Lazy-load defers them: the browser downloads what’s visible first and loads the rest only as the user gets close to it. The result is a page that appears ready much sooner, because it doesn’t wait for images nobody is looking at yet.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Today lazy-load is almost free to turn on: just a standard attribute on the image, `loading="lazy"`, and browsers do the rest. Watch out for one thing: it shouldn’t go on the most important image at the top of the page, the one the user sees right away — deferring it would make perceived speed worse instead of better. Lazy-load is for what’s below the fold, not for the star of the page.</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">The right sizes and Core Web Vitals<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">The third pillar: serve every image at the size it will actually be shown at. There’s no point sending a 3000-pixel photo to a screen that will display 600. The techniques for this — responsive images that adapt resolution to the device — avoid downloading pixels nobody will see. And you should always specify the image’s width and height, so the browser reserves the space in advance and the page doesn’t “jump” while loading: that jump even has its own metric, the CLS in Core Web Vitals.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">This is where it comes full circle with the speed Google measures. The large image at the top is usually the element that decides your LCP — the metric measuring how long it takes for the main content to appear. Lightening it with WebP, giving it the right size and not lazy-loading it is often the single change that moves a page from orange to green. Images and Core Web Vitals are, to a large extent, the same problem.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<figure class="wp-block-image size-large" style="margin:36px 0 8px"><img src="/wp-content/themes/remarka-studio/assets/img/blog/immagini-velocita-schema.svg" alt="Optimizing images: WebP instead of JPEG, lazy-load below the fold, correct sizes for LCP and CLS" width="1200" height="500" loading="lazy" style="max-width:100%;height:auto;display:block;border:1px solid var(--sr-bordo)"/><figcaption class="sr-mono" style="margin-top:12px;font-size:12.5px;letter-spacing:0.04em;color:var(--sr-grigio);max-width:75ch">The three levers for optimizing a site’s images: the modern format (WebP or AVIF instead of JPEG/PNG, up to 25-35% less weight), lazy-load for what’s below the fold (never for the main image at the top), and the right sizes served to the device — with width and height declared so the page doesn’t “jump”. Together they improve LCP and CLS, two of the three Core Web Vitals.</figcaption></figure>
<!-- /wp:html -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Light, not heavy<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Optimizing images isn’t some technical whim: it’s the fastest, most concrete way to make a site fast, and therefore more welcome to visitors and to Google. Modern format, lazy loading, correct sizing: three interventions that don’t touch the design but change the experience, especially on mobile and slow networks — that is, for the majority of people visiting you today.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">In the sites we build, images are treated this way by default: converted to modern formats, served at the right size, with lazy-load where it’s needed. It isn’t an extra to sell separately, it’s the minimum for a page full of photos to stay light. A site that’s beautiful but heavy isn’t a good site: it’s a page visitors won’t wait to see load.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<p class="sr-card-link" style="margin-top:14px"><a href="/en/services/redesign-migration/">Redesign and migration: getting a slow site back into shape →</a></p><p class="sr-card-link" style="margin-top:14px"><a href="/en/blog/inp-core-web-vitals-metric/">Read also: INP, the new Core Web Vitals metric →</a></p>
<!-- /wp:html -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Sources<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:16px;line-height:1.7;max-width:75ch;margin-top:8px">The figures and claims in this article come from here. These are primary sources, not summaries: open them and check for yourself.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<ul style="list-style:none;padding:0;margin:20px 0 0;border-top:1px solid var(--sr-bordo)"><li style="margin-top:16px;line-height:1.55"><a href="https://web.dev/learn/images/" target="_blank" rel="noopener">web.dev — Learn Images (Google)</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">The official course on images for the web: formats, compression, responsive images. Practical and up to date.</span></li><li style="margin-top:16px;line-height:1.55"><a href="https://web.dev/articles/serve-images-webp" target="_blank" rel="noopener">web.dev — serving images in WebP</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">Why and how to use WebP: the same visual quality with files much lighter than old JPEGs and PNGs.</span></li><li style="margin-top:16px;line-height:1.55"><a href="https://developer.mozilla.org/en-US/docs/Web/Performance/Lazy_loading" target="_blank" rel="noopener">MDN — Lazy loading</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">The reference guide to lazy loading: how the loading="lazy" attribute works and when (not) to use it.</span></li><li style="margin-top:16px;line-height:1.55"><a href="https://web.dev/articles/lcp" target="_blank" rel="noopener">web.dev — Largest Contentful Paint (LCP)</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">The Core Web Vitals metric most tied to images: often it’s the photo at the top that decides your LCP.</span></li></ul>
<!-- /wp:html -->
<!-- wp:html -->
<p class="sr-card-link" style="margin-top:32px"><a href="/en/tools/speed-test/">Measure your site’s weight and speed for free →</a></p>
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
