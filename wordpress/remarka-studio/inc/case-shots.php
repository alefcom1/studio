<?php
/**
 * Screenshot dei casi studio reali (docs/copy-casi-studio.md): finché il
 * proprietario non carica gli scatti definitivi in assets/img/casi/, le
 * pagine mostrano un segnaposto brandizzato invece di un'immagine rotta.
 *
 * Meccanica scelta apposta: shortcode `[sr_shot]`, non un tag <img> statico.
 * Le pagine dei pattern (patterns/pages/*.php) vengono lette UNA VOLTA da
 * deploy-import.php e il loro output HTML viene congelato in post_content
 * nel database — qualunque logica PHP nei pattern gira solo in fase di
 * import, mai quando un visitatore apre la pagina. Uno shortcode, invece,
 * resta testo letterale nel post_content e viene eseguito da WordPress a
 * ogni caricamento (the_content → do_shortcode). Risultato pratico per il
 * proprietario: basta copiare i file in assets/img/casi/ e sincronizzare il
 * tema (scenario 2 della shpargalka, cp + niente wp eval-file) — NESSUN
 * nuovo giro di `REMARKA_FORCE=1 wp eval-file deploy-import.php`, perché il
 * contenuto della pagina in database resta invariato: cambia solo cosa
 * restituisce la funzione PHP che lo shortcode richiama.
 */

defined( 'ABSPATH' ) || exit;

/**
 * [sr_shot file="tms-board-1440.jpg" alt="…" caption="TMS — bacheca ordini, desktop" mobile="0"]
 *
 * file    — nome file atteso in assets/img/casi/ (nome FINALE concordato,
 *           vedi docs/copy-casi-studio.md §3 dell'istruzione implementatore).
 * alt     — alt text reale dell'immagine (usato anche come aria-label del segnaposto).
 * caption — riga leggibile «cosa c'è nell'inquadratura», mostrata solo nel segnaposto.
 * mobile  — "1" per la cornice mobile stretta (Mini App, ukrinitsy), "0" desktop (default).
 */
function remarka_sr_shot_shortcode( $atts ): string {
	$atts = shortcode_atts( array(
		'file'    => '',
		'alt'     => '',
		'caption' => '',
		'mobile'  => '0',
	), $atts, 'sr_shot' );

	$filename = sanitize_file_name( $atts['file'] );
	$rel_path = 'assets/img/casi/' . $filename;
	$abs_path = get_stylesheet_directory() . '/' . $rel_path;
	$mobile   = ( '1' === (string) $atts['mobile'] );

	if ( $filename && file_exists( $abs_path ) ) {
		$src = get_stylesheet_directory_uri() . '/' . $rel_path;
		return sprintf(
			'<figure class="wp-block-image size-large"><img src="%1$s" alt="%2$s" loading="lazy"/></figure>',
			esc_url( $src ),
			esc_attr( $atts['alt'] )
		);
	}

	return sprintf(
		'<div class="sr-shot-placeholder%1$s" role="img" aria-label="%2$s"><span class="sr-shot-placeholder__file">%3$s</span><span class="sr-shot-placeholder__caption">%4$s</span></div>',
		$mobile ? ' sr-shot-placeholder--mobile' : '',
		esc_attr( $atts['alt'] ?: $atts['caption'] ),
		esc_html( $rel_path ),
		esc_html( $atts['caption'] )
	);
}
add_shortcode( 'sr_shot', 'remarka_sr_shot_shortcode' );
