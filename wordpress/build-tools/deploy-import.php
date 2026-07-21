<?php
/**
 * Remarka Studio — importer: crea Home + tutte le pagine dai pattern,
 * costruisce il menu principale e imposta la homepage statica.
 *
 * Uso (dopo aver attivato il tema Remarka Studio):
 *   wp eval-file wp-content/themes/remarka-studio/../../../wordpress/build-tools/deploy-import.php --path=/percorso/a/wordpress
 * oppure, più semplice, copiare questo file dentro il tema e lanciarlo da lì:
 *   wp eval-file wp-content/themes/remarka-studio/deploy-import.php --path=/percorso/a/wordpress
 *
 * Sicurezza: lo script NON sovrascrive mai pagine già esistenti con lo
 * stesso slug — le salta e lo segnala. Rilanciabile senza rischio: alla
 * seconda esecuzione non fa nulla (tutto già esiste). Per rigenerare il
 * contenuto di una pagina, cancellarla manualmente prima di rilanciare,
 * oppure lanciare con REMARKA_FORCE=1 (aggiorna solo le pagine create da
 * questo script, riconosciute dal meta _remarka_generated — non tocca
 * pagine modificate a mano che non hanno quel meta o il cui contenuto è
 * stato salvato dall'editor dopo la generazione):
 *   REMARKA_FORCE=1 wp eval-file wp-content/themes/remarka-studio/deploy-import.php --path=/percorso/a/wordpress
 *
 * Deve girare via `wp eval-file`: usa funzioni WP (wp_insert_post,
 * wp_update_nav_menu_item, get_page_by_path, ecc.) non disponibili fuori
 * da un bootstrap WordPress completo.
 */

if ( ! defined( 'ABSPATH' ) ) {
	fwrite( STDERR, "Questo script va eseguito con `wp eval-file`, non con `php` diretto.\n" );
	exit( 1 );
}

// `wp eval-file <file> --force` fa fallire wp-cli ("unknown --force parameter"):
// il runner valida ogni token `--xxx` contro il synopsis del comando eval-file,
// che non dichiara --force, quindi lo rifiuta prima ancora di eseguire lo script.
// Una variabile d'ambiente bypassa completamente il parser di wp-cli.
$force = getenv( 'REMARKA_FORCE' ) === '1'
	|| in_array( '--force', $args ?? $GLOBALS['argv'] ?? array(), true );

$theme_dir    = get_stylesheet_directory();
$patterns_dir = $theme_dir . '/patterns';
$pages_dir    = $patterns_dir . '/pages';

if ( ! is_dir( $pages_dir ) ) {
	WP_CLI::error( "Cartella pattern non trovata: $pages_dir — il tema Remarka Studio è attivo?" );
}

/** Legge un file pattern e ne restituisce [title, content]. */
function remarka_deploy_read_pattern( string $file ): array {
	$data = get_file_data( $file, array(
		'title' => 'Title',
		'slug'  => 'Slug',
	) );
	ob_start();
	include $file;
	$content = ob_get_clean();
	return array( $data['title'], $content );
}

/**
 * Crea (o aggiorna, se --force e già gestita da noi) una pagina. Ritorna l'ID.
 * $path — percorso COMPLETO della pagina (es. 'servizi/e-commerce'): con gli
 * alberi linguistici gli slug si ripetono tra lingue (en/blog, ru/blog),
 * quindi il controllo di esistenza deve usare il percorso, non lo slug —
 * get_page_by_path() con il solo slug non trova le pagine annidate e i
 * rilanci creerebbero duplicati 'slug-2'.
 */
function remarka_deploy_upsert_page( string $path, string $title, string $content, int $parent_id = 0, bool $force = false ): int {
	$slug     = basename( $path );
	$existing = get_page_by_path( $path, OBJECT, 'page' );

	if ( $existing ) {
		$managed = get_post_meta( $existing->ID, '_remarka_generated', true );
		if ( ! $force || ! $managed ) {
			WP_CLI::log( "  = saltata (esiste già): /$path/" );
			return $existing->ID;
		}
		wp_update_post( array(
			'ID'           => $existing->ID,
			'post_title'   => $title,
			'post_content' => $content,
			'post_parent'  => $parent_id,
		) );
		WP_CLI::log( "  ↻ aggiornata: /$path/" );
		return $existing->ID;
	}

	$id = wp_insert_post( array(
		'post_type'    => 'page',
		'post_status'  => 'publish',
		'post_title'   => $title,
		'post_name'    => $slug,
		'post_content' => $content,
		'post_parent'  => $parent_id,
	), true );

	if ( is_wp_error( $id ) ) {
		WP_CLI::warning( "  ✗ errore creando /$path/: " . $id->get_error_message() );
		return 0;
	}

	update_post_meta( $id, '_remarka_generated', 'v1' );
	WP_CLI::log( "  + creata: /$path/ (ID $id)" );
	return $id;
}

WP_CLI::log( 'Studio Remarka — import contenuti' . ( $force ? ' (--force attivo)' : '' ) );
WP_CLI::log( '=================================' );

/* ---------- 1. Home: concatenazione delle 11 sezioni, in ordine ---------- */

WP_CLI::log( "\nHome:" );
$home_sections = array(
	'hero-home', 'checkup-home', 'trust-strip', 'tre-numeri', 'manifesto', 'lingue-mercati', 'servizi-cards', 'prezzi-teaser',
	'perche-remarka', 'caso-evidenza', 'recensioni', 'come-lavoriamo', 'area-clienti-blocco', 'garanzie-dark', 'strumenti-cards', 'faq', 'contatti',
);

/*
 * RU-воронка самодостаточна (фаза B): собственный набор и порядок секций
 * главной, не зеркалит IT/EN (niente lingue-mercati/strumenti-cards; al loro
 * posto vyhod-evropa e seo-lingue). Vedi piano-implementazione-fase-B.md §1 Б-1/Б-2.
 */
$home_sections_ru = array(
	'hero-home', 'checkup-home', 'trust-strip', 'vyhod-evropa', 'tre-numeri', 'manifesto', 'seo-lingue', 'servizi-cards',
	'prezzi-teaser', 'perche-remarka', 'caso-evidenza', 'recensioni', 'come-lavoriamo', 'area-clienti-blocco', 'garanzie-dark', 'faq', 'contatti',
);
$home_content = '';
foreach ( $home_sections as $slug ) {
	$file = "$patterns_dir/$slug.php";
	if ( ! file_exists( $file ) ) {
		WP_CLI::warning( "  sezione mancante: $slug.php" );
		continue;
	}
	list( , $content ) = remarka_deploy_read_pattern( $file );
	$home_content      .= $content . "\n";
}
$home_id = remarka_deploy_upsert_page( 'home', 'Home', $home_content, 0, $force );

update_option( 'show_on_front', 'page' );
update_option( 'page_on_front', $home_id );
WP_CLI::log( "  homepage statica impostata su ID $home_id" );

