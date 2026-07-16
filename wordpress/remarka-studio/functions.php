<?php
/**
 * Remarka Studio — дочерняя тема Prespa.
 *
 * Дизайн-система Studio Remarka поверх каркаса Prespa:
 * токены в theme.json, компоненты в assets/css/remarka.css,
 * анимации barra/counter/reveal в assets/js/remarka.js,
 * контент — Gutenberg-паттерны категории «Remarka» (папка /patterns).
 */

defined( 'ABSPATH' ) || exit;

define( 'REMARKA_STUDIO_VERSION', '1.0.0' );

// Мультиязычный рантайм (/en/, /ru/): язык, hreflang, строки, меню.
require_once get_stylesheet_directory() . '/inc/multilang.php';

// Check-up completo: copy deck del report PDF + rendering dompdf (M3).
require_once get_stylesheet_directory() . '/inc/checkup-report-pdf.php';

// Remarka Lab — 3 strumenti AI (Anthropic Messages API) + AI-insight nel PDF
// check-up (docs/piano-ai-tools.md).
require_once get_stylesheet_directory() . '/inc/ai-tools.php';

// Segnaposto per gli screenshot dei casi studio reali, in attesa dei file
// definitivi (docs/copy-casi-studio.md): shortcode [sr_shot], risolto a runtime.
require_once get_stylesheet_directory() . '/inc/case-shots.php';

/**
 * Есть ли локальные шрифты? Маркер — главный woff2 Clash Display.
 * Пока владелец не положил файлы в assets/fonts, тема грузит CDN
 * (Fontshare + Google Fonts), после — только самохостинг.
 */
function remarka_has_local_fonts(): bool {
	return file_exists( get_stylesheet_directory() . '/assets/fonts/ClashDisplay-Semibold.woff2' );
}

/** Подключение стилей и скриптов фронта. */
function remarka_enqueue_assets(): void {
	$dir = get_stylesheet_directory_uri();

	if ( remarka_has_local_fonts() ) {
		wp_enqueue_style(
			'remarka-fonts',
			$dir . '/assets/css/fonts-local.css',
			array(),
			REMARKA_STUDIO_VERSION
		);
	} else {
		wp_enqueue_style(
			'remarka-fonts-cdn',
			'https://api.fontshare.com/v2/css?f[]=clash-display@500,600&f[]=general-sans@400,500,600&display=swap',
			array(),
			null
		);
		wp_enqueue_style(
			'remarka-fonts-mono-cdn',
			'https://fonts.googleapis.com/css2?family=Fragment+Mono&display=swap',
			array(),
			null
		);
	}

	$css_path = get_stylesheet_directory() . '/assets/css/remarka.css';
	$js_path  = get_stylesheet_directory() . '/assets/js/remarka.js';

	wp_enqueue_style(
		'remarka-studio',
		$dir . '/assets/css/remarka.css',
		array( 'prespa-style' ),
		file_exists( $css_path ) ? (string) filemtime( $css_path ) : REMARKA_STUDIO_VERSION
	);

	wp_enqueue_script(
		'remarka-studio',
		$dir . '/assets/js/remarka.js',
		array(),
		file_exists( $js_path ) ? (string) filemtime( $js_path ) : REMARKA_STUDIO_VERSION,
		array(
			'in_footer' => true,
			'strategy'  => 'defer',
		)
	);

	// Config per il JS: chiave PageSpeed (Customizer, opzionale — senza
	// chiave la quota anonima di Google è bassa ma basta all'inizio),
	// endpoint AJAX e nonce del modulo contatti.
	/*
	 * La chiave PSI NON viene più stampata nel sorgente della pagina: la via
	 * diretta del browser va senza chiave (quota condivisa anonima, quando
	 * c'è), e al fallimento il JS ripiega sul proxy remarka_tool_psi, dove la
	 * chiave vive solo lato PHP. Così nessuno può rubarla e bruciare la quota.
	 */
	wp_add_inline_script(
		'remarka-studio',
		'window.remarkaPSI = ' . wp_json_encode( array(
			'ajaxUrl'    => admin_url( 'admin-ajax.php' ),
			'formNonce'  => wp_create_nonce( 'remarka_contact' ),
			'toolsNonce' => wp_create_nonce( 'remarka_tools' ),
			'locale'     => remarka_current_lang(),
		) ) . ';'
		. 'window.remarkaForm = ' . wp_json_encode( array(
			'step'    => remarka_str( 'form_step' ),
			'of'      => remarka_str( 'form_di' ),
			'back'    => remarka_str( 'form_indietro' ),
			'next'    => remarka_str( 'form_continua' ),
			'sending' => remarka_str( 'form_invio_corso' ),
			'choose'  => remarka_str( 'form_err_scelta' ),
		) ) . ';',
		'before'
	);
}
add_action( 'wp_enqueue_scripts', 'remarka_enqueue_assets', 20 );

/** Preload критичных начертаний при самохостинге. */
function remarka_preload_fonts(): void {
	if ( ! remarka_has_local_fonts() ) {
		return;
	}
	$dir = get_stylesheet_directory_uri();
	printf(
		'<link rel="preload" href="%s/assets/fonts/ClashDisplay-Semibold.woff2" as="font" type="font/woff2" crossorigin>' . "\n",
		esc_url( $dir )
	);
	printf(
		'<link rel="preload" href="%s/assets/fonts/GeneralSans-Regular.woff2" as="font" type="font/woff2" crossorigin>' . "\n",
		esc_url( $dir )
	);
}
add_action( 'wp_head', 'remarka_preload_fonts', 5 );

/** Стили редактора: паттерны в Gutenberg выглядят как на фронте. */
function remarka_editor_setup(): void {
	add_theme_support( 'editor-styles' );
	add_editor_style( 'assets/css/remarka.css' );
	if ( remarka_has_local_fonts() ) {
		add_editor_style( 'assets/css/fonts-local.css' );
	}
}
add_action( 'after_setup_theme', 'remarka_editor_setup' );

/**
 * Location di menu per il footer proprietario (vedi remarka_render_footer):
 * due colonne di link, ognuna gestibile in Aspetto → Menu senza toccare
 * il codice. Non ha niente a che fare con menu-1/menu-2 di Prespa.
 */
function remarka_register_footer_menus(): void {
	register_nav_menus( array(
		'footer-pagine' => __( 'Footer — Pagine', 'remarka-studio' ),
		'footer-studio' => __( 'Footer — Studio', 'remarka-studio' ),
	) );
}
add_action( 'after_setup_theme', 'remarka_register_footer_menus', 20 );

/**
 * Категории паттернов. «Remarka» — секции для сборки страниц вручную;
 * «Remarka — Pagine complete» — готовые полные страницы (сгенерированы
 * build-tools/generate_pages.py): вставить целиком и опубликовать.
 * Файлы из /patterns и /patterns/pages регистрируются WP автоматически.
 */
function remarka_pattern_category(): void {
	register_block_pattern_category(
		'remarka',
		array( 'label' => __( 'Remarka', 'remarka-studio' ) )
	);
	register_block_pattern_category(
		'remarka-pagine',
		array( 'label' => __( 'Remarka — Pagine complete', 'remarka-studio' ) )
	);
}
add_action( 'init', 'remarka_pattern_category', 5 );

/**
 * WordPress регистрирует автоматически только верхний уровень /patterns
 * (без рекурсии), поэтому «полные страницы» из /patterns/pages
 * (сгенерированы build-tools/generate_pages.py) регистрируем вручную —
 * тем же способом, каким это делает ядро для основной папки.
 */
function remarka_register_page_patterns(): void {
	$base  = get_stylesheet_directory() . '/patterns';
	$files = array();
	// pages — полные страницы (IT + en-/ru- переводы);
	// lang-en / lang-ru — переведённые секции Home.
	foreach ( array( 'pages', 'lang-en', 'lang-ru' ) as $sub ) {
		if ( is_dir( "$base/$sub" ) ) {
			$files = array_merge( $files, glob( "$base/$sub/*.php" ) ?: array() );
		}
	}
	foreach ( $files as $file ) {
		$data = get_file_data( $file, array(
			'title'         => 'Title',
			'slug'          => 'Slug',
			'description'   => 'Description',
			'viewportWidth' => 'Viewport Width',
			'categories'    => 'Categories',
		) );
		if ( empty( $data['slug'] ) || empty( $data['title'] ) ) {
			continue;
		}
		ob_start();
		include $file;
		$content = ob_get_clean();

		register_block_pattern( $data['slug'], array(
			'title'         => $data['title'],
			'description'   => $data['description'],
			'content'       => $content,
			'categories'    => array_filter( array_map( 'trim', explode( ',', $data['categories'] ?? 'remarka-pagine' ) ) ),
			'viewportWidth' => $data['viewportWidth'] ? (int) $data['viewportWidth'] : 1400,
		) );
	}
}
add_action( 'init', 'remarka_register_page_patterns', 9 );

/**
 * Стили блоков: дизайн переключается в сайдбаре редактора,
 * без ручного вписывания CSS-классов.
 */
function remarka_block_styles(): void {
	$group_styles = array(
		'sr-section'         => __( 'Sezione Remarka', 'remarka-studio' ),
		'sr-section--bianco' => __( 'Sezione bianca', 'remarka-studio' ),
		'sr-dark'            => __( 'Sezione scura', 'remarka-studio' ),
		'sr-hero'            => __( 'Hero con griglia', 'remarka-studio' ),
		'sr-card'            => __( 'Card Remarka', 'remarka-studio' ),
		'sr-card--carta'     => __( 'Card su carta', 'remarka-studio' ),
	);
	foreach ( $group_styles as $class => $label ) {
		register_block_style(
			'core/group',
			array(
				'name'  => $class,
				'label' => $label,
			)
		);
	}

	register_block_style(
		'core/columns',
		array(
			'name'  => 'sr-steps',
			'label' => __( 'Passaggi numerati', 'remarka-studio' ),
		)
	);

	register_block_style(
		'core/button',
		array(
			'name'  => 'sr-btn-whatsapp',
			'label' => __( 'WhatsApp', 'remarka-studio' ),
		)
	);

	register_block_style(
		'core/paragraph',
		array(
			'name'  => 'sr-eyebrow',
			'label' => __( 'Eyebrow (mono)', 'remarka-studio' ),
		)
	);
}
add_action( 'init', 'remarka_block_styles' );

/**
 * Гигиена производительности: эмодзи-скрипт и wp-embed сайту не нужны.
 * Обе меры обратимы удалением этих строк.
 */
function remarka_performance_cleanup(): void {
	remove_action( 'wp_head', 'print_emoji_detection_script', 7 );
	remove_action( 'wp_print_styles', 'print_emoji_styles' );
	remove_action( 'admin_print_scripts', 'print_emoji_detection_script' );
	remove_action( 'admin_print_styles', 'print_emoji_styles' );
	add_filter( 'emoji_svg_url', '__return_false' );
}
add_action( 'init', 'remarka_performance_cleanup' );

function remarka_deregister_wp_embed(): void {
	if ( ! is_admin() ) {
		wp_deregister_script( 'wp-embed' );
	}
}
add_action( 'wp_footer', 'remarka_deregister_wp_embed' );

/**
 * Prezzo lancio — promo sui primi 5 progetti (requisito del titolare,
 * 15.07.2026). I posti rimasti vivono in un'option, niente Customizer:
 * si gestisce da SSH con `wp option update remarka_lancio_slots N`
 * (sempre clampata 0–5 in lettura, per sicurezza anche se l'option viene
 * scritta a mano con un valore fuori range).
 *
 * Il contenuto delle pagine promo (patterns/**) è statico in post_content,
 * quindi il conteggio va sostituito a runtime, non rigenerato: i pattern
 * toccati dalla promo portano il placeholder letterale "{{lancio_slots}}"
 * e due coppie di marcatori testuali "{{lancio}}…{{/lancio}}" /
 * "{{listino}}…{{/listino}}". Il filtro the_content qui sotto mostra un
 * solo blocco per volta: finché restano posti (slots > 0) si vede il
 * blocco lancio col conteggio; quando gli slot finiscono (slots = 0) la
 * promo sparisce da sola e resta il solo listino pieno — fine di
 * campagna elegante, senza nessun redeploy.
 *
 * Priorità 8: gira PRIMA di do_blocks() (priorità 9 su the_content), così
 * i marcatori operano sui commenti-blocco Gutenberg ancora intatti nel
 * post_content grezzo, invece che sull'HTML già renderizzato.
 */
