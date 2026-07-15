<?php
/**
 * Check-up completo — generatore del report PDF (M3).
 *
 * Contiene: il copy deck statico IT/EN/RU per il PDF (docs/copy-checkup.md
 * §2.5/3.5/4.5), il ricalcolo server-side del punteggio composito (mai ci
 * fidiamo del valore mandato dal client: lo ricalcoliamo dai punteggi delle
 * 7 dimensioni, già sanificati), e il rendering HTML → PDF con dompdf
 * (bundle locale in lib/dompdf/, vedi lib/dompdf/VERSIONS.md per versioni
 * e licenze). Nessuna dipendenza da remarka_current_lang(): la lingua del
 * report è quella dichiarata dal client nel payload, sanificata a monte.
 */

defined( 'ABSPATH' ) || exit;

/**
 * Estensioni PHP richieste da dompdf per generare un PDF corretto: dom (parsing
 * HTML), mbstring (testo UTF-8/cirillico), gd (rasterizzazione di eventuali
 * immagini — non usiamo loghi raster nel report, ma dompdf la richiede per
 * inizializzarsi in alcuni path). Ritorna l'elenco di quelle mancanti.
 */
function remarka_checkup_pdf_missing_extensions(): array {
	$required = array( 'dom', 'mbstring', 'gd' );
	$missing  = array();
	foreach ( $required as $ext ) {
		if ( ! extension_loaded( $ext ) ) {
			$missing[] = $ext;
		}
	}
	return $missing;
}

/** Le 7 dimensioni nell'ordine dei pesi (docs/copy-checkup.md §1.1). */
function remarka_checkup_dimensions(): array {
	return array(
		'perf' => 25,
		'seo'  => 20,
		'a11y' => 15,
		'gdpr' => 15,
		'bp'   => 10,
		'ai'   => 10,
		'co2'  => 5,
	);
}

/** Soglie dei semafori, identiche per ogni dimensione e per il composito (§1.4). */
function remarka_checkup_level( int $score ): int {
	if ( $score >= 90 ) {
		return 0;
	}
	if ( $score >= 75 ) {
		return 1;
	}
	if ( $score >= 50 ) {
		return 2;
	}
	return 3;
}

function remarka_checkup_flag( int $level ): string {
	if ( $level <= 1 ) {
		return 'good';
	}
	return 2 === $level ? 'warn' : 'bad';
}

/**
 * Ricalcola il composito lato server dai punteggi già sanificati — non ci
 * fidiamo del valore `composite`/`measured` mandato dal client, anche se
 * l'impatto di un valore falsificato sarebbe basso (report indirizzato allo
 * stesso utente): coerenza interna del PDF prima di tutto. Stessa formula
 * del client (remarka.js `checkupComposite`), §1.3/§1.5.
 */
function remarka_checkup_composite( array $scores ): array {
	$sum_w      = 0;
	$sum_ws     = 0;
	$n          = 0;
	$has_perf_seo = false;
	foreach ( remarka_checkup_dimensions() as $key => $weight ) {
		$score = $scores[ $key ] ?? null;
		if ( null === $score ) {
			continue;
		}
		$sum_w  += $weight;
		$sum_ws += $weight * $score;
		++$n;
		if ( 'perf' === $key || 'seo' === $key ) {
			$has_perf_seo = true;
		}
	}
	$valid = $n >= 4 && $has_perf_seo;
	return array(
		'composite' => ( $valid && $sum_w > 0 ) ? (int) round( $sum_ws / $sum_w ) : null,
		'measured'  => $n,
		'valid'     => $valid,
	);
}

/** Le 3 priorità: stesso ranking del client (`weight * (100 - score)` desc). */
function remarka_checkup_priorities( array $scores, array $copy ): array {
	$candidates = array();
	foreach ( remarka_checkup_dimensions() as $key => $weight ) {
		$score = $scores[ $key ] ?? null;
		if ( null === $score ) {
			continue;
		}
		$level = remarka_checkup_level( (int) $score );
		$candidates[] = array(
			'key'     => $key,
			'weight'  => $weight,
			'score'   => (int) $score,
			'impact'  => $weight * ( 100 - $score ),
			'label'   => $copy['dims'][ $key ]['label'],
			'word'    => $copy['words'][ $level ],
			'flag'    => remarka_checkup_flag( $level ),
			'finding' => $copy['dims'][ $key ]['findings'][ $level ],
		);
	}
	usort(
		$candidates,
		static function ( $a, $b ) {
			return $b['impact'] <=> $a['impact'];
		}
	);
	return array_slice( $candidates, 0, 3 );
}

/**
 * Dati societari per il report, per lingua ESPLICITA (non dipende dalla pagina
 * corrente: nel contesto AJAX non esiste una "pagina corrente" coerente).
 * Stessa fonte di remarka_company_lang_data(), duplicata qui in forma
 * parametrica per evitare di alterare una funzione usata anche dal footer.
 */
function remarka_checkup_company_data( string $locale ): array {
	if ( 'ru' === $locale ) {
		return array(
			'name'          => 'Студия Ремарка',
			'address'       => array( '125009, Москва, Глинищевский пер., д. 6, оф. 2', '350000, Краснодар, ул. Кузнечная, 6, офис 4' ),
			'tax'           => array( array( 'ИНН', '231149349191' ), array( 'ОГРНИП', '323237500359402' ) ),
			'email'         => 'info@remarka.biz',
			'phone_display' => '+7 918 263 00 13',
		);
	}
	if ( 'en' === $locale ) {
		return array(
			'name'          => remarka_footer_mod( 'remarka_company_name' ),
			'address'       => array( 'Milan, 20144, Vicolo Privato Lavandai, 2a', 'Turin, 10153, Corso Regina Margherita, 94', 'Rome, 00196, Via Flaminia, 122' ),
			'tax'           => array( array( 'VAT', remarka_footer_mod( 'remarka_company_piva' ) ) ),
			'email'         => remarka_footer_mod( 'remarka_company_email' ),
			'phone_display' => remarka_footer_mod( 'remarka_company_phone' ),
		);
	}
	return array(
		'name'          => remarka_footer_mod( 'remarka_company_name' ),
		'address'       => array_filter( array_map( 'trim', explode( "\n", (string) remarka_footer_mod( 'remarka_company_address' ) ) ) ),
		'tax'           => array( array( 'P.IVA', remarka_footer_mod( 'remarka_company_piva' ) ) ),
		'email'         => remarka_footer_mod( 'remarka_company_email' ),
		'phone_display' => remarka_footer_mod( 'remarka_company_phone' ),
	);
}

