<?php
/**
 * Mega-menu della barra principale (#masthead).
 *
 * Il sito è cresciuto: 9 servizi, 12 strumenti + Monitor, decine di articoli.
 * Due voci — «Servizi» e «Strumenti» — aprono un pannello a tendina che
 * raggruppa le sottopagine, invece di costringere l'utente a entrare
 * nell'indice e scorrere.
 *
 * Meccanica NON invasiva: non sostituiamo il menu (la CTA, lo switch lingua e
 * il layout dell'header di Prespa restano intatti). Due filtri arricchiscono
 * SOLO le due voci:
 *   - nav_menu_css_class    → aggiunge la classe .sr-has-mega alla <li>;
 *   - walker_nav_menu_start_el → appende il pannello dopo il link.
 * I filtri agganciano la voce per suffisso URL, così funzionano su tutti e tre
 * i menu localizzati (servizi|services|uslugi, strumenti|tools|instrumenty).
 * Il contenuto del pannello è localizzato via remarka_current_lang().
 *
 * @package remarka-studio
 */

defined( 'ABSPATH' ) || exit;

/** Lingua corrente, con fallback a 'it'. */
function remarka_mega_lang(): string {
	$l = function_exists( 'remarka_current_lang' ) ? remarka_current_lang() : 'it';
	return in_array( $l, array( 'it', 'en', 'ru' ), true ) ? $l : 'it';
}

/**
 * Dati del mega-menu per la lingua corrente.
 * Ritorna array( 'servizi' => [...], 'lab' => [...] ).
 */