function remarka_lancio_slots(): int {
	$n = (int) get_option( 'remarka_lancio_slots', 5 );
	return max( 0, min( 5, $n ) );
}

function remarka_lancio_filter_content( string $content ): string {
	if ( false === strpos( $content, '{{lancio' ) && false === strpos( $content, '{{listino' ) ) {
		return $content;
	}
	if ( remarka_lancio_slots() > 0 ) {
		$content = preg_replace( '/\{\{lancio\}\}(.*?)\{\{\/lancio\}\}/s', '$1', $content );
		$content = preg_replace( '/\{\{listino\}\}(.*?)\{\{\/listino\}\}/s', '', $content );
		$content = str_replace( '{{lancio_slots}}', (string) remarka_lancio_slots(), $content );
	} else {
		$content = preg_replace( '/\{\{lancio\}\}(.*?)\{\{\/lancio\}\}/s', '', $content );
		$content = preg_replace( '/\{\{listino\}\}(.*?)\{\{\/listino\}\}/s', '$1', $content );
	}
	return $content;
}
add_filter( 'the_content', 'remarka_lancio_filter_content', 8 );

/**
 * Cookie banner (GDPR, Rifiuta = Accetta по весу) и WhatsApp FAB —
 * сайтвайд, без необходимости вставлять паттерн на каждую страницу.
 * Numero WhatsApp per lingua (IT/EN condividono lo stesso, RU ha il suo),
 * configurabile da Customizer o dalla costante REMARKA_WHATSAPP_NUMBER
 * (quest'ultima ha sempre la precedenza, indipendentemente dalla lingua).
 */
function remarka_whatsapp_number(): string {
	if ( defined( 'REMARKA_WHATSAPP_NUMBER' ) ) {
		return REMARKA_WHATSAPP_NUMBER;
	}
	if ( 'ru' === remarka_current_lang() ) {
		return get_theme_mod( 'remarka_whatsapp_number_ru', '79182630013' );
	}
	return get_theme_mod( 'remarka_whatsapp_number', '393478311141' );
}

/** Link WhatsApp pronto per l'uso in un href, numero della lingua corrente. */
function remarka_whatsapp_link(): string {
	return 'https://api.whatsapp.com/send?phone=' . rawurlencode( remarka_whatsapp_number() ) . '&text=';
}

function remarka_footer_widgets(): void {
	$wa_link = esc_url( remarka_whatsapp_link() );
	?>
	<div class="sr-cookie-banner" data-sr-cookie-banner hidden>
		<div class="sr-cookie-banner__inner">
			<p class="sr-cookie-banner__text">
				<?php echo esc_html( remarka_str( 'cookie_testo' ) ); ?>
				<a href="<?php echo esc_url( home_url( '/cookie-preferenze/' ) ); ?>"><?php echo esc_html( remarka_str( 'cookie_preferenze' ) ); ?></a>
				·
				<a href="<?php echo esc_url( home_url( '/cookie-policy/' ) ); ?>"><?php echo esc_html( remarka_str( 'cookie_policy' ) ); ?></a>
			</p>
			<div class="sr-cookie-banner__actions">
				<button type="button" class="sr-cookie-btn" data-sr-cookie-choice="rejected"><?php echo esc_html( remarka_str( 'cookie_rifiuta' ) ); ?></button>
				<button type="button" class="sr-cookie-btn" data-sr-cookie-choice="accepted"><?php echo esc_html( remarka_str( 'cookie_accetta' ) ); ?></button>
			</div>
		</div>
	</div>
	<a href="<?php echo $wa_link; ?>" class="sr-wa-fab" data-sr-wa-fab target="_blank" rel="noopener noreferrer" aria-label="<?php echo esc_attr( remarka_str( 'wa_label' ) ); ?>">
		<svg width="30" height="30" viewBox="0 0 32 32" fill="#FFFFFF" aria-hidden="true"><path d="M16.003 3C9.377 3 4 8.373 4 15c0 2.294.638 4.437 1.746 6.264L4 29l7.94-1.708A11.93 11.93 0 0 0 16.003 27C22.63 27 28 21.627 28 15S22.63 3 16.003 3Zm6.98 16.998c-.294.826-1.457 1.512-2.386 1.71-.634.135-1.462.243-4.248-.911-3.562-1.475-5.855-5.086-6.033-5.322-.177-.236-1.44-1.916-1.44-3.655 0-1.74.913-2.594 1.237-2.95.324-.354.708-.443.944-.443.236 0 .472.002.678.012.217.011.508-.082.795.607.294.708.998 2.447 1.086 2.625.088.177.147.384.03.62-.118.236-.177.383-.35.59-.177.207-.37.463-.53.62-.177.176-.36.367-.155.72.206.354.914 1.51 1.963 2.446 1.348 1.202 2.485 1.575 2.838 1.751.353.177.56.147.766-.088.207-.236.884-1.03 1.12-1.383.235-.354.47-.295.795-.177.324.118 2.06.972 2.414 1.148.353.177.588.265.677.412.088.147.088.855-.206 1.68Z"/></svg>
	</a>
	<?php
}
add_action( 'wp_footer', 'remarka_footer_widgets' );

/**
 * Testi e link del footer proprietario, tutti modificabili da Aspetto →
 * Personalizza senza toccare codice o database a mano.
 */
/**
 * Unica fonte di verità per i campi testuali del footer: usata sia per
 * registrare i controlli Customizer sia per leggerne il valore in
 * remarka_render_footer(). Prima erano duplicati (default qui, '' come
 * fallback nel render), e finché nessuno apre il Customizer get_theme_mod()
 * restituiva quel fallback vuoto invece del default — footer che sembrava
 * "vuoto" pur essendo tutto configurato correttamente lato codice.
 */
function remarka_footer_field_defs(): array {
	return array(
		'remarka_company_name'          => array( 'section' => 'remarka_contatti', 'label' => 'Ragione sociale', 'type' => 'text', 'default' => 'Studio Remarka S.r.l.' ),
		'remarka_company_address'       => array( 'section' => 'remarka_contatti', 'label' => 'Indirizzo (usare Invio per andare a capo)', 'type' => 'textarea', 'default' => "Milano, 20144, Vicolo Privato Lavandai, 2a\nTorino, 10153, Corso Regina Margherita, 94\nRoma, 00196, Via Flaminia, 122" ),
		'remarka_company_piva'          => array( 'section' => 'remarka_contatti', 'label' => 'Partita IVA', 'type' => 'text', 'default' => 'GE 302230994' ),
		'remarka_company_email'         => array( 'section' => 'remarka_contatti', 'label' => 'Email di contatto', 'type' => 'email', 'default' => 'info@remarka.biz' ),
		'remarka_company_phone'         => array( 'section' => 'remarka_contatti', 'label' => 'Telefono/WhatsApp', 'type' => 'text', 'default' => '+39 347 83 11141' ),
		'remarka_footer_tagline'        => array( 'section' => 'remarka_footer_cta', 'label' => 'Descrizione breve sotto il logo', 'type' => 'textarea', 'default' => 'Siti progressivi per PMI italiane. Parte del gruppo Remarka, nel settore linguistico e digitale dal 2001.' ),
		'remarka_footer_cta_heading'    => array( 'section' => 'remarka_footer_cta', 'label' => 'Titolo banner', 'type' => 'text', 'default' => 'Parliamo del vostro sito' ),
		'remarka_footer_cta_text'       => array( 'section' => 'remarka_footer_cta', 'label' => 'Sottotitolo banner', 'type' => 'textarea', 'default' => 'Analisi gratuita del sito attuale, preventivo chiuso entro 24 ore dalla chiamata.' ),
		'remarka_footer_cta_btn1_label' => array( 'section' => 'remarka_footer_cta', 'label' => 'Testo pulsante 1', 'type' => 'text', 'default' => 'Richiedi preventivo in 24 ore' ),
		'remarka_footer_cta_btn1_url'   => array( 'section' => 'remarka_footer_cta', 'label' => 'Link pulsante 1', 'type' => 'url', 'default' => '/#contatti' ),
		'remarka_footer_cta_btn2_label' => array( 'section' => 'remarka_footer_cta', 'label' => 'Testo pulsante 2', 'type' => 'text', 'default' => 'Analizza il tuo sito — gratis' ),
		'remarka_footer_cta_btn2_url'   => array( 'section' => 'remarka_footer_cta', 'label' => 'Link pulsante 2', 'type' => 'url', 'default' => '/strumenti/test-velocita/' ),
	);
}

/** Legge un campo footer da Customizer, col vero default (mai '') come fallback. */
function remarka_footer_mod( string $key ) {
	$defs = remarka_footer_field_defs();
	return get_theme_mod( $key, $defs[ $key ]['default'] ?? '' );
}

function remarka_customize_register( WP_Customize_Manager $wp_customize ): void {
	$wp_customize->add_section( 'remarka_contatti', array(
		'title'    => __( 'Remarka — Contatti e dati societari', 'remarka-studio' ),
		'priority' => 30,
	) );
	$wp_customize->add_setting( 'remarka_whatsapp_number', array(
		'default'           => '393478311141',
		'sanitize_callback' => 'sanitize_text_field',
	) );
	$wp_customize->add_control( 'remarka_whatsapp_number', array(
		'label'       => __( 'Numero WhatsApp — IT/EN (solo cifre, con prefisso internazionale)', 'remarka-studio' ),
		'description' => __( 'Usato dal bottone WhatsApp fluttuante su tutte le pagine in italiano e inglese.', 'remarka-studio' ),
		'section'     => 'remarka_contatti',
		'type'        => 'text',
	) );
	$wp_customize->add_setting( 'remarka_whatsapp_number_ru', array(
		'default'           => '79182630013',
		'sanitize_callback' => 'sanitize_text_field',
	) );
	$wp_customize->add_control( 'remarka_whatsapp_number_ru', array(
		'label'       => __( 'Numero WhatsApp — RU (solo cifre, con prefisso internazionale)', 'remarka-studio' ),
		'description' => __( 'Usato dal bottone WhatsApp fluttuante sulle pagine in russo.', 'remarka-studio' ),
		'section'     => 'remarka_contatti',
		'type'        => 'text',
	) );

	$wp_customize->add_section( 'remarka_footer_cta', array(
		'title'    => __( 'Remarka — Banner e footer', 'remarka-studio' ),
		'priority' => 31,
	) );

	foreach ( remarka_footer_field_defs() as $id => $field ) {
		$wp_customize->add_setting( $id, array(
			'default'           => $field['default'],
			'sanitize_callback' => 'url' === $field['type'] ? 'esc_url_raw' : 'sanitize_textarea_field',
		) );
		$wp_customize->add_control( $id, array(
			'label'   => $field['label'],
			'section' => $field['section'],
			'type'    => $field['type'],
		) );
	}

	$wp_customize->add_setting( 'remarka_footer_pagespeed_score', array(
		'default'           => 95,
		'sanitize_callback' => 'absint',
	) );
	$wp_customize->add_control( 'remarka_footer_pagespeed_score', array(
		'label'       => __( 'Punteggio PageSpeed da mostrare in footer (aggiornare a mano dopo un test reale)', 'remarka-studio' ),
		'section'     => 'remarka_footer_cta',
		'type'        => 'number',
		'input_attrs' => array( 'min' => 0, 'max' => 100 ),
	) );

	$wp_customize->add_setting( 'remarka_psi_api_key', array(
		'default'           => '',
		'sanitize_callback' => 'sanitize_text_field',
	) );
	$wp_customize->add_control( 'remarka_psi_api_key', array(
		'label'       => __( 'Chiave Google PageSpeed Insights API (per test velocità reali; senza chiave la quota è limitata)', 'remarka-studio' ),
		'description' => __( 'Gratuita: console.cloud.google.com → API e servizi → PageSpeed Insights API → Credenziali.', 'remarka-studio' ),
		'section'     => 'remarka_contatti',
		'type'        => 'text',
	) );

	$wp_customize->add_setting( 'remarka_anthropic_api_key', array(
		'default'           => '',
		'sanitize_callback' => 'sanitize_text_field',
	) );
	$wp_customize->add_control( 'remarka_anthropic_api_key', array(
		'label'       => __( 'Chiave Anthropic API (strumenti AI del Lab)', 'remarka-studio' ),
		'description' => __( 'Senza chiave gli strumenti AI restano in «manutenzione». console.anthropic.com → API Keys.', 'remarka-studio' ),
		'section'     => 'remarka_contatti',
		'type'        => 'text',
	) );

	$wp_customize->add_setting( 'remarka_form_recipient', array(
		'default'           => '',
		'sanitize_callback' => 'sanitize_email',
	) );
	$wp_customize->add_control( 'remarka_form_recipient', array(
		'label'       => __( 'Email che riceve le richieste del modulo contatti', 'remarka-studio' ),
		'description' => __( 'Se vuoto, usa l’email amministratore di WordPress.', 'remarka-studio' ),
		'section'     => 'remarka_contatti',
		'type'        => 'email',
	) );
}
add_action( 'customize_register', 'remarka_customize_register' );

