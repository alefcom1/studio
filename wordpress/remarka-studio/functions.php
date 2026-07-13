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
	$dir = get_stylesheet_directory() . '/patterns/pages';
	if ( ! is_dir( $dir ) ) {
		return;
	}
	foreach ( glob( $dir . '/*.php' ) as $file ) {
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
 * Cookie banner (GDPR, Rifiuta = Accetta по весу) и WhatsApp FAB —
 * сайтвайд, без необходимости вставлять паттерн на каждую страницу.
 * Номер WhatsApp настраивается через customizer (remarka_whatsapp_number)
 * или константу REMARKA_WHATSAPP_NUMBER; заглушка — 390000000000.
 */
function remarka_whatsapp_number(): string {
	if ( defined( 'REMARKA_WHATSAPP_NUMBER' ) ) {
		return REMARKA_WHATSAPP_NUMBER;
	}
	$opt = get_theme_mod( 'remarka_whatsapp_number', '' );
	return $opt ? $opt : '390000000000';
}

function remarka_footer_widgets(): void {
	$phone = esc_attr( remarka_whatsapp_number() );
	?>
	<div class="sr-cookie-banner" data-sr-cookie-banner hidden>
		<div class="sr-cookie-banner__inner">
			<p class="sr-cookie-banner__text">
				<?php esc_html_e( "Usiamo solo cookie tecnici necessari al funzionamento del sito. Nessuna profilazione, nessun tracciamento pubblicitario.", 'remarka-studio' ); ?>
				<a href="<?php echo esc_url( home_url( '/cookie-preferenze/' ) ); ?>"><?php esc_html_e( 'Preferenze', 'remarka-studio' ); ?></a>
				·
				<a href="<?php echo esc_url( home_url( '/cookie-policy/' ) ); ?>"><?php esc_html_e( 'Cookie policy', 'remarka-studio' ); ?></a>
			</p>
			<div class="sr-cookie-banner__actions">
				<button type="button" class="sr-cookie-btn" data-sr-cookie-choice="rejected"><?php esc_html_e( 'Rifiuta', 'remarka-studio' ); ?></button>
				<button type="button" class="sr-cookie-btn" data-sr-cookie-choice="accepted"><?php esc_html_e( 'Accetta', 'remarka-studio' ); ?></button>
			</div>
		</div>
	</div>
	<a href="https://wa.me/<?php echo $phone; ?>" class="sr-wa-fab" data-sr-wa-fab target="_blank" rel="noopener noreferrer" aria-label="<?php esc_attr_e( 'Scrivici su WhatsApp', 'remarka-studio' ); ?>">
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
		'remarka_company_address'       => array( 'section' => 'remarka_contatti', 'label' => 'Indirizzo (usare Invio per andare a capo)', 'type' => 'textarea', 'default' => "Via Andrea Solari 43\n20144 Milano (MI)" ),
		'remarka_company_piva'          => array( 'section' => 'remarka_contatti', 'label' => 'Partita IVA', 'type' => 'text', 'default' => 'IT 01234567890' ),
		'remarka_company_pec'           => array( 'section' => 'remarka_contatti', 'label' => 'PEC', 'type' => 'text', 'default' => 'studioremarka@pec.it' ),
		'remarka_company_email'         => array( 'section' => 'remarka_contatti', 'label' => 'Email di contatto', 'type' => 'email', 'default' => 'info@studioremarka.it' ),
		'remarka_company_phone'         => array( 'section' => 'remarka_contatti', 'label' => 'Telefono', 'type' => 'text', 'default' => '+39 02 8736 5412' ),
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
		'default'           => '390000000000',
		'sanitize_callback' => 'sanitize_text_field',
	) );
	$wp_customize->add_control( 'remarka_whatsapp_number', array(
		'label'   => __( 'Numero WhatsApp Business (solo cifre, con prefisso 39...)', 'remarka-studio' ),
		'section' => 'remarka_contatti',
		'type'    => 'text',
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

function remarka_render_footer(): void {
	$score = (int) get_theme_mod( 'remarka_footer_pagespeed_score', 95 );
	?>
	<footer class="sr-footer">
		<div class="sr-footer-cta">
			<div class="sr-footer-cta__inner">
				<div>
					<h2 class="sr-footer-cta__heading"><?php echo esc_html( remarka_footer_mod( 'remarka_footer_cta_heading' ) ); ?><span class="sr-accent-dot">.</span></h2>
					<p class="sr-footer-cta__text"><?php echo esc_html( remarka_footer_mod( 'remarka_footer_cta_text' ) ); ?></p>
				</div>
				<div class="sr-footer-cta__buttons">
					<a class="sr-footer-cta__btn sr-footer-cta__btn--primary" href="<?php echo esc_url( remarka_footer_link_url( 'remarka_footer_cta_btn1_url', '/#contatti' ) ); ?>"><?php echo esc_html( remarka_footer_mod( 'remarka_footer_cta_btn1_label' ) ); ?></a>
					<a class="sr-footer-cta__btn sr-footer-cta__btn--outline" href="<?php echo esc_url( remarka_footer_link_url( 'remarka_footer_cta_btn2_url', '/' ) ); ?>"><?php echo esc_html( remarka_footer_mod( 'remarka_footer_cta_btn2_label' ) ); ?></a>
				</div>
			</div>
		</div>

		<div class="sr-footer-main">
			<div class="sr-footer-main__inner">
				<div class="sr-footer-col sr-footer-col--brand">
					<div class="sr-footer-logo"><?php the_custom_logo(); ?><span><?php bloginfo( 'name' ); ?></span></div>
					<p><?php echo esc_html( remarka_footer_mod( 'remarka_footer_tagline' ) ); ?></p>
				</div>

				<div class="sr-footer-col">
					<p class="sr-footer-col__title"><?php esc_html_e( 'Pagine', 'remarka-studio' ); ?></p>
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
					<p class="sr-footer-col__title"><?php esc_html_e( 'Studio', 'remarka-studio' ); ?></p>
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
					<p class="sr-footer-col__title"><?php esc_html_e( 'Dati societari', 'remarka-studio' ); ?></p>
					<p class="sr-footer-company">
						<strong><?php echo esc_html( remarka_footer_mod( 'remarka_company_name' ) ); ?></strong><br>
						<?php echo nl2br( esc_html( remarka_footer_mod( 'remarka_company_address' ) ) ); ?>
					</p>
					<p class="sr-mono">P.IVA <?php echo esc_html( remarka_footer_mod( 'remarka_company_piva' ) ); ?></p>
					<p>PEC <?php echo esc_html( remarka_footer_mod( 'remarka_company_pec' ) ); ?></p>
					<p><a href="mailto:<?php echo esc_attr( remarka_footer_mod( 'remarka_company_email' ) ); ?>"><?php echo esc_html( remarka_footer_mod( 'remarka_company_email' ) ); ?></a></p>
					<p><?php echo esc_html( remarka_footer_mod( 'remarka_company_phone' ) ); ?></p>
				</div>
			</div>
		</div>

		<div class="sr-footer-bottom">
			<div class="sr-footer-bottom__inner">
				<div class="sr-barra sr-barra--h4" data-sr-target="<?php echo esc_attr( $score ); ?>%" aria-hidden="true"><div class="sr-barra__fill"></div></div>
				<div class="sr-footer-bottom__row">
					<span>&copy; <?php echo esc_html( gmdate( 'Y' ) ); ?> <?php echo esc_html( remarka_footer_mod( 'remarka_company_name' ) ); ?> — <?php esc_html_e( 'Tutti i diritti riservati', 'remarka-studio' ); ?></span>
					<span class="sr-footer-score"><?php esc_html_e( 'Punteggio PageSpeed medio', 'remarka-studio' ); ?>: <b><?php echo esc_html( $score ); ?></b>/100</span>
				</div>
			</div>
		</div>
	</footer>
	<?php
}
add_action( 'wp_footer', 'remarka_render_footer', 5 );

/**
 * Класс автоматически на пункт меню «Preventivo…»: владельцу не нужно
 * вручную ставить CSS-класс sr-menu-cta в настройках меню (см. #masthead
 * .sr-menu-cta > a в remarka.css).
 */
function remarka_auto_cta_menu_item_class( array $classes, WP_Post $item ): array {
	if ( false !== stripos( $item->title, 'Preventivo' ) ) {
		$classes[] = 'sr-menu-cta';
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
	if ( ! is_front_page() ) {
		return;
	}
	$schema = array(
		'@context' => 'https://schema.org',
		'@type'    => 'ProfessionalService',
		'name'     => 'Studio Remarka',
		'url'      => home_url( '/' ),
		'areaServed' => 'IT',
		'priceRange' => '€€',
	);
	echo '<script type="application/ld+json">' . wp_json_encode( $schema ) . '</script>' . "\n";
}
add_action( 'wp_head', 'remarka_organization_schema' );