/**
 * Copy deck completo del report per lingua — testi statici verbatim da
 * docs/copy-checkup.md §2 (IT) / §3 (EN) / §4 (RU), struttura PDF §2.5/3.5/4.5.
 * Le uniche parti non verbatim (il deck non le specifica a questo livello di
 * dettaglio) sono: le 3 "cosa fare" per dimensione e le 4 etichette del
 * composito in EN/RU (il deck ne dà solo una come esempio); sono scritte in
 * coerenza terminologica col resto del deck, honeste (consigli generici di
 * buona pratica, nessun dato inventato).
 */
function remarka_checkup_copy( string $locale ): array {
	$decks = array(
		'it' => array(
			'words'            => array( 'Eccellente', 'Buono', 'Da migliorare', 'Critico' ),
			'composite_labels' => array( 'Sito in salute eccellente', 'Sito in buona salute', 'Sito da migliorare', 'Sito a rischio' ),
			'cover_title'      => 'Check-up completo del sito',
			'cover_domain'     => 'Sito analizzato',
			'cover_date'       => 'Data',
			'cover_partial'    => 'Su {n} misurazioni di 7',
			'summary_h1'       => "Lo stato di salute in un colpo d'occhio",
			'summary_th'       => array( 'Dimensione', 'Peso', 'Punteggio', 'Verdetto' ),
			'na_word'          => 'N/D',
			'na_finding'       => 'Non siamo riusciti a misurare questo aspetto: il sito ha rifiutato la lettura o il servizio Google era saturo. Rilanciate il test tra qualche minuto.',
			'dim_score_suffix' => '/100',
			'dim_found_h3'     => 'Cosa abbiamo trovato',
			'dim_todo_h3'      => 'Cosa fare',
			'dim_method_label' => 'Misura',
			'priorities_h1'    => 'Da dove partire',
			'priorities_lead'  => 'I tre interventi con il maggiore impatto sul punteggio, ordinati per peso × margine di miglioramento.',
			'whatwedo_h1'      => 'Cosa faremmo noi, e con quali garanzie',
			'whatwedo_text'    => "Trasformiamo questo report in un piano a prezzo chiuso: consegna a data fissa con penale, PageSpeed 90+ garantito, 12 mesi di assistenza. Prima di ogni intervento, un preventivo chiuso in 24 ore.",
			'whatwedo_cta'     => 'Richiedi la consulenza gratuita',
			'whatwedo_cta_url' => '/#contatti',
			'eeat_h1'          => 'Chi ha preparato questo report',
			'eeat_intro'       => 'Studio Remarka S.r.l., parte del gruppo Remarka, nel settore linguistico e digitale dal 2001. Siti aziendali, e-commerce e localizzazione con redattori madrelingua.',
			'eeat_sedi_label'  => 'Sedi',
			'eeat_method_h2'   => 'Nota metodologica',
			'eeat_method_text' => "Motori usati: Google PageSpeed Insights / Lighthouse (prestazioni, SEO, accessibilità, best practice); modello Sustainable Web Design (impatto CO₂); verifiche proprietarie Studio Remarka (privacy/cookie, prontezza AI). Limiti dichiarati: il check GDPR è indicativo, non un parere legale; nessuna promessa di posizione su Google; l'accessibilità segue lo standard WCAG 2.1 AA richiesto dall'European Accessibility Act.",
			'footer_note'      => 'Studio Remarka — nel settore linguistico e digitale dal 2001',
			'monthly_note'     => 'Avete richiesto anche il monitoraggio mensile dei Core Web Vitals: vi scriveremo a questo indirizzo con i prossimi aggiornamenti.',
			'email_subject'    => 'Il check-up completo di {domain} — report in PDF',
			'email_body'       => "Buongiorno,\n\nin allegato trovate il report completo del check-up di {domain}: punteggio di salute {score}/100, i sette semafori e le raccomandazioni in ordine di impatto.\n\nLe prestazioni, la SEO, l'accessibilità e le best practice sono misurate con l'API Google PageSpeed Insights; privacy, prontezza AI e impatto CO₂ con le nostre verifiche, tutte con i limiti dichiarati nel report.\n\nSe volete, guardiamo insieme le priorità e vi diamo un piano d'intervento a prezzo chiuso — la consulenza è gratuita.\n\nRichiedi la consulenza gratuita → {cta_url}\n\nStudio Remarka — nel settore linguistico e digitale dal 2001\ninfo@remarka.biz · +39 347 83 11141",
			'cta_full_url'     => 'https://remarka.biz/#contatti',
		),
		'en' => array(
			'words'            => array( 'Excellent', 'Good', 'Needs work', 'Critical' ),
			'composite_labels' => array( 'Excellent site health', 'Good site health', 'Site needs work', 'Site at risk' ),
			'cover_title'      => 'Full website check-up',
			'cover_domain'     => 'Site analysed',
			'cover_date'       => 'Date',
			'cover_partial'    => 'Based on {n} of 7 measurements',
			'summary_h1'       => "Your site's health at a glance",
			'summary_th'       => array( 'Dimension', 'Weight', 'Score', 'Verdict' ),
			'na_word'          => 'N/A',
			'na_finding'       => "We couldn't measure this aspect: the site refused the reading, or Google's service was overloaded. Re-run the test in a few minutes.",
			'dim_score_suffix' => '/100',
			'dim_found_h3'     => 'What we found',
			'dim_todo_h3'      => 'What to do',
			'dim_method_label' => 'Measured by',
			'priorities_h1'    => 'Where to start',
			'priorities_lead'  => 'The three fixes with the biggest impact on the score, ranked by weight × room for improvement.',
			'whatwedo_h1'      => 'What we would do, and with what guarantees',
			'whatwedo_text'    => 'We turn this report into a fixed-price action plan: a fixed delivery date with a contractual penalty, PageSpeed 90+ guaranteed, 12 months of support. Before any work starts, a fixed quote within 24 hours.',
			'whatwedo_cta'     => 'Book a free consultation',
			'whatwedo_cta_url' => '/en/#contatti',
			'eeat_h1'          => 'Who prepared this report',
			'eeat_intro'       => 'Studio Remarka S.r.l., part of the Remarka group, in language and digital services since 2001. Business websites, e-commerce and localisation with native-speaking editors.',
			'eeat_sedi_label'  => 'Offices',
			'eeat_method_h2'   => 'Methodology note',
			'eeat_method_text' => "Engines used: Google PageSpeed Insights / Lighthouse (performance, SEO, accessibility, best practices); the Sustainable Web Design model (CO₂ impact); Studio Remarka's own checks (privacy/cookies, AI-readiness). Stated limits: the GDPR check is indicative, not a legal opinion; no Google ranking is promised; accessibility follows the WCAG 2.1 AA standard required by the European Accessibility Act.",
			'footer_note'      => 'Studio Remarka — in language and digital services since 2001',
			'monthly_note'     => "You also asked for the monthly Core Web Vitals monitoring: we'll write to this address with the next updates.",
			'email_subject'    => 'Your full check-up for {domain} — PDF report',
			'email_body'       => "Hello,\n\nattached is the complete check-up report for {domain}: health score {score}/100, the seven traffic lights and the recommendations ranked by impact.\n\nPerformance, SEO, accessibility and best practices are measured with the Google PageSpeed Insights API; privacy, AI-readiness and CO2 impact with our own checks, all with the limits stated in the report.\n\nIf you'd like, we'll go through the priorities together and hand you a fixed-price action plan — the consultation is free.\n\nBook your free consultation -> {cta_url}\n\nStudio Remarka -- in language and digital services since 2001\ninfo@remarka.biz . +39 347 83 11141",
			'cta_full_url'     => 'https://remarka.biz/en/#contatti',
		),
		'ru' => array(
			'words'            => array( 'Отлично', 'Хорошо', 'Внимание', 'Критично' ),
			'composite_labels' => array( 'Отличное здоровье сайта', 'Хорошее здоровье сайта', 'Сайт требует доработки', 'Сайт в зоне риска' ),
			'cover_title'      => 'Полная проверка сайта',
			'cover_domain'     => 'Проверенный сайт',
			'cover_date'       => 'Дата',
			'cover_partial'    => 'По {n} измерениям из 7',
			'summary_h1'       => 'Состояние здоровья сайта — в одном взгляде',
			'summary_th'       => array( 'Измерение', 'Вес', 'Балл', 'Вердикт' ),
			'na_word'          => 'Н/Д',
			'na_finding'       => 'Не удалось измерить этот аспект: сайт отказал в чтении, либо сервис Google был перегружен. Повторите тест через несколько минут.',
			'dim_score_suffix' => '/100',
			'dim_found_h3'     => 'Что мы нашли',
			'dim_todo_h3'      => 'Что делать',
			'dim_method_label' => 'Измерение',
			'priorities_h1'    => 'С чего начать',
			'priorities_lead'  => 'Три задачи с наибольшим влиянием на оценку, по убыванию веса × запаса на улучшение.',
			'whatwedo_h1'      => 'Что сделали бы мы — и с какими гарантиями',
			'whatwedo_text'    => 'Превращаем этот отчёт в план работ по фиксированной цене: точная дата сдачи с неустойкой в договоре, PageSpeed 90+ по договору, 12 месяцев сопровождения. Перед началом работ — закрытая смета в течение 24 часов.',
			'whatwedo_cta'     => 'Бесплатная консультация',
			'whatwedo_cta_url' => '/ru/#contatti',
			'eeat_h1'          => 'Кто подготовил этот отчёт',
			'eeat_intro'       => 'Студия Ремарка — часть группы Remarka, в языковой и цифровой сфере с 2001 года. Сайты, интернет-магазины и локализация носителями языка.',
			'eeat_sedi_label'  => 'Офисы',
			'eeat_method_h2'   => 'Методологическая заметка',
			'eeat_method_text' => 'Используемые движки: Google PageSpeed Insights / Lighthouse (скорость, SEO, доступность, технические стандарты); модель Sustainable Web Design (углеродный след); собственные проверки Студии Ремарка (приватность/cookie, готовность к ИИ). Заявленные границы: проверка GDPR — ориентировочная, не юридическое заключение; без обещаний позиций в Google; доступность — по стандарту WCAG 2.1 AA, обязательному по European Accessibility Act.',
			'footer_note'      => 'Студия Ремарка — в языковой и цифровой сфере с 2001 года',
			'monthly_note'     => 'Вы также запросили ежемесячный мониторинг Core Web Vitals: будем писать на этот адрес с новыми обновлениями.',
			'email_subject'    => 'Полная проверка {domain} — отчёт в PDF',
			'email_body'       => "Здравствуйте,\n\nво вложении — полный отчёт проверки {domain}: оценка здоровья {score}/100, семь светофоров и рекомендации по степени влияния.\n\nСкорость, SEO, доступность и стандарты измерены через API Google PageSpeed Insights; приватность, готовность к ИИ и углеродный след — нашими проверками, все с границами, указанными в отчёте.\n\nЕсли хотите, разберём приоритеты вместе и дадим план работ по фиксированной цене — консультация бесплатная.\n\nЗаписаться на бесплатную консультацию → {cta_url}\n\nСтудия Ремарка — в языковой и цифровой сфере с 2001 года\ninfo@remarka.biz · +7 918 263 00 13",
			'cta_full_url'     => 'https://remarka.biz/ru/#contatti',
		),
	);

	$deck        = $decks[ $locale ] ?? $decks['it'];
	$deck['dims'] = remarka_checkup_dim_copy( $locale );
	return $deck;
}