/* ---------- 1b. Home EN e RU: stesse sezioni dai pattern tradotti ----------
 * Le versioni linguistiche vivono come alberi di pagine annidate sotto
 * /en/ e /ru/ (vedi inc/multilang.php). La pagina 'en'/'ru' È la home
 * della lingua; le sezioni tradotte stanno in patterns/lang-{en,ru}. */

$lang_homes = array(
	'en' => array( 'dir' => 'lang-en', 'title' => 'Studio Remarka — Web development studio in Milan' ),
	'ru' => array( 'dir' => 'lang-ru', 'title' => 'Studio Remarka — Студия веб-разработки в Милане' ),
);
foreach ( $lang_homes as $lang_slug => $cfg ) {
	$lang_dir      = $patterns_dir . '/' . $cfg['dir'];
	$lang_content  = '';
	$lang_sections = ( 'ru' === $lang_slug ) ? $home_sections_ru : $home_sections;
	foreach ( $lang_sections as $slug ) {
		$file = "$lang_dir/$slug.php";
		if ( ! file_exists( $file ) ) {
			WP_CLI::warning( "  [$lang_slug] sezione mancante: $slug.php" );
			continue;
		}
		list( , $content ) = remarka_deploy_read_pattern( $file );
		$lang_content      .= $content . "\n";
	}
	$lid = remarka_deploy_upsert_page( $lang_slug, $cfg['title'], $lang_content, 0, $force );
	WP_CLI::log( "  home /$lang_slug/ pronta (ID $lid)" );
}

/* ---------- 2. Pagine dai pattern in /patterns/pages ---------- */

/**
 * slug_pattern => [slug pagina, slug genitore|null, titolo override|null]
 * Il titolo, se null, viene ricavato dal Title del pattern togliendo
 * il prefisso "Pagina — " usato nei commenti dei file generati.
 */
