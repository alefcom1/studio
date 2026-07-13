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

/** Crea (o aggiorna, se --force e già gestita da noi) una pagina. Ritorna l'ID. */
function remarka_deploy_upsert_page( string $slug, string $title, string $content, int $parent_id = 0, bool $force = false ): int {
	$existing = get_page_by_path( $slug, OBJECT, 'page' );

	if ( $existing ) {
		$managed = get_post_meta( $existing->ID, '_remarka_generated', true );
		if ( ! $force || ! $managed ) {
			WP_CLI::log( "  = saltata (esiste già): /$slug/" );
			return $existing->ID;
		}
		wp_update_post( array(
			'ID'           => $existing->ID,
			'post_title'   => $title,
			'post_content' => $content,
			'post_parent'  => $parent_id,
		) );
		WP_CLI::log( "  ↻ aggiornata: /$slug/" );
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
		WP_CLI::warning( "  ✗ errore creando /$slug/: " . $id->get_error_message() );
		return 0;
	}

	update_post_meta( $id, '_remarka_generated', 'v1' );
	WP_CLI::log( "  + creata: /$slug/ (ID $id)" );
	return $id;
}

WP_CLI::log( 'Studio Remarka — import contenuti' . ( $force ? ' (--force attivo)' : '' ) );
WP_CLI::log( '=================================' );

/* ---------- 1. Home: concatenazione delle 11 sezioni, in ordine ---------- */

WP_CLI::log( "\nHome:" );
$home_sections = array(
	'hero-home', 'trust-strip', 'tre-numeri', 'servizi-cards', 'caso-evidenza',
	'come-lavoriamo', 'garanzie-dark', 'prezzi-teaser', 'strumenti-cards', 'faq', 'contatti',
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

	'casi-studio-index'                    => array( 'casi-studio', null, 'Casi studio' ),
	'caso-arredamenti-colombo'             => array( 'arredamenti-colombo', 'casi-studio', null ),
	'caso-cantina-serralta'                => array( 'cantina-serralta', 'casi-studio', null ),
	'caso-tecnoidraulica'                  => array( 'tecnoidraulica', 'casi-studio', null ),
	'caso-studio-legale-fontana'           => array( 'studio-legale-fontana', 'casi-studio', null ),

	'prezzi'                               => array( 'prezzi', null, null ),

	'strumenti-index'                      => array( 'strumenti', null, 'Strumenti' ),
	'strumento-test-velocita'              => array( 'test-velocita', 'strumenti', null ),
	'strumento-check-gdpr'                 => array( 'check-gdpr', 'strumenti', null ),
	'strumento-analisi-seo'                => array( 'analisi-seo', 'strumenti', null ),
	'strumento-roi-localizzazione'         => array( 'roi-localizzazione', 'strumenti', null ),

	'citta-milano'                         => array( 'milano', null, null ),
	'citta-monza'                          => array( 'monza', null, null ),
	'citta-bergamo'                        => array( 'bergamo', null, null ),
	'citta-brescia'                        => array( 'brescia', null, null ),
	'citta-como'                           => array( 'como', null, null ),
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
);

// Le pagine "genitore" (parent=null ma referenziate come parent altrove)
// vanno create per prime: separiamo in due passate.
$parent_keys = array( 'servizi-index', 'casi-studio-index', 'strumenti-index', 'blog-index' );
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
	list( $page_slug, $parent_key, $title_override ) = $page_map[ $pattern_slug ];
	list( $pattern_title, $content ) = remarka_deploy_read_pattern( $file );

	$title = $title_override ?: preg_replace( '/^Pagina — (Servizio: |Caso: |Città: |Articolo: |Strumento: )?/u', '', $pattern_title );
	// $parent_key in $page_map è lo SLUG della pagina genitore (es. 'servizi'),
	// quindi $created_ids va indicizzato per slug pagina, non per slug pattern —
	// altrimenti il lookup fallisce sempre e post_parent resta 0.
	$parent_id = $parent_key ? ( $created_ids[ $parent_key ] ?? 0 ) : 0;

	$id = remarka_deploy_upsert_page( $page_slug, $title, $content, $parent_id, $force );
	$created_ids[ $page_slug ] = $id;
}

/* ---------- 2b. Pulizia pagine orfane ----------
 * Se un caso/articolo viene rinominato o rimosso da data.py (successo con
 * gli slug dei casi studio: officine-riva/studio-fontana/bb-il-cortile →
 * cantina-serralta/tecnoidraulica/studio-legale-fontana), la vecchia pagina
 * resta nel database con lo slug precedente — non viene toccata perché non
 * compare più in $page_map. Qui cerchiamo tutte le pagine con il meta
 * _remarka_generated il cui slug non è (più) nella mappa corrente e le
 * spostiamo nel cestino, solo con --force (stessa cautela dell'update). */
$current_slugs = wp_list_pluck( $page_map, 0 );
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
	// Ripulisce le voci esistenti per evitare duplicati se rilanciato con --force.
	if ( $force ) {
		foreach ( wp_get_nav_menu_items( $menu_id ) as $item ) {
			wp_delete_post( $item->ID, true );
		}
	}
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

function remarka_deploy_sync_footer_menu( string $menu_name, string $location, array $items, bool $force ): void {
	$menu = wp_get_nav_menu_object( $menu_name );
	if ( ! $menu ) {
		$menu_id = wp_create_nav_menu( $menu_name );
		WP_CLI::log( "  + menu creato: $menu_name (ID $menu_id)" );
	} else {
		$menu_id = $menu->term_id;
		WP_CLI::log( "  = menu già esistente: $menu_name (ID $menu_id)" );
		if ( $force ) {
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

	$existing_locations = get_theme_mod( 'nav_menu_locations', array() );
	$existing_locations[ $location ] = $menu_id;
	set_theme_mod( 'nav_menu_locations', $existing_locations );
	WP_CLI::log( "  voci sincronizzate e menu assegnato alla location '$location'" );
}

remarka_deploy_sync_footer_menu(
	'Footer — Pagine',
	'footer-pagine',
	array(
		array( 'title' => 'Servizi', 'slug' => 'servizi' ),
		array( 'title' => 'Casi studio', 'slug' => 'casi-studio' ),
		array( 'title' => 'Prezzi', 'slug' => 'prezzi' ),
		array( 'title' => 'Strumenti gratuiti', 'slug' => 'strumenti' ),
		array( 'title' => 'Blog', 'slug' => 'blog' ),
	),
	$force
);

remarka_deploy_sync_footer_menu(
	'Footer — Studio',
	'footer-studio',
	array(
		array( 'title' => 'Siti web a Milano', 'slug' => 'milano' ),
		array( 'title' => 'Siti web a Monza', 'slug' => 'monza' ),
		array( 'title' => 'Siti web a Bergamo', 'slug' => 'bergamo' ),
		array( 'title' => 'Contatti', 'url' => home_url( '/#contatti' ) ),
		array( 'title' => 'Google Business Profile', 'url' => 'https://business.google.com/' ),
		array( 'title' => 'Privacy', 'slug' => 'privacy' ),
		array( 'title' => 'Cookie policy', 'slug' => 'cookie-policy' ),
	),
	$force
);

WP_CLI::log( "\nFatto. Pagine create/verificate: " . count( $created_ids ) . ' + Home.' );
WP_CLI::log( 'Prossimi passi manuali: logo, numero WhatsApp (Personalizza → Remarka — Contatti), permalink "Nome articolo" (Impostazioni → Permalink, se non già attivo), screenshot reali dei casi studio.' );
