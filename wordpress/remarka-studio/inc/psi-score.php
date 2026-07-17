<?php
/**
 * Punteggio PageSpeed reale per il footer — misura automatica.
 *
 * Prima 17.07.2026: il footer mostrava un numero scritto a mano nel
 * Customizer (remarka_footer_pagespeed_score). Il titolare ha chiesto un
 * numero vero, misurato in automatico: questo file aggiunge un cron
 * giornaliero che interroga l'API PageSpeed Insights (stesso endpoint v5 di
 * remarka_tool_psi_handler() in functions.php, ma lato server: niente nonce
 * né rate-limit, che servono solo alla chiamata dal browser) e salva la media
 * in un'option che remarka_render_footer() legge in via prioritaria.
 *
 * Nessuna libreria esterna: solo wp_remote_get(), come nel resto del tema.
 */

defined( 'ABSPATH' ) || exit;

/**
 * Le 3 URL misurate: home + una pagina servizio + una pagina città, per una
 * media rappresentativa senza consumare troppa quota API ogni giorno.
 */
function remarka_psi_score_urls(): array {
	return array(
		home_url( '/' ),
		home_url( '/servizi/siti-aziendali/' ),
		home_url( '/milano/' ),
	);
}

/**
 * Misura una singola URL (strategy=mobile, solo categoria performance).
 * Ritorna il punteggio 0-100 (float, non arrotondato — l'arrotondamento è
 * solo sulla media finale in remarka_psi_score_run()) o null se la chiamata
 * o la risposta non sono utilizzabili.
 *
 * Timeout più corto del proxy client-side (remarka_tool_psi_handler usa 55s
 * per una singola chiamata interattiva): qui giriamo in cron, in sequenza su
 * 3 URL, e un timeout lungo moltiplicato per 3 rischierebbe di far scattare
 * i limiti di esecuzione del cron di WordPress.
 */
function remarka_psi_score_measure_url( string $url, string $key ): ?float {
	$endpoint = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=' . rawurlencode( $url )
		. '&strategy=mobile&category=PERFORMANCE&key=' . rawurlencode( $key );

	$resp = wp_remote_get( $endpoint, array( 'timeout' => 15 ) );
	if ( is_wp_error( $resp ) ) {
		return null;
	}
	if ( 200 !== (int) wp_remote_retrieve_response_code( $resp ) ) {
		return null;
	}

	$body    = wp_remote_retrieve_body( $resp );
	$decoded = json_decode( $body );
	if ( null === $decoded || ! isset( $decoded->lighthouseResult->categories->performance->score )
		|| ! is_numeric( $decoded->lighthouseResult->categories->performance->score ) ) {
		return null;
	}

	return (float) $decoded->lighthouseResult->categories->performance->score * 100;
}

/**
 * Callback del cron: misura le 3 URL una alla volta, salva la media di
 * quelle risposte con successo.
 *
 * - Chiave API vuota → uscita silenziosa, nessun log visibile (il titolare
 *   non ha ancora inserito la chiave: non è un errore da segnalare).
 * - Successo parziale (1 o 2 pagine su 3) → media di quelle riuscite.
 * - Fallimento totale (0 pagine) → l'option NON viene toccata: resta il
 *   valore del giorno precedente invece di sparire dal footer.
 */
function remarka_psi_score_run(): void {
	$key = get_theme_mod( 'remarka_psi_api_key', '' );
	if ( ! $key ) {
		return;
	}

	$scores = array();
	foreach ( remarka_psi_score_urls() as $url ) {
		$score = remarka_psi_score_measure_url( $url, $key );
		if ( null !== $score ) {
			$scores[] = $score;
		}
	}

	if ( ! $scores ) {
		return;
	}

	update_option( 'remarka_psi_score_auto', array(
		'score' => (int) floor( array_sum( $scores ) / count( $scores ) ),
		'date'  => gmdate( 'Y-m-d' ),
		'pages' => count( $scores ),
	) );
}

/**
 * Pianificazione lazy su 'init', come da convenzione del tema (nessun file
 * plugin, quindi nessun hook di attivazione classico register_activation_hook
 * a disposizione): se l'evento giornaliero non è già in coda lo pianifica.
 *
 * Bootstrap: se manca ancora remarka_psi_score_auto (mai misurato) e la
 * chiave è già configurata, pianifica ANCHE un run singolo fra un minuto, su
 * un hook separato — così dopo il deploy il numero compare subito invece di
 * aspettare la prossima mezzanotte del cron giornaliero.
 */
function remarka_psi_score_cron_init(): void {
	if ( ! wp_next_scheduled( 'remarka_psi_score_daily' ) ) {
		wp_schedule_event( time(), 'daily', 'remarka_psi_score_daily' );
	}

	$key = get_theme_mod( 'remarka_psi_api_key', '' );
	if ( $key && false === get_option( 'remarka_psi_score_auto', false ) && ! wp_next_scheduled( 'remarka_psi_score_first_run' ) ) {
		wp_schedule_single_event( time() + MINUTE_IN_SECONDS, 'remarka_psi_score_first_run' );
	}
}
add_action( 'init', 'remarka_psi_score_cron_init' );
add_action( 'remarka_psi_score_daily', 'remarka_psi_score_run' );
add_action( 'remarka_psi_score_first_run', 'remarka_psi_score_run' );