/**
 * Footer proprietario: sostituisce interamente #colophon di Prespa (nascosto
 * via CSS in remarka.css) invece di sovrascrivere footer.php — così non si
 * rischia di rompere markup/JS di Prespa (ricerca, menu mobile) di cui non
 * abbiamo il sorgente completo. Testi e link vengono da Customizer; le due
 * colonne di link sono normali menu WordPress (Aspetto → Menu).
 */
/** Accetta sia percorsi relativi ("/#contatti") sia URL esterni completi. */
function remarka_footer_link_url( string $theme_mod_key, string $default ): string {
	$value = get_theme_mod( $theme_mod_key, $default );
	return preg_match( '#^https?://#i', $value ) ? $value : home_url( $value );
}

/**
 * Dati societari per lingua: in IT vengono da Customizer (li modifica il
 * titolare), in EN/RU sono fissi — stessa scelta già fatta per i testi del
 * banner footer in remarka_footer_text(), perché RU è un soggetto giuridico
 * diverso (Студия Ремарка, non Studio Remarka S.r.l.) con un proprio schema
 * di identificativi fiscali (ИНН/ОГРНИП invece di partita IVA).
 * 'tax' è un elenco di coppie [etichetta, valore] per gestire in modo
 * uniforme sia il caso a una riga (P.IVA/VAT) sia quello a due (ИНН+ОГРНИП).
 */
function remarka_company_lang_data(): array {
	$lang = remarka_current_lang();

	if ( 'ru' === $lang ) {
		return array(
			'name'    => 'Студия Ремарка',
			'address' => "125009, Москва, Глинищевский пер., д. 6, оф. 2\n350000, Краснодар, ул. Кузнечная, 6, офис 4",
			'tax'     => array(
				array( 'ИНН', '231149349191' ),
				array( 'ОГРНИП', '323237500359402' ),
			),
			'email'         => 'info@remarka.biz',
			'phone_display' => '+7 918 263 00 13',
		);
	}

	if ( 'en' === $lang ) {
		return array(
			'name'    => remarka_footer_mod( 'remarka_company_name' ),
			'address' => "Milan, 20144, Vicolo Privato Lavandai, 2a\nTurin, 10153, Corso Regina Margherita, 94\nRome, 00196, Via Flaminia, 122",
			'tax'     => array(
				array( 'VAT', remarka_footer_mod( 'remarka_company_piva' ) ),
			),
			'email'         => remarka_footer_mod( 'remarka_company_email' ),
			'phone_display' => remarka_footer_mod( 'remarka_company_phone' ),
		);
	}

	return array(
		'name'    => remarka_footer_mod( 'remarka_company_name' ),
		'address' => remarka_footer_mod( 'remarka_company_address' ),
		'tax'     => array(
			array( 'P.IVA', remarka_footer_mod( 'remarka_company_piva' ) ),
		),
		'email'         => remarka_footer_mod( 'remarka_company_email' ),
		'phone_display' => remarka_footer_mod( 'remarka_company_phone' ),
	);
}

/**
 * Città con una landing dedicata, per lingua. Le pagine città esistono in
 * italiano (Milano + provincia lombarda); in EN/RU solo Milano è tradotta
 * (le altre sono escluse dalla traduzione, vedi build-tools). Ritorna
 * [etichetta => URL]. Usata dalla fascia "Dove operiamo" nel footer, che
 * fa anche da cross-link tra le landing (altrimenti orfane).
 */
function remarka_cities_for_lang(): array {
	switch ( remarka_current_lang() ) {
		case 'en':
			return array( 'Milan' => home_url( '/en/milan/' ) );
		case 'ru':
			return array( 'Милан' => home_url( '/ru/milan/' ) );
		default:
			return array(
				'Milano'  => home_url( '/milano/' ),
				'Monza'   => home_url( '/monza/' ),
				'Bergamo' => home_url( '/bergamo/' ),
				'Brescia' => home_url( '/brescia/' ),
				'Como'    => home_url( '/como/' ),
			);
	}
}

function remarka_render_footer(): void {
	$score   = (int) get_theme_mod( 'remarka_footer_pagespeed_score', 95 );
	$company = remarka_company_lang_data();
	$cities  = remarka_cities_for_lang();
	?>
	<footer class="sr-footer">
		<div class="sr-footer-cta">
			<div class="sr-footer-cta__inner">
				<div>
					<h2 class="sr-footer-cta__heading"><?php echo esc_html( remarka_footer_text( 'remarka_footer_cta_heading', 'cta_heading' ) ); ?><span class="sr-accent-dot">.</span></h2>
					<p class="sr-footer-cta__text"><?php echo esc_html( remarka_footer_text( 'remarka_footer_cta_text', 'cta_text' ) ); ?></p>
				</div>
				<div class="sr-footer-cta__buttons">
					<a class="sr-footer-cta__btn sr-footer-cta__btn--primary" href="<?php echo esc_url( remarka_footer_link_url( 'remarka_footer_cta_btn1_url', '/#contatti' ) ); ?>"><?php echo esc_html( remarka_footer_text( 'remarka_footer_cta_btn1_label', 'cta_btn1' ) ); ?></a>
					<a class="sr-footer-cta__btn sr-footer-cta__btn--outline" href="<?php echo esc_url( remarka_footer_link_url( 'remarka_footer_cta_btn2_url', '/' ) ); ?>"><?php echo esc_html( remarka_footer_text( 'remarka_footer_cta_btn2_label', 'cta_btn2' ) ); ?></a>
				</div>
			</div>
		</div>

		<div class="sr-footer-main">
			<div class="sr-footer-main__inner">
				<div class="sr-footer-col sr-footer-col--brand">
					<div class="sr-footer-logo"><?php the_custom_logo(); ?><span><?php bloginfo( 'name' ); ?></span></div>
					<p><?php echo esc_html( remarka_footer_text( 'remarka_footer_tagline', 'footer_tagline' ) ); ?></p>
				</div>

				<div class="sr-footer-col">
					<p class="sr-footer-col__title"><?php echo esc_html( remarka_str( 'footer_pagine' ) ); ?></p>
					<?php
					wp_nav_menu( array(
						'theme_location' => 'footer-pagine',
						'container'      => false,
						'menu_class'     => '',
						'items_wrap'     => '<ul class="sr-footer-links">%3$s</ul>',
						'fallback_cb'    => false,
					) );
					?>
				</div>

				<div class="sr-footer-col">
					<p class="sr-footer-col__title"><?php echo esc_html( remarka_str( 'footer_studio' ) ); ?></p>
					<?php
					wp_nav_menu( array(
						'theme_location' => 'footer-studio',
						'container'      => false,
						'menu_class'     => '',
						'items_wrap'     => '<ul class="sr-footer-links">%3$s</ul>',
						'fallback_cb'    => false,
					) );
					?>
				</div>

				<div class="sr-footer-col">
					<p class="sr-footer-col__title"><?php echo esc_html( remarka_str( 'footer_dati' ) ); ?></p>
					<p class="sr-footer-company">
						<strong><?php echo esc_html( $company['name'] ); ?></strong><br>
						<?php echo nl2br( esc_html( $company['address'] ) ); ?>
					</p>
					<?php foreach ( $company['tax'] as list( $tax_label, $tax_value ) ) : ?>
						<p class="sr-mono"><?php echo esc_html( $tax_label ); ?> <?php echo esc_html( $tax_value ); ?></p>
					<?php endforeach; ?>
					<p><a href="mailto:<?php echo esc_attr( $company['email'] ); ?>"><?php echo esc_html( $company['email'] ); ?></a></p>
					<p><?php echo esc_html( remarka_str( 'footer_tel' ) ); ?>: <a href="<?php echo esc_url( remarka_whatsapp_link() ); ?>" target="_blank" rel="noopener noreferrer"><?php echo esc_html( $company['phone_display'] ); ?></a></p>
				</div>
			</div>
		</div>

		<?php if ( count( $cities ) > 1 ) : ?>
		<div class="sr-footer-cities">
			<div class="sr-footer-cities__inner">
				<span class="sr-footer-cities__label"><?php echo esc_html( remarka_str( 'footer_citta' ) ); ?></span>
				<ul class="sr-footer-cities__list">
					<?php foreach ( $cities as $label => $url ) : ?>
						<li><a href="<?php echo esc_url( $url ); ?>"><?php echo esc_html( $label ); ?></a></li>
					<?php endforeach; ?>
				</ul>
			</div>
		</div>
		<?php endif; ?>

		<div class="sr-footer-bottom">
			<div class="sr-footer-bottom__inner">
				<div class="sr-barra sr-barra--h4" data-sr-target="<?php echo esc_attr( $score ); ?>%" aria-hidden="true"><div class="sr-barra__fill"></div></div>
				<div class="sr-footer-bottom__row">
					<span>&copy; <?php echo esc_html( gmdate( 'Y' ) ); ?> <?php echo esc_html( $company['name'] ); ?> — <?php echo esc_html( remarka_str( 'footer_diritti' ) ); ?></span>
					<span class="sr-footer-score"><?php echo esc_html( remarka_str( 'footer_pagespeed' ) ); ?>: <b><?php echo esc_html( $score ); ?></b>/100</span>
				</div>
			</div>
		</div>
	</footer>
	<?php
}
add_action( 'wp_footer', 'remarka_render_footer', 5 );

/**
 * Yandex.Metrika: счётчик в футере всех страниц сайта.
 */
function remarka_yandex_metrika(): void {
	?>
	<!-- Yandex.Metrika counter -->
	<script type="text/javascript">
		(function(m,e,t,r,i,k,a){
			m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
			m[i].l=1*new Date();
			for (var j = 0; j < document.scripts.length; j++) {if (document.scripts[j].src === r) { return; }}
			k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)
		})(window, document,'script','https://mc.yandex.ru/metrika/tag.js?id=110723466', 'ym');

		ym(110723466, 'init', {ssr:true, webvisor:true, clickmap:true, ecommerce:"dataLayer", referrer: document.referrer, url: location.href, accurateTrackBounce:true, trackLinks:true});
	</script>
	<noscript><div><img src="https://mc.yandex.ru/watch/110723466" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
	<!-- /Yandex.Metrika counter -->
	<?php
}
add_action( 'wp_footer', 'remarka_yandex_metrika' );

/**
 * Класс автоматически на пункт меню-CTA («Preventivo…» / «Get a quote…» /
 * «Смета…»): владельцу не нужно вручную ставить CSS-класс sr-menu-cta в
 * настройках меню (см. #masthead .sr-menu-cta > a в remarka.css). Совпадение
 * по метке на всех трёх языках; mb_stripos — чтобы корректно ловить кириллицу.
 * Стиль применяется только в шапке (#masthead), поэтому одноимённые пункты в
 * футере, если и получат класс, визуально не изменятся.
 */
function remarka_auto_cta_menu_item_class( array $classes, WP_Post $item ): array {
	$needles = array( 'Preventivo', 'quote', 'Смета' );
	foreach ( $needles as $needle ) {
		if ( false !== mb_stripos( (string) $item->title, $needle ) ) {
			$classes[] = 'sr-menu-cta';
			break;
		}
	}
	return $classes;
}
add_filter( 'nav_menu_css_class', 'remarka_auto_cta_menu_item_class', 10, 2 );

/**
 * Organization + WebSite schema.org (JSON-LD) — базовая структурированная
 * разметка сайтвайд. Service/FAQPage/Article schema добавляются по мере
 * появления соответствующих плагинов SEO (Rank Math/Yoast) — см. план.
 */