$page_map = array(
	'servizi-index'                       => array( 'servizi', null, 'Servizi' ),
	'servizio-siti-aziendali'              => array( 'siti-aziendali', 'servizi', null ),
	'servizio-e-commerce'                  => array( 'e-commerce', 'servizi', null ),
	'servizio-siti-pwa'                    => array( 'siti-pwa', 'servizi', null ),
	'servizio-restyling-migrazione'        => array( 'restyling-migrazione', 'servizi', null ),
	'servizio-seo-tecnica'                 => array( 'seo-tecnica', 'servizi', null ),
	'servizio-siti-multilingue'            => array( 'siti-multilingue', 'servizi', null ),
	'servizio-export-ready'                => array( 'export-ready', 'servizi', 'Export Ready' ),
	'servizio-web-app'                     => array( 'web-app', 'servizi', 'Web app su misura' ),
	'servizio-adeguamento-eaa'             => array( 'adeguamento-eaa', 'servizi', 'Adeguamento EAA' ),

	// Catalogo unico con schede-àncora (docs/copy-casi-studio.md §8.3). Le
	// vecchie voci caso-<slug> con clienti INVENTATI restano rimosse. Da
	// 21.07.2026 riapriamo pagine singole SOLO per i progetti REALI del
	// gruppo (repo verificabili, niente clienti finti): approfondimenti
	// tecnici con forte potenziale SEO. Prima: TMS (flagship, template).
	'casi-studio-index'                    => array( 'casi-studio', null, 'Casi studio' ),
	'caso-tms-perevod4'                    => array( 'tms-perevod4', 'casi-studio', 'TMS Perevod4' ),
	'caso-1russian'                        => array( '1russian', 'casi-studio', '1russian.com' ),
	'caso-att'                             => array( 'att', 'casi-studio', 'ATT · traduzione.tech' ),

	'prezzi'                               => array( 'prezzi', null, null ),

	'brief'                                => array( 'brief', null, 'Brief progetto' ),

	'strumenti-index'                      => array( 'strumenti', null, 'Strumenti' ),
	'strumento-check-up-completo'          => array( 'check-up-completo', 'strumenti', null ),
	'strumento-test-velocita'              => array( 'test-velocita', 'strumenti', null ),
	'strumento-check-gdpr'                 => array( 'check-gdpr', 'strumenti', null ),
	'strumento-analisi-seo'                => array( 'analisi-seo', 'strumenti', null ),
	'strumento-roi-localizzazione'         => array( 'roi-localizzazione', 'strumenti', null ),
	'strumento-verifica-accessibilita'     => array( 'verifica-accessibilita', 'strumenti', null ),
	'strumento-sito-pronto-ai'             => array( 'sito-pronto-ai', 'strumenti', null ),
	'strumento-impatto-co2'                => array( 'impatto-co2', 'strumenti', null ),
	'strumento-segnali-eeat'               => array( 'segnali-eeat', 'strumenti', null ),
	'strumento-sito-letto-dallai'          => array( 'sito-letto-dallai', 'strumenti', null ),
	'strumento-suona-madrelingua'          => array( 'suona-madrelingua', 'strumenti', null ),
	'strumento-generatore-llms-txt'        => array( 'generatore-llms-txt', 'strumenti', null ),

	'citta-roma'                           => array( 'roma', null, null ),
	'citta-torino'                         => array( 'torino', null, null ),
	'citta-milano'                         => array( 'milano', null, null ),
	'citta-monza'                          => array( 'monza', null, null ),
	'citta-bergamo'                        => array( 'bergamo', null, null ),
	'citta-brescia'                        => array( 'brescia', null, null ),
	'citta-como'                           => array( 'como', null, null ),
	'citta-bologna'                        => array( 'bologna', null, null ),
	'citta-verona'                         => array( 'verona', null, null ),
	'citta-padova'                         => array( 'padova', null, null ),
	'citta-venezia'                        => array( 'venezia', null, null ),
	'citta-genova'                         => array( 'genova', null, null ),
	'citta-firenze'                        => array( 'firenze', null, null ),
	'citta-napoli'                         => array( 'napoli', null, null ),
	'citta-bari'                           => array( 'bari', null, null ),
	'citta-palermo'                        => array( 'palermo', null, null ),
	'citta-catania'                        => array( 'catania', null, null ),

	'dove-lavoriamo'                       => array( 'dove-lavoriamo', null, 'Dove lavoriamo' ),
	'area-clienti'                         => array( 'area-clienti', null, 'Area clienti' ),
	'chi-siamo'                            => array( 'chi-siamo', null, null ),
	'privacy'                              => array( 'privacy', null, null ),
	'cookie-policy'                        => array( 'cookie-policy', null, null ),
	'cookie-preferenze'                    => array( 'cookie-preferenze', null, null ),

	'blog-index'                                => array( 'blog', null, 'Blog' ),
	'blog-sito-quattro-lingue-costi-tempi'      => array( 'sito-quattro-lingue-costi-tempi', 'blog', null ),
	'blog-cookie-banner-checklist-garante-2026' => array( 'cookie-banner-checklist-garante-2026', 'blog', null ),
	'blog-migrare-wordpress-senza-perdere-seo'  => array( 'migrare-wordpress-senza-perdere-seo', 'blog', null ),
	'blog-pwa-per-pmi-quando-app-non-serve'     => array( 'pwa-per-pmi-quando-app-non-serve', 'blog', null ),
	'blog-quanto-costa-sito-aziendale-italia'   => array( 'quanto-costa-sito-aziendale-italia', 'blog', null ),
	'blog-core-web-vitals-2026'                 => array( 'core-web-vitals-2026', 'blog', null ),
	'blog-quanto-costa-ecommerce-italia'        => array( 'quanto-costa-ecommerce-italia', 'blog', null ),
	'blog-sito-lento-cause-costi'               => array( 'sito-lento-cause-costi', 'blog', null ),
	'blog-european-accessibility-act-ecommerce' => array( 'european-accessibility-act-ecommerce', 'blog', null ),
	'blog-llms-txt-cos-e'                       => array( 'llms-txt-cos-e', 'blog', null ),
	'blog-farsi-trovare-da-chatgpt-geo'         => array( 'farsi-trovare-da-chatgpt-geo', 'blog', null ),
	'blog-check-up-sito-web-7-misure'           => array( 'check-up-sito-web-7-misure', 'blog', null ),
	'blog-eeat-come-google-giudica-credibilita' => array( 'eeat-come-google-giudica-credibilita', 'blog', null ),
	'blog-preventivo-sito-web-come-leggerlo'    => array( 'preventivo-sito-web-come-leggerlo', 'blog', null ),
	'blog-sito-web-in-3-settimane'              => array( 'sito-web-in-3-settimane', 'blog', null ),
	'blog-restyling-o-sito-nuovo-5-domande'     => array( 'restyling-o-sito-nuovo-5-domande', 'blog', null ),
	'blog-impatto-ambientale-sito-web'          => array( 'impatto-ambientale-sito-web', 'blog', null ),
	'blog-dichiarazione-di-accessibilita-guida-2026' => array( 'dichiarazione-di-accessibilita-guida-2026', 'blog', null ),
	'blog-telegram-mini-app-business'           => array( 'telegram-mini-app-business', 'blog', null ),
	'blog-gestionale-su-misura-vs-excel'        => array( 'gestionale-su-misura-vs-excel', 'blog', null ),
	'blog-dati-strutturati-schema-org'          => array( 'dati-strutturati-schema-org', 'blog', null ),
	'blog-gamification-b2b'                      => array( 'gamification-b2b', 'blog', null ),
	'blog-hosting-sito-web-italia'              => array( 'hosting-sito-web-italia', 'blog', null ),
	'blog-seo-locale-milano'                    => array( 'seo-locale-milano', 'blog', null ),
	'blog-google-business-profile-guida'        => array( 'google-business-profile-guida', 'blog', null ),
	'blog-hreflang-sito-multilingue'            => array( 'hreflang-sito-multilingue', 'blog', null ),
	'blog-sito-per-export'                      => array( 'sito-per-export', 'blog', null ),
	'blog-manutenzione-wordpress'               => array( 'manutenzione-wordpress', 'blog', null ),
	'blog-area-clienti-agenzia-web'             => array( 'area-clienti-agenzia-web', 'blog', null ),
	'blog-monitoraggio-sito-dopo-lancio'        => array( 'monitoraggio-sito-dopo-lancio', 'blog', null ),
	'blog-perche-il-sito-non-converte'          => array( 'perche-il-sito-non-converte', 'blog', null ),
	'blog-landing-page-che-converte'            => array( 'landing-page-che-converte', 'blog', null ),
	'blog-recensioni-riprova-sociale-onesta'    => array( 'recensioni-riprova-sociale-onesta', 'blog', null ),
	'blog-whatsapp-business-pmi'                => array( 'whatsapp-business-pmi', 'blog', null ),
	'blog-copywriting-sito-web-prima-del-design' => array( 'copywriting-sito-web-prima-del-design', 'blog', null ),

	// ---- Albero EN (genitore = percorso completo) ----
	'en-servizi-index'                             => array( 'services', 'en', 'Services' ),
	'en-casi-studio-index'                         => array( 'case-studies', 'en', 'Case studies' ),
	'en-caso-tms-perevod4'                         => array( 'tms-perevod4', 'en/case-studies', 'TMS Perevod4' ),
	'en-caso-1russian'                             => array( '1russian', 'en/case-studies', '1russian.com' ),
	'en-caso-att'                                  => array( 'att', 'en/case-studies', 'ATT · traduzione.tech' ),
	'en-strumenti-index'                           => array( 'tools', 'en', 'Tools' ),
	'en-blog-index'                                => array( 'blog', 'en', 'Blog' ),
	'en-servizio-siti-aziendali'                   => array( 'business-websites', 'en/services', null ),
	'en-servizio-e-commerce'                       => array( 'e-commerce', 'en/services', null ),
	'en-servizio-siti-pwa'                         => array( 'progressive-web-apps', 'en/services', null ),
	'en-servizio-restyling-migrazione'             => array( 'redesign-migration', 'en/services', null ),
	'en-servizio-seo-tecnica'                      => array( 'technical-seo', 'en/services', null ),
	'en-servizio-siti-multilingue'                 => array( 'multilingual-websites', 'en/services', null ),
	'en-servizio-export-ready'                     => array( 'export-ready', 'en/services', null ),
	'en-servizio-web-app'                          => array( 'custom-web-apps', 'en/services', null ),
	'en-servizio-adeguamento-eaa'                  => array( 'eaa-compliance', 'en/services', 'EAA compliance' ),
	'en-strumento-check-up-completo'               => array( 'full-site-checkup', 'en/tools', 'Full site check-up' ),
	'en-strumento-test-velocita'                   => array( 'speed-test', 'en/tools', 'Speed test' ),
	'en-strumento-check-gdpr'                      => array( 'gdpr-check', 'en/tools', 'GDPR & cookie check' ),
	'en-strumento-analisi-seo'                     => array( 'seo-audit', 'en/tools', 'SEO audit' ),
	'en-strumento-roi-localizzazione'              => array( 'localization-roi', 'en/tools', 'Localization ROI' ),
	'en-strumento-verifica-accessibilita'          => array( 'accessibility-check', 'en/tools', 'Accessibility check' ),
	'en-strumento-sito-pronto-ai'                  => array( 'ai-readiness', 'en/tools', 'AI readiness check' ),
	'en-strumento-impatto-co2'                     => array( 'website-carbon', 'en/tools', 'CO₂ impact' ),
	'en-strumento-segnali-eeat'                    => array( 'eeat-signals', 'en/tools', 'E-E-A-T signals' ),
	'en-strumento-sito-letto-dallai'               => array( 'read-by-ai', 'en/tools', 'Your website, read by AI' ),
	'en-strumento-suona-madrelingua'               => array( 'does-it-sound-native', 'en/tools', 'Does it sound native?' ),
	'en-strumento-generatore-llms-txt'             => array( 'llms-txt-generator', 'en/tools', 'llms.txt generator' ),
	'en-blog-sito-quattro-lingue-costi-tempi'      => array( 'website-four-languages-costs', 'en/blog', null ),
	'en-blog-cookie-banner-checklist-garante-2026' => array( 'cookie-banner-compliance-italy-2026', 'en/blog', null ),
	'en-blog-migrare-wordpress-senza-perdere-seo'  => array( 'migrate-wordpress-without-losing-seo', 'en/blog', null ),
	'en-blog-pwa-per-pmi-quando-app-non-serve'     => array( 'pwa-for-smbs', 'en/blog', null ),
	'en-blog-quanto-costa-sito-aziendale-italia'   => array( 'business-website-cost-italy', 'en/blog', null ),
	'en-blog-core-web-vitals-2026'                 => array( 'core-web-vitals-2026', 'en/blog', null ),
	'en-blog-quanto-costa-ecommerce-italia'        => array( 'ecommerce-cost-italy-2026', 'en/blog', null ),
	'en-blog-sito-lento-cause-costi'               => array( 'slow-website-causes-fixes', 'en/blog', null ),
	'en-blog-european-accessibility-act-ecommerce' => array( 'eaa-ecommerce-risks', 'en/blog', null ),
	'en-blog-llms-txt-cos-e'                       => array( 'llms-txt-explained', 'en/blog', null ),
	'en-blog-farsi-trovare-da-chatgpt-geo'         => array( 'get-cited-by-chatgpt-geo', 'en/blog', null ),
	'en-blog-check-up-sito-web-7-misure'           => array( 'website-checkup-7-metrics', 'en/blog', null ),
	'en-blog-eeat-come-google-giudica-credibilita' => array( 'eeat-how-google-judges-credibility', 'en/blog', null ),
	'en-blog-preventivo-sito-web-come-leggerlo'    => array( 'website-quote-how-to-read-it', 'en/blog', null ),
	'en-blog-sito-web-in-3-settimane'              => array( 'website-in-3-weeks', 'en/blog', null ),
	'en-blog-restyling-o-sito-nuovo-5-domande'     => array( 'redesign-or-new-website-5-questions', 'en/blog', null ),
	'en-blog-impatto-ambientale-sito-web'          => array( 'website-environmental-impact', 'en/blog', null ),
	'en-blog-dichiarazione-di-accessibilita-guida-2026' => array( 'accessibility-statement-guide-2026', 'en/blog', null ),
	'en-blog-telegram-mini-app-business'           => array( 'telegram-mini-app-for-business', 'en/blog', null ),
	'en-blog-gestionale-su-misura-vs-excel'        => array( 'custom-management-software-vs-excel', 'en/blog', null ),
	'en-blog-dati-strutturati-schema-org'          => array( 'schema-org-structured-data-for-smes', 'en/blog', null ),
	'en-blog-gamification-b2b'                      => array( 'gamification-in-b2b', 'en/blog', null ),
	'en-blog-hosting-sito-web-italia'              => array( 'website-hosting-italy-vs-cloud', 'en/blog', null ),
	'en-blog-seo-locale-milano'                    => array( 'local-seo-milan', 'en/blog', null ),
	'en-blog-google-business-profile-guida'        => array( 'google-business-profile-guide', 'en/blog', null ),
	'en-blog-hreflang-sito-multilingue'            => array( 'hreflang-multilingual-website', 'en/blog', null ),
	'en-blog-sito-per-export'                      => array( 'website-for-export', 'en/blog', null ),
	'en-blog-manutenzione-wordpress'               => array( 'wordpress-maintenance', 'en/blog', null ),
	'en-blog-area-clienti-agenzia-web'             => array( 'web-agency-client-portal', 'en/blog', null ),
	'en-blog-monitoraggio-sito-dopo-lancio'        => array( 'website-monitoring-after-launch', 'en/blog', null ),
	'en-blog-perche-il-sito-non-converte'          => array( 'why-your-website-doesnt-convert', 'en/blog', null ),
	'en-blog-landing-page-che-converte'            => array( 'landing-page-that-converts', 'en/blog', null ),
	'en-blog-recensioni-riprova-sociale-onesta'    => array( 'reviews-social-proof-done-right', 'en/blog', null ),
	'en-blog-whatsapp-business-pmi'                => array( 'whatsapp-business-for-smes', 'en/blog', null ),
	'en-blog-copywriting-sito-web-prima-del-design' => array( 'website-copywriting-before-design', 'en/blog', null ),
	'en-prezzi'                                    => array( 'pricing', 'en', null ),
	'en-brief'                                     => array( 'brief', 'en', 'Brief' ),
	'en-citta-milano'                              => array( 'milan', 'en', null ),
	'en-area-clienti'                              => array( 'client-area', 'en', 'Client area' ),
	'en-chi-siamo'                                 => array( 'about', 'en', null ),
	'en-privacy'                                   => array( 'privacy', 'en', null ),
	'en-cookie-policy'                             => array( 'cookie-policy', 'en', null ),
	'en-cookie-preferenze'                         => array( 'cookie-preferences', 'en', null ),

	// ---- Albero RU (genitore = percorso completo) ----
	'ru-servizi-index'                             => array( 'uslugi', 'ru', 'Услуги' ),
	'ru-casi-studio-index'                         => array( 'kejsy', 'ru', 'Кейсы' ),
	'ru-caso-tms-perevod4'                         => array( 'tms-perevod4', 'ru/kejsy', 'TMS Perevod4' ),
	'ru-caso-1russian'                             => array( '1russian', 'ru/kejsy', '1russian.com' ),
	'ru-caso-att'                                  => array( 'att', 'ru/kejsy', 'ATT · traduzione.tech' ),
	'ru-strumenti-index'                           => array( 'instrumenty', 'ru', 'Инструменты' ),
	'ru-blog-index'                                => array( 'blog', 'ru', 'Блог' ),
	'ru-servizio-siti-aziendali'                   => array( 'korporativnye-sajty', 'ru/uslugi', null ),
	'ru-servizio-e-commerce'                       => array( 'internet-magaziny', 'ru/uslugi', null ),
	'ru-servizio-siti-pwa'                         => array( 'pwa-sajty', 'ru/uslugi', null ),
	'ru-servizio-restyling-migrazione'             => array( 'redizajn-i-migracija', 'ru/uslugi', null ),
	'ru-servizio-seo-tecnica'                      => array( 'tehnicheskoe-seo', 'ru/uslugi', null ),
	'ru-servizio-siti-multilingue'                 => array( 'mnogojazychnye-sajty', 'ru/uslugi', null ),
	'ru-servizio-export-ready'                     => array( 'export-ready', 'ru/uslugi', null ),
	'ru-servizio-web-app'                          => array( 'veb-prilozhenija', 'ru/uslugi', null ),
	'ru-servizio-adeguamento-eaa'                  => array( 'dostupnost-eaa', 'ru/uslugi', 'Доступность и EAA' ),
	'ru-sajt-dlya-evropy'                          => array( 'sajt-dlya-evropy', 'ru/uslugi', 'Сайт для выхода на рынок Италии и Европы' ),
	'ru-seo-prodvizhenie'                          => array( 'seo-prodvizhenie', 'ru/uslugi', 'SEO-продвижение в Италии и Европе' ),
	'ru-strumento-check-up-completo'               => array( 'polnaya-proverka-sajta', 'ru/instrumenty', 'Полная проверка сайта' ),
	'ru-strumento-test-velocita'                   => array( 'test-skorosti', 'ru/instrumenty', 'Тест скорости' ),
	'ru-strumento-check-gdpr'                      => array( 'proverka-gdpr', 'ru/instrumenty', 'Проверка GDPR и cookie' ),
	'ru-strumento-analisi-seo'                     => array( 'seo-audit', 'ru/instrumenty', 'SEO-аудит' ),
	'ru-strumento-roi-localizzazione'              => array( 'roi-lokalizacii', 'ru/instrumenty', 'ROI локализации' ),
	'ru-strumento-verifica-accessibilita'          => array( 'proverka-dostupnosti', 'ru/instrumenty', 'Проверка доступности' ),
	'ru-strumento-sito-pronto-ai'                  => array( 'gotovnost-k-ii', 'ru/instrumenty', 'Готовность к ИИ' ),
	'ru-strumento-impatto-co2'                     => array( 'uglerodnyj-sled', 'ru/instrumenty', 'Углеродный след' ),
	'ru-strumento-segnali-eeat'                    => array( 'signaly-eeat', 'ru/instrumenty', 'Сигналы E-E-A-T' ),
	'ru-strumento-sito-letto-dallai'               => array( 'sajt-glazami-ii', 'ru/instrumenty', 'Ваш сайт глазами ИИ' ),
	'ru-strumento-suona-madrelingua'               => array( 'zvuchit-kak-u-nositelya', 'ru/instrumenty', 'Звучит как у носителя?' ),
	'ru-strumento-generatore-llms-txt'             => array( 'generator-llms-txt', 'ru/instrumenty', 'Генератор llms.txt' ),
	'ru-blog-sito-quattro-lingue-costi-tempi'      => array( 'sajt-na-4-jazykah', 'ru/blog', null ),
	'ru-blog-cookie-banner-checklist-garante-2026' => array( 'cookie-banner-trebovanija-2026', 'ru/blog', null ),
	'ru-blog-migrare-wordpress-senza-perdere-seo'  => array( 'migracija-wordpress-bez-poteri-seo', 'ru/blog', null ),
	'ru-blog-pwa-per-pmi-quando-app-non-serve'     => array( 'pwa-dlja-biznesa', 'ru/blog', null ),
	'ru-blog-quanto-costa-sito-aziendale-italia'   => array( 'skolko-stoit-sajt-v-italii', 'ru/blog', null ),
	'ru-blog-core-web-vitals-2026'                 => array( 'core-web-vitals-2026', 'ru/blog', null ),
	'ru-blog-quanto-costa-ecommerce-italia'        => array( 'skolko-stoit-internet-magazin', 'ru/blog', null ),
	'ru-blog-sito-lento-cause-costi'               => array( 'medlennyj-sajt-prichiny', 'ru/blog', null ),
	// Blog · Batch 5 — RU-only (scritti a mano, senza specchio IT/EN). Slug RU
	// finale = slug-foglia; genitore ru/blog (indice già presente sopra).
	'ru-blog-sajt-dlya-vyhoda-na-rynok-italii'     => array( 'sajt-dlya-vyhoda-na-rynok-italii', 'ru/blog', null ),
	'ru-blog-seo-v-italii-po-russki'               => array( 'seo-v-italii-po-russki', 'ru/blog', null ),
	'ru-blog-gdpr-dlya-russkoyazychnogo-biznesa-v-es' => array( 'gdpr-dlya-russkoyazychnogo-biznesa-v-es', 'ru/blog', null ),
	'ru-blog-perevesti-ili-lokalizovat-sajt'       => array( 'perevesti-ili-lokalizovat-sajt', 'ru/blog', null ),
	'ru-blog-cena-sajta-v-italii'                  => array( 'cena-sajta-v-italii', 'ru/blog', null ),
	// Blog · Batch 6 — RU-only (scritti a mano, senza specchio IT/EN).
	'ru-blog-telegram-prilozhenie-dlya-biznesa-v-evrope' => array( 'telegram-prilozhenie-dlya-biznesa-v-evrope', 'ru/blog', null ),
	'ru-blog-kak-proverit-veb-studiyu'             => array( 'kak-proverit-veb-studiyu', 'ru/blog', null ),
	'ru-blog-zakon-o-dostupnosti-sajtov'           => array( 'zakon-o-dostupnosti-sajtov', 'ru/blog', null ),
	'ru-blog-sajt-v-chatgpt'                       => array( 'sajt-v-chatgpt', 'ru/blog', null ),
	'ru-blog-russkoyazychnaya-auditoriya-v-evrope' => array( 'russkoyazychnaya-auditoriya-v-evrope', 'ru/blog', null ),
	'ru-prezzi'                                    => array( 'ceny', 'ru', null ),
	'ru-brief'                                     => array( 'brif', 'ru', 'Бриф' ),
	'ru-citta-milano'                              => array( 'milan', 'ru', null ),
	'ru-area-clienti'                              => array( 'kabinet-klienta', 'ru', 'Кабинет клиента' ),
	'ru-chi-siamo'                                 => array( 'o-studii', 'ru', null ),
	'ru-privacy'                                   => array( 'privacy', 'ru', null ),
	'ru-cookie-policy'                             => array( 'cookie-policy', 'ru', null ),
	'ru-cookie-preferenze'                         => array( 'cookie-preferences', 'ru', null ),
);