function remarka_mega_data(): array {
	$lang = remarka_mega_lang();

	// ── Etichette UI localizzate ──────────────────────────────────────────────
	$t = array(
		'it' => array(
			'creare' => 'Creare', 'crescere' => 'Crescere', 'sistemare' => 'Sistemare',
			'all_serv' => 'Tutti i servizi', 'prezzi' => 'Prezzi', 'casi' => 'Casi studio',
			'serv_feat_k' => 'Non sapete da dove partire?',
			'serv_feat_t' => 'Analisi gratuita + preventivo in 24 ore',
			'serv_feat_cta' => 'Parliamone',
			'tools_free' => 'Strumenti gratuiti', 'perf' => 'Prestazioni',
			'conf' => 'Conformità', 'ai' => 'AI', 'mercati' => 'Mercati',
			'all_tools' => 'Tutti i 12 strumenti',
			'checkup_k' => 'In evidenza · gratuito', 'checkup_t' => 'Check-up completo',
			'checkup_d' => 'Sette misure del sito in un minuto.',
			'mon_k' => 'Remarka Lab · Monitor', 'mon_t' => 'Un sito sotto controllo, gratis',
			'mon_live' => 'Guarda il nostro sito in diretta', 'mon_cta' => 'Prova gratis',
		),
		'en' => array(
			'creare' => 'Build', 'crescere' => 'Grow', 'sistemare' => 'Fix',
			'all_serv' => 'All services', 'prezzi' => 'Pricing', 'casi' => 'Case studies',
			'serv_feat_k' => 'Not sure where to start?',
			'serv_feat_t' => 'Free review + a quote within 24 hours',
			'serv_feat_cta' => 'Let’s talk',
			'tools_free' => 'Free tools', 'perf' => 'Performance',
			'conf' => 'Compliance', 'ai' => 'AI', 'mercati' => 'Markets',
			'all_tools' => 'All 12 tools',
			'checkup_k' => 'Featured · free', 'checkup_t' => 'Full site check-up',
			'checkup_d' => 'Seven site measures in one minute.',
			'mon_k' => 'Remarka Lab · Monitor', 'mon_t' => 'One site under watch, free',
			'mon_live' => 'See our site live', 'mon_cta' => 'Try it free',
		),
		'ru' => array(
			'creare' => 'Создать', 'crescere' => 'Расти', 'sistemare' => 'Исправить',
			'all_serv' => 'Все услуги', 'prezzi' => 'Цены', 'casi' => 'Кейсы',
			'serv_feat_k' => 'Не знаете, с чего начать?',
			'serv_feat_t' => 'Бесплатный анализ + смета за 24 часа',
			'serv_feat_cta' => 'Обсудим',
			'tools_free' => 'Бесплатные инструменты', 'perf' => 'Скорость',
			'conf' => 'Соответствие', 'ai' => 'ИИ', 'mercati' => 'Рынки',
			'all_tools' => 'Все 12 инструментов',
			'checkup_k' => 'В центре · бесплатно', 'checkup_t' => 'Полная проверка сайта',
			'checkup_d' => 'Семь замеров сайта за минуту.',
			'mon_k' => 'Remarka Lab · Monitor', 'mon_t' => 'Один сайт под контролем, бесплатно',
			'mon_live' => 'Наш сайт вживую', 'mon_cta' => 'Попробовать',
		),
	);
	$s = $t[ $lang ];

	// ── URL localizzate (generate da lang.py) + etichette voce ────────────────
	$serv_url = array(
		'it' => array( 'siti-aziendali' => '/servizi/siti-aziendali/', 'e-commerce' => '/servizi/e-commerce/', 'web-app' => '/servizi/web-app/', 'siti-pwa' => '/servizi/siti-pwa/', 'seo-tecnica' => '/servizi/seo-tecnica/', 'siti-multilingue' => '/servizi/siti-multilingue/', 'export-ready' => '/servizi/export-ready/', 'restyling-migrazione' => '/servizi/restyling-migrazione/', 'adeguamento-eaa' => '/servizi/adeguamento-eaa/', 'index' => '/servizi/', 'prezzi' => '/prezzi/', 'casi' => '/casi-studio/', 'contatti' => '/#contatti' ),
		'en' => array( 'siti-aziendali' => '/en/services/business-websites/', 'e-commerce' => '/en/services/e-commerce/', 'web-app' => '/en/services/custom-web-apps/', 'siti-pwa' => '/en/services/progressive-web-apps/', 'seo-tecnica' => '/en/services/technical-seo/', 'siti-multilingue' => '/en/services/multilingual-websites/', 'export-ready' => '/en/services/export-ready/', 'restyling-migrazione' => '/en/services/redesign-migration/', 'adeguamento-eaa' => '/en/services/eaa-compliance/', 'index' => '/en/services/', 'prezzi' => '/en/pricing/', 'casi' => '/en/case-studies/', 'contatti' => '/en/#contatti' ),
		'ru' => array( 'siti-aziendali' => '/ru/uslugi/korporativnye-sajty/', 'e-commerce' => '/ru/uslugi/internet-magaziny/', 'web-app' => '/ru/uslugi/veb-prilozhenija/', 'siti-pwa' => '/ru/uslugi/pwa-sajty/', 'seo-tecnica' => '/ru/uslugi/tehnicheskoe-seo/', 'siti-multilingue' => '/ru/uslugi/mnogojazychnye-sajty/', 'export-ready' => '/ru/uslugi/export-ready/', 'restyling-migrazione' => '/ru/uslugi/redizajn-i-migracija/', 'adeguamento-eaa' => '/ru/uslugi/dostupnost-eaa/', 'index' => '/ru/uslugi/', 'prezzi' => '/ru/ceny/', 'casi' => '/ru/kejsy/', 'contatti' => '/ru/#contatti' ),
	);
	$tool_url = array(
		'it' => array( 'check-up-completo' => '/strumenti/check-up-completo/', 'test-velocita' => '/strumenti/test-velocita/', 'analisi-seo' => '/strumenti/analisi-seo/', 'segnali-eeat' => '/strumenti/segnali-eeat/', 'check-gdpr' => '/strumenti/check-gdpr/', 'verifica-accessibilita' => '/strumenti/verifica-accessibilita/', 'impatto-co2' => '/strumenti/impatto-co2/', 'sito-pronto-ai' => '/strumenti/sito-pronto-ai/', 'sito-letto-dallai' => '/strumenti/sito-letto-dallai/', 'generatore-llms-txt' => '/strumenti/generatore-llms-txt/', 'roi-localizzazione' => '/strumenti/roi-localizzazione/', 'suona-madrelingua' => '/strumenti/suona-madrelingua/', 'index' => '/strumenti/' ),
		'en' => array( 'check-up-completo' => '/en/tools/full-site-checkup/', 'test-velocita' => '/en/tools/speed-test/', 'analisi-seo' => '/en/tools/seo-audit/', 'segnali-eeat' => '/en/tools/eeat-signals/', 'check-gdpr' => '/en/tools/gdpr-check/', 'verifica-accessibilita' => '/en/tools/accessibility-check/', 'impatto-co2' => '/en/tools/website-carbon/', 'sito-pronto-ai' => '/en/tools/ai-readiness/', 'sito-letto-dallai' => '/en/tools/read-by-ai/', 'generatore-llms-txt' => '/en/tools/llms-txt-generator/', 'roi-localizzazione' => '/en/tools/localization-roi/', 'suona-madrelingua' => '/en/tools/does-it-sound-native/', 'index' => '/en/tools/' ),
		'ru' => array( 'check-up-completo' => '/ru/instrumenty/polnaya-proverka-sajta/', 'test-velocita' => '/ru/instrumenty/test-skorosti/', 'analisi-seo' => '/ru/instrumenty/seo-audit/', 'segnali-eeat' => '/ru/instrumenty/signaly-eeat/', 'check-gdpr' => '/ru/instrumenty/proverka-gdpr/', 'verifica-accessibilita' => '/ru/instrumenty/proverka-dostupnosti/', 'impatto-co2' => '/ru/instrumenty/uglerodnyj-sled/', 'sito-pronto-ai' => '/ru/instrumenty/gotovnost-k-ii/', 'sito-letto-dallai' => '/ru/instrumenty/sajt-glazami-ii/', 'generatore-llms-txt' => '/ru/instrumenty/generator-llms-txt/', 'roi-localizzazione' => '/ru/instrumenty/roi-lokalizacii/', 'suona-madrelingua' => '/ru/instrumenty/zvuchit-kak-u-nositelya/', 'index' => '/ru/instrumenty/' ),
	);
	$su = $serv_url[ $lang ];
	$tu = $tool_url[ $lang ];

	// Etichette voce (per servizi e strumenti) localizzate.
	$serv_label = array(
		'it' => array( 'siti-aziendali' => 'Siti aziendali', 'e-commerce' => 'E-commerce', 'web-app' => 'Web app su misura', 'siti-pwa' => 'Siti PWA', 'seo-tecnica' => 'SEO tecnica', 'siti-multilingue' => 'Siti multilingue', 'export-ready' => 'Export-ready', 'restyling-migrazione' => 'Restyling & migrazione', 'adeguamento-eaa' => 'Accessibilità (EAA)' ),
		'en' => array( 'siti-aziendali' => 'Business websites', 'e-commerce' => 'E-commerce', 'web-app' => 'Custom web apps', 'siti-pwa' => 'Progressive web apps', 'seo-tecnica' => 'Technical SEO', 'siti-multilingue' => 'Multilingual websites', 'export-ready' => 'Export-ready', 'restyling-migrazione' => 'Redesign & migration', 'adeguamento-eaa' => 'Accessibility (EAA)' ),
		'ru' => array( 'siti-aziendali' => 'Корпоративные сайты', 'e-commerce' => 'Интернет-магазины', 'web-app' => 'Веб-приложения', 'siti-pwa' => 'PWA-сайты', 'seo-tecnica' => 'Техническое SEO', 'siti-multilingue' => 'Многоязычные сайты', 'export-ready' => 'Export-ready', 'restyling-migrazione' => 'Редизайн и миграция', 'adeguamento-eaa' => 'Доступность (EAA)' ),
	);
	$tool_label = array(
		'it' => array( 'test-velocita' => 'Test velocità', 'analisi-seo' => 'Analisi SEO', 'segnali-eeat' => 'Segnali E-E-A-T', 'check-gdpr' => 'Check GDPR', 'verifica-accessibilita' => 'Accessibilità', 'impatto-co2' => 'Impatto CO₂', 'sito-pronto-ai' => 'Pronto per l’AI', 'sito-letto-dallai' => 'Letto dall’AI', 'generatore-llms-txt' => 'Generatore llms.txt', 'roi-localizzazione' => 'ROI localizzazione', 'suona-madrelingua' => 'Suona madrelingua?' ),
		'en' => array( 'test-velocita' => 'Speed test', 'analisi-seo' => 'SEO audit', 'segnali-eeat' => 'E-E-A-T signals', 'check-gdpr' => 'GDPR check', 'verifica-accessibilita' => 'Accessibility', 'impatto-co2' => 'Website carbon', 'sito-pronto-ai' => 'AI readiness', 'sito-letto-dallai' => 'Read by AI', 'generatore-llms-txt' => 'llms.txt generator', 'roi-localizzazione' => 'Localization ROI', 'suona-madrelingua' => 'Native-sounding?' ),
		'ru' => array( 'test-velocita' => 'Тест скорости', 'analisi-seo' => 'SEO-аудит', 'segnali-eeat' => 'Сигналы E-E-A-T', 'check-gdpr' => 'Проверка GDPR', 'verifica-accessibilita' => 'Доступность', 'impatto-co2' => 'Углеродный след', 'sito-pronto-ai' => 'Готовность к ИИ', 'sito-letto-dallai' => 'Сайт глазами ИИ', 'generatore-llms-txt' => 'Генератор llms.txt', 'roi-localizzazione' => 'ROI локализации', 'suona-madrelingua' => 'Как у носителя?' ),
	);
	$sl = $serv_label[ $lang ];
	$tl = $tool_label[ $lang ];

	$serv_item = function ( $slug ) use ( $su, $sl ) {
		return array( 'label' => $sl[ $slug ], 'url' => $su[ $slug ] );
	};
	$tool_item = function ( $slug ) use ( $tu, $tl ) {
		return array( 'label' => $tl[ $slug ], 'url' => $tu[ $slug ] );
	};

	return array(
		'strings'  => $s,
		'serv_url' => $su,
		'tool_url' => $tu,
		'servizi'  => array(
			array( 'eyebrow' => $s['creare'], 'items' => array( $serv_item( 'siti-aziendali' ), $serv_item( 'e-commerce' ), $serv_item( 'web-app' ), $serv_item( 'siti-pwa' ) ) ),
			array( 'eyebrow' => $s['crescere'], 'items' => array( $serv_item( 'seo-tecnica' ), $serv_item( 'siti-multilingue' ), $serv_item( 'export-ready' ) ) ),
			array( 'eyebrow' => $s['sistemare'], 'items' => array( $serv_item( 'restyling-migrazione' ), $serv_item( 'adeguamento-eaa' ) ) ),
		),
		'lab'      => array(
			array( 'eyebrow' => $s['perf'], 'items' => array( $tool_item( 'test-velocita' ), $tool_item( 'analisi-seo' ), $tool_item( 'segnali-eeat' ) ) ),
			array( 'eyebrow' => $s['conf'], 'items' => array( $tool_item( 'check-gdpr' ), $tool_item( 'verifica-accessibilita' ), $tool_item( 'impatto-co2' ) ) ),
			array( 'eyebrow' => $s['ai'], 'items' => array( $tool_item( 'sito-pronto-ai' ), $tool_item( 'sito-letto-dallai' ), $tool_item( 'generatore-llms-txt' ) ) ),
			array( 'eyebrow' => $s['mercati'], 'items' => array( $tool_item( 'roi-localizzazione' ), $tool_item( 'suona-madrelingua' ) ) ),
		),
	);
}