function remarka_organization_schema(): void {
	if ( is_front_page() ) {
		$schema = array(
			'@context' => 'https://schema.org',
			'@type'    => 'ProfessionalService',
			'name'     => 'Studio Remarka',
			'url'      => home_url( '/' ),
			'areaServed' => 'IT',
			'priceRange' => '€€',
		);
		echo '<script type="application/ld+json">' . wp_json_encode( $schema ) . '</script>' . "\n";
		return;
	}

	// LocalBusiness на городских лендингах (piano-contenuti-seo §4.1):
	// адрес указываем только миланский (реальный офис), остальные города —
	// через areaServed, без выдуманных адресов.
	$city_slugs = array( 'milano' => 'Milano', 'monza' => 'Monza', 'bergamo' => 'Bergamo', 'brescia' => 'Brescia', 'como' => 'Como' );
	if ( is_page( array_keys( $city_slugs ) ) ) {
		$slug   = get_post_field( 'post_name', get_queried_object_id() );
		$schema = array(
			'@context'   => 'https://schema.org',
			'@type'      => 'LocalBusiness',
			'name'       => 'Studio Remarka',
			'url'        => get_permalink(),
			'telephone'  => remarka_footer_mod( 'remarka_company_phone' ),
			'email'      => remarka_footer_mod( 'remarka_company_email' ),
			'priceRange' => '€€',
			'address'    => array(
				'@type'           => 'PostalAddress',
				'streetAddress'   => 'Vicolo Privato Lavandai, 2a',
				'postalCode'      => '20144',
				'addressLocality' => 'Milano',
				'addressCountry'  => 'IT',
			),
			'areaServed' => $city_slugs[ $slug ] ?? 'Lombardia',
		);
		echo '<script type="application/ld+json">' . wp_json_encode( $schema ) . '</script>' . "\n";
	}
}
add_action( 'wp_head', 'remarka_organization_schema' );

/**
 * WebApplication + FAQPage (JSON-LD) sulla pagina «Check-up completo del sito»
 * (docs/copy-checkup.md §5.2, scope M2/M4). Non duplica l'Organization già
 * emessa da remarka_organization_schema() (solo su home/città): qui il
 * `provider` resta un riferimento minimo, con nome/e-mail per lingua da
 * remarka_company_lang_data() (nessun indirizzo/numero inventato). Niente
 * aggregateRating: il titolare ha escluso recensioni/valutazioni fittizie.
 * M4: le 3 pagine per lingua condividono lo stesso slug-check (is_page con
 * array di slug), name/featureList/FAQ sono localizzati da
 * docs/copy-checkup.md §2.2/§3.2/§4.2 — verbatim identico al testo reso
 * dal pattern della pagina in quella lingua.
 */
function remarka_checkup_tool_schema(): void {
	if ( ! is_page( array( 'check-up-completo', 'full-site-checkup', 'polnaya-proverka-sajta' ) ) ) {
		return;
	}
	$lang = remarka_current_lang();

	$copy = array(
		'it' => array(
			'name'         => 'Check-up completo del sito',
			'feature_list' => array(
				'Prestazioni (Google PageSpeed Insights)',
				'SEO (Google PageSpeed Insights)',
				'Accessibilità (Google PageSpeed Insights)',
				'Privacy e cookie (verifica indicativa)',
				'Best practice (Google PageSpeed Insights)',
				'Pronto per l’AI (4 segnali tecnici)',
				'Impatto CO₂ (modello Sustainable Web Design)',
			),
			'faq'          => array(
				array(
					'q' => 'Il punteggio è quello vero di Google?',
					'a' => 'Per prestazioni, SEO, accessibilità e best practice sì: arrivano dall’API ufficiale PageSpeed Insights, strategia mobile. Privacy, prontezza AI e CO₂ sono nostre verifiche, con il metodo dichiarato in ogni sezione.',
				),
				array(
					'q' => 'Il check-up GDPR sostituisce un consulente privacy?',
					'a' => 'No. È una verifica tecnica indicativa a quattro segnali: intercetta i problemi evidenti — banner assente, tracker prima del consenso — ma non è un parere legale e non sostituisce un consulente.',
				),
				array(
					'q' => 'Cosa ricevo nel report PDF che non vedo già a schermo?',
					'a' => 'A schermo vedete il punteggio, i sette semafori e le tre priorità. Nel PDF trovate una pagina per dimensione con tutte le criticità rilevate, le raccomandazioni operative in ordine di impatto e cosa faremmo noi, con i nostri riferimenti aziendali.',
				),
			),
		),
		'en' => array(
			'name'         => 'Full website check-up',
			'feature_list' => array(
				'Performance (Google PageSpeed Insights)',
				'SEO (Google PageSpeed Insights)',
				'Accessibility (Google PageSpeed Insights)',
				'Privacy & cookies (indicative check)',
				'Best practices (Google PageSpeed Insights)',
				'AI-readiness (4 technical signals)',
				'CO₂ impact (Sustainable Web Design model)',
			),
			'faq'          => array(
				array(
					'q' => 'Is the score the real Google one?',
					'a' => 'For performance, SEO, accessibility and best practices, yes — it comes from the official PageSpeed Insights API, mobile strategy. Privacy, AI-readiness and CO₂ are our own checks, with the method stated in each section.',
				),
				array(
					'q' => 'Does the GDPR check replace a privacy consultant?',
					'a' => 'No. It’s an indicative, four-signal technical check: it catches the obvious problems — missing banner, trackers before consent — but it’s not a legal opinion and doesn’t replace a consultant.',
				),
				array(
					'q' => 'What’s in the PDF that I don’t already see on screen?',
					'a' => 'On screen you see the score, the seven traffic lights and the three priorities. The PDF gives you a page per dimension with every issue found, the fixes ranked by impact, and what we would do, with our company details.',
				),
			),
		),
		'ru' => array(
			'name'         => 'Полная проверка сайта',
			'feature_list' => array(
				'Скорость (Google PageSpeed Insights)',
				'SEO (Google PageSpeed Insights)',
				'Доступность (Google PageSpeed Insights)',
				'Приватность и cookie (ориентировочная проверка)',
				'Технические стандарты (Google PageSpeed Insights)',
				'Готовность к ИИ (4 технических сигнала)',
				'Углеродный след (модель Sustainable Web Design)',
			),
			'faq'          => array(
				array(
					'q' => 'Оценка — настоящая от Google?',
					'a' => 'Для скорости, SEO, доступности и стандартов — да: она из официального API PageSpeed Insights, мобильная стратегия. Приватность, готовность к ИИ и CO₂ — наши проверки, метод описан в каждом разделе.',
				),
				array(
					'q' => 'Проверка GDPR заменяет консультанта по приватности?',
					'a' => 'Нет. Это ориентировочная техническая проверка по четырём сигналам: она ловит очевидные проблемы — нет баннера, трекеры до согласия, — но это не юридическое заключение и не замена консультанту.',
				),
				array(
					'q' => 'Что в PDF-отчёте, чего нет на экране?',
					'a' => 'На экране — оценка, семь светофоров и три приоритета. В PDF — по странице на каждое из семи измерений со всеми найденными проблемами, рекомендации по степени влияния и раздел «что сделали бы мы» с нашими реквизитами.',
				),
			),
		),
	);
	$c           = $copy[ $lang ];
	$company     = remarka_company_lang_data();
	$lang_prefix = 'it' === $lang ? '/' : "/$lang/";

	$app = array(
		'@context'            => 'https://schema.org',
		'@type'               => 'WebApplication',
		'name'                => $c['name'],
		'url'                 => get_permalink(),
		'applicationCategory' => 'BusinessApplication',
		'operatingSystem'     => 'Web',
		'inLanguage'          => $lang,
		'isAccessibleForFree' => true,
		'offers'              => array(
			'@type'         => 'Offer',
			'price'         => '0',
			'priceCurrency' => 'EUR',
		),
		'featureList'         => $c['feature_list'],
		'provider'            => array(
			'@type' => 'Organization',
			'name'  => $company['name'],
			'url'   => home_url( $lang_prefix ),
			'email' => $company['email'],
		),
	);
	echo '<script type="application/ld+json">' . wp_json_encode( $app ) . '</script>' . "\n";

	// Le 3 FAQ della pagina (docs/copy-checkup.md §2.2/§3.2/§4.2) — testo
	// statico, identico a quello reso da details_faq() nel pattern della
	// pagina in quella lingua.
	$faq        = $c['faq'];
	$faq_schema = array(
		'@context'   => 'https://schema.org',
		'@type'      => 'FAQPage',
		'mainEntity' => array_map(
			static function ( array $item ): array {
				return array(
					'@type'          => 'Question',
					'name'           => $item['q'],
					'acceptedAnswer' => array(
						'@type' => 'Answer',
						'text'  => $item['a'],
					),
				);
			},
			$faq
		),
	);
	echo '<script type="application/ld+json">' . wp_json_encode( $faq_schema ) . '</script>' . "\n";
}
add_action( 'wp_head', 'remarka_checkup_tool_schema' );

/**
 * BlogPosting (JSON-LD) su ogni pagina-articolo del blog, nelle tre lingue
 * (piano-blog.md, requisito del titolare 15.07). Segue lo stesso schema di
 * remarka_checkup_tool_schema(): niente duplicazione dell'Organization della
 * home, niente aggregateRating.
 *
 * I dati non testuali (data di pubblicazione, obbligatoria; obbligatoria la
 * dateModified del ritrofit; immagine di copertina, quando esiste) vengono da
 * inc/blog-schema-map.php, generato da build-tools/generate_pages.py
 * (build_blog_schema_map) a partire da BLOG_POSTS + lang.BLOG_SLUGS: una sola
 * fonte di verità, nessun titolo o data ricopiato a mano. L'headline non sta
 * nella mappa: usiamo get_the_title(), già localizzato dalla pagina in quella
 * lingua (RU compreso), così non si duplicano i titoli. author e publisher
 * sono l'Organization Studio Remarka da remarka_company_lang_data() (nome/URL
 * per lingua, nessun dato inventato).
 */
function remarka_blog_posting_schema(): void {
	if ( ! is_page() ) {
		return;
	}
	static $map = null;
	if ( null === $map ) {
		$map = require get_stylesheet_directory() . '/inc/blog-schema-map.php';
	}
	$slug = get_post_field( 'post_name', get_queried_object_id() );
	if ( ! isset( $map['posts'][ $slug ] ) ) {
		return;
	}
	$entry       = $map['posts'][ $slug ];
	$lang        = remarka_current_lang();
	$lang_prefix = 'it' === $lang ? '/' : "/$lang/";
	$company     = remarka_company_lang_data();

	$organization = array(
		'@type' => 'Organization',
		'name'  => $company['name'],
		'url'   => home_url( $lang_prefix ),
	);

	$schema = array(
		'@context'         => 'https://schema.org',
		'@type'            => 'BlogPosting',
		'headline'         => wp_strip_all_tags( get_the_title() ),
		'datePublished'    => $entry['date'],
		'dateModified'     => $map['_modified'],
		'inLanguage'       => $lang,
		'url'              => get_permalink(),
		'mainEntityOfPage' => array(
			'@type' => 'WebPage',
			'@id'   => get_permalink(),
		),
		'author'           => $organization,
		'publisher'        => $organization,
	);
	if ( ! empty( $entry['image'] ) ) {
		$schema['image'] = home_url( $entry['image'] );
	}
	echo '<script type="application/ld+json">' . wp_json_encode( $schema ) . '</script>' . "\n";
}
add_action( 'wp_head', 'remarka_blog_posting_schema' );

/**
 * ---------- Modulo contatti nativo ----------
 * Shortcode [remarka_form]: nessun plugin, invio via wp_mail.
 * Anti-spam: honeypot + nonce + rate-limit per IP (1 invio/60s, transient).
 * Progressive enhancement: senza JS il form fa POST a admin-post.php e
 * torna con ?remarka_inviato=1#contatti; con JS remarka.js intercetta
 * il submit e usa fetch su admin-ajax (stessa validazione server).
 * Destinatario: Customizer remarka_form_recipient, default admin_email.
 */
function remarka_form_recipient(): string {
	$to = get_theme_mod( 'remarka_form_recipient', '' );
	return $to && is_email( $to ) ? $to : get_option( 'admin_email' );
}

/**
 * Etichette CANONICHE (in italiano) delle opzioni del modulo: usate sia per
 * validare il valore inviato (whitelist) sia per comporre l'email verso lo
 * studio, che resta sempre in italiano a prescindere dalla lingua del
 * visitatore. Chiave = value inviato dal radio.
 */
