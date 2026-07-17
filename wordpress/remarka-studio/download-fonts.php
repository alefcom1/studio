<?php
/**
 * Remarka Studio — self-hosting dei font (perf: toglie i due CSS dei font dai
 * CDN esterni dal percorso critico e li serve same-origin, con preload).
 *
 * Perché: senza i file in assets/fonts/, functions.php ripiega su Fontshare +
 * Google Fonts (due <link> a origin esterni, render-blocking → LCP alto). Il
 * tema è già predisposto per il self-hosting: remarka_has_local_fonts()
 * controlla la presenza di ClashDisplay-Semibold.woff2 e, se c'è, carica
 * assets/css/fonts-local.css + preload dei woff2. Questo script scarica i 6
 * file attesi da fonts-local.css.
 *
 * Uso (sul server, che ha internet aperto — l'ambiente agent non raggiunge
 * Fontshare):
 *   docker compose ... run --rm wpcli eval-file wp-content/themes/remarka-studio/download-fonts.php
 * oppure, hosting classico:
 *   wp eval-file wp-content/themes/remarka-studio/download-fonts.php --allow-root --path=/percorso/wp
 *
 * I file finiscono in <tema>/assets/fonts/ e NON sono nel repository git:
 * `cp -r` in fase di deploy non li cancella (copia additiva), quindi
 * sopravvivono ai sync successivi. Rilanciabile senza rischio (sovrascrive).
 * Per tornare ai CDN: cancellare la cartella assets/fonts/.
 */

if ( ! defined( 'ABSPATH' ) ) {
	fwrite( STDERR, "Eseguire con `wp eval-file`, non con `php` diretto.\n" );
	exit( 1 );
}

$theme_dir = get_stylesheet_directory();
$fonts_dir = $theme_dir . '/assets/fonts';

// UA di un browser moderno: Fontshare e Google servono woff2 solo a chi lo
// dichiara supportato — con l'UA di default di WordPress arriverebbero ttf.
$ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36';

// I due CSS @font-face da cui ricavare gli url reali dei woff2.
$css_sources = array(
	'https://api.fontshare.com/v2/css?f[]=clash-display@500,600&f[]=general-sans@400,500,600&display=swap',
	'https://fonts.googleapis.com/css2?family=Fragment+Mono&display=swap',
);

// Mappa (famiglia|peso) => nome file atteso da fonts-local.css.
$targets = array(
	'clash display|500' => 'ClashDisplay-Medium.woff2',
	'clash display|600' => 'ClashDisplay-Semibold.woff2',
	'general sans|400'  => 'GeneralSans-Regular.woff2',
	'general sans|500'  => 'GeneralSans-Medium.woff2',
	'general sans|600'  => 'GeneralSans-Semibold.woff2',
	'fragment mono|400' => 'FragmentMono-Regular.woff2',
);

/**
 * Estrae dai blocchi @font-face le triple (famiglia, peso, url woff2).
 * Se per la stessa coppia famiglia/peso esistono più blocchi (Google spezza
 * per subset), preferisce quello con il range latino di base (U+0000-00FF).
 */
function remarka_fonts_parse_css( string $css ): array {
	$found = array(); // key => array( 'url' => ..., 'latin' => bool )
	if ( ! preg_match_all( '/@font-face\s*\{([^}]*)\}/is', $css, $blocks ) ) {
		return $found;
	}
	foreach ( $blocks[1] as $block ) {
		if ( ! preg_match( '/font-family:\s*[\'"]?([^;\'"]+)/i', $block, $fam ) ) {
			continue;
		}
		if ( ! preg_match( '/font-weight:\s*(\d+)/i', $block, $wgt ) ) {
			continue;
		}
		if ( ! preg_match( '/url\(\s*[\'"]?(https?:\/\/[^)\'"]+\.woff2)/i', $block, $url ) ) {
			continue;
		}
		$key      = strtolower( trim( $fam[1] ) ) . '|' . $wgt[1];
		$is_latin = (bool) preg_match( '/unicode-range:[^;]*0000-00ff/i', $block );
		// Primo trovato, oppure sostituisci se questo è il subset latino di base.
		if ( ! isset( $found[ $key ] ) || ( $is_latin && ! $found[ $key ]['latin'] ) ) {
			$found[ $key ] = array( 'url' => $url[1], 'latin' => $is_latin );
		}
	}
	return $found;
}

if ( ! wp_mkdir_p( $fonts_dir ) ) {
	WP_CLI::error( "Impossibile creare $fonts_dir (permessi?)." );
}

WP_CLI::log( 'Remarka — self-hosting font' );
WP_CLI::log( '===========================' );

$catalog = array();
foreach ( $css_sources as $src ) {
	$resp = wp_remote_get( $src, array( 'timeout' => 20, 'headers' => array( 'User-Agent' => $ua ) ) );
	if ( is_wp_error( $resp ) || 200 !== (int) wp_remote_retrieve_response_code( $resp ) ) {
		WP_CLI::warning( "  CSS non letto: $src" );
		continue;
	}
	$catalog += remarka_fonts_parse_css( wp_remote_retrieve_body( $resp ) );
}

$ok = 0;
$missing = array();
foreach ( $targets as $key => $filename ) {
	if ( empty( $catalog[ $key ]['url'] ) ) {
		$missing[] = $filename;
		WP_CLI::warning( "  ✗ url non trovato per $filename ($key)" );
		continue;
	}
	$resp = wp_remote_get( $catalog[ $key ]['url'], array( 'timeout' => 30, 'headers' => array( 'User-Agent' => $ua ) ) );
	$body = is_wp_error( $resp ) ? '' : wp_remote_retrieve_body( $resp );
	// woff2 valido inizia con la signature 'wOF2'.
	if ( strlen( $body ) < 1000 || 'wOF2' !== substr( $body, 0, 4 ) ) {
		$missing[] = $filename;
		WP_CLI::warning( "  ✗ download non valido: $filename" );
		continue;
	}
	if ( false === file_put_contents( "$fonts_dir/$filename", $body ) ) {
		$missing[] = $filename;
		WP_CLI::warning( "  ✗ scrittura fallita: $filename" );
		continue;
	}
	$ok++;
	WP_CLI::log( sprintf( '  + %s (%d KB)', $filename, (int) round( strlen( $body ) / 1024 ) ) );
}

WP_CLI::log( "\nScaricati $ok/" . count( $targets ) . ' font in ' . $fonts_dir );
if ( $missing ) {
	WP_CLI::warning( 'Mancanti: ' . implode( ', ', $missing ) . '. Il self-hosting si attiva solo con ClashDisplay-Semibold.woff2 presente; se manca un altro peso, quel testo userà il fallback di sistema. Scaricare a mano da fontshare.com / fonts.google.com e mettere il file in assets/fonts/.' );
} else {
	WP_CLI::success( 'Tutti i font presenti. Ora svuotare la cache: il tema passa da solo al self-hosting (fonts-local.css + preload).' );
}