/** Renderizza una colonna (eyebrow + lista di voci). */
function remarka_mega_col( array $col ): string {
	$out = '<div class="sr-mega__col"><p class="sr-mega__eyebrow">' . esc_html( $col['eyebrow'] ) . '</p><ul class="sr-mega__list">';
	foreach ( $col['items'] as $it ) {
		$out .= '<li><a href="' . esc_url( home_url( $it['url'] ) ) . '">' . esc_html( $it['label'] ) . '</a></li>';
	}
	return $out . '</ul></div>';
}

/** Pannello «Servizi». */
function remarka_mega_panel_servizi(): string {
	$d = remarka_mega_data();
	$s = $d['strings'];
	$su = $d['serv_url'];
	$cols = '';
	foreach ( $d['servizi'] as $col ) {
		$cols .= remarka_mega_col( $col );
	}
	$feat = '<a class="sr-mega__feat" href="' . esc_url( home_url( $su['contatti'] ) ) . '">'
		. '<span class="sr-mega__feat-k">' . esc_html( $s['serv_feat_k'] ) . '</span>'
		. '<span class="sr-mega__feat-t">' . esc_html( $s['serv_feat_t'] ) . '</span>'
		. '<span class="sr-mega__feat-cta">' . esc_html( $s['serv_feat_cta'] ) . ' &rarr;</span></a>';
	$foot = '<div class="sr-mega__foot">'
		. '<a href="' . esc_url( home_url( $su['index'] ) ) . '">' . esc_html( $s['all_serv'] ) . ' &rarr;</a>'
		. '<a href="' . esc_url( home_url( $su['prezzi'] ) ) . '">' . esc_html( $s['prezzi'] ) . ' &rarr;</a>'
		. '<a href="' . esc_url( home_url( $su['casi'] ) ) . '">' . esc_html( $s['casi'] ) . ' &rarr;</a></div>';
	return '<div class="sr-mega sr-mega--servizi"><div class="sr-mega__box"><div class="sr-mega__inner">' . $cols . $feat . '</div>' . $foot . '</div></div>';
}

