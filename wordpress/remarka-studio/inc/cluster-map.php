<?php
/**
 * Mappa dei cluster tematici (pillar → articoli-satellite del blog).
 * Usata dallo shortcode [remarka_cluster slug="..."] per stampare in fondo alle
 * pagine-pillar (servizi, /prezzi/, home, strumenti) il blocco «Approfondimenti»
 * con i link agli articoli del cluster. Questa è la metà top-down della
 * perelinkovka (pillar → cluster); quella bottom-up (articolo → pillar) è già
 * nei singoli articoli in data.py.
 *
 * Ogni voce: slug dell'articolo (foglia uguale in IT/EN) + anchor breve IT/EN.
 * URL costruito a runtime: /blog/<slug>/ (IT), /en/blog/<slug>/ (EN).
 * Il blocco si stampa solo su IT ed EN (gli articoli batch 7–10 non hanno RU).
 *
 * @package remarka-studio
 */
defined( 'ABSPATH' ) || exit;

return array(
	// --- Home ---
	'home' => array(
		array( 'slug' => 'sito-web-in-3-settimane', 'it' => 'Sito web in 3 settimane', 'en' => 'A website in 3 weeks' ),
		array( 'slug' => 'quanto-costa-sito-aziendale-italia', 'it' => 'Quanto costa un sito aziendale', 'en' => 'What a business website costs' ),
		array( 'slug' => 'perche-il-sito-non-converte', 'it' => 'Perché il sito non converte', 'en' => 'Why your site doesn’t convert' ),
		array( 'slug' => 'check-up-sito-web-7-misure', 'it' => 'Check-up del sito: 7 misure', 'en' => 'Website check-up: 7 metrics' ),
		array( 'slug' => 'restyling-o-sito-nuovo-5-domande', 'it' => 'Restyling o sito nuovo?', 'en' => 'Redesign or new site?' ),
	),
	// --- Servizi ---
	'siti-aziendali' => array(
		array( 'slug' => 'cosa-include-sito-aziendale', 'it' => 'Cosa include un sito aziendale', 'en' => 'What a business website includes' ),
		array( 'slug' => 'sito-web-in-3-settimane', 'it' => 'Sito web in 3 settimane', 'en' => 'A website in 3 weeks' ),
		array( 'slug' => 'perche-il-sito-non-converte', 'it' => 'Perché il sito non converte', 'en' => 'Why your site doesn’t convert' ),
		array( 'slug' => 'hosting-sito-web-italia', 'it' => 'Hosting in Italia o cloud', 'en' => 'Hosting in Italy or cloud' ),
		array( 'slug' => 'manutenzione-wordpress', 'it' => 'Manutenzione WordPress', 'en' => 'WordPress maintenance' ),
		array( 'slug' => 'area-clienti-agenzia-web', 'it' => 'Area clienti: cosa pretendere', 'en' => 'Client area: what to expect' ),
	),
	'e-commerce' => array(
		array( 'slug' => 'piattaforma-ecommerce-quale-scegliere', 'it' => 'Quale piattaforma e-commerce', 'en' => 'Which e-commerce platform' ),
		array( 'slug' => 'ecommerce-checklist-prima-del-lancio', 'it' => 'Checklist prima del lancio', 'en' => 'Pre-launch checklist' ),
		array( 'slug' => 'quanto-costa-ecommerce-italia', 'it' => 'Quanto costa un e-commerce', 'en' => 'What an e-commerce costs' ),
		array( 'slug' => 'european-accessibility-act-ecommerce', 'it' => 'EAA 2026 per l’e-commerce', 'en' => 'EAA 2026 for e-commerce' ),
	),
	'siti-pwa' => array(
		array( 'slug' => 'pwa-per-pmi-quando-app-non-serve', 'it' => 'PWA: quando l’app non serve', 'en' => 'PWA: when you don’t need an app' ),
		array( 'slug' => 'core-web-vitals-2026', 'it' => 'Core Web Vitals nel 2026', 'en' => 'Core Web Vitals in 2026' ),
		array( 'slug' => 'sito-lento-cause-costi', 'it' => 'Sito lento: 7 cause', 'en' => 'Slow site: 7 causes' ),
	),
	'restyling-migrazione' => array(
		array( 'slug' => 'restyling-o-sito-nuovo-5-domande', 'it' => 'Restyling o sito nuovo?', 'en' => 'Redesign or new site?' ),
		array( 'slug' => 'migrare-wordpress-senza-perdere-seo', 'it' => 'Migrare senza perdere SEO', 'en' => 'Migrate without losing SEO' ),
		array( 'slug' => 'check-up-sito-web-7-misure', 'it' => 'Check-up del sito: 7 misure', 'en' => 'Website check-up: 7 metrics' ),
		array( 'slug' => 'impatto-ambientale-sito-web', 'it' => 'Impatto ambientale del sito', 'en' => 'A site’s environmental impact' ),
	),
	'seo-tecnica' => array(
		array( 'slug' => 'eeat-come-google-giudica-credibilita', 'it' => 'E-E-A-T: credibilità per Google', 'en' => 'E-E-A-T: credibility for Google' ),
		array( 'slug' => 'dati-strutturati-schema-org', 'it' => 'Dati strutturati Schema.org', 'en' => 'Schema.org structured data' ),
		array( 'slug' => 'migrare-wordpress-senza-perdere-seo', 'it' => 'Migrare senza perdere SEO', 'en' => 'Migrate without losing SEO' ),
		array( 'slug' => 'core-web-vitals-2026', 'it' => 'Core Web Vitals nel 2026', 'en' => 'Core Web Vitals in 2026' ),
		array( 'slug' => 'seo-locale-milano', 'it' => 'SEO locale a Milano', 'en' => 'Local SEO in Milan' ),
		array( 'slug' => 'farsi-trovare-da-chatgpt-geo', 'it' => 'Farsi trovare da ChatGPT (GEO)', 'en' => 'Get found by ChatGPT (GEO)' ),
		array( 'slug' => 'ai-overviews-google-restare-visibili', 'it' => 'AI Overviews di Google', 'en' => 'Google’s AI Overviews' ),
		array( 'slug' => 'autorevolezza-tematica-batte-keyword', 'it' => 'Autorevolezza tematica', 'en' => 'Topical authority' ),
		array( 'slug' => 'link-interni-seo-gratis', 'it' => 'Link interni: la SEO gratis', 'en' => 'Internal links: free SEO' ),
	),
	'siti-multilingue' => array(
		array( 'slug' => 'sito-quattro-lingue-costi-tempi', 'it' => 'Un sito in quattro lingue', 'en' => 'A site in four languages' ),
		array( 'slug' => 'hreflang-sito-multilingue', 'it' => 'Hreflang senza mal di testa', 'en' => 'Hreflang without headaches' ),
		array( 'slug' => 'sito-per-export', 'it' => 'Vendere all’estero online', 'en' => 'Selling abroad online' ),
		array( 'slug' => 'napoli-turismo-sito-multilingue', 'it' => 'Napoli: un sito che fa prenotare', 'en' => 'Naples: a site that gets bookings' ),
		array( 'slug' => 'traduzione-madrelingua-vs-ai', 'it' => 'Traduzione madrelingua o AI', 'en' => 'Native translation or AI' ),
	),
	'export-ready' => array(
		array( 'slug' => 'sito-per-export', 'it' => 'Vendere all’estero online', 'en' => 'Selling abroad online' ),
		array( 'slug' => 'sito-quattro-lingue-costi-tempi', 'it' => 'Un sito in quattro lingue', 'en' => 'A site in four languages' ),
		array( 'slug' => 'hreflang-sito-multilingue', 'it' => 'Hreflang senza mal di testa', 'en' => 'Hreflang without headaches' ),
		array( 'slug' => 'roi-localizzazione-sito', 'it' => 'ROI della localizzazione', 'en' => 'Localization ROI' ),
	),
	'web-app' => array(
		array( 'slug' => 'gestionale-su-misura-vs-excel', 'it' => 'Gestionale su misura vs Excel', 'en' => 'Custom software vs Excel' ),
		array( 'slug' => 'telegram-mini-app-business', 'it' => 'Telegram Mini App per il business', 'en' => 'Telegram Mini Apps for business' ),
		array( 'slug' => 'whatsapp-business-pmi', 'it' => 'WhatsApp Business per le PMI', 'en' => 'WhatsApp Business for SMBs' ),
		array( 'slug' => 'gamification-b2b', 'it' => 'Gamification nel B2B', 'en' => 'Gamification in B2B' ),
		array( 'slug' => 'area-clienti-agenzia-web', 'it' => 'Area clienti: cosa pretendere', 'en' => 'Client area: what to expect' ),
	),
	'adeguamento-eaa' => array(
		array( 'slug' => 'european-accessibility-act-ecommerce', 'it' => 'EAA 2026: cosa rischiate', 'en' => 'EAA 2026: what’s at stake' ),
		array( 'slug' => 'dichiarazione-di-accessibilita-guida-2026', 'it' => 'Dichiarazione di accessibilità', 'en' => 'Accessibility statement' ),
	),
	// --- Strumenti (Lab) ---
	'check-gdpr' => array(
		array( 'slug' => 'consent-mode-v2-cosa-cambia', 'it' => 'Google Consent Mode v2', 'en' => 'Google Consent Mode v2' ),
		array( 'slug' => 'google-analytics-4-privacy-ue', 'it' => 'GA4 e privacy in UE', 'en' => 'GA4 and privacy in the EU' ),
		array( 'slug' => 'cookie-policy-o-privacy-policy', 'it' => 'Cookie policy o privacy policy', 'en' => 'Cookie vs privacy policy' ),
		array( 'slug' => 'cookie-banner-checklist-garante-2026', 'it' => 'Cookie banner a norma 2026', 'en' => 'Compliant cookie banner 2026' ),
		array( 'slug' => 'alternative-google-analytics-privacy', 'it' => 'Alternative a Google Analytics', 'en' => 'Google Analytics alternatives' ),
		array( 'slug' => 'backup-e-sicurezza-sito-web', 'it' => 'Backup e sicurezza del sito', 'en' => 'Website backup and security' ),
	),
	'sito-pronto-ai' => array(
		array( 'slug' => 'llms-txt-cos-e', 'it' => 'llms.txt: cos’è', 'en' => 'llms.txt: what it is' ),
		array( 'slug' => 'farsi-trovare-da-chatgpt-geo', 'it' => 'Farsi trovare da ChatGPT (GEO)', 'en' => 'Get found by ChatGPT (GEO)' ),
	),
	'test-velocita' => array(
		array( 'slug' => 'sito-lento-cause-costi', 'it' => 'Sito lento: 7 cause', 'en' => 'Slow site: 7 causes' ),
		array( 'slug' => 'core-web-vitals-2026', 'it' => 'Core Web Vitals nel 2026', 'en' => 'Core Web Vitals in 2026' ),
		array( 'slug' => 'check-up-sito-web-7-misure', 'it' => 'Check-up del sito: 7 misure', 'en' => 'Website check-up: 7 metrics' ),
		array( 'slug' => 'hosting-sito-web-italia', 'it' => 'Hosting in Italia o cloud', 'en' => 'Hosting in Italy or cloud' ),
		array( 'slug' => 'impatto-ambientale-sito-web', 'it' => 'Impatto ambientale del sito', 'en' => 'A site’s environmental impact' ),
		array( 'slug' => 'inp-metrica-core-web-vitals', 'it' => 'INP: la nuova metrica', 'en' => 'INP: the new metric' ),
		array( 'slug' => 'immagini-velocita-webp-lazy-load', 'it' => 'Immagini e velocità', 'en' => 'Images and speed' ),
	),
	'verifica-accessibilita' => array(
		array( 'slug' => 'dichiarazione-di-accessibilita-guida-2026', 'it' => 'Dichiarazione di accessibilità', 'en' => 'Accessibility statement' ),
		array( 'slug' => 'european-accessibility-act-ecommerce', 'it' => 'EAA 2026 per l’e-commerce', 'en' => 'EAA 2026 for e-commerce' ),
	),
	'prezzi' => array(
		array( 'slug' => 'quanto-costa-sito-aziendale-italia', 'it' => 'Quanto costa un sito aziendale', 'en' => 'What a business website costs' ),
		array( 'slug' => 'quanto-costa-ecommerce-italia', 'it' => 'Quanto costa un e-commerce', 'en' => 'What an e-commerce costs' ),
		array( 'slug' => 'preventivo-sito-web-come-leggerlo', 'it' => 'Leggere un preventivo', 'en' => 'Reading a quote' ),
		array( 'slug' => 'sito-web-in-3-settimane', 'it' => 'Sito web in 3 settimane', 'en' => 'A website in 3 weeks' ),
	),
);