// Le pagine "genitore" (parent=null ma referenziate come parent altrove)
// vanno create per prime: separiamo in due passate.
$parent_keys = array(
	'servizi-index', 'casi-studio-index', 'strumenti-index', 'blog-index',
	'en-servizi-index', 'en-casi-studio-index', 'en-strumenti-index', 'en-blog-index',
	'ru-servizi-index', 'ru-casi-studio-index', 'ru-strumenti-index', 'ru-blog-index',
);
$ordered     = array_merge(
	$parent_keys,
	array_diff( array_keys( $page_map ), $parent_keys )
);

WP_CLI::log( "\nPagine:" );
$created_ids = array();
foreach ( $ordered as $pattern_slug ) {
	$file = "$pages_dir/$pattern_slug.php";
	if ( ! file_exists( $file ) ) {
		WP_CLI::warning( "  pattern mancante: $pattern_slug.php" );
		continue;
	}
	list( $page_slug, $parent_path, $title_override ) = $page_map[ $pattern_slug ];
	list( $pattern_title, $content ) = remarka_deploy_read_pattern( $file );

	$title = $title_override ?: preg_replace( '/^Pagina — (Servizio: |Caso: |Città: |Articolo: |Strumento: )?/u', '', $pattern_title );
	// $parent_path è il PERCORSO completo del genitore ('servizi',
	// 'en/services', ...). Risoluzione: prima le pagine create in questo
	// stesso run, poi il database (per i genitori 'en'/'ru' creati al §1b).
	$parent_id = 0;
	if ( $parent_path ) {
		$parent_id = $created_ids[ $parent_path ]
			?? ( ( $p = get_page_by_path( $parent_path, OBJECT, 'page' ) ) ? $p->ID : 0 );
		if ( ! $parent_id ) {
			WP_CLI::warning( "  genitore non trovato: $parent_path (per $page_slug)" );
		}
	}

	$full_path = $parent_path ? "$parent_path/$page_slug" : $page_slug;
	$id        = remarka_deploy_upsert_page( $full_path, $title, $content, $parent_id, $force );
	$created_ids[ $full_path ] = $id;

	// Commenti nativi WP SOLO sugli articoli del blog (decisione owner
	// 19.07.2026, raccolta feedback): tutte le altre pagine restano chiuse.
	$is_blog_article = ( 0 === strpos( $pattern_slug, 'blog-' ) || 0 === strpos( $pattern_slug, 'en-blog-' ) || 0 === strpos( $pattern_slug, 'ru-blog-' ) )
		&& false === strpos( $pattern_slug, 'blog-index' );
	if ( $id && $is_blog_article ) {
		wp_update_post( array( 'ID' => $id, 'comment_status' => 'open' ) );
	}
}