function remarka_form_canonical(): array {
	return array(
		'tipo' => array(
			'siti-aziendali' => 'Sito aziendale',
			'e-commerce'     => 'E-commerce',
			'siti-pwa'       => 'Sito progressivo (PWA)',
			'restyling'      => 'Restyling e migrazione',
			'multilingue'    => 'Sito multilingue',
			'web-app'        => 'Web app su misura',
			'export-ready'   => 'Export Ready',
			'non-so'         => 'Non lo so ancora',
		),
		'budget' => array(
			'lt-3k'       => 'Meno di € 3.000',
			'3-8k'        => '€ 3.000 – 8.000',
			'8-15k'       => '€ 8.000 – 15.000',
			'15-35k'      => '€ 15.000 – 35.000',
			'gt-35k'      => 'Oltre € 35.000',
			'da-definire' => 'Da definire',
		),
		'tempi' => array(
			'subito'    => 'Il prima possibile',
			'1-2-mesi'  => 'Entro 1–2 mesi',
			'3-6-mesi'  => 'Fra 3–6 mesi',
			'valutando' => 'Sto solo valutando',
		),
	);
}

/**
 * Etichette LOCALIZZATE per il rendering dei radio, nella lingua corrente.
 * Stesse chiavi (value) di remarka_form_canonical(); su IT coincidono.
 */
function remarka_form_options( string $group ): array {
	$lang = remarka_current_lang();
	$maps = array(
		'tipo' => array(
			'en' => array( 'siti-aziendali' => 'Business website', 'e-commerce' => 'E-commerce', 'siti-pwa' => 'Progressive web app (PWA)', 'restyling' => 'Redesign & migration', 'multilingue' => 'Multilingual website', 'web-app' => 'Custom web app', 'export-ready' => 'Export Ready', 'non-so' => 'Not sure yet' ),
			'ru' => array( 'siti-aziendali' => 'Корпоративный сайт', 'e-commerce' => 'Интернет-магазин', 'siti-pwa' => 'Прогрессивный сайт (PWA)', 'restyling' => 'Редизайн и миграция', 'multilingue' => 'Многоязычный сайт', 'web-app' => 'Веб-приложение', 'export-ready' => 'Export Ready', 'non-so' => 'Пока не знаю' ),
		),
		'budget' => array(
			'en' => array( 'lt-3k' => 'Under € 3,000', '3-8k' => '€ 3,000 – 8,000', '8-15k' => '€ 8,000 – 15,000', '15-35k' => '€ 15,000 – 35,000', 'gt-35k' => 'Over € 35,000', 'da-definire' => 'To be defined' ),
			'ru' => array( 'lt-3k' => 'До € 3 000', '3-8k' => '€ 3 000 – 8 000', '8-15k' => '€ 8 000 – 15 000', '15-35k' => '€ 15 000 – 35 000', 'gt-35k' => 'Более € 35 000', 'da-definire' => 'Обсудим' ),
		),
		'tempi' => array(
			'en' => array( 'subito' => 'As soon as possible', '1-2-mesi' => 'Within 1–2 months', '3-6-mesi' => 'In 3–6 months', 'valutando' => 'Just exploring' ),
			'ru' => array( 'subito' => 'Как можно скорее', '1-2-mesi' => 'В течение 1–2 месяцев', '3-6-mesi' => 'Через 3–6 месяцев', 'valutando' => 'Просто оцениваю' ),
		),
	);
	if ( 'it' !== $lang && isset( $maps[ $group ][ $lang ] ) ) {
		return $maps[ $group ][ $lang ];
	}
	return remarka_form_canonical()[ $group ];
}

/** Rende un gruppo di radio (card o pill). */
function remarka_form_radio_group( string $name, string $group, string $style ): void {
	$wrap = 'card' === $style ? 'sr-choice-grid' : 'sr-pill-group';
	echo '<div class="' . esc_attr( $wrap ) . '">';
	foreach ( remarka_form_options( $group ) as $value => $label ) {
		if ( 'card' === $style ) {
			printf(
				'<label class="sr-choice"><input type="radio" class="sr-choice__input" name="%1$s" value="%2$s" required><span class="sr-choice__tick"></span><span>%3$s</span></label>',
				esc_attr( $name ), esc_attr( $value ), esc_html( $label )
			);
		} else {
			printf(
				'<label class="sr-pill"><input type="radio" class="sr-pill__input" name="%1$s" value="%2$s" required><span>%3$s</span></label>',
				esc_attr( $name ), esc_attr( $value ), esc_html( $label )
			);
		}
	}
	echo '</div>';
}

function remarka_form_shortcode(): string {
	$sent = isset( $_GET['remarka_inviato'] ); // phpcs:ignore WordPress.Security.NonceVerification.Recommended
	ob_start();
	?>
	<form class="sr-contact-form sr-stepform" data-sr-contact-form method="post" enctype="multipart/form-data"
	      action="<?php echo esc_url( admin_url( 'admin-post.php' ) ); ?>" <?php echo $sent ? 'hidden' : ''; ?>>
		<input type="hidden" name="action" value="remarka_contact">
		<?php wp_nonce_field( 'remarka_contact', 'remarka_nonce' ); ?>
		<p class="sr-hp-field" aria-hidden="true"><label>Sito web<input type="text" name="sr_sito" tabindex="-1" autocomplete="off"></label></p>

		<div class="sr-form-progress" data-sr-progress hidden>
			<span class="sr-form-progress__label" data-sr-progress-label></span>
			<div class="sr-form-progress__bar"><div class="sr-form-progress__fill" data-sr-progress-fill></div></div>
		</div>

		<fieldset class="sr-step" data-sr-step>
			<legend class="sr-step__q"><?php echo esc_html( remarka_str( 'form_q_tipo' ) ); ?></legend>
			<p class="sr-step__hint"><?php echo esc_html( remarka_str( 'form_q_tipo_hint' ) ); ?></p>
			<?php remarka_form_radio_group( 'sr_tipo', 'tipo', 'card' ); ?>
		</fieldset>

		<fieldset class="sr-step" data-sr-step>
			<legend class="sr-step__q"><?php echo esc_html( remarka_str( 'form_q_budget' ) ); ?></legend>
			<p class="sr-step__hint"><?php echo esc_html( remarka_str( 'form_q_budget_hint' ) ); ?></p>
			<span class="sr-field-label"><?php echo esc_html( remarka_str( 'form_lbl_budget' ) ); ?></span>
			<?php remarka_form_radio_group( 'sr_budget', 'budget', 'pill' ); ?>
			<span class="sr-field-label"><?php echo esc_html( remarka_str( 'form_lbl_tempi' ) ); ?></span>
			<?php remarka_form_radio_group( 'sr_tempi', 'tempi', 'pill' ); ?>
		</fieldset>

		<fieldset class="sr-step" data-sr-step>
			<legend class="sr-step__q"><?php echo esc_html( remarka_str( 'form_q_contatti' ) ); ?></legend>
			<p class="sr-step__hint"><?php echo esc_html( remarka_str( 'form_q_contatti_hint' ) ); ?></p>
			<p><label class="sr-field-label" for="sr-nome"><?php echo esc_html( remarka_str( 'form_nome' ) ); ?></label>
			<input class="sr-text-input" id="sr-nome" name="sr_nome" type="text" required maxlength="120"></p>
			<p><label class="sr-field-label" for="sr-contatto"><?php echo esc_html( remarka_str( 'form_contatto' ) ); ?></label>
			<input class="sr-text-input" id="sr-contatto" name="sr_contatto" type="text" required maxlength="160"></p>
			<p><label class="sr-field-label" for="sr-messaggio"><?php echo esc_html( remarka_str( 'form_messaggio' ) ); ?> <span class="sr-optional"><?php echo esc_html( remarka_str( 'form_msg_opt' ) ); ?></span></label>
			<textarea class="sr-text-input" id="sr-messaggio" name="sr_messaggio" rows="3" maxlength="4000"></textarea></p>
			<span class="sr-field-label"><?php echo esc_html( remarka_str( 'form_lbl_file' ) ); ?> <span class="sr-optional"><?php echo esc_html( remarka_str( 'form_file_opt' ) ); ?></span></span>
			<label class="sr-upload" data-sr-upload>
				<input type="file" class="sr-upload__input" name="sr_file" accept=".pdf,.doc,.docx,.png,.jpg,.jpeg">
				<span class="sr-upload__text" data-sr-upload-text><b><?php echo esc_html( remarka_str( 'form_upload_drag' ) ); ?></b> <?php echo esc_html( remarka_str( 'form_upload_or' ) ); ?></span>
				<span class="sr-upload__hint"><?php echo esc_html( remarka_str( 'form_upload_hint' ) ); ?></span>
			</label>
		</fieldset>

		<p class="sr-form-error" data-sr-form-error hidden></p>
		<button type="submit" class="wp-block-button__link wp-element-button" style="width:100%" data-sr-submit><?php echo esc_html( remarka_str( 'form_invia_finale' ) ); ?></button>
	</form>
	<div class="sr-form-success" data-sr-form-success <?php echo $sent ? '' : 'hidden'; ?>>
		<p class="sr-mono" style="color:var(--sr-verde)"><?php echo esc_html( remarka_str( 'form_inviata' ) ); ?></p>
		<p><?php echo esc_html( remarka_str( 'form_grazie' ) ); ?></p>
	</div>
	<?php
	return (string) ob_get_clean();
}
add_shortcode( 'remarka_form', 'remarka_form_shortcode' );

/**
 * Валидация + отправка. Возвращает null при успехе или текст ошибки.
 * Общая для AJAX и admin-post путей.
 */
function remarka_form_process(): ?string {
	if ( ! isset( $_POST['remarka_nonce'] ) || ! wp_verify_nonce( sanitize_key( $_POST['remarka_nonce'] ), 'remarka_contact' ) ) {
		return remarka_str( 'form_err_sessione' );
	}
	if ( ! empty( $_POST['sr_sito'] ) ) { // honeypot: люди это поле не видят.
		return null; // Боту отвечаем «успехом», письмо не шлём.
	}

	$ip  = isset( $_SERVER['REMOTE_ADDR'] ) ? sanitize_text_field( wp_unslash( $_SERVER['REMOTE_ADDR'] ) ) : '';
	$key = 'remarka_rl_' . md5( $ip );
	if ( get_transient( $key ) ) {
		return remarka_str( 'form_err_ratelimit' );
	}

	$nome      = sanitize_text_field( wp_unslash( $_POST['sr_nome'] ?? '' ) );
	$contatto  = sanitize_text_field( wp_unslash( $_POST['sr_contatto'] ?? '' ) );
	$messaggio = sanitize_textarea_field( wp_unslash( $_POST['sr_messaggio'] ?? '' ) );

	// Opzioni a scelta: validate contro la whitelist canonica; il messaggio
	// è facoltativo (il tipo di progetto è già una descrizione della richiesta).
	$canon = remarka_form_canonical();
	$tipo_v   = sanitize_key( $_POST['sr_tipo'] ?? '' );
	$budget_v = sanitize_key( $_POST['sr_budget'] ?? '' );
	$tempi_v  = sanitize_key( $_POST['sr_tempi'] ?? '' );

	if ( '' === $nome || '' === $contatto
		|| ! isset( $canon['tipo'][ $tipo_v ] )
		|| ! isset( $canon['budget'][ $budget_v ] )
		|| ! isset( $canon['tempi'][ $tempi_v ] ) ) {
		return remarka_str( 'form_err_campi' );
	}

	// Allegato facoltativo: validato e passato a wp_mail come file temporaneo,
	// MAI salvato nella Media Library né servito dal sito (privacy delle
	// richieste). Cancellato subito dopo l'invio.
	$attachments   = array();
	$tmp_to_delete = null;
	if ( isset( $_FILES['sr_file'] ) && ! empty( $_FILES['sr_file']['name'] )
		&& isset( $_FILES['sr_file']['error'] ) && UPLOAD_ERR_NO_FILE !== (int) $_FILES['sr_file']['error'] ) {
		$file = $_FILES['sr_file']; // phpcs:ignore
		if ( UPLOAD_ERR_OK !== (int) $file['error'] || (int) $file['size'] > 8 * MB_IN_BYTES ) {
			return remarka_str( 'form_err_file_dim' );
		}
		$ext     = strtolower( pathinfo( sanitize_file_name( $file['name'] ), PATHINFO_EXTENSION ) );
		$allowed = array( 'pdf', 'doc', 'docx', 'png', 'jpg', 'jpeg' );
		if ( ! in_array( $ext, $allowed, true ) || ! is_uploaded_file( $file['tmp_name'] ) ) {
			return remarka_str( 'form_err_file_tipo' );
		}
		$safe = sanitize_file_name( $file['name'] );
		$dest = trailingslashit( get_temp_dir() ) . wp_unique_filename( get_temp_dir(), $safe );
		if ( move_uploaded_file( $file['tmp_name'], $dest ) ) {
			$attachments[]  = $dest;
			$tmp_to_delete  = $dest;
			$allegato_nome  = $safe;
		}
	}

	$body  = 'Tipo di progetto: ' . $canon['tipo'][ $tipo_v ] . "\n";
	$body .= 'Budget: ' . $canon['budget'][ $budget_v ] . "\n";
	$body .= 'Tempi: ' . $canon['tempi'][ $tempi_v ] . "\n\n";
	$body .= "Nome: $nome\n";
	$body .= "Contatto: $contatto\n\n";
	$body .= 'Messaggio:' . "\n" . ( '' !== $messaggio ? $messaggio : '(nessun messaggio)' ) . "\n\n";
	$body .= 'Allegato: ' . ( isset( $allegato_nome ) ? $allegato_nome : 'nessuno' ) . "\n---\n";
	$body .= 'Pagina: ' . esc_url_raw( wp_get_referer() ?: home_url( '/' ) ) . "\n";
	$body .= 'Lingua: ' . remarka_current_lang() . "\n";
	$body .= "IP: $ip\n";
	$body .= 'Data: ' . current_time( 'mysql' ) . "\n";

	$headers = array();
	if ( is_email( $contatto ) ) {
		$headers[] = 'Reply-To: ' . $contatto;
	}

	$ok = wp_mail(
		remarka_form_recipient(),
		sprintf( '[remarka.biz] Richiesta di preventivo — %s (%s)', $nome, $canon['tipo'][ $tipo_v ] ),
		$body,
		$headers,
		$attachments
	);

	if ( $tmp_to_delete && file_exists( $tmp_to_delete ) ) {
		wp_delete_file( $tmp_to_delete );
	}

	if ( ! $ok ) {
		return remarka_str( 'form_err_tecnico' );
	}

	set_transient( $key, 1, MINUTE_IN_SECONDS );
	return null;
}

