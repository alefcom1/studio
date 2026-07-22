<?php
/**
 * Title: Pagina — Articolo: Google Consent Mode v2: cosa cambia per annunci e analytics
 * Slug: remarka-studio/en-blog-consent-mode-v2-cosa-cambia
 * Categories: remarka-pagine
 * Description: Articolo blog: Google Consent Mode v2: cosa cambia per annunci e analytics
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1440px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:html -->
<p class="sr-mono" style="color:var(--sr-grigio);font-size:13px">22 JUL 2026</p>
<!-- /wp:html -->
<!-- wp:heading {"level":1,"style":{"typography":{"fontSize":"clamp(32px,4vw,48px)"}}} -->
<h1 class="wp-block-heading" style="font-size:clamp(32px,4vw,48px)">Google Consent Mode v2: what changes for ads and analytics</h1>
<!-- /wp:heading -->
<!-- wp:html -->
<figure class="wp-block-image size-large" style="margin:8px 0 8px"><img src="/wp-content/themes/remarka-studio/assets/img/blog/consent-cover.svg" alt="Consent Mode v2: what changes for ads and analytics with cookie consent" width="1200" height="630" loading="lazy" style="max-width:100%;height:auto;display:block;border:1px solid var(--sr-bordo)"/></figure>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1440px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:18px;line-height:1.75;max-width:75ch">If you advertise with Google or measure your site with Analytics, since 2024 a label has appeared that you can no longer ignore: Consent Mode v2. It isn’t yet another technical fad — it’s how Google has tied its tools to the cookie consent that every European site already has to request. Skip the setup and you see less effective campaigns and data thinning out, without understanding why. Let’s look at what Consent Mode v2 is, what really changes for ads and analytics, and how to set it up so it respects the visitor’s choice — rather than working around it.</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">What Consent Mode is (and why v2 arrived)<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Consent Mode is the bridge between your cookie banner and Google’s tags. In practice it tells the tags — Analytics, Google Ads — how to behave depending on what the visitor chose: whether they accepted measurement cookies, whether they refused advertising ones, and so on. It isn’t entirely new: it had existed for a few years already. Version 2 adds two new consent signals, dedicated to the advertising uses of data, and makes them mandatory.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">The reason is simple: since March 2024 Google requires Consent Mode v2 from anyone who wants to keep using European audience data for advertising — remarketing, audience lists, conversions. Without those two signals, some features switch off for users in the European Economic Area. Google did it to align with EU consent rules, not on a whim: it’s its answer to the fact that in Europe, before tracking anyone, valid consent has to be genuinely requested.</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">What really changes for ads and analytics<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">On the advertising side the change is sharp: if you don’t transmit the new signals, remarketing lists and audience segments built on European users stop being fed. The campaigns don’t stop, but they gradually lose the fuel that made them precise. Those who notice late end up with less targeted ads and a cost per lead that climbs, with no obvious cause.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">On the measurement side, instead, the nature of the data changes. When a visitor refuses, the tags don’t write cookies but can send Google anonymous, aggregated signals, from which the tools estimate — not record — part of what happened. Your reports change face: fewer identified users, more statistical modelling. It’s a deliberate trade-off, privacy first, and it has to be understood so you don’t read the numbers as if they were still the old ones.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<p class="sr-card-link" style="margin-top:14px"><a href="/en/tools/gdpr-check/">Check your site’s cookie and consent compliance for free →</a></p>
<!-- /wp:html -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Consent Mode v2 doesn’t replace the banner (or consent)<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">This is where most sites fall down. Consent Mode isn’t a cookie banner and isn’t a consent-collection platform: it’s the plumbing that reads the choice a serious banner collects. The real banner has to block the tags before consent and offer a refusal as easy as acceptance. On this the Italian Garante, in its cookie guidelines, and the European EDPB taskforce are explicit: pre-ticked boxes and “accept by scrolling” are not valid consent.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Order matters. First the banner blocks the scripts by default; then the visitor chooses; only then does Consent Mode transmit that choice to Google’s tags. If the banner is fake — that is, it loads everything anyway and asks permission after the fact — Consent Mode becomes a fig leaf, not proof of compliance. Google’s technology only works when it rests on consent collected properly.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<p class="sr-card-link" style="margin-top:14px"><a href="/en/services/technical-seo/">Technical SEO and clean tracking as standard on every page →</a></p><p class="sr-card-link" style="margin-top:14px"><a href="/en/blog/cookie-policy-vs-privacy-policy/">Read also: cookie policy or privacy policy, what serves whom →</a></p>
<!-- /wp:html -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">How to set it up without breaking anything<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">In practice you need three pieces working together. A consent management platform (a CMP) that collects the choice and is compatible with Consent Mode v2; the link between the CMP and Google’s tags, so the two new signals fire correctly; and an honest check that, before consent, no analytics or advertising cookie is written. That’s the right order, not a detail to postpone until launch.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Then you measure the result. Check that with consent denied the modelled data arrives and not zero, that the advertising signals activate only after acceptance, and above all that the banner really does block at the start. A cookie and GDPR compliance scan tells you in a few seconds whether the tags fire before consent — the most common and most expensive mistake.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<figure class="wp-block-image size-large" style="margin:36px 0 8px"><img src="/wp-content/themes/remarka-studio/assets/img/blog/consent-v2.svg" alt="How Consent Mode v2 works: from the cookie banner to the consent signals sent to Google" width="1200" height="480" loading="lazy" style="max-width:100%;height:auto;display:block;border:1px solid var(--sr-bordo)"/><figcaption class="sr-mono" style="margin-top:12px;font-size:12.5px;letter-spacing:0.04em;color:var(--sr-grigio);max-width:75ch">How Consent Mode v2 works: the banner blocks the tags by default (1), the visitor chooses (2), the CMP transmits the choice and the two new advertising signals to Google (3). With consent denied the tags don’t write cookies but send anonymous, aggregated signals. Consent Mode reads consent, it doesn’t collect it.</figcaption></figure>
<!-- /wp:html -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Consent first, measurement after<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">The whole point is an order: consent first, measurement after. Consent Mode v2 aligns Google’s tools with the consent you’re required to collect anyway. Set up well, it leaves you all the measurement the law allows without betraying your visitors. Set up badly, or skipped, it makes you lose two things at once — compliance and data — and you often notice only when campaigns pay off less and the reports empty out.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Our line is simple: we build sites where the banner blocks by default and measurement respects the visitor’s choice. Measuring is fine; measuring at the expense of trust is not. And the good news is that, done in the right order, compliance isn’t the enemy of data: it’s the condition for having it clean and defensible.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<p class="sr-card-link" style="margin-top:14px"><a href="/en/blog/google-analytics-4-gdpr-eu/">Read also: Google Analytics 4 and privacy in the EU, are you compliant? →</a></p>
<!-- /wp:html -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Sources<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:16px;line-height:1.7;max-width:75ch;margin-top:8px">The figures and claims in this article come from here. These are primary sources, not summaries: open them and check for yourself.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<ul style="list-style:none;padding:0;margin:20px 0 0;border-top:1px solid var(--sr-bordo)"><li style="margin-top:16px;line-height:1.55"><a href="https://developers.google.com/tag-platform/security/guides/consent" target="_blank" rel="noopener">Google — Consent Mode (developer guide)</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">The official documentation: what the consent signals do and how the tags behave before and after the choice.</span></li><li style="margin-top:16px;line-height:1.55"><a href="https://www.google.com/about/company/user-consent-policy/" target="_blank" rel="noopener">Google — EU user consent policy</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">The policy that requires anyone using Google’s tools in the EU to collect valid consent: the reason for Consent Mode v2.</span></li><li style="margin-top:16px;line-height:1.55"><a href="https://www.edpb.europa.eu/our-work-tools/our-documents/other/report-work-undertaken-cookie-banner-taskforce_en" target="_blank" rel="noopener">EDPB — cookie banner taskforce report</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">What is not valid consent according to Europe’s regulators: pre-ticked boxes and “accept by scrolling” aren’t enough.</span></li><li style="margin-top:16px;line-height:1.55"><a href="https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/9677876" target="_blank" rel="noopener">Garante Privacy — cookie guidelines</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">Italy’s rules on the banner: pre-emptive blocking of tags and a refusal as easy as acceptance.</span></li></ul>
<!-- /wp:html -->
<!-- wp:html -->
<p class="sr-card-link" style="margin-top:32px"><a href="/en/tools/gdpr-check/">Check your site’s consent and cookies for free →</a></p>
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