/** Pannello «Strumenti» → hub Remarka Lab (strumenti gratuiti + Monitor). */
function remarka_mega_panel_lab(): string {
	$d = remarka_mega_data();
	$s = $d['strings'];
	$tu = $d['tool_url'];

	$checkup = '<a class="sr-mega__checkup" href="' . esc_url( home_url( $tu['check-up-completo'] ) ) . '">'
		. '<span class="sr-mega__eyebrow sr-mega__eyebrow--accent">' . esc_html( $s['checkup_k'] ) . '</span>'
		. '<span class="sr-mega__checkup-t">' . esc_html( $s['checkup_t'] ) . '</span>'
		. '<span class="sr-mega__checkup-d">' . esc_html( $s['checkup_d'] ) . '</span></a>';

	$cols = '';
	foreach ( $d['lab'] as $col ) {
		$cols .= remarka_mega_col( $col );
	}

	$monitor = '<div class="sr-mega__monitor">'
		. '<p class="sr-mega__eyebrow sr-mega__eyebrow--light">' . esc_html( $s['mon_k'] ) . '</p>'
		. '<p class="sr-mega__monitor-t">' . esc_html( $s['mon_t'] ) . '</p>'
		. '<a class="sr-mega__monitor-live" href="https://lab.remarka.biz/showcase" target="_blank" rel="noopener">' . esc_html( $s['mon_live'] ) . ' &rarr;</a>'
		. '<a class="sr-mega__monitor-cta" href="https://lab.remarka.biz/showcase" target="_blank" rel="noopener">' . esc_html( $s['mon_cta'] ) . ' &rarr;</a></div>';

	$foot = '<div class="sr-mega__foot"><a href="' . esc_url( home_url( $tu['index'] ) ) . '">' . esc_html( $s['all_tools'] ) . ' &rarr;</a></div>';

	return '<div class="sr-mega sr-mega--lab"><div class="sr-mega__box"><div class="sr-mega__inner">'
		. '<div class="sr-mega__labtools">' . $checkup . '<div class="sr-mega__toolgrid">' . $cols . '</div></div>'
		. $monitor . '</div>' . $foot . '</div></div>';
}