function remarka_form_handle_ajax(): void {
	$error = remarka_form_process();
	if ( null === $error ) {
		wp_send_json_success();
	}
	wp_send_json_error( array( 'message' => $error ) );
}
add_action( 'wp_ajax_remarka_contact', 'remarka_form_handle_ajax' );
add_action( 'wp_ajax_nopriv_remarka_contact', 'remarka_form_handle_ajax' );

function remarka_form_handle_post(): void {
	$error    = remarka_form_process();
	$back     = wp_get_referer() ?: home_url( '/' );
	$fragment = '#contatti';
	if ( null === $error ) {
		wp_safe_redirect( add_query_arg( 'remarka_inviato', '1', strtok( $back, '#' ) ) . $fragment );
	} else {
		wp_safe_redirect( add_query_arg( 'remarka_errore', rawurlencode( $error ), strtok( $back, '#' ) ) . $fragment );
	}
	exit;
}
add_action( 'admin_post_remarka_contact', 'remarka_form_handle_post' );

/* ============================================================================
 * Remarka Lab — endpoint di fetch server-side per gli strumenti (GDPR/AI).
 *
 * Il browser non può leggere HTML/robots.txt/llms.txt di siti terzi (CORS):
 * lo scarichiamo qui, con difesa SSRF completa, e restituiamo il corpo grezzo
 * al client che lo analizza. NON è un proxy generico: schemi/porte/IP/redirect
 * sono tutti verificati; solo contenuti testuali; corpo troncato.
 *
 * Le funzioni pure (validazione URL, resolve host, IP privati, fetch con
 * redirect manuale) sono estraibili singolarmente per lo stub-harness di test.
 * ========================================================================== */

/**
 * Blocca un IP se non è pubblico (privato/riservato/loopback/link-local, sia
 * IPv4 sia IPv6). Copre 127/8, 10/8, 172.16/12, 192.168/16, 169.254/16, 0/8,
 * ::1, fc00::/7, fe80::/10 e tutti i range riservati IANA.
 */
function remarka_tool_is_blocked_ip( $ip ) {
	if ( ! filter_var( $ip, FILTER_VALIDATE_IP ) ) {
		return true; // non è un IP valido → blocca per sicurezza.
	}
	// NO_PRIV_RANGE|NO_RES_RANGE → false quando l'IP è privato o riservato.
	if ( ! filter_var( $ip, FILTER_VALIDATE_IP, FILTER_FLAG_NO_PRIV_RANGE | FILTER_FLAG_NO_RES_RANGE ) ) {
		return true;
	}
	return false;
}

/** Risolve un host in lista di IP (A + AAAA). IP-literal → restituito così com'è. */
function remarka_tool_resolve_host( $host ) {
	if ( filter_var( $host, FILTER_VALIDATE_IP ) ) {
		return array( $host );
	}
	$ips = array();
	$v4  = gethostbynamel( $host );
	if ( is_array( $v4 ) ) {
		$ips = array_merge( $ips, $v4 );
	}
	$v6 = dns_get_record( $host, DNS_AAAA );
	if ( is_array( $v6 ) ) {
		foreach ( $v6 as $rec ) {
			if ( ! empty( $rec['ipv6'] ) ) {
				$ips[] = $rec['ipv6'];
			}
		}
	}
	return $ips;
}

/**
 * Valida un singolo URL: schema http/https, porta 80/443, host che risolve in
 * un IP pubblico. Ritorna array(ok, error, host, ips).
 */
function remarka_tool_check_url( $url ) {
	$parts = parse_url( $url );
	if ( ! is_array( $parts ) || empty( $parts['scheme'] ) || empty( $parts['host'] ) ) {
		return array( 'ok' => false, 'error' => 'url_non_valido' );
	}
	$scheme = strtolower( $parts['scheme'] );
	if ( 'http' !== $scheme && 'https' !== $scheme ) {
		return array( 'ok' => false, 'error' => 'schema_non_ammesso' );
	}
	$port = isset( $parts['port'] ) ? (int) $parts['port'] : ( 'https' === $scheme ? 443 : 80 );
	if ( 80 !== $port && 443 !== $port ) {
		return array( 'ok' => false, 'error' => 'porta_non_ammessa' );
	}
	$host = $parts['host'];
	$ips  = remarka_tool_resolve_host( $host );
	if ( empty( $ips ) ) {
		return array( 'ok' => false, 'error' => 'host_non_risolto' );
	}
	foreach ( $ips as $ip ) {
		if ( remarka_tool_is_blocked_ip( $ip ) ) {
			return array( 'ok' => false, 'error' => 'ip_privato_o_riservato' );
		}
	}
	return array( 'ok' => true, 'host' => $host, 'ips' => $ips );
}

/** Risolve una Location di redirect (assoluta o relativa) contro l'URL base. */
function remarka_tool_resolve_redirect( $base, $location ) {
	$location = trim( $location );
	if ( preg_match( '#^https?://#i', $location ) ) {
		return $location;
	}
	$p = parse_url( $base );
	if ( ! is_array( $p ) || empty( $p['scheme'] ) || empty( $p['host'] ) ) {
		return $location;
	}
	$origin = $p['scheme'] . '://' . $p['host'] . ( isset( $p['port'] ) ? ':' . $p['port'] : '' );
	if ( '' !== $location && '/' === $location[0] ) {
		return $origin . $location;
	}
	$dir = isset( $p['path'] ) ? preg_replace( '#/[^/]*$#', '/', $p['path'] ) : '/';
	return $origin . $dir . $location;
}

/** Content-Type accettati: testuali. text/* più i formati XML/JSON testuali
 *  (necessari per sitemap.xml / feed / JSON-LD). Nota: la spec chiedeva text/*;
 *  esteso ai tipi XML testuali per supportare path:sitemap.xml. */
function remarka_tool_ct_allowed( $ct ) {
	if ( '' === $ct ) {
		return true; // alcuni server non mandano Content-Type: non blocchiamo.
	}
	$ct = strtolower( $ct );
	if ( 0 === strpos( $ct, 'text/' ) ) {
		return true;
	}
	foreach ( array( 'application/xml', 'application/xhtml+xml', 'application/json', 'application/rss+xml', 'application/atom+xml', 'application/ld+json' ) as $ok ) {
		if ( 0 === strpos( $ct, $ok ) ) {
			return true;
		}
	}
	return false;
}

/**
 * Scarica un URL in sicurezza: loop manuale di redirect (max 3), ogni hop
 * ri-verificato (SSRF su ogni destinazione), timeout 8s, corpo ≤512KB, solo
 * Content-Type testuali. Ritorna array(ok, status, body, error).
 */
function remarka_tool_safe_fetch( $url, $max_redirects = 3 ) {
	$current = $url;
	$limit   = 512 * 1024;
	for ( $hop = 0; $hop <= $max_redirects; $hop++ ) {
		$check = remarka_tool_check_url( $current );
		if ( empty( $check['ok'] ) ) {
			return array( 'ok' => false, 'status' => 0, 'body' => '', 'error' => $check['error'] );
		}
		$resp = wp_remote_get( $current, array(
			'timeout'             => 8,
			'redirection'         => 0,
			'limit_response_size' => $limit,
			'user-agent'          => 'RemarkaLab/1.0 (+https://remarka.biz)',
			'headers'             => array( 'Accept' => 'text/html,text/plain,application/xml,*/*' ),
		) );
		if ( is_wp_error( $resp ) ) {
			return array( 'ok' => false, 'status' => 0, 'body' => '', 'error' => 'richiesta_fallita' );
		}
		$status = (int) wp_remote_retrieve_response_code( $resp );
		if ( $status >= 300 && $status < 400 ) {
			$location = wp_remote_retrieve_header( $resp, 'location' );
			if ( '' === $location ) {
				return array( 'ok' => false, 'status' => $status, 'body' => '', 'error' => 'redirect_senza_destinazione' );
			}
			$current = remarka_tool_resolve_redirect( $current, $location );
			continue; // ricomincia: il prossimo giro ri-valida l'host.
		}
		$ct = wp_remote_retrieve_header( $resp, 'content-type' );
		if ( ! remarka_tool_ct_allowed( $ct ) ) {
			return array( 'ok' => false, 'status' => $status, 'body' => '', 'error' => 'content_type_non_testuale' );
		}
		$body = (string) wp_remote_retrieve_body( $resp );
		if ( strlen( $body ) > $limit ) {
			$body = substr( $body, 0, $limit );
		}
		return array( 'ok' => true, 'status' => $status, 'body' => $body, 'error' => '' );
	}
	return array( 'ok' => false, 'status' => 0, 'body' => '', 'error' => 'troppi_redirect' );
}

/** Costruisce l'URL bersaglio dal mode: html (url intero) | path:<file>. */
function remarka_tool_target_url( $url, $mode ) {
	if ( 0 === strpos( $mode, 'path:' ) ) {
		$path    = substr( $mode, 5 );
		$allowed = array( 'llms.txt', 'robots.txt', 'sitemap.xml' );
		if ( ! in_array( $path, $allowed, true ) ) {
			return array( 'ok' => false, 'error' => 'path_non_ammesso' );
		}
		$p = parse_url( $url );
		if ( ! is_array( $p ) || empty( $p['scheme'] ) || empty( $p['host'] ) ) {
			return array( 'ok' => false, 'error' => 'url_non_valido' );
		}
		$origin = strtolower( $p['scheme'] ) . '://' . $p['host'] . ( isset( $p['port'] ) ? ':' . (int) $p['port'] : '' );
		return array( 'ok' => true, 'url' => $origin . '/' . $path );
	}
	return array( 'ok' => true, 'url' => $url );
}

/** Handler AJAX: nonce + rate-limit 10/min/IP + fetch sicuro → JSON {ok,status,body}. */
function remarka_tool_fetch_handler(): void {
	if ( ! isset( $_POST['nonce'] ) || ! wp_verify_nonce( sanitize_key( $_POST['nonce'] ), 'remarka_tools' ) ) {
		wp_send_json_error( array( 'message' => 'sessione scaduta' ), 403 );
	}

	$ip    = isset( $_SERVER['REMOTE_ADDR'] ) ? sanitize_text_field( wp_unslash( $_SERVER['REMOTE_ADDR'] ) ) : '';
	$key   = 'remarka_tl_' . md5( $ip );
	$count = (int) get_transient( $key );
	if ( $count >= 10 ) {
		wp_send_json_error( array( 'message' => 'troppe richieste, riprovate tra un minuto' ), 429 );
	}
	set_transient( $key, $count + 1, MINUTE_IN_SECONDS );

	$url  = esc_url_raw( wp_unslash( $_POST['url'] ?? '' ) );
	$mode = sanitize_text_field( wp_unslash( $_POST['mode'] ?? 'html' ) );
	if ( '' === $url ) {
		wp_send_json_error( array( 'message' => 'url mancante' ), 400 );
	}

	$target = remarka_tool_target_url( $url, $mode );
	if ( empty( $target['ok'] ) ) {
		wp_send_json_error( array( 'message' => $target['error'] ), 400 );
	}

	$result = remarka_tool_safe_fetch( $target['url'] );
	if ( empty( $result['ok'] ) ) {
		wp_send_json_error( array( 'message' => $result['error'], 'status' => $result['status'] ), 200 );
	}

	wp_send_json_success( array(
		'ok'     => true,
		'status' => $result['status'],
		'body'   => $result['body'],
	) );
}
add_action( 'wp_ajax_remarka_tool_fetch', 'remarka_tool_fetch_handler' );
add_action( 'wp_ajax_nopriv_remarka_tool_fetch', 'remarka_tool_fetch_handler' );