/** Copy per-dimensione: etichetta, sotto-riga motore, 4 verdetti, metodo, 3 "cosa fare". */
function remarka_checkup_dim_copy( string $locale ): array {
	$tables = array(
		'it' => array(
			'perf' => array(
				'label' => 'Prestazioni', 'engine' => 'Google PageSpeed',
				'findings' => array(
					'Il sito è rapido su mobile: rispetta gli standard Google.',
					'Velocità buona; restano margini misurabili su qualche pagina.',
					'Nella media del web, ma lontano dagli standard consigliati.',
					'Il sito è lento su mobile: gran parte dei visitatori abbandona prima del caricamento.',
				),
				'method' => 'Misura: Google PageSpeed Insights, Lighthouse strategia mobile.',
				'todo'   => array( 'Comprimete e ridimensionate le immagini prima del caricamento.', 'Attivate cache del browser e compressione (gzip/brotli) lato server.', 'Rimandate il JavaScript non essenziale dopo il primo rendering (lazy-load, defer).' ),
			),
			'seo' => array(
				'label' => 'SEO', 'engine' => 'Google PageSpeed',
				'findings' => array(
					"Basi tecniche on-page in ordine: nessun ostacolo all'indicizzazione.",
					'Struttura solida; poche correzioni per completare le basi.',
					'Alcuni elementi on-page mancano o sono duplicati.',
					"Qualcosa ostacola l'indicizzazione: da sistemare prima di tutto.",
				),
				'method' => 'Misura: Google PageSpeed Insights, Lighthouse strategia mobile.',
				'todo'   => array( 'Verificate che ogni pagina abbia un title e una meta description unici.', 'Controllate la gerarchia dei titoli (un solo H1, H2/H3 coerenti).', 'Aggiungete testo alternativo (alt) a tutte le immagini rilevanti.' ),
			),
			'a11y' => array(
				'label' => 'Accessibilità', 'engine' => 'WCAG 2.1 / EAA',
				'findings' => array(
					'Poche o nessuna barriera: sito fruibile secondo WCAG 2.1 AA.',
					'Buon livello; restano barriere minori da rimuovere.',
					'Diverse barriere rilevate: contrasti, etichette, navigazione.',
					'Barriere gravi: il sito è difficile da usare per molte persone (obbligo EAA).',
				),
				'method' => 'Misura: Google PageSpeed Insights, Lighthouse strategia mobile.',
				'todo'   => array( 'Alzate il contrasto testo/sfondo dove è marginale.', 'Aggiungete etichette (label) a tutti i campi dei form.', 'Assicuratevi che il sito sia navigabile da tastiera, senza mouse.' ),
			),
			'gdpr' => array(
				'label' => 'Privacy e cookie', 'engine' => 'Verifica indicativa',
				'findings' => array(
					"Banner, informative e tracker in ordine nell'HTML iniziale.",
					'Impianto presente; un paio di punti da verificare a mano.',
					'Mancano elementi o alcuni tracker vanno governati meglio.',
					'Tracker attivi senza banner o policy assenti: rischio concreto col Garante.',
				),
				'method' => "Verifica indicativa Studio Remarka su 4 segnali — non è un parere legale.",
				'todo'   => array( "Bloccate ogni tracker/cookie non tecnico finché l'utente non dà il consenso.", 'Rendete visibile un link a privacy policy e cookie policy da ogni pagina.', 'Configurate il banner cookie in modo che «rifiuta» sia facile quanto «accetta».' ),
			),
			'bp' => array(
				'label' => 'Best practice', 'engine' => 'Google PageSpeed',
				'findings' => array(
					'Sito tecnicamente pulito: HTTPS, console senza errori, librerie aggiornate.',
					'Buon livello tecnico; qualche avviso da chiudere.',
					'Diversi avvisi tecnici: sicurezza, errori console, immagini.',
					'Problemi tecnici diffusi che indeboliscono affidabilità e sicurezza.',
				),
				'method' => 'Misura: Google PageSpeed Insights, Lighthouse strategia mobile.',
				'todo'   => array( 'Servite il sito solo in HTTPS, senza contenuti misti.', 'Ripulite la console del browser da errori e warning JavaScript.', 'Aggiornate le librerie di terze parti alle versioni supportate.' ),
			),
			'ai' => array(
				'label' => "Pronto per l'AI", 'engine' => '4 segnali tecnici',
				'findings' => array(
					'4 segnali su 4: il sito è leggibile e citabile dai modelli AI.',
					'3 segnali su 4: manca poco alla piena prontezza AI.',
					'2 segnali su 4: dati strutturati o sitemap da completare.',
					'0–1 segnali: i modelli AI faticano a leggere e citare il sito.',
				),
				'method' => 'Verifica indicativa Studio Remarka su 4 segnali tecnici (llms.txt, robots, dati strutturati, sitemap).',
				'todo'   => array( 'Pubblicate un file llms.txt che riassuma cosa fa il sito.', 'Aggiungete dati strutturati JSON-LD alle pagine principali.', 'Verificate che i crawler AI non siano bloccati in robots.txt e che la sitemap.xml sia aggiornata.' ),
			),
			'co2' => array(
				'label' => 'Impatto CO₂', 'engine' => 'Modello SWD',
				'findings' => array(
					'Pagina leggera: emissioni sotto la media del web.',
					"Vicino alla media; c'è margine per alleggerire.",
					'Sopra la media: la pagina è pesante da caricare.',
					'Molto sopra la media: pagina pesante, costo ambientale e di velocità.',
				),
				'method' => 'Stima con il modello Sustainable Web Design, sui byte della pagina misurati da PageSpeed.',
				'todo'   => array( 'Comprimete immagini e video: sono la voce più pesante del peso pagina.', 'Caricate script di terze parti (chat, tracker) solo se necessari.', 'Attivate una cache/CDN per ridurre i byte trasferiti a ogni visita.' ),
			),
		),
		'en' => array(
			'perf' => array(
				'label' => 'Performance', 'engine' => 'Google PageSpeed',
				'findings' => array(
					"Fast on mobile: meets Google's standards.",
					'Good speed; measurable room on some pages.',
					'Average for the web, but far from the recommended standards.',
					'Slow on mobile: most visitors leave before it loads.',
				),
				'method' => 'Measured by: Google PageSpeed Insights, Lighthouse mobile strategy.',
				'todo'   => array( 'Compress and resize images before upload.', 'Turn on browser caching and server-side compression (gzip/brotli).', 'Defer non-essential JavaScript until after first render (lazy-load, defer).' ),
			),
			'seo' => array(
				'label' => 'SEO', 'engine' => 'Google PageSpeed',
				'findings' => array(
					'On-page foundations in order: no barrier to indexing.',
					'Solid structure; a few fixes to finish the basics.',
					'Some on-page elements are missing or duplicated.',
					'Something blocks indexing: fix this first.',
				),
				'method' => 'Measured by: Google PageSpeed Insights, Lighthouse mobile strategy.',
				'todo'   => array( 'Make sure every page has a unique title and meta description.', 'Check heading hierarchy (a single H1, consistent H2/H3).', 'Add descriptive alt text to every meaningful image.' ),
			),
			'a11y' => array(
				'label' => 'Accessibility', 'engine' => 'WCAG 2.1 / EAA',
				'findings' => array(
					'Few or no barriers: usable under WCAG 2.1 AA.',
					'Good level; minor barriers left to remove.',
					'Several barriers found: contrast, labels, navigation.',
					'Serious barriers: hard to use for many people (EAA obligation).',
				),
				'method' => 'Measured by: Google PageSpeed Insights, Lighthouse mobile strategy.',
				'todo'   => array( "Increase text/background contrast where it's marginal.", 'Add labels to every form field.', 'Make sure the site is fully usable by keyboard, without a mouse.' ),
			),
			'gdpr' => array(
				'label' => 'Privacy & cookies', 'engine' => 'Indicative check',
				'findings' => array(
					'Banner, policies and trackers in order in the initial HTML.',
					'Framework in place; a couple of points to check by hand.',
					'Elements missing or some trackers poorly governed.',
					'Trackers active without a banner, or policies missing: real regulatory risk.',
				),
				'method' => 'Studio Remarka indicative check, 4 signals — not a legal opinion.',
				'todo'   => array( 'Block every non-essential tracker/cookie until the user consents.', 'Make privacy and cookie policy links visible from every page.', 'Configure the cookie banner so "reject" is as easy as "accept".' ),
			),
			'bp' => array(
				'label' => 'Best practices', 'engine' => 'Google PageSpeed',
				'findings' => array(
					'Technically clean: HTTPS, no console errors, up-to-date libraries.',
					'Good technical level; a few warnings to close.',
					'Several technical warnings: security, console errors, images.',
					'Widespread technical issues weakening reliability and security.',
				),
				'method' => 'Measured by: Google PageSpeed Insights, Lighthouse mobile strategy.',
				'todo'   => array( 'Serve the site over HTTPS only, with no mixed content.', 'Clear the browser console of JavaScript errors and warnings.', 'Update third-party libraries to supported versions.' ),
			),
			'ai' => array(
				'label' => 'AI-readiness', 'engine' => '4 technical signals',
				'findings' => array(
					'4 of 4 signals: readable and citable by AI models.',
					'3 of 4 signals: nearly fully AI-ready.',
					'2 of 4 signals: structured data or sitemap to complete.',
					'0–1 signals: AI models struggle to read and cite the site.',
				),
				'method' => 'Studio Remarka indicative check, 4 technical signals (llms.txt, robots, structured data, sitemap).',
				'todo'   => array( "Publish an llms.txt file summarising what the site does.", 'Add JSON-LD structured data to the main pages.', "Check that AI crawlers aren't blocked in robots.txt and that sitemap.xml is up to date." ),
			),
			'co2' => array(
				'label' => 'CO₂ impact', 'engine' => 'SWD model',
				'findings' => array(
					'Light page: emissions below the web average.',
					'Near the average; room to slim down.',
					'Above average: the page is heavy to load.',
					'Well above average: heavy page, an environmental and speed cost.',
				),
				'method' => "Estimate using the Sustainable Web Design model, on the page bytes measured by PageSpeed.",
				'todo'   => array( "Compress images and video: they're the heaviest part of page weight.", 'Only load third-party scripts (chat widgets, trackers) when needed.', 'Turn on caching/CDN to cut bytes transferred on every visit.' ),
			),
		),
		'ru' => array(
			'perf' => array(
				'label' => 'Скорость', 'engine' => 'Google PageSpeed',
				'findings' => array(
					'Сайт быстрый на мобильном: соответствует стандартам Google.',
					'Скорость хорошая; на части страниц есть измеримый запас.',
					'В среднем по вебу, но далеко от рекомендуемых стандартов.',
					'Сайт медленный на мобильном: большинство уходит до загрузки.',
				),
				'method' => 'Измерение: Google PageSpeed Insights, мобильная стратегия Lighthouse.',
				'todo'   => array( 'Сжимайте и уменьшайте изображения перед загрузкой.', 'Включите кэширование браузера и сжатие на сервере (gzip/brotli).', 'Откладывайте несущественный JavaScript до первой отрисовки (lazy-load, defer).' ),
			),
			'seo' => array(
				'label' => 'SEO', 'engine' => 'Google PageSpeed',
				'findings' => array(
					'Технические основы страницы в порядке: ничто не мешает индексации.',
					'Структура крепкая; несколько правок, чтобы завершить основы.',
					'Часть элементов страницы отсутствует или дублируется.',
					'Что-то мешает индексации: исправить в первую очередь.',
				),
				'method' => 'Измерение: Google PageSpeed Insights, мобильная стратегия Lighthouse.',
				'todo'   => array( 'Проверьте, что у каждой страницы уникальные title и meta description.', 'Проверьте иерархию заголовков (один H1, последовательные H2/H3).', 'Добавьте атрибут alt для всех значимых изображений.' ),
			),
			'a11y' => array(
				'label' => 'Доступность', 'engine' => 'WCAG 2.1 / EAA',
				'findings' => array(
					'Барьеров мало или нет: сайт пригоден по WCAG 2.1 AA.',
					'Хороший уровень; остались мелкие барьеры.',
					'Найдено несколько барьеров: контраст, подписи, навигация.',
					'Серьёзные барьеры: сайтом трудно пользоваться многим (требование EAA).',
				),
				'method' => 'Измерение: Google PageSpeed Insights, мобильная стратегия Lighthouse.',
				'todo'   => array( 'Повысьте контраст текста и фона там, где он на грани нормы.', 'Добавьте подписи (label) ко всем полям форм.', 'Убедитесь, что сайт полностью управляется с клавиатуры, без мыши.' ),
			),
			'gdpr' => array(
				'label' => 'Приватность и cookie', 'engine' => 'Ориентировочная проверка',
				'findings' => array(
					'Баннер, политики и трекеры в начальном HTML в порядке.',
					'Механизм есть; пару пунктов стоит проверить вручную.',
					'Не хватает элементов или трекеры управляются плохо.',
					'Трекеры работают без баннера или нет политик: реальный юридический риск.',
				),
				'method' => 'Ориентировочная проверка Студии Ремарка по 4 сигналам — не юридическое заключение.',
				'todo'   => array( 'Блокируйте все нетехнические трекеры и cookie до согласия пользователя.', 'Сделайте ссылки на политику конфиденциальности и cookie видимыми на каждой странице.', 'Настройте баннер cookie так, чтобы «отклонить» было так же просто, как «принять».' ),
			),
			'bp' => array(
				'label' => 'Технические стандарты', 'engine' => 'Google PageSpeed',
				'findings' => array(
					'Технически чисто: HTTPS, консоль без ошибок, актуальные библиотеки.',
					'Хороший уровень; несколько предупреждений закрыть.',
					'Несколько технических предупреждений: безопасность, ошибки консоли, картинки.',
					'Много технических проблем, ослабляющих надёжность и безопасность.',
				),
				'method' => 'Измерение: Google PageSpeed Insights, мобильная стратегия Lighthouse.',
				'todo'   => array( 'Отдавайте сайт только по HTTPS, без смешанного контента.', 'Устраните ошибки и предупреждения JavaScript в консоли браузера.', 'Обновите сторонние библиотеки до поддерживаемых версий.' ),
			),
			'ai' => array(
				'label' => 'Готовность к ИИ', 'engine' => '4 технических сигнала',
				'findings' => array(
					'4 сигнала из 4: сайт читаем и цитируем ИИ-моделями.',
					'3 сигнала из 4: до полной готовности немного.',
					'2 сигнала из 4: доработать структурированные данные или sitemap.',
					'0–1 сигнал: ИИ-моделям трудно читать и цитировать сайт.',
				),
				'method' => 'Ориентировочная проверка Студии Ремарка по 4 техническим сигналам (llms.txt, robots, структурированные данные, sitemap).',
				'todo'   => array( 'Опубликуйте файл llms.txt с кратким описанием сайта.', 'Добавьте структурированные данные JSON-LD на основные страницы.', 'Проверьте, что ИИ-краулеры не заблокированы в robots.txt и что sitemap.xml актуален.' ),
			),
			'co2' => array(
				'label' => 'Углеродный след', 'engine' => 'Модель SWD',
				'findings' => array(
					'Лёгкая страница: выбросы ниже среднего по вебу.',
					'Около среднего; есть запас, чтобы облегчить.',
					'Выше среднего: страница тяжёлая при загрузке.',
					'Заметно выше среднего: тяжёлая страница, цена для экологии и скорости.',
				),
				'method' => 'Оценка по модели Sustainable Web Design, по объёму страницы, измеренному PageSpeed.',
				'todo'   => array( 'Сжимайте изображения и видео — это самая тяжёлая часть веса страницы.', 'Подключайте сторонние скрипты (чаты, трекеры) только при необходимости.', 'Включите кэширование/CDN, чтобы снизить объём данных при каждом визите.' ),
			),
		),
	);

	return $tables[ $locale ] ?? $tables['it'];
}