/* Impostazioni discussione (idempotenti): OGNI commento passa dalla
 * moderazione prima di apparire; niente registrazione obbligatoria;
 * opt-in esplicito per i cookie del form (GDPR). */
update_option( 'comment_moderation', 1 );
update_option( 'comment_previously_approved', 0 );
update_option( 'require_name_email', 1 );
update_option( 'comment_registration', 0 );
update_option( 'show_comments_cookies_opt_in', 1 );
update_option( 'close_comments_for_old_posts', 0 );
WP_CLI::log( '  commenti: aperti sugli articoli del blog, moderazione totale attiva' );

/* ---------- 2b. Pulizia pagine orfane ----------
 * Se un caso/articolo viene rinominato o rimosso da data.py (successo con
 * i quattro casi studio con clienti inventati, sostituiti dal catalogo
 * unico di progetti reali — docs/copy-casi-studio.md), la vecchia pagina
 * resta nel database con lo slug precedente — non viene toccata perché non
 * compare più in $page_map. Qui cerchiamo tutte le pagine con il meta
 * _remarka_generated il cui slug non è (più) nella mappa corrente e le
 * spostiamo nel cestino, solo con --force (stessa cautela dell'update). */
// 'home', 'en', 'ru' sono create al §1/§1b con percorso proprio e non
// figurano mai in $page_map: senza questa protezione ogni run con --force
// le classifica come "orfane" e le cestina (bug osservato: homepage sparita
// dopo il deploy multilingua).
$current_slugs = array_merge( wp_list_pluck( $page_map, 0 ), array( 'home', 'en', 'ru' ) );
$orphans       = get_posts( array(
	'post_type'   => 'page',
	'post_status' => 'any',
	'numberposts' => -1,
	'meta_key'    => '_remarka_generated',
) );
$orphans = array_filter( $orphans, function ( $p ) use ( $current_slugs ) {
	return ! in_array( $p->post_name, $current_slugs, true );
} );
if ( $orphans ) {
	WP_CLI::log( "\nPagine orfane (slug non più in uso):" );
	foreach ( $orphans as $p ) {
		if ( $force ) {
			wp_trash_post( $p->ID );
			WP_CLI::log( "  ✗ /{$p->post_name}/ spostata nel cestino (ID {$p->ID})" );
		} else {
			WP_CLI::warning( "  /{$p->post_name}/ non più referenziata — rilanciare con REMARKA_FORCE=1 per spostarla nel cestino" );
		}
	}
}

