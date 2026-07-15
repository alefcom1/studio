<?php
/**
 * Remarka Studio — мультиязычный рантайм без плагинов.
 *
 * Архитектура: IT в корне, /en/ и /ru/ — обычные деревья вложенных страниц
 * WordPress. Этот файл добавляет: определение языка по пути страницы,
 * hreflang + x-default, атрибут lang, подмену меню по языку, строки
 * интерфейса темы (футер/форма/cookie) и конфиг переключателя для JS.
 * Карта соответствия путей — inc/lang-map.php (генерируется lang.py).
 */

defined( 'ABSPATH' ) || exit;

/** Языковая карта страниц: array of ['it'=>path,'en'=>path,'ru'=>path]. */
function remarka_lang_map(): array {
	static $map = null;
	if ( null === $map ) {
		$file = get_stylesheet_directory() . '/inc/lang-map.php';
		$map  = file_exists( $file ) ? include $file : array();
	}
	return $map;
}

/** Путь текущей страницы в формате карты (без ведущего/замыкающего слеша). */
function remarka_current_path(): string {
	if ( is_front_page() ) {
		return '';
	}
	$id = get_queried_object_id();
	if ( $id && 'page' === get_post_type( $id ) ) {
		return (string) get_page_uri( $id );
	}
	return trim( (string) wp_parse_url( add_query_arg( array() ), PHP_URL_PATH ), '/' );
}

/** Текущий язык: it|en|ru. */
function remarka_current_lang(): string {
	$path = remarka_current_path();
	if ( 'en' === $path || str_starts_with( $path, 'en/' ) ) {
		return 'en';
	}
	if ( 'ru' === $path || str_starts_with( $path, 'ru/' ) ) {
		return 'ru';
	}
	return 'it';
}

/** Строка карты для текущей страницы или null. */
function remarka_lang_row(): ?array {
	$path = remarka_current_path();
	$lang = remarka_current_lang();
	foreach ( remarka_lang_map() as $row ) {
		if ( $row[ $lang ] === $path ) {
			return $row;
		}
	}
	return null;
}

/* ---------- Атрибут lang ---------- */

function remarka_language_attributes( string $output ): string {
	$lang = remarka_current_lang();
	$attr = array( 'it' => 'it-IT', 'en' => 'en-US', 'ru' => 'ru-RU' )[ $lang ];
	return preg_replace( '/lang="[^"]*"/', 'lang="' . esc_attr( $attr ) . '"', $output )
		?: $output . ' lang="' . esc_attr( $attr ) . '"';
}
add_filter( 'language_attributes', 'remarka_language_attributes' );

/* ---------- hreflang + x-default ---------- */

function remarka_hreflang_tags(): void {
	$row = remarka_lang_row();
	if ( ! $row ) {
		return;
	}
	$langs = array( 'it' => 'it-IT', 'en' => 'en-US', 'ru' => 'ru-RU' );
	foreach ( $langs as $lang => $hreflang ) {
		$url = home_url( '/' . ( $row[ $lang ] ? $row[ $lang ] . '/' : '' ) );
		printf( '<link rel="alternate" hreflang="%s" href="%s" />' . "\n", esc_attr( $hreflang ), esc_url( $url ) );
	}
	printf( '<link rel="alternate" hreflang="x-default" href="%s" />' . "\n",
		esc_url( home_url( '/' . ( $row['it'] ? $row['it'] . '/' : '' ) ) ) );
}
add_action( 'wp_head', 'remarka_hreflang_tags', 3 );

/* ---------- Конфиг переключателя языка для JS ---------- */

function remarka_lang_switch_config(): void {
	$row  = remarka_lang_row();
	$lang = remarka_current_lang();
	$urls = array();
	if ( $row ) {
		foreach ( array( 'it', 'en', 'ru' ) as $l ) {
			$urls[ $l ] = home_url( '/' . ( $row[ $l ] ? $row[ $l ] . '/' : '' ) );
		}
	} else {
		// Страница вне карты (напр. городской лендинг без перевода):
		// ведём на Home соответствующего языка.
		$urls = array(
			'it' => home_url( '/' ),
			'en' => home_url( '/en/' ),
			'ru' => home_url( '/ru/' ),
		);
	}
	printf(
		'<script>window.remarkaLang = %s;</script>' . "\n",
		wp_json_encode( array( 'current' => $lang, 'urls' => $urls ) )
	);
}
add_action( 'wp_head', 'remarka_lang_switch_config', 4 );