/** Colori di brand replicati da assets/css/remarka.css (:root) per il PDF. */
function remarka_checkup_pdf_colors(): array {
	return array(
		'carta'      => '#F7F6F2',
		'bianco'     => '#FFFFFF',
		'inchiostro' => '#14161A',
		'grigio'     => '#5A5E66',
		'bordo'      => '#DDDBD4',
		'traccia'    => '#EBEAE4',
		'oltremare'  => '#2440C8',
		'verde'      => '#1E7F4F',
		'ambra'      => '#C98A00',
		'rosso'      => '#CC3333',
	);
}

function remarka_checkup_flag_color( string $flag ): string {
	$c = remarka_checkup_pdf_colors();
	if ( 'good' === $flag ) {
		return $c['verde'];
	}
	if ( 'warn' === $flag ) {
		return $c['ambra'];
	}
	if ( 'bad' === $flag ) {
		return $c['rosso'];
	}
	return $c['bordo'];
}

/** Cerchio-semaforo HTML (dompdf: border-radius su div è supportato). */
function remarka_checkup_pdf_dot( string $flag ): string {
	$color = remarka_checkup_flag_color( $flag );
	return '<span class="dot" style="background:' . esc_attr( $color ) . '"></span>';
}

/**
 * Costruisce l'HTML completo del report (12 pagine) — separata dalla
 * conversione PDF apposta per essere testabile in isolamento (verifica che
 * ogni stringa di provenienza client, es. il dominio nell'url, esca sempre
 * via esc_html() e non possa iniettare markup nel report).
 * $data = array(url, scores[7], consent_monthly, date_display).
 */