/* ---------- 3. Menu principale ---------- */

WP_CLI::log( "\nMenu:" );
$menu_name = 'Menu principale — Remarka';
$menu      = wp_get_nav_menu_object( $menu_name );
if ( ! $menu ) {
	$menu_id = wp_create_nav_menu( $menu_name );
	WP_CLI::log( "  + menu creato: $menu_name (ID $menu_id)" );
} else {
	$menu_id = $menu->term_id;
	WP_CLI::log( "  = menu già esistente: $menu_name (ID $menu_id)" );
	// НЕ стираем существующие пункты даже с --force: владелец добавляет в
	// главное меню подпункты (выпадающие) руками в админке, и wipe при каждом
	// «Полном цикле» их уничтожал (инцидент 20.07.2026 — «пропало выпадающее
	// меню»). Дубликаты и так исключены проверкой по title ниже; канонические
	// пункты только ДОБАВЛЯЮТСЯ, если их нет.
}

$menu_items = array(
	array( 'title' => 'Servizi', 'slug' => 'servizi' ),
	array( 'title' => 'Casi studio', 'slug' => 'casi-studio' ),
	array( 'title' => 'Prezzi', 'slug' => 'prezzi' ),
	array( 'title' => 'Strumenti', 'slug' => 'strumenti' ),
	array( 'title' => 'Blog', 'slug' => 'blog' ),
);

$existing_items = wp_get_nav_menu_items( $menu_id );
$existing_titles = $existing_items ? wp_list_pluck( $existing_items, 'title' ) : array();

foreach ( $menu_items as $item ) {
	if ( in_array( $item['title'], $existing_titles, true ) ) {
		continue;
	}
	$page = get_page_by_path( $item['slug'], OBJECT, 'page' );
	if ( ! $page ) {
		WP_CLI::warning( "  pagina /{$item['slug']}/ non trovata, voce di menu saltata" );
		continue;
	}
	wp_update_nav_menu_item( $menu_id, 0, array(
		'menu-item-title'     => $item['title'],
		'menu-item-object-id' => $page->ID,
		'menu-item-object'    => 'page',
		'menu-item-type'      => 'post_type',
		'menu-item-status'    => 'publish',
	) );
}

if ( ! in_array( 'Preventivo in 24 ore', $existing_titles, true ) ) {
	wp_update_nav_menu_item( $menu_id, 0, array(
		'menu-item-title'  => 'Preventivo in 24 ore',
		'menu-item-url'    => home_url( '/#contatti' ),
		'menu-item-type'   => 'custom',
		'menu-item-status' => 'publish',
	) );
}
WP_CLI::log( '  voci di menu sincronizzate (Servizi · Casi studio · Prezzi · Strumenti · Blog · Preventivo in 24 ore)' );