/* ---------- Breadcrumb Rank Math: voce "Home" localizzata per URL ----------
 * Con locale WordPress in russo, l'etichetta "Home" del breadcrumb diventa
 * "Главная" anche sulle pagine italiane. Qui forziamo l'etichetta e il link
 * della prima voce in base alla lingua del percorso (it→/, en→/en/, ru→/ru/),
 * indipendentemente dal locale del sito. Attivo solo se Rank Math è presente. */
function remarka_breadcrumb_localize_home( $crumbs ) {
	if ( is_array( $crumbs ) && ! empty( $crumbs[0] ) && is_array( $crumbs[0] ) ) {
		$lang        = remarka_current_lang();
		$home_paths  = array( 'it' => '/', 'en' => '/en/', 'ru' => '/ru/' );
		$crumbs[0][0] = remarka_str( 'breadcrumb_home' );
		$crumbs[0][1] = home_url( $home_paths[ $lang ] ?? '/' );
	}
	return $crumbs;
}
add_filter( 'rank_math/frontend/breadcrumb/items', 'remarka_breadcrumb_localize_home' );

/* ---------- Redirect 301 dai vecchi URL piatti EN/RU ---------- */

/**
 * Durante il deploy del 14-07-2026 (risoluzione del genitore en/ru fallita
 * per un incidente separato), l'intero albero EN/RU venne creato una volta
 * in radice (es. /services/business-websites/ invece di
 * /en/services/business-websites/) e la pulizia orfani non lo vede: verifica
 * solo lo slug nudo, non il percorso completo, quindi "services" in radice
 * risulta indistinguibile da "services" sotto /en/. Quei duplicati vengono
 * cestinati manualmente (vedi docs/deploy-ssh.md); qui restano solo i
 * redirect 301, per chi ha già indicizzato/salvato i vecchi URL piatti.
 * Costruita da inc/lang-map.php: un URL piatto esiste solo se coincide con
 * un percorso en/ru meno il proprio prefisso di lingua — non serve una
 * lista scritta a mano, resta sincronizzata con lang.py.
 */
function remarka_legacy_flat_redirect_map(): array {
	static $map = null;
	if ( null !== $map ) {
		return $map;
	}
	$map = array(
		// URL creati prima di questo progetto (post_name già percent-encoded
		// in DB per gli slug non latini — così arriva anche da wp_parse_url()).
		'%d0%b3%d0%bb%d0%b0%d0%b2%d0%bd%d0%b0%d1%8f' => '',        // главная
		'%d0%b1%d0%bb%d0%be%d0%b3'                   => 'ru/blog', // блог (URL cirillico → blog RU)
		'sample-page'                                => '',
	);
	/*
	 * Guardia anti-collisione: se il percorso EN/RU meno il prefisso di lingua
	 * coincide con un percorso ITALIANO reale (indice blog: it 'blog' vs
	 * en 'en/blog'; articoli con slug identico nelle lingue, es.
	 * core-web-vitals-2026), quel "flat" NON è un URL legacy — è la pagina
	 * italiana viva, e redirigerla manderebbe gli utenti IT sulla versione EN.
	 */
	$it_paths = array();
	foreach ( remarka_lang_map() as $row ) {
		if ( ! empty( $row['it'] ) ) {
			$it_paths[ (string) $row['it'] ] = true;
		}
	}
	foreach ( remarka_lang_map() as $row ) {
		foreach ( array( 'en', 'ru' ) as $lang ) {
			$path = $row[ $lang ];
			$flat = preg_replace( '#^' . $lang . '/#', '', (string) $path );
			if ( $path && $flat !== $path && ! isset( $it_paths[ $flat ] ) && ! isset( $map[ $flat ] ) ) {
				$map[ $flat ] = $path;
			}
		}
	}
	return $map;
}