function remarka_checkup_render_html( array $data, string $locale ): string {
	$copy    = remarka_checkup_copy( $locale );
	$company = remarka_checkup_company_data( $locale );
	$colors  = remarka_checkup_pdf_colors();
	$scores  = $data['scores'];
	$comp    = remarka_checkup_composite( $scores );
	$dims    = remarka_checkup_dimensions();

	$domain = preg_replace( '#^https?://#i', '', (string) $data['url'] );
	$domain = rtrim( $domain, '/' );

	ob_start();
	?>
	<!DOCTYPE html>
	<html>
	<head>
	<meta charset="utf-8">
	<style>
		@page { margin: 26mm 18mm 22mm 18mm; }
		* { box-sizing: border-box; }
		body { font-family: "DejaVu Sans", sans-serif; color: <?php echo esc_html( $colors['inchiostro'] ); ?>; font-size: 11.5px; line-height: 1.55; }
		h1, h2, h3 { font-family: "DejaVu Sans", sans-serif; font-weight: bold; margin: 0 0 10px; color: <?php echo esc_html( $colors['inchiostro'] ); ?>; }
		h1 { font-size: 22px; }
		h2 { font-size: 16px; }
		h3 { font-size: 12.5px; text-transform: uppercase; letter-spacing: 0.04em; color: <?php echo esc_html( $colors['grigio'] ); ?>; }
		p { margin: 0 0 8px; }
		.mono { font-family: "DejaVu Sans Mono", monospace; }
		.muted { color: <?php echo esc_html( $colors['grigio'] ); ?>; }
		.page { page-break-after: always; }
		.page:last-child { page-break-after: auto; }
		.brand { font-family: "DejaVu Sans Mono", monospace; letter-spacing: 0.12em; text-transform: uppercase; font-size: 10.5px; color: <?php echo esc_html( $colors['oltremare'] ); ?>; }
		.footer { position: fixed; bottom: -16mm; left: 0; right: 0; font-size: 8.5px; color: <?php echo esc_html( $colors['grigio'] ); ?>; text-align: center; }
		.dot { display: inline-block; width: 9px; height: 9px; border-radius: 5px; margin-right: 6px; }
		table { width: 100%; border-collapse: collapse; }
		table.summary th, table.summary td { border-bottom: 1px solid <?php echo esc_html( $colors['bordo'] ); ?>; padding: 7px 4px; text-align: left; font-size: 11px; }
		table.summary th { font-family: "DejaVu Sans Mono", monospace; text-transform: uppercase; font-size: 9px; letter-spacing: 0.05em; color: <?php echo esc_html( $colors['grigio'] ); ?>; }
		.cover { text-align: center; padding-top: 70mm; }
		.cover .brand { font-size: 13px; }
		.cover h1 { font-size: 30px; margin-top: 18px; }
		.cover .domain { font-size: 15px; margin-top: 10px; }
		.badge { display: inline-block; margin-top: 26px; padding: 16px 26px; border: 2px solid <?php echo esc_html( $colors['inchiostro'] ); ?>; border-radius: 12px; }
		.badge .num { font-family: "DejaVu Sans Mono", monospace; font-size: 40px; font-weight: bold; }
		.dim-head { border-bottom: 2px solid <?php echo esc_html( $colors['inchiostro'] ); ?>; padding-bottom: 10px; margin-bottom: 16px; }
		.dim-score { font-family: "DejaVu Sans Mono", monospace; font-size: 30px; font-weight: bold; }
		.box { border: 1px solid <?php echo esc_html( $colors['bordo'] ); ?>; border-radius: 8px; padding: 14px 16px; margin-top: 12px; background: <?php echo esc_html( $colors['carta'] ); ?>; }
		.pri-row { border-bottom: 1px solid <?php echo esc_html( $colors['bordo'] ); ?>; padding: 10px 0; }
		.pri-idx { font-family: "DejaVu Sans Mono", monospace; font-size: 16px; color: <?php echo esc_html( $colors['oltremare'] ); ?>; }
		ul { margin: 0 0 8px 16px; padding: 0; }
		li { margin-bottom: 4px; }
		a { color: <?php echo esc_html( $colors['oltremare'] ); ?>; }
	</style>
	</head>
	<body>
	<div class="footer"><span class="mono"><?php echo esc_html( $copy['footer_note'] ); ?> · <?php echo esc_html( $domain ); ?></span></div>

	<?php /* ---------- 1. Copertina ---------- */ ?>
	<div class="page cover">
		<p class="brand">Studio Remarka</p>
		<h1><?php echo esc_html( $copy['cover_title'] ); ?></h1>
		<p class="domain mono"><?php echo esc_html( $copy['cover_domain'] ); ?>: <?php echo esc_html( $domain ); ?></p>
		<p class="mono muted"><?php echo esc_html( $copy['cover_date'] ); ?>: <?php echo esc_html( $data['date_display'] ); ?></p>
		<div class="badge">
			<?php if ( null !== $comp['composite'] ) : ?>
				<div class="num"><?php echo esc_html( (string) $comp['composite'] ); ?>/100</div>
				<div class="mono"><?php echo esc_html( $copy['composite_labels'][ remarka_checkup_level( $comp['composite'] ) ] ); ?></div>
			<?php else : ?>
				<div class="mono"><?php echo esc_html( $copy['na_word'] ); ?></div>
			<?php endif; ?>
		</div>
		<?php if ( $comp['measured'] < 7 ) : ?>
			<p class="mono muted" style="margin-top:14px"><?php echo esc_html( str_replace( '{n}', (string) $comp['measured'], $copy['cover_partial'] ) ); ?></p>
		<?php endif; ?>
	</div>

	<?php /* ---------- 2. Riepilogo ---------- */ ?>
	<div class="page">
		<h1><?php echo esc_html( $copy['summary_h1'] ); ?></h1>
		<table class="summary">
			<thead><tr>
				<th><?php echo esc_html( $copy['summary_th'][0] ); ?></th>
				<th><?php echo esc_html( $copy['summary_th'][1] ); ?></th>
				<th><?php echo esc_html( $copy['summary_th'][2] ); ?></th>
				<th><?php echo esc_html( $copy['summary_th'][3] ); ?></th>
			</tr></thead>
			<tbody>
			<?php foreach ( $dims as $key => $weight ) :
				$score = $scores[ $key ] ?? null;
				?>
				<tr>
					<td><?php echo esc_html( $copy['dims'][ $key ]['label'] ); ?></td>
					<td class="mono"><?php echo esc_html( (string) $weight ); ?></td>
					<?php if ( null === $score ) : ?>
						<td class="mono"><?php echo esc_html( $copy['na_word'] ); ?></td>
						<td><?php echo remarka_checkup_pdf_dot( 'na' ); ?><?php echo esc_html( $copy['na_word'] ); ?></td>
					<?php else :
						$level = remarka_checkup_level( (int) $score );
						?>
						<td class="mono"><?php echo esc_html( (string) $score ); ?>/100</td>
						<td><?php echo remarka_checkup_pdf_dot( remarka_checkup_flag( $level ) ); ?><?php echo esc_html( $copy['words'][ $level ] ); ?></td>
					<?php endif; ?>
				</tr>
			<?php endforeach; ?>
			</tbody>
		</table>
		<?php
		$n_bad  = 0;
		$n_warn = 0;
		foreach ( $dims as $key => $weight ) {
			$score = $scores[ $key ] ?? null;
			if ( null === $score ) {
				continue;
			}
			$level = remarka_checkup_level( (int) $score );
			if ( 3 === $level ) {
				++$n_bad;
			} elseif ( 2 === $level ) {
				++$n_warn;
			}
		}
		?>
		<p class="box mono">
			<?php
			if ( null !== $comp['composite'] ) {
				echo esc_html( $copy['composite_labels'][ remarka_checkup_level( $comp['composite'] ) ] );
			}
			?>
			 — <?php echo esc_html( sprintf( '%d/7', $comp['measured'] ) ); ?>
			<?php if ( $n_bad > 0 || $n_warn > 0 ) : ?>
				 (<?php echo esc_html( (string) $n_bad ); ?>× <?php echo esc_html( $copy['words'][3] ); ?>, <?php echo esc_html( (string) $n_warn ); ?>× <?php echo esc_html( $copy['words'][2] ); ?>)
			<?php endif; ?>
		</p>
	</div>

	<?php /* ---------- 3-9. Una pagina per dimensione ---------- */ ?>
	<?php foreach ( $dims as $key => $weight ) :
		$dim_copy = $copy['dims'][ $key ];
		$score    = $scores[ $key ] ?? null;
		?>
		<div class="page">
			<div class="dim-head">
				<h3 style="margin-bottom:2px"><?php echo esc_html( $dim_copy['engine'] ); ?> · <?php echo esc_html( sprintf( '%s %d', 'it' === $locale ? 'Peso' : ( 'ru' === $locale ? 'Вес' : 'Weight' ), $weight ) ); ?></h3>
				<h1 style="margin-bottom:8px"><?php echo esc_html( $dim_copy['label'] ); ?></h1>
				<?php if ( null === $score ) : ?>
					<div class="dim-score"><?php echo remarka_checkup_pdf_dot( 'na' ); ?><?php echo esc_html( $copy['na_word'] ); ?></div>
				<?php else :
					$level = remarka_checkup_level( (int) $score );
					?>
					<div class="dim-score"><?php echo remarka_checkup_pdf_dot( remarka_checkup_flag( $level ) ); ?><?php echo esc_html( (string) $score ); ?><span style="font-size:16px"><?php echo esc_html( $copy['dim_score_suffix'] ); ?></span> — <?php echo esc_html( $copy['words'][ $level ] ); ?></div>
				<?php endif; ?>
			</div>

			<h3><?php echo esc_html( $copy['dim_found_h3'] ); ?></h3>
			<p><?php echo esc_html( null === $score ? $copy['na_finding'] : $dim_copy['findings'][ remarka_checkup_level( (int) $score ) ] ); ?></p>

			<h3 style="margin-top:14px"><?php echo esc_html( $copy['dim_todo_h3'] ); ?></h3>
			<ul>
				<?php foreach ( $dim_copy['todo'] as $item ) : ?>
					<li><?php echo esc_html( $item ); ?></li>
				<?php endforeach; ?>
			</ul>

			<p class="mono muted" style="margin-top:14px"><?php echo esc_html( $dim_copy['method'] ); ?></p>
		</div>
	<?php endforeach; ?>

	<?php /* ---------- 10. I 3 interventi prioritari ---------- */ ?>
	<div class="page">
		<h1><?php echo esc_html( $copy['priorities_h1'] ); ?></h1>
		<p class="muted"><?php echo esc_html( $copy['priorities_lead'] ); ?></p>
		<?php foreach ( remarka_checkup_priorities( $scores, $copy ) as $i => $p ) : ?>
			<div class="pri-row">
				<table><tr>
					<td style="width:34px;vertical-align:top"><span class="pri-idx">0<?php echo esc_html( (string) ( $i + 1 ) ); ?></span></td>
					<td>
						<p style="font-weight:bold"><?php echo remarka_checkup_pdf_dot( $p['flag'] ); ?><?php echo esc_html( $p['label'] . ' · ' . $p['word'] ); ?></p>
						<p class="muted"><?php echo esc_html( $p['finding'] ); ?></p>
					</td>
				</tr></table>
			</div>
		<?php endforeach; ?>
	</div>

	<?php /* ---------- 11. Cosa faremmo noi ---------- */ ?>
	<div class="page">
		<h1><?php echo esc_html( $copy['whatwedo_h1'] ); ?></h1>
		<p style="font-size:13px;line-height:1.7;max-width:120mm"><?php echo esc_html( $copy['whatwedo_text'] ); ?></p>
		<?php if ( ! empty( $data['consent_monthly'] ) ) : ?>
			<p class="box"><?php echo esc_html( $copy['monthly_note'] ); ?></p>
		<?php endif; ?>
		<p class="box mono" style="margin-top:22px"><?php echo esc_html( $copy['whatwedo_cta'] ); ?> → <?php echo esc_html( $copy['cta_full_url'] ); ?></p>
	</div>

	<?php /* ---------- 12. Chi ha preparato questo report (E-E-A-T) ---------- */ ?>
	<div class="page">
		<h1><?php echo esc_html( $copy['eeat_h1'] ); ?></h1>
		<p style="font-size:12.5px;line-height:1.7;max-width:130mm"><?php echo esc_html( $copy['eeat_intro'] ); ?></p>

		<h3 style="margin-top:18px"><?php echo esc_html( $copy['eeat_sedi_label'] ); ?></h3>
		<?php foreach ( $company['address'] as $line ) : ?>
			<p class="mono"><?php echo esc_html( $line ); ?></p>
		<?php endforeach; ?>

		<p class="mono" style="margin-top:10px">
			<?php
			$tax_bits = array();
			foreach ( $company['tax'] as $pair ) {
				$tax_bits[] = $pair[0] . ' ' . $pair[1];
			}
			echo esc_html( implode( ' · ', $tax_bits ) );
			?>
		</p>
		<p class="mono"><?php echo esc_html( $company['email'] ); ?> · <?php echo esc_html( $company['phone_display'] ); ?></p>

		<h2 style="margin-top:26px"><?php echo esc_html( $copy['eeat_method_h2'] ); ?></h2>
		<p class="muted" style="font-size:11px;line-height:1.7"><?php echo esc_html( $copy['eeat_method_text'] ); ?></p>
	</div>

	</body>
	</html>
	<?php
	return (string) ob_get_clean();
}