/**
 * Proxy server-side per Google PageSpeed Insights.
 *
 * Perché esiste: dal browser la chiamata diretta a googleapis.com può fallire
 * in modo sistematico (CSP dell'hosting, estensioni, restrizioni della chiave
 * API legate al referrer); dal server passa sempre, e la chiave resta lato
 * PHP invece di essere esposta nel sorgente della pagina. Il JS prova prima
 * la via diretta e ripiega qui (vedi psiFetch in remarka.js).
 * Cache: transient 10 minuti per url+categorie+lingua — le ripetizioni di uno
 * stesso test non consumano quota. Rate-limit separato da tool_fetch.
 */
function remarka_tool_psi_handler(): void {
	if ( ! isset( $_GET['nonce'] ) || ! wp_verify_nonce( sanitize_key( $_GET['nonce'] ), 'remarka_tools' ) ) {
		wp_send_json_error( array( 'message' => 'sessione scaduta' ), 403 );
	}

	$ip    = isset( $_SERVER['REMOTE_ADDR'] ) ? sanitize_text_field( wp_unslash( $_SERVER['REMOTE_ADDR'] ) ) : '';
	$rl    = 'remarka_psi_' . md5( $ip );
	$count = (int) get_transient( $rl );
	if ( $count >= 8 ) {
		wp_send_json_error( array( 'message' => 'troppe richieste, riprovate tra un minuto' ), 429 );
	}
	set_transient( $rl, $count + 1, MINUTE_IN_SECONDS );

	$url = esc_url_raw( wp_unslash( $_GET['url'] ?? '' ) );
	if ( '' === $url || ! preg_match( '#^https?://#i', $url ) ) {
		wp_send_json_error( array( 'message' => 'url non valido' ), 400 );
	}

	$allowed = array( 'PERFORMANCE', 'ACCESSIBILITY', 'SEO', 'BEST_PRACTICES' );
	$cats    = array_values( array_intersect(
		array_map( 'strtoupper', array_map( 'trim', explode( ',', sanitize_text_field( wp_unslash( $_GET['categories'] ?? '' ) ) ) ) ),
		$allowed
	) );
	if ( ! $cats ) {
		$cats = $allowed;
	}

	$locale = sanitize_key( wp_unslash( $_GET['locale'] ?? 'it' ) );
	if ( ! in_array( $locale, array( 'it', 'en', 'ru' ), true ) ) {
		$locale = 'it';
	}

	$cache_key = 'remarka_psic_' . md5( $url . '|' . implode( ',', $cats ) . '|' . $locale );
	$cached    = get_transient( $cache_key );
	if ( false !== $cached ) {
		header( 'Content-Type: application/json; charset=utf-8' );
		echo $cached; // phpcs:ignore WordPress.Security.EscapeOutput -- JSON già validato alla scrittura in cache.
		wp_die();
	}

	$endpoint = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=' . rawurlencode( $url )
		. '&strategy=mobile&locale=' . rawurlencode( $locale );
	foreach ( $cats as $c ) {
		$endpoint .= '&category=' . $c;
	}
	$psi_key = get_theme_mod( 'remarka_psi_api_key', '' );
	if ( $psi_key ) {
		$endpoint .= '&key=' . rawurlencode( $psi_key );
	}

	if ( function_exists( 'set_time_limit' ) ) {
		@set_time_limit( 90 );
	}
	$resp = wp_remote_get( $endpoint, array( 'timeout' => 55 ) );
	if ( is_wp_error( $resp ) ) {
		wp_send_json_error( array( 'message' => 'psi non raggiungibile: ' . $resp->get_error_message() ), 502 );
	}
	$code = (int) wp_remote_retrieve_response_code( $resp );
	$body = wp_remote_retrieve_body( $resp );
	if ( 200 !== $code || '' === $body ) {
		// Il corpo d'errore di Google contiene il motivo (chiave/quota): lo
		// passiamo nel log del server, al client solo lo stato.
		error_log( 'remarka_tool_psi: upstream HTTP ' . $code . ' — ' . substr( (string) $body, 0, 300 ) );
		wp_send_json_error( array( 'message' => 'psi upstream ' . $code ), 502 );
	}
	$decoded = json_decode( $body );
	if ( null === $decoded || empty( $decoded->lighthouseResult ) ) {
		wp_send_json_error( array( 'message' => 'psi risposta non valida' ), 502 );
	}
	if ( strlen( $body ) < 3 * MB_IN_BYTES ) {
		set_transient( $cache_key, $body, 10 * MINUTE_IN_SECONDS );
	}
	header( 'Content-Type: application/json; charset=utf-8' );
	echo $body; // phpcs:ignore WordPress.Security.EscapeOutput -- passthrough JSON di Google, decodificato e validato sopra.
	wp_die();
}
add_action( 'wp_ajax_remarka_tool_psi', 'remarka_tool_psi_handler' );
add_action( 'wp_ajax_nopriv_remarka_tool_psi', 'remarka_tool_psi_handler' );

add_action( 'admin_post_nopriv_remarka_contact', 'remarka_form_handle_post' );

/* ============================================================================
 * Check-up completo — CPT lead + endpoint report PDF (M3).
 * ========================================================================== */

/**
 * CPT privato: base dei lead del check-up. Non pubblico (`public => false`),
 * niente archivio/rewrite, visibile solo in admin a chi ha `manage_options`
 * (stesso ruolo del titolare). Cancellare un lead dalla lista WP lo elimina
 * per sempre — post + tutti i suoi post_meta — il che *è* la cancellazione
 * GDPR su richiesta dell'interessato: nessun soft-delete nascosto altrove.
 */
function remarka_register_sr_lead_cpt(): void {
	register_post_type(
		'sr_lead',
		array(
			'labels'           => array(
				'name'          => 'Lead check-up',
				'singular_name' => 'Lead check-up',
				'menu_name'     => 'Lead check-up',
				'add_new_item'  => 'Nuovo lead',
				'edit_item'     => 'Lead check-up',
				'search_items'  => 'Cerca lead',
				'not_found'     => 'Nessun lead trovato',
			),
			'public'           => false,
			'show_ui'          => true,
			'show_in_menu'     => true,
			'show_in_rest'     => false,
			'menu_icon'        => 'dashicons-clipboard',
			'capability_type'  => 'page',
			'capabilities'     => array(
				'edit_post'          => 'manage_options',
				'read_post'          => 'manage_options',
				'delete_post'        => 'manage_options',
				'edit_posts'         => 'manage_options',
				'edit_others_posts'  => 'manage_options',
				'publish_posts'      => 'manage_options',
				'read_private_posts' => 'manage_options',
				'delete_posts'       => 'manage_options',
			),
			'map_meta_cap'     => true,
			'supports'         => array( 'title' ),
			'has_archive'      => false,
			'rewrite'          => false,
			'exclude_from_search' => true,
		)
	);
}
add_action( 'init', 'remarka_register_sr_lead_cpt' );

/** Colonne della lista lead in admin: Email · Sito · Punteggio · Lingua · Monitoraggio · Data. */
function remarka_sr_lead_columns( array $columns ): array {
	$new           = array();
	$new['cb']     = $columns['cb'] ?? '';
	$new['title']  = 'Email';
	$new['sr_url'] = 'Sito';
	$new['sr_score']      = 'Punteggio';
	$new['sr_locale']     = 'Lingua';
	$new['sr_monitoring'] = 'Monitoraggio';
	$new['date']          = $columns['date'] ?? 'Data';
	return $new;
}
add_filter( 'manage_edit-sr_lead_columns', 'remarka_sr_lead_columns' );

function remarka_sr_lead_column_content( string $column, int $post_id ): void {
	switch ( $column ) {
		case 'sr_url':
			echo esc_html( (string) get_post_meta( $post_id, 'sr_url', true ) );
			break;
		case 'sr_score':
			$score = get_post_meta( $post_id, 'sr_composite', true );
			echo '' === $score ? '—' : esc_html( $score . '/100' );
			break;
		case 'sr_locale':
			echo esc_html( strtoupper( (string) get_post_meta( $post_id, 'sr_locale', true ) ) );
			break;
		case 'sr_monitoring':
			echo get_post_meta( $post_id, 'sr_consent_monthly', true ) ? '✓' : '—';
			break;
	}
}
add_action( 'manage_sr_lead_posts_custom_column', 'remarka_sr_lead_column_content', 10, 2 );

/** Assicura un index.php-заглушка nella cartella upload dei report (niente directory listing). */
function remarka_checkup_reports_dir_guard( string $dir ): void {
	$index = trailingslashit( $dir ) . 'index.php';
	if ( ! file_exists( $index ) ) {
		file_put_contents( $index, "<?php\n// Silence is golden.\n" ); // phpcs:ignore WordPress.WP.AlternativeFunctions.file_system_read_file_put_contents
	}
}

/** Salva il lead nel CPT dopo l'invio riuscito del report PDF. */
function remarka_checkup_save_lead( string $email, array $data, array $comp, bool $consent_monthly ): void {
	$post_id = wp_insert_post(
		array(
			'post_type'   => 'sr_lead',
			'post_title'  => $email . ' — ' . date_i18n( 'd.m.Y H:i' ),
			'post_status' => 'publish',
		),
		true
	);
	if ( is_wp_error( $post_id ) || ! $post_id ) {
		return;
	}
	update_post_meta( $post_id, 'sr_email', $email );
	update_post_meta( $post_id, 'sr_url', $data['url'] );
	update_post_meta( $post_id, 'sr_composite', $comp['composite'] );
	update_post_meta( $post_id, 'sr_locale', $data['locale'] );
	update_post_meta( $post_id, 'sr_consent_monthly', $consent_monthly ? 1 : 0 );
}

/** Whitelist delle 7 chiavi punteggio ammesse nel payload JSON del client. */
function remarka_checkup_score_keys(): array {
	return array( 'perf', 'seo', 'a11y', 'gdpr', 'bp', 'ai', 'co2' );
}

/**
 * Sanifica i rilievi individuali (M5, docs/piano-checkup-sito.md) — stessi
 * cap del client (§ CHECKUP_FINDING_LABELS/buildCheckupFindings in remarka.js),
 * riverificati qui perché il client non è fidato: whitelist delle 7 chiavi di
 * dimensione, max 4 gruppi per dimensione, max 3 item per gruppo, ogni
 * stringa passata da wp_strip_all_tags() + troncata, ogni url validato con
 * esc_url_raw() solo http/https (altrimenti scartato, non l'intero gruppo).
 * Un gruppo senza titolo e senza item validi viene scartato: non produce
 * righe vuote nel PDF.
 */
function remarka_tool_report_sanitize_findings( $raw ): array {
	$out = array();
	foreach ( remarka_checkup_score_keys() as $dim_key ) {
		$out[ $dim_key ] = array();
	}
	if ( ! is_array( $raw ) ) {
		return $out;
	}
	foreach ( remarka_checkup_score_keys() as $dim_key ) {
		$groups_in = is_array( $raw[ $dim_key ] ?? null ) ? $raw[ $dim_key ] : array();
		$groups    = array();
		foreach ( array_slice( $groups_in, 0, 4 ) as $group ) {
			if ( ! is_array( $group ) ) {
				continue;
			}
			$title = is_string( $group['t'] ?? null ) ? mb_substr( wp_strip_all_tags( (string) $group['t'] ), 0, 200 ) : '';

			$items_in = is_array( $group['items'] ?? null ) ? $group['items'] : array();
			$items    = array();
			foreach ( array_slice( $items_in, 0, 3 ) as $item ) {
				if ( ! is_array( $item ) ) {
					continue;
				}
				$u_raw = is_string( $item['u'] ?? null ) ? mb_substr( (string) $item['u'], 0, 300 ) : '';
				$u     = '' !== $u_raw ? esc_url_raw( $u_raw, array( 'http', 'https' ) ) : '';
				$v     = is_string( $item['v'] ?? null ) ? mb_substr( wp_strip_all_tags( (string) $item['v'] ), 0, 200 ) : '';
				if ( '' === $u && '' === $v ) {
					continue;
				}
				$items[] = array(
					'u' => $u,
					'v' => $v,
				);
			}

			if ( '' === $title && empty( $items ) ) {
				continue;
			}
			$groups[] = array(
				't'     => $title,
				'items' => $items,
			);
		}
		$out[ $dim_key ] = $groups;
	}
	return $out;
}