function remarka_redirect_legacy_flat_urls(): void {
	$path = strtolower( remarka_current_path() );
	$map  = remarka_legacy_flat_redirect_map();
	if ( isset( $map[ $path ] ) ) {
		wp_safe_redirect( home_url( '/' . $map[ $path ] . ( $map[ $path ] ? '/' : '' ) ), 301 );
		exit;
	}
}
add_action( 'template_redirect', 'remarka_redirect_legacy_flat_urls', 1 );

/* ---------- Подмена меню по языку ---------- */

function remarka_lang_menu_name( string $location, string $lang ): ?string {
	$names = array(
		'en' => array(
			'menu-1'        => 'Menu EN — Remarka',
			'footer-pagine' => 'Footer EN — Pages',
			'footer-studio' => 'Footer EN — Studio',
		),
		'ru' => array(
			'menu-1'        => 'Menu RU — Remarka',
			'footer-pagine' => 'Footer RU — Страницы',
			'footer-studio' => 'Footer RU — Студия',
		),
	);
	return $names[ $lang ][ $location ] ?? null;
}

function remarka_swap_menu_by_lang( $args ) {
	$lang = remarka_current_lang();
	if ( 'it' === $lang || empty( $args['theme_location'] ) ) {
		return $args;
	}
	$name = remarka_lang_menu_name( $args['theme_location'], $lang );
	if ( $name && wp_get_nav_menu_object( $name ) ) {
		$args['menu'] = $name;
	}
	return $args;
}
add_filter( 'wp_nav_menu_args', 'remarka_swap_menu_by_lang' );

/* ---------- Строки интерфейса темы ---------- */