/**
 * Converte l'HTML del report in PDF con dompdf (bundle locale, vedi
 * lib/dompdf/VERSIONS.md). Ritorna la stringa binaria del PDF, o null se le
 * estensioni PHP richieste mancano (il chiamante gestisce l'errore in modo
 * grazioso via JSON, § remarka_checkup_pdf_missing_extensions()).
 */
function remarka_checkup_render_pdf( array $data, string $locale ): ?string {
	if ( ! empty( remarka_checkup_pdf_missing_extensions() ) ) {
		return null;
	}

	require_once get_stylesheet_directory() . '/lib/dompdf/autoload.php';

	$html = remarka_checkup_render_html( $data, $locale );

	$upload_dir = wp_upload_dir();
	$font_dir   = trailingslashit( $upload_dir['basedir'] ) . 'checkup-reports/fonts';
	wp_mkdir_p( $font_dir );

	$options = new \Dompdf\Options();
	$options->setFontDir( $font_dir );
	$options->setFontCache( $font_dir );
	$options->setDefaultFont( 'DejaVu Sans' );
	$options->setIsRemoteEnabled( false );
	$options->setIsHtml5ParserEnabled( true );
	$options->setChroot( get_stylesheet_directory() . '/lib/dompdf' );

	$dompdf  = new \Dompdf\Dompdf( $options );
	$bundled = get_stylesheet_directory() . '/lib/dompdf/dompdf/lib/fonts';
	$fm      = $dompdf->getFontMetrics();
	$fm->registerFont( array( 'family' => 'DejaVu Sans', 'style' => 'normal', 'weight' => 'normal' ), $bundled . '/DejaVuSans.ttf' );
	$fm->registerFont( array( 'family' => 'DejaVu Sans', 'style' => 'normal', 'weight' => 'bold' ), $bundled . '/DejaVuSans-Bold.ttf' );
	$fm->registerFont( array( 'family' => 'DejaVu Sans Mono', 'style' => 'normal', 'weight' => 'normal' ), $bundled . '/DejaVuSansMono.ttf' );
	$fm->registerFont( array( 'family' => 'DejaVu Sans Mono', 'style' => 'normal', 'weight' => 'bold' ), $bundled . '/DejaVuSansMono.ttf' );

	$dompdf->loadHtml( $html );
	$dompdf->setPaper( 'A4', 'portrait' );
	$dompdf->render();

	return $dompdf->output();
}

/** Oggetto e corpo dell'e-mail di consegna, per lingua (docs/copy-checkup.md §2.4/3.4/4.4). */
function remarka_checkup_email_subject( string $locale, string $domain ): string {
	$copy = remarka_checkup_copy( $locale );
	return str_replace( '{domain}', $domain, $copy['email_subject'] );
}

function remarka_checkup_email_body( string $locale, string $domain, ?int $score ): string {
	$copy       = remarka_checkup_copy( $locale );
	$score_text = null === $score ? 'N/D' : (string) $score;
	$body       = str_replace(
		array( '{domain}', '{score}', '{cta_url}' ),
		array( $domain, $score_text, $copy['cta_full_url'] ),
		$copy['email_body']
	);
	return $body;
}
