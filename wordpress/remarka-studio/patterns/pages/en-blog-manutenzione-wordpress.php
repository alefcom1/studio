<?php
/**
 * Title: Pagina — Articolo: Manutenzione WordPress: cosa succede se non la fate
 * Slug: remarka-studio/en-blog-manutenzione-wordpress
 * Categories: remarka-pagine
 * Description: Articolo blog: Manutenzione WordPress: cosa succede se non la fate
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:html -->
<p class="sr-mono" style="color:var(--sr-grigio);font-size:13px">18 JUL 2026</p>
<!-- /wp:html -->
<!-- wp:heading {"level":1,"style":{"typography":{"fontSize":"clamp(32px,4vw,48px)"}}} -->
<h1 class="wp-block-heading" style="font-size:clamp(32px,4vw,48px)">WordPress maintenance: what happens if you skip it</h1>
<!-- /wp:heading -->
<!-- wp:html -->
<figure class="wp-block-image size-large" style="margin:8px 0 8px"><img src="/wp-content/themes/remarka-studio/assets/img/blog/manutenzione-cover.svg" alt="WordPress maintenance: backups, updates, testing and monitoring that keep a site secure and standing over time" width="1200" height="630" loading="lazy" style="max-width:100%;height:auto;display:block;border:1px solid var(--sr-bordo)"/></figure>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:18px;line-height:1.75;max-width:75ch">“The site works, why pay for maintenance?” It’s the question that saves you a hundred euros a year and loses you a thousand in one night. A WordPress site isn’t a painting on the wall: it’s living software, made of a core, of plugins and of a theme that the world around it — browsers, PHP, security standards — keeps changing. Not updating it doesn’t mean “leaving it as it is”: it means letting it age until one day it stops opening, or worse, until someone gets in. Let’s see what maintaining a WordPress site really involves, what those who skip it risk, and why it’s not a cost but insurance.</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Why a WordPress doesn’t “stay as it is”<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">WordPress runs a huge slice of the web, and that reach has a flip side: it’s also the favourite target of those hunting for exploitable holes. The core is well maintained and gets security updates constantly — often automatic — but the site isn’t just the core: it’s the core plus the plugins plus the theme. And that’s where the problem opens up. According to Patchstack’s annual WordPress security report, almost all discovered vulnerabilities are not in the core, but in third-party plugins and themes.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">The figure is stark: in 2024 almost eight thousand new vulnerabilities were found in the WordPress ecosystem, and around 96% concerned plugins. Every un-updated plugin is a door someone, sooner or later, tries to open. Not updating doesn’t freeze the site in a secure state: it leaves it exposed to holes that become public and exploitable as the months pass. “Staying as it is” is an illusion — what stays is only the risk, and it grows.</p>
<!-- /wp:paragraph -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">What maintenance involves (done right)<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">Maintenance doesn’t mean “clicking update at random.” It means an orderly cycle that keeps the site secure, fast and recoverable. It’s a few things, but they must be done methodically — the official WordPress.org documentation insists on every one of them.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<div class="sr-list-rows"><div><span class="sr-mono">a</span><span>Backup before every intervention: database and files, complete and verified. Without a working backup, an update gone wrong is a disaster; with one, it’s a ten-minute setback.</span></div><div><span class="sr-mono">b</span><span>Controlled updates: core, plugins and theme updated with judgment, tested first on a staging environment when the update is delicate — not blindly on the live site.</span></div><div><span class="sr-mono">c</span><span>Security and hardening: strong passwords, limited access, unused plugins removed (a deactivated but still-present plugin can still be exploited).</span></div><div><span class="sr-mono">d</span><span>Monitoring: uptime, speed and integrity checked over time, so a problem is spotted before a customer spots it.</span></div></div>
<!-- /wp:html -->
<!-- wp:html -->
<figure class="wp-block-image size-large" style="margin:36px 0 8px"><img src="/wp-content/themes/remarka-studio/assets/img/blog/manutenzione-ciclo.svg" alt="The maintenance cycle of a WordPress site: backup, controlled updates, testing, hardening and monitoring" width="1200" height="500" loading="lazy" style="max-width:100%;height:auto;display:block;border:1px solid var(--sr-bordo)"/><figcaption class="sr-mono" style="margin-top:12px;font-size:12.5px;letter-spacing:0.04em;color:var(--sr-grigio);max-width:75ch">The cycle of WordPress maintenance done right: full backup, controlled updates (core, plugins, theme), testing on a staging environment, hardening and continuous monitoring. 96% of vulnerabilities are in plugins: updating them methodically is the main defence. Sources: WordPress.org, Patchstack.</figcaption></figure>
<!-- /wp:html -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">What those who skip it risk<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">The risks aren’t textbook hypotheses, they’re the phone calls we get. The breached site that redirects to spam pages or serves malware — and Google flags it as “dangerous” to visitors, burning years of reputation in a day. The site that, after a server PHP update, simply stops opening, because a plugin frozen three years ago is no longer compatible. The white screen with no backup, the only copy “somewhere” that nobody can find.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">And then there’s the silent cost, the one that makes no noise: the contact form that stopped sending emails months ago and nobody noticed, customer enquiries fallen into the void. Maintenance isn’t the expense line it seems: it’s what keeps these disasters away, and it almost always costs a fraction of what fixing them afterwards costs. A periodic check-up is the cheapest way to know what state your site is really in, before a customer tells you.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<p class="sr-card-link" style="margin-top:14px"><a href="https://wordpress.org/documentation/article/updating-wordpress/" target="_blank" rel="noopener">WordPress.org — updating WordPress →</a></p><p class="sr-card-link" style="margin-top:14px"><a href="/en/tools/full-site-checkup/">Measure your site’s technical health for free →</a></p>
<!-- /wp:html -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Our approach: included, then optional<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">We know “maintenance” sounds like an imposed subscription, and we don’t like it either. That’s why, on the sites we deliver, the first 12 months of support, updates and measurements are included in the build price, no surprises. After that, the fee is optional — or the site stays with you as it is: code and data are yours from day one. No technical blackmail, no forced dependency.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px">And we don’t say it in the abstract: we keep 28 projects under continuous maintenance, and for two years we’ve been running an internal management system — the group’s TMS — that handles over 2,000 orders a year and can’t afford to be down for an hour. We do maintenance first of all on our own systems, with our own money and reputation on the line. It’s the same care, and the same engineering, we put into a business website for you.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<p class="sr-card-link" style="margin-top:14px"><a href="/en/services/business-websites/">A business website with maintenance included for the first 12 months →</a></p><p class="sr-card-link" style="margin-top:14px"><a href="/en/tools/full-site-checkup/">Run a check-up on your current site, for free →</a></p><p class="sr-card-link" style="margin-top:14px"><a href="/en/blog/website-hosting-italy-vs-cloud/">Read also: hosting in Italy or the cloud, speed and GDPR →</a></p>
<!-- /wp:html -->
<!-- wp:heading {"style":{"typography":{"fontSize":"clamp(24px,2.6vw,32px)"}}} -->
<h2 class="wp-block-heading" style="font-size:clamp(24px,2.6vw,32px)">Sources<span class="sr-accent-dot">.</span></h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"base"} -->
<p class="has-base-font-size" style="font-size:16px;line-height:1.7;max-width:75ch;margin-top:8px">The figures and claims in this article come from here. These are primary sources, not summaries: open them and check for yourself.</p>
<!-- /wp:paragraph -->
<!-- wp:html -->
<ul style="list-style:none;padding:0;margin:20px 0 0;border-top:1px solid var(--sr-bordo)"><li style="margin-top:16px;line-height:1.55"><a href="https://wordpress.org/documentation/article/updating-wordpress/" target="_blank" rel="noopener">WordPress.org — updating WordPress</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">The official documentation: why a backup before every update is the step you never skip.</span></li><li style="margin-top:16px;line-height:1.55"><a href="https://developer.wordpress.org/advanced-administration/security/hardening/" target="_blank" rel="noopener">WordPress.org — hardening (securing WordPress)</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">The official measures to reduce the attack surface: access, plugins, permissions.</span></li><li style="margin-top:16px;line-height:1.55"><a href="https://patchstack.com/whitepaper/state-of-wordpress-security-in-2024/" target="_blank" rel="noopener">Patchstack — State of WordPress Security 2024</a><span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">The annual report: almost 8,000 vulnerabilities in 2024, around 96% in plugins, very few in the core.</span></li></ul>
<!-- /wp:html -->
<!-- wp:html -->
<p class="sr-card-link" style="margin-top:32px"><a href="/en/services/business-websites/">A business website with 12 months of maintenance included, at a fixed price →</a></p>
<!-- /wp:html -->
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section sr-cta-band","layout":{"type":"constrained","contentSize":"1240px"}} -->
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
</section>
<!-- /wp:group -->
<!-- wp:group {"tagName":"section","className":"sr-section","layout":{"type":"constrained","contentSize":"1240px"}} -->
<section class="wp-block-group is-layout-constrained sr-section"><!-- wp:buttons {"style":{"spacing":{"blockGap":"14px"}},"layout":{"type":"flex","justifyContent":"center"}} -->
<div class="wp-block-buttons"><!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/en/blog/">← All articles</a></div>
<!-- /wp:button -->
</div>
<!-- /wp:buttons -->
</section>
<!-- /wp:group -->