$locations = get_registered_nav_menus();
if ( empty( $locations ) ) {
	WP_CLI::warning( '  Il tema Prespa non registra location di menu rilevate — assegnare il menu a mano in Aspetto → Menu.' );
} else {
	// Preferisce esplicitamente 'menu-1' (location primaria di Prespa) invece
	// del primo elemento dell'array: da quando il tema registra anche
	// footer-pagine/footer-studio, "il primo registrato" non è più affidabile
	// e dipende dall'ordine di caricamento parent/child.
	$existing_locations = get_theme_mod( 'nav_menu_locations', array() );
	$first_location      = isset( $locations['menu-1'] ) ? 'menu-1' : array_key_first( $locations );
	$existing_locations[ $first_location ] = $menu_id;
	set_theme_mod( 'nav_menu_locations', $existing_locations );
	WP_CLI::log( "  menu assegnato alla location '$first_location' ({$locations[$first_location]})" );
}

/* ---------- 4. Menu del footer proprietario ---------- */

WP_CLI::log( "\nMenu footer:" );

function remarka_deploy_sync_footer_menu( string $menu_name, string $location, array $items, bool $force, bool $wipe_on_force = true ): void {
	$menu = wp_get_nav_menu_object( $menu_name );
	if ( ! $menu ) {
		$menu_id = wp_create_nav_menu( $menu_name );
		WP_CLI::log( "  + menu creato: $menu_name (ID $menu_id)" );
	} else {
		$menu_id = $menu->term_id;
		WP_CLI::log( "  = menu già esistente: $menu_name (ID $menu_id)" );
		// $wipe_on_force=false — для ГЛАВНЫХ меню EN/RU: владелец добавляет
		// туда выпадающие подпункты руками, wipe их уничтожал (инцидент
		// 20.07.2026). Футерные меню полностью канонические — им wipe нужен.
		if ( $force && $wipe_on_force ) {
			foreach ( wp_get_nav_menu_items( $menu_id ) as $item ) {
				wp_delete_post( $item->ID, true );
			}
		}
	}

	$existing_items  = wp_get_nav_menu_items( $menu_id );
	$existing_titles = $existing_items ? wp_list_pluck( $existing_items, 'title' ) : array();

	foreach ( $items as $item ) {
		if ( in_array( $item['title'], $existing_titles, true ) ) {
			continue;
		}
		if ( isset( $item['slug'] ) ) {
			$page = get_page_by_path( $item['slug'], OBJECT, 'page' );
			if ( ! $page ) {
				WP_CLI::warning( "    pagina /{$item['slug']}/ non trovata, voce '{$item['title']}' saltata" );
				continue;
			}
			wp_update_nav_menu_item( $menu_id, 0, array(
				'menu-item-title'     => $item['title'],
				'menu-item-object-id' => $page->ID,
				'menu-item-object'    => 'page',
				'menu-item-type'      => 'post_type',
				'menu-item-status'    => 'publish',
			) );
		} else {
			wp_update_nav_menu_item( $menu_id, 0, array(
				'menu-item-title'  => $item['title'],
				'menu-item-url'    => $item['url'],
				'menu-item-type'   => 'custom',
				'menu-item-status' => 'publish',
			) );
		}
	}

	if ( '' !== $location ) {
		$existing_locations = get_theme_mod( 'nav_menu_locations', array() );
		$existing_locations[ $location ] = $menu_id;
		set_theme_mod( 'nav_menu_locations', $existing_locations );
		WP_CLI::log( "  voci sincronizzate e menu assegnato alla location '$location'" );
	} else {
		// Menu linguistici: nessuna location — vengono sostituiti a runtime
		// per nome da remarka_swap_menu_by_lang() (inc/multilang.php).
		WP_CLI::log( '  voci sincronizzate (menu per lingua, senza location)' );
	}
}

// Colonna «Servizi» (footer-pagine): servizi principali + pagine commerciali.
// L'elenco completo dei servizi vive sull'indice /servizi/, linkato dal titolo
// della colonna (vedi remarka_render_footer). Contatti è migrato qui dalla ex
// colonna Studio; i link legali sono nella riga di chiusura del footer.
remarka_deploy_sync_footer_menu(
	'Footer — Pagine',
	'footer-pagine',
	array(
		array( 'title' => 'Siti aziendali', 'slug' => 'servizi/siti-aziendali' ),
		array( 'title' => 'E-commerce', 'slug' => 'servizi/e-commerce' ),
		array( 'title' => 'Web app su misura', 'slug' => 'servizi/web-app' ),
		array( 'title' => 'SEO tecnica', 'slug' => 'servizi/seo-tecnica' ),
		array( 'title' => 'Casi studio', 'slug' => 'casi-studio' ),
		array( 'title' => 'Prezzi', 'slug' => 'prezzi' ),
		array( 'title' => 'Blog', 'slug' => 'blog' ),
		array( 'title' => 'Area clienti', 'slug' => 'area-clienti' ),
		array( 'title' => 'Contatti', 'url' => home_url( '/#contatti' ) ),
	),
	$force
);

// Colonna «Strumenti gratuiti» (footer-strumenti): TUTTI gli strumenti del Lab
// (ordine di data.py:TOOLS). Il titolo della colonna linka l'indice /strumenti/.
remarka_deploy_sync_footer_menu(
	'Footer — Strumenti',
	'footer-strumenti',
	array(
		array( 'title' => 'Check-up completo', 'slug' => 'strumenti/check-up-completo' ),
		array( 'title' => 'Test velocità', 'slug' => 'strumenti/test-velocita' ),
		array( 'title' => 'Analisi SEO on-page', 'slug' => 'strumenti/analisi-seo' ),
		array( 'title' => 'Check GDPR e cookie', 'slug' => 'strumenti/check-gdpr' ),
		array( 'title' => 'ROI localizzazione', 'slug' => 'strumenti/roi-localizzazione' ),
		array( 'title' => 'Verifica accessibilità', 'slug' => 'strumenti/verifica-accessibilita' ),
		array( 'title' => 'Sito pronto per l’AI', 'slug' => 'strumenti/sito-pronto-ai' ),
		array( 'title' => 'Impatto CO₂', 'slug' => 'strumenti/impatto-co2' ),
		array( 'title' => 'Segnali E-E-A-T', 'slug' => 'strumenti/segnali-eeat' ),
		array( 'title' => 'Il vostro sito, letto dall’AI', 'slug' => 'strumenti/sito-letto-dallai' ),
		array( 'title' => 'Suona madrelingua?', 'slug' => 'strumenti/suona-madrelingua' ),
		array( 'title' => 'Generatore di llms.txt', 'slug' => 'strumenti/generatore-llms-txt' ),
	),
	$force
);