/**
 * Sanifica il payload JSON mandato dal client — cappato a 64KB già lato JS,
 * ma qui riverificato server-side perché non ci si fida mai del client:
 * whitelist delle chiavi, punteggi clampati a interi 0-100 (o null se
 * mancanti/non numerici — stessa semantica "N/D" del client), url ristretto
 * a http/https, locale whitelisted it|en|ru (fallback it), rilievi
 * individuali (M5) sanificati da remarka_tool_report_sanitize_findings().
 * `composite` e `measured` mandati dal client sono ignorati: si ricalcolano
 * sempre da `scores` in remarka_checkup_composite(), per coerenza interna
 * del PDF.
 */
function remarka_tool_report_sanitize_payload( string $raw ): ?array {
	if ( strlen( $raw ) > 65536 ) {
		return null;
	}
	$decoded = json_decode( $raw, true );
	if ( ! is_array( $decoded ) ) {
		return null;
	}

	$url_raw = is_string( $decoded['url'] ?? null ) ? $decoded['url'] : '';
	$url     = esc_url_raw( $url_raw, array( 'http', 'https' ) );
	if ( '' === $url || ! preg_match( '#^https?://[^/]+#i', $url ) ) {
		return null;
	}

	$locale = sanitize_key( (string) ( $decoded['locale'] ?? '' ) );
	if ( ! in_array( $locale, array( 'it', 'en', 'ru' ), true ) ) {
		$locale = 'it';
	}

	$scores_in = is_array( $decoded['scores'] ?? null ) ? $decoded['scores'] : array();
	$scores    = array();
	foreach ( remarka_checkup_score_keys() as $dim_key ) {
		$val = $scores_in[ $dim_key ] ?? null;
		if ( is_numeric( $val ) ) {
			$scores[ $dim_key ] = (int) max( 0, min( 100, round( (float) $val ) ) );
		} else {
			$scores[ $dim_key ] = null;
		}
	}

	return array(
		'url'      => $url,
		'locale'   => $locale,
		'scores'   => $scores,
		'findings' => remarka_tool_report_sanitize_findings( $decoded['findings'] ?? null ),
	);
}

/**
 * Handler AJAX `remarka_tool_report`: invia il report PDF via e-mail.
 * Ordine dei controlli (non negoziabile): nonce → honeypot (successo muto,
 * niente PDF/lead) → rate-limit IP (3/ora, transient separato da tool_fetch)
 * → e-mail valida + consenso obbligatorio → payload sanificato → PDF →
 * wp_mail con allegato → lead nel CPT sr_lead. Ogni uscita è JSON con un
 * `code` macchina-leggibile; i testi di successo/errore li rende il JS (M2).
 */
function remarka_tool_report_handler(): void {
	if ( ! isset( $_POST['nonce'] ) || ! wp_verify_nonce( sanitize_key( $_POST['nonce'] ), 'remarka_tools' ) ) {
		wp_send_json_error( array( 'message' => 'sessione scaduta', 'code' => 'nonce' ), 403 );
	}

	if ( ! empty( $_POST['sr_checkup_hp'] ) ) { // honeypot: i bot lo compilano, le persone no.
		wp_send_json_success( array( 'ok' => true ) );
	}

	$ip    = isset( $_SERVER['REMOTE_ADDR'] ) ? sanitize_text_field( wp_unslash( $_SERVER['REMOTE_ADDR'] ) ) : '';
	$key   = 'remarka_rpt_' . md5( $ip );
	$count = (int) get_transient( $key );
	if ( $count >= 3 ) {
		wp_send_json_error( array( 'message' => 'troppe richieste, riprovate tra un\'ora', 'code' => 'rate_limit' ), 429 );
	}
	set_transient( $key, $count + 1, HOUR_IN_SECONDS );

	$email = sanitize_email( wp_unslash( $_POST['email'] ?? '' ) );
	if ( '' === $email || ! is_email( $email ) ) {
		wp_send_json_error( array( 'message' => 'email non valida', 'code' => 'invalid_email' ), 400 );
	}
	if ( empty( $_POST['consent'] ) ) {
		wp_send_json_error( array( 'message' => 'consenso mancante', 'code' => 'consent_required' ), 400 );
	}
	$consent_monthly = ! empty( $_POST['consent_monthly'] );

	$raw = wp_unslash( $_POST['payload'] ?? '' );
	$data = is_string( $raw ) && '' !== $raw ? remarka_tool_report_sanitize_payload( $raw ) : null;
	if ( null === $data ) {
		wp_send_json_error( array( 'message' => 'payload non valido', 'code' => 'invalid_payload' ), 400 );
	}

	$missing_ext = remarka_checkup_pdf_missing_extensions();
	if ( ! empty( $missing_ext ) ) {
		wp_send_json_error( array( 'message' => 'servizio PDF non disponibile', 'code' => 'pdf_unavailable' ), 500 );
	}

	$data['consent_monthly'] = $consent_monthly;
	$data['date_display']    = date_i18n( 'd.m.Y' );

	$pdf = remarka_checkup_render_pdf( $data, $data['locale'] );
	if ( null === $pdf || '' === $pdf ) {
		wp_send_json_error( array( 'message' => 'generazione PDF fallita', 'code' => 'pdf_failed' ), 500 );
	}

	$domain = preg_replace( '#^https?://#i', '', $data['url'] );
	$domain = rtrim( (string) $domain, '/' );

	$upload_dir = wp_upload_dir();
	$dir        = trailingslashit( $upload_dir['basedir'] ) . 'checkup-reports';
	wp_mkdir_p( $dir );
	remarka_checkup_reports_dir_guard( $dir );

	$path = trailingslashit( $dir ) . 'checkup-' . wp_generate_password( 16, false, false ) . '.pdf';
	if ( false === file_put_contents( $path, $pdf ) ) { // phpcs:ignore WordPress.WP.AlternativeFunctions.file_system_read_file_put_contents
		wp_send_json_error( array( 'message' => 'salvataggio PDF fallito', 'code' => 'pdf_write_failed' ), 500 );
	}

	$comp    = remarka_checkup_composite( $data['scores'] );
	$subject = remarka_checkup_email_subject( $data['locale'], $domain );
	$body    = remarka_checkup_email_body( $data['locale'], $domain, $comp['composite'] );
	$headers = array( 'Reply-To: ' . remarka_form_recipient() );

	$ok = wp_mail( $email, $subject, $body, $headers, array( $path ) );

	if ( file_exists( $path ) ) {
		wp_delete_file( $path );
	}

	if ( ! $ok ) {
		wp_send_json_error( array( 'message' => 'invio fallito', 'code' => 'mail_failed' ), 500 );
	}

	remarka_checkup_save_lead( $email, $data, $comp, $consent_monthly );

	wp_send_json_success( array( 'ok' => true ) );
}
add_action( 'wp_ajax_remarka_tool_report', 'remarka_tool_report_handler' );
add_action( 'wp_ajax_nopriv_remarka_tool_report', 'remarka_tool_report_handler' );

/* ---------- llms.txt: indice testuale per i crawler AI ----------
 * Proposta emergente llmstxt.org: un indice Markdown del sito, che i
 * crawler dei modelli AI (ChatGPT, Perplexity, Claude…) leggono più
 * volentieri dell'HTML o di una sitemap XML. La nostra card "Pronto per
 * l'AI" del check-up (generate_pages.py::_CHECKUP_DIMS, chiave 'ai') lo
 * misura fra i quattro segnali tecnici — un check-up su remarka.biz stesso
 * lo segnalava mancante (15-07-2026). Contenuto assemblato dai dati reali
 * del tema (remarka_company_lang_data(), remarka_str(), percorsi di
 * inc/lang-map.php): nessun testo inventato. Serve un
 * `wp rewrite flush` dopo il deploy perché la regola è nuova. */
function remarka_llms_txt_rewrite(): void {
	add_rewrite_rule( '^llms\.txt$', 'index.php?remarka_llms_txt=1', 'top' );
}
add_action( 'init', 'remarka_llms_txt_rewrite' );

function remarka_llms_txt_query_vars( array $vars ): array {
	$vars[] = 'remarka_llms_txt';
	return $vars;
}
add_filter( 'query_vars', 'remarka_llms_txt_query_vars' );

/** Corpo del file, separato dall'handler HTTP per poterlo testare senza stubbare l'output. */
function remarka_llms_txt_content(): string {
	$company = remarka_company_lang_data();
	$lines   = array(
		'# Studio Remarka',
		'',
		'> ' . remarka_str( 'footer_tagline' ),
		'',
		'## Servizi',
		'- [Servizi](' . home_url( '/servizi/' ) . ')',
		'- [Siti aziendali](' . home_url( '/servizi/siti-aziendali/' ) . ')',
		'- [E-commerce](' . home_url( '/servizi/e-commerce/' ) . ')',
		'',
		'## Prezzi',
		'- [Prezzi e tempi](' . home_url( '/prezzi/' ) . ')',
		'',
		'## Strumenti gratuiti',
		'- [Check-up completo del sito](' . home_url( '/strumenti/check-up-completo/' ) . ')',
		'- [Tutti gli strumenti](' . home_url( '/strumenti/' ) . ')',
		'',
		'## Casi studio',
		'- [Casi studio](' . home_url( '/casi-studio/' ) . ')',
		'',
		'## Blog',
		'- [Blog](' . home_url( '/blog/' ) . ')',
		'',
		'## Contatti',
		'- [' . $company['name'] . '](' . home_url( '/#contatti' ) . ') — ' . $company['email'],
		'',
		'## Languages',
		'- [English](' . home_url( '/en/' ) . ')',
		'- [Русский](' . home_url( '/ru/' ) . ')',
	);
	return implode( "\n", $lines ) . "\n";
}

function remarka_llms_txt_output(): void {
	if ( ! get_query_var( 'remarka_llms_txt' ) ) {
		return;
	}
	header( 'Content-Type: text/plain; charset=utf-8' );
	echo remarka_llms_txt_content(); // phpcs:ignore WordPress.Security.EscapeOutput -- Markdown statico dal tema, nessun input utente.
	exit;
}
add_action( 'template_redirect', 'remarka_llms_txt_output' );

/* ---------- /sitemap.xml → wp-sitemap.xml (o sitemap_index.xml con Rank Math) ----------
 * WordPress core pubblica la sitemap XML su wp-sitemap.xml (dalla 5.5); le
 * verifiche automatiche — la nostra card "Pronto per l'AI" inclusa, e i
 * crawler AI in generale — cercano per convenzione /sitemap.xml, che sul
 * core resta un 404. Se Rank Math è attivo con il modulo Sitemap, la sua
 * sitemap vive su sitemap_index.xml e va rispettata: qui NON la
 * sovrascriviamo, redirigiamo lì invece che su wp-sitemap.xml. Nessuna
 * regola di rewrite: come remarka_redirect_legacy_flat_urls(), si aggancia
 * al percorso corrente su template_redirect, valido anche per URL che non
 * corrispondono a nessun contenuto WordPress. */
function remarka_rank_math_sitemap_active(): bool {
	if ( function_exists( 'rank_math_is_module_active' ) ) {
		return (bool) rank_math_is_module_active( 'sitemap' );
	}
	// Rank Math presente ma il modulo non è verificabile (helper non
	// caricato ancora): il Sitemap è abilitato di default, meglio assumerlo
	// attivo che rischiare due sitemap in conflitto.
	return defined( 'RANK_MATH_VERSION' );
}

function remarka_sitemap_redirect(): void {
	if ( 'sitemap.xml' !== strtolower( remarka_current_path() ) ) {
		return;
	}
	$target = remarka_rank_math_sitemap_active() ? 'sitemap_index.xml' : 'wp-sitemap.xml';
	wp_safe_redirect( home_url( '/' . $target ), 301 );
	exit;
}
add_action( 'template_redirect', 'remarka_sitemap_redirect', 1 );