function remarka_str( string $key ): string {
	static $table = array(
		'footer_pagine'    => array( 'it' => 'Pagine', 'en' => 'Pages', 'ru' => 'Страницы' ),
		'footer_studio'    => array( 'it' => 'Studio', 'en' => 'Studio', 'ru' => 'Студия' ),
		'footer_dati'      => array( 'it' => 'Dati societari', 'en' => 'Company details', 'ru' => 'Реквизиты' ),
		'footer_diritti'   => array( 'it' => 'Tutti i diritti riservati', 'en' => 'All rights reserved', 'ru' => 'Все права защищены' ),
		'footer_pagespeed' => array( 'it' => 'Punteggio PageSpeed medio', 'en' => 'Average PageSpeed score', 'ru' => 'Средний балл PageSpeed' ),
		'footer_tagline'   => array(
			'it' => 'Siti progressivi per PMI italiane. Parte del gruppo Remarka, nel settore linguistico e digitale dal 2001.',
			'en' => 'Progressive websites for Italian SMBs. Part of the Remarka group, in language and digital services since 2001.',
			'ru' => 'Прогрессивные сайты для малого и среднего бизнеса Италии. Часть группы Remarka — в языковой и цифровой сфере с 2001 года.',
		),
		'cta_heading'      => array( 'it' => 'Parliamo del vostro sito', 'en' => 'Let’s talk about your website', 'ru' => 'Поговорим о вашем сайте' ),
		'cta_text'         => array(
			'it' => 'Analisi gratuita del sito attuale, preventivo chiuso entro 24 ore dalla chiamata.',
			'en' => 'Free analysis of your current website; a fixed quote within 24 hours of the call.',
			'ru' => 'Бесплатный анализ текущего сайта и фиксированная смета в течение 24 часов после звонка.',
		),
		'cta_btn1'         => array( 'it' => 'Richiedi preventivo in 24 ore', 'en' => 'Get a quote in 24 hours', 'ru' => 'Смета за 24 часа' ),
		'cta_btn2'         => array( 'it' => 'Analizza il tuo sito — gratis', 'en' => 'Test your website — free', 'ru' => 'Проверить сайт — бесплатно' ),
		'form_nome'        => array( 'it' => 'Nome e cognome', 'en' => 'Full name', 'ru' => 'Имя и фамилия' ),
		'form_contatto'    => array( 'it' => 'Email o telefono', 'en' => 'Email or phone', 'ru' => 'Email или телефон' ),
		'form_messaggio'   => array( 'it' => 'Messaggio', 'en' => 'Message', 'ru' => 'Сообщение' ),
		'form_invia'       => array( 'it' => 'Invia la richiesta', 'en' => 'Send the request', 'ru' => 'Отправить заявку' ),
		'form_inviata'     => array( 'it' => 'RICHIESTA INVIATA ✓', 'en' => 'REQUEST SENT ✓', 'ru' => 'ЗАЯВКА ОТПРАВЛЕНА ✓' ),
		'form_grazie'      => array(
			'it' => 'Grazie. Vi rispondiamo entro un giorno lavorativo con un’analisi o un preventivo chiuso.',
			'en' => 'Thank you. We’ll reply within one business day with an analysis or a fixed quote.',
			'ru' => 'Спасибо. Ответим в течение одного рабочего дня — с анализом или фиксированной сметой.',
		),
		'form_err_campi'   => array( 'it' => 'Compilate tutti i campi, per favore.', 'en' => 'Please fill in all the fields.', 'ru' => 'Пожалуйста, заполните все поля.' ),
		'form_err_sessione' => array( 'it' => 'Sessione scaduta: ricaricate la pagina e riprovate.', 'en' => 'Session expired: reload the page and try again.', 'ru' => 'Сессия истекла: обновите страницу и попробуйте ещё раз.' ),
		'form_err_ratelimit' => array( 'it' => 'Avete appena inviato una richiesta: attendete un minuto prima di riprovare.', 'en' => 'You just sent a request: please wait a minute before trying again.', 'ru' => 'Вы только что отправили заявку: подождите минуту перед повторной отправкой.' ),
		'form_err_tecnico' => array( 'it' => 'Invio non riuscito per un problema tecnico. Scriveteci su WhatsApp o via email.', 'en' => 'Sending failed due to a technical issue. Reach us on WhatsApp or by email.', 'ru' => 'Не удалось отправить из-за технической ошибки. Напишите нам в WhatsApp или на email.' ),
		'cookie_testo'     => array(
			'it' => 'Usiamo solo cookie tecnici necessari al funzionamento del sito. Nessuna profilazione, nessun tracciamento pubblicitario.',
			'en' => 'We only use technical cookies required for the website to work. No profiling, no ad tracking.',
			'ru' => 'Мы используем только технические cookie, необходимые для работы сайта. Без профилирования и рекламного трекинга.',
		),
		'cookie_preferenze' => array( 'it' => 'Preferenze', 'en' => 'Preferences', 'ru' => 'Настройки' ),
		'cookie_policy'    => array( 'it' => 'Cookie policy', 'en' => 'Cookie policy', 'ru' => 'Политика cookie' ),
		'cookie_rifiuta'   => array( 'it' => 'Rifiuta', 'en' => 'Decline', 'ru' => 'Отклонить' ),
		'cookie_accetta'   => array( 'it' => 'Accetta', 'en' => 'Accept', 'ru' => 'Принять' ),
		'wa_label'         => array( 'it' => 'Scrivici su WhatsApp', 'en' => 'Message us on WhatsApp', 'ru' => 'Написать нам в WhatsApp' ),
		'footer_tel'       => array( 'it' => 'Tel./WhatsApp', 'en' => 'Phone/WhatsApp', 'ru' => 'Тел./WhatsApp' ),
		// --- Modulo preventivo a step ---
		'form_q_tipo'      => array( 'it' => 'Di cosa hai bisogno?', 'en' => 'What do you need?', 'ru' => 'Что вам нужно?' ),
		'form_q_tipo_hint' => array(
			'it' => 'Scegli il tipo di progetto: ci serve per prepararti un preventivo su misura.',
			'en' => 'Pick the type of project — we need it to prepare a tailored quote.',
			'ru' => 'Выберите тип проекта — по нему подготовим смету под вас.',
		),
		'form_q_budget'    => array( 'it' => 'Budget e tempi', 'en' => 'Budget and timing', 'ru' => 'Бюджет и сроки' ),
		'form_q_budget_hint' => array(
			'it' => 'Un’indicazione di massima basta: serve solo a proporti la soluzione giusta.',
			'en' => 'A rough idea is enough — it just helps us propose the right solution.',
			'ru' => 'Достаточно примерной оценки — это нужно, чтобы предложить подходящее решение.',
		),
		'form_lbl_budget'  => array( 'it' => 'Budget indicativo', 'en' => 'Approximate budget', 'ru' => 'Примерный бюджет' ),
		'form_lbl_tempi'   => array( 'it' => 'Quando vorresti partire?', 'en' => 'When would you like to start?', 'ru' => 'Когда хотите начать?' ),
		'form_q_contatti'  => array( 'it' => 'Come ti ricontattiamo?', 'en' => 'How should we reach you?', 'ru' => 'Как с вами связаться?' ),
		'form_q_contatti_hint' => array(
			'it' => 'Ti rispondiamo entro un giorno lavorativo con un preventivo chiuso.',
			'en' => 'We reply within one business day with a fixed quote.',
			'ru' => 'Ответим в течение рабочего дня с фиксированной сметой.',
		),
		'form_lbl_file'    => array( 'it' => 'Allega un file', 'en' => 'Attach a file', 'ru' => 'Прикрепить файл' ),
		'form_file_opt'    => array( 'it' => '— brief, logo (facoltativo)', 'en' => '— brief, logo (optional)', 'ru' => '— бриф, логотип (необязательно)' ),
		'form_upload_drag' => array( 'it' => 'Trascina un file', 'en' => 'Drag a file', 'ru' => 'Перетащите файл' ),
		'form_upload_or'   => array( 'it' => 'o clicca per caricarlo', 'en' => 'or click to upload', 'ru' => 'или нажмите для загрузки' ),
		'form_upload_hint' => array( 'it' => 'PDF, DOC, PNG, JPG — max 8 MB', 'en' => 'PDF, DOC, PNG, JPG — max 8 MB', 'ru' => 'PDF, DOC, PNG, JPG — до 8 МБ' ),
		'form_msg_opt'     => array( 'it' => '— facoltativo', 'en' => '— optional', 'ru' => '— необязательно' ),
		'form_continua'    => array( 'it' => 'Continua →', 'en' => 'Continue →', 'ru' => 'Далее →' ),
		'form_indietro'    => array( 'it' => '← Indietro', 'en' => '← Back', 'ru' => '← Назад' ),
		'form_invia_finale' => array( 'it' => 'Ricevi il preventivo in 24 ore →', 'en' => 'Get your quote in 24 hours →', 'ru' => 'Получить смету за 24 часа →' ),
		'form_step'        => array( 'it' => 'Passo', 'en' => 'Step', 'ru' => 'Шаг' ),
		'form_di'          => array( 'it' => 'di', 'en' => 'of', 'ru' => 'из' ),
		'form_invio_corso' => array( 'it' => 'Invio in corso…', 'en' => 'Sending…', 'ru' => 'Отправка…' ),
		'form_err_scelta'  => array( 'it' => 'Seleziona un’opzione per continuare.', 'en' => 'Select an option to continue.', 'ru' => 'Выберите вариант, чтобы продолжить.' ),
		'form_err_file_tipo' => array( 'it' => 'Formato file non ammesso. Usa PDF, DOC, PNG o JPG.', 'en' => 'File type not allowed. Use PDF, DOC, PNG or JPG.', 'ru' => 'Недопустимый тип файла. Используйте PDF, DOC, PNG или JPG.' ),
		'form_err_file_dim' => array( 'it' => 'Il file supera 8 MB. Caricane uno più leggero.', 'en' => 'The file exceeds 8 MB. Upload a smaller one.', 'ru' => 'Файл больше 8 МБ. Загрузите меньше.' ),
		'footer_citta'     => array( 'it' => 'Dove operiamo', 'en' => 'Where we work', 'ru' => 'Где мы работаем' ),
		'breadcrumb_home'  => array( 'it' => 'Home', 'en' => 'Home', 'ru' => 'Главная' ),
	);
	$lang = remarka_current_lang();
	return $table[ $key ][ $lang ] ?? $table[ $key ]['it'] ?? $key;
}

/**
 * Тексты футера: на IT — из Customizer (правит владелец); на EN/RU — наши
 * переводы дефолтов из таблицы выше (кастомизации владельца остаются
 * итальянскими, это документированное ограничение без плагина).
 */
function remarka_footer_text( string $customizer_key, string $str_key ): string {
	if ( 'it' === remarka_current_lang() ) {
		return remarka_footer_mod( $customizer_key );
	}
	return remarka_str( $str_key );
}