/* ---------- 5. Menu per lingua (EN/RU) ----------
 * Senza location: inc/multilang.php li sostituisce a runtime per NOME —
 * i nomi qui devono combaciare con remarka_lang_menu_name(). */

WP_CLI::log( "\nMenu EN/RU:" );

remarka_deploy_sync_footer_menu( 'Menu EN — Remarka', '', array(
	array( 'title' => 'Services', 'slug' => 'en/services' ),
	array( 'title' => 'Case studies', 'slug' => 'en/case-studies' ),
	array( 'title' => 'Pricing', 'slug' => 'en/pricing' ),
	array( 'title' => 'Tools', 'slug' => 'en/tools' ),
	array( 'title' => 'Blog', 'slug' => 'en/blog' ),
	array( 'title' => 'Get a quote in 24 hours', 'url' => home_url( '/en/#contatti' ) ),
), $force, false );

remarka_deploy_sync_footer_menu( 'Footer EN — Pages', '', array(
	array( 'title' => 'Business websites', 'slug' => 'en/services/business-websites' ),
	array( 'title' => 'E-commerce', 'slug' => 'en/services/e-commerce' ),
	array( 'title' => 'Custom web apps', 'slug' => 'en/services/custom-web-apps' ),
	array( 'title' => 'Technical SEO', 'slug' => 'en/services/technical-seo' ),
	array( 'title' => 'Case studies', 'slug' => 'en/case-studies' ),
	array( 'title' => 'Pricing', 'slug' => 'en/pricing' ),
	array( 'title' => 'Blog', 'slug' => 'en/blog' ),
	array( 'title' => 'Client area', 'slug' => 'en/client-area' ),
	array( 'title' => 'Contact us', 'url' => home_url( '/en/#contatti' ) ),
	// Unica landing città tradotta in EN: la conserviamo qui (in fondo) per non
	// perdere l'unico link cittadino di questa lingua (ex colonna Studio).
	array( 'title' => 'Websites in Milan', 'slug' => 'en/milan' ),
), $force );

remarka_deploy_sync_footer_menu( 'Footer EN — Tools', '', array(
	array( 'title' => 'Full check-up', 'slug' => 'en/tools/full-site-checkup' ),
	array( 'title' => 'Speed test', 'slug' => 'en/tools/speed-test' ),
	array( 'title' => 'On-page SEO analysis', 'slug' => 'en/tools/seo-audit' ),
	array( 'title' => 'GDPR and cookie check', 'slug' => 'en/tools/gdpr-check' ),
	array( 'title' => 'Localization ROI', 'slug' => 'en/tools/localization-roi' ),
	array( 'title' => 'Accessibility check', 'slug' => 'en/tools/accessibility-check' ),
	array( 'title' => 'AI readiness check', 'slug' => 'en/tools/ai-readiness' ),
	array( 'title' => 'CO₂ impact', 'slug' => 'en/tools/website-carbon' ),
	array( 'title' => 'E-E-A-T signals', 'slug' => 'en/tools/eeat-signals' ),
	array( 'title' => 'Your website, read by AI', 'slug' => 'en/tools/read-by-ai' ),
	array( 'title' => 'Does it sound native?', 'slug' => 'en/tools/does-it-sound-native' ),
	array( 'title' => 'llms.txt generator', 'slug' => 'en/tools/llms-txt-generator' ),
), $force );

remarka_deploy_sync_footer_menu( 'Menu RU — Remarka', '', array(
	array( 'title' => 'Услуги', 'slug' => 'ru/uslugi' ),
	array( 'title' => 'Кейсы', 'slug' => 'ru/kejsy' ),
	array( 'title' => 'Цены', 'slug' => 'ru/ceny' ),
	array( 'title' => 'Инструменты', 'slug' => 'ru/instrumenty' ),
	array( 'title' => 'Блог', 'slug' => 'ru/blog' ),
	array( 'title' => 'Смета за 24 часа', 'url' => home_url( '/ru/#contatti' ) ),
), $force, false );

// Colonna «Услуги» RU — elenco esatto dettato dal titolare (18.07.2026).
// «Сайты в Милане» chiude la colonna (unica landing città RU, ex colonna Студия).
remarka_deploy_sync_footer_menu( 'Footer RU — Страницы', '', array(
	array( 'title' => 'Разработка сайтов для Европы', 'slug' => 'ru/uslugi/sajt-dlya-evropy' ),
	array( 'title' => 'SEO-продвижение', 'slug' => 'ru/uslugi/seo-prodvizhenie' ),
	array( 'title' => 'Кейсы', 'slug' => 'ru/kejsy' ),
	array( 'title' => 'Цены', 'slug' => 'ru/ceny' ),
	array( 'title' => 'Блог', 'slug' => 'ru/blog' ),
	array( 'title' => 'Кабинет клиента', 'slug' => 'ru/kabinet-klienta' ),
	array( 'title' => 'Контакты', 'url' => home_url( '/ru/#contatti' ) ),
	array( 'title' => 'Сайты в Милане', 'slug' => 'ru/milan' ),
), $force );

remarka_deploy_sync_footer_menu( 'Footer RU — Инструменты', '', array(
	array( 'title' => 'Полная проверка сайта', 'slug' => 'ru/instrumenty/polnaya-proverka-sajta' ),
	array( 'title' => 'Тест скорости', 'slug' => 'ru/instrumenty/test-skorosti' ),
	array( 'title' => 'SEO-анализ страницы', 'slug' => 'ru/instrumenty/seo-audit' ),
	array( 'title' => 'Проверка GDPR и cookie', 'slug' => 'ru/instrumenty/proverka-gdpr' ),
	array( 'title' => 'ROI локализации', 'slug' => 'ru/instrumenty/roi-lokalizacii' ),
	array( 'title' => 'Проверка доступности', 'slug' => 'ru/instrumenty/proverka-dostupnosti' ),
	array( 'title' => 'Готовность к ИИ', 'slug' => 'ru/instrumenty/gotovnost-k-ii' ),
	array( 'title' => 'Углеродный след', 'slug' => 'ru/instrumenty/uglerodnyj-sled' ),
	array( 'title' => 'Сигналы E-E-A-T', 'slug' => 'ru/instrumenty/signaly-eeat' ),
	array( 'title' => 'Ваш сайт глазами ИИ', 'slug' => 'ru/instrumenty/sajt-glazami-ii' ),
	array( 'title' => 'Звучит как у носителя?', 'slug' => 'ru/instrumenty/zvuchit-kak-u-nositelya' ),
	array( 'title' => 'Генератор llms.txt', 'slug' => 'ru/instrumenty/generator-llms-txt' ),
), $force );

WP_CLI::log( "\nFatto. Pagine create/verificate: " . count( $created_ids ) . ' + Home.' );
WP_CLI::log( 'Prossimi passi manuali: logo, numero WhatsApp (Personalizza → Remarka — Contatti), permalink "Nome articolo" (Impostazioni → Permalink, se non già attivo), screenshot reali dei casi studio.' );