/** Suffisso URL → quale pannello (o null). Copre le tre lingue. */
function remarka_mega_which( string $url ): ?string {
	$path = trim( (string) wp_parse_url( $url, PHP_URL_PATH ), '/' );
	$last = strtolower( substr( strrchr( '/' . $path, '/' ), 1 ) );
	if ( in_array( $last, array( 'servizi', 'services', 'uslugi' ), true ) ) {
		return 'servizi';
	}
	if ( in_array( $last, array( 'strumenti', 'tools', 'instrumenty' ), true ) ) {
		return 'lab';
	}
	return null;
}

/** Aggiunge .sr-has-mega alla <li> di Servizi/Strumenti (solo nella barra). */
function remarka_mega_menu_css_class( array $classes, $item, $args ): array {
	if ( ! isset( $args->theme_location ) || 'menu-1' !== $args->theme_location ) {
		return $classes;
	}
	$which = remarka_mega_which( (string) ( $item->url ?? '' ) );
	if ( $which ) {
		$classes[] = 'sr-has-mega';
		$classes[] = 'sr-has-mega--' . $which;
	}
	return $classes;
}
add_filter( 'nav_menu_css_class', 'remarka_mega_menu_css_class', 20, 3 );

/** Appende il pannello dopo il link della voce (solo nella barra). */
function remarka_mega_menu_start_el( string $item_output, $item, $depth, $args ): string {
	if ( ! isset( $args->theme_location ) || 'menu-1' !== $args->theme_location ) {
		return $item_output;
	}
	$which = remarka_mega_which( (string) ( $item->url ?? '' ) );
	if ( 'servizi' === $which ) {
		$item_output .= remarka_mega_panel_servizi();
	} elseif ( 'lab' === $which ) {
		$item_output .= remarka_mega_panel_lab();
	}
	return $item_output;
}
add_filter( 'walker_nav_menu_start_el', 'remarka_mega_menu_start_el', 20, 4 );
