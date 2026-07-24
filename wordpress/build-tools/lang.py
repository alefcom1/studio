"""Языковая карта сайта: слаги и пути IT → EN → RU.

Единый источник для: (1) генератора страниц (--lang en/ru), (2) PHP-карты
hreflang/переключателя языка (emit_php_lang_map), (3) deploy-import.

Архитектура (concept §8): итальянский в корне, /en/ и /ru/ — деревья
вложенных страниц WordPress (без мультиязычных плагинов). Городские
лендинги кроме Milano не переводятся — это ниши итальянского локального
поиска (piano-contenuti-seo §2).
"""

# Разделы (родительские страницы).
SECTIONS = {
    'servizi':     {'en': 'services',      'ru': 'uslugi'},
    'casi-studio': {'en': 'case-studies',  'ru': 'kejsy'},
    'strumenti':   {'en': 'tools',         'ru': 'instrumenty'},
    'blog':        {'en': 'blog',          'ru': 'blog'},
}

# Одиночные страницы верхнего уровня.
SINGLES = {
    'prezzi':            {'en': 'pricing',            'ru': 'ceny'},
    'brief':             {'en': 'brief',              'ru': 'brif'},
    'milano':            {'en': 'milan',              'ru': 'milan'},
    'chi-siamo':         {'en': 'about',              'ru': 'o-studii'},
    'area-clienti':      {'en': 'client-area',        'ru': 'kabinet-klienta'},
    'privacy':           {'en': 'privacy',            'ru': 'privacy'},
    'cookie-policy':     {'en': 'cookie-policy',      'ru': 'cookie-policy'},
    'cookie-preferenze': {'en': 'cookie-preferences', 'ru': 'cookie-preferences'},
}

SERVICES_SLUGS = {
    'siti-aziendali':       {'en': 'business-websites',     'ru': 'korporativnye-sajty'},
    'e-commerce':           {'en': 'e-commerce',            'ru': 'internet-magaziny'},
    'siti-pwa':             {'en': 'progressive-web-apps',  'ru': 'pwa-sajty'},
    'restyling-migrazione': {'en': 'redesign-migration',    'ru': 'redizajn-i-migracija'},
    'seo-tecnica':          {'en': 'technical-seo',         'ru': 'tehnicheskoe-seo'},
    'siti-multilingue':     {'en': 'multilingual-websites', 'ru': 'mnogojazychnye-sajty'},
    'export-ready':         {'en': 'export-ready',          'ru': 'export-ready'},
    'web-app':              {'en': 'custom-web-apps',       'ru': 'veb-prilozhenija'},
    'adeguamento-eaa':      {'en': 'eaa-compliance',        'ru': 'dostupnost-eaa'},
}

# Casi studio: oltre al catalogo unico con schede-àncora, dal 21.07.2026
# esistono di nuovo pagine dedicate /casi-studio/<slug>/ per i progetti REALI
# del gruppo (approfondimenti tecnici, forte SEO). La foglia dello slug è
# uguale nelle tre lingue; cambia solo il genitore localizzato (casi-studio /
# case-studies / kejsy), gestito da paths_for(). Le pagine EN/RU sono tradotte
# a mano (translate_pages SKIP), ma lo slug qui serve a href-map e hreflang.
CASES_SLUGS = {
    'tms-perevod4': {'en': 'tms-perevod4', 'ru': 'tms-perevod4'},
    '1russian':     {'en': '1russian',     'ru': '1russian'},
    'att':          {'en': 'att',          'ru': 'att'},
    'remarka-ai':   {'en': 'remarka-ai',    'ru': 'remarka-ai'},
    'mini-app-telegram': {'en': 'mini-app-telegram', 'ru': 'mini-app-telegram'},
    'pere-rf': {'en': 'pere-rf', 'ru': 'pere-rf'},
    'perevod4-catalogo': {'en': 'perevod4-catalogo', 'ru': 'perevod4-catalogo'},
    'moscowtrans-techperevod': {'en': 'moscowtrans-techperevod', 'ru': 'moscowtrans-techperevod'},
    'ukrinitsy': {'en': 'ukrinitsy', 'ru': 'ukrinitsy'},
    'gioco': {'en': 'gioco', 'ru': 'gioco'},
    'test-traduttori': {'en': 'test-traduttori', 'ru': 'test-traduttori'},
}

TOOLS_SLUGS = {
    'test-velocita':          {'en': 'speed-test',           'ru': 'test-skorosti'},
    'check-gdpr':             {'en': 'gdpr-check',           'ru': 'proverka-gdpr'},
    'analisi-seo':            {'en': 'seo-audit',            'ru': 'seo-audit'},
    'roi-localizzazione':     {'en': 'localization-roi',     'ru': 'roi-lokalizacii'},
    'verifica-accessibilita': {'en': 'accessibility-check',  'ru': 'proverka-dostupnosti'},
    'sito-pronto-ai':         {'en': 'ai-readiness',         'ru': 'gotovnost-k-ii'},
    'impatto-co2':            {'en': 'website-carbon',       'ru': 'uglerodnyj-sled'},
    'check-up-completo':      {'en': 'full-site-checkup',    'ru': 'polnaya-proverka-sajta'},
    'segnali-eeat':           {'en': 'eeat-signals',         'ru': 'signaly-eeat'},
    'sito-letto-dallai':      {'en': 'read-by-ai',           'ru': 'sajt-glazami-ii'},
    'suona-madrelingua':      {'en': 'does-it-sound-native', 'ru': 'zvuchit-kak-u-nositelya'},
    'generatore-llms-txt':    {'en': 'llms-txt-generator',   'ru': 'generator-llms-txt'},
}

BLOG_SLUGS = {
    # SEO gap-fill (cluster e-commerce, siti-aziendali) — IT+EN-only.
    'piattaforma-ecommerce-quale-scegliere': {'en': 'which-ecommerce-platform', 'ru': 'kakuju-platformu-ecommerce'},
    'ecommerce-checklist-prima-del-lancio': {'en': 'ecommerce-pre-launch-checklist', 'ru': 'chek-list-pered-zapuskom-magazina'},
    'cosa-include-sito-aziendale': {'en': 'what-a-business-website-includes', 'ru': 'chto-vhodit-v-korporativnyj-sajt'},
    'sito-quattro-lingue-costi-tempi':      {'en': 'website-four-languages-costs',        'ru': 'sajt-na-4-jazykah'},
    'cookie-banner-checklist-garante-2026': {'en': 'cookie-banner-compliance-italy-2026', 'ru': 'cookie-banner-trebovanija-2026'},
    'migrare-wordpress-senza-perdere-seo':  {'en': 'migrate-wordpress-without-losing-seo', 'ru': 'migracija-wordpress-bez-poteri-seo'},
    'pwa-per-pmi-quando-app-non-serve':     {'en': 'pwa-for-smbs',                        'ru': 'pwa-dlja-biznesa'},
    'quanto-costa-sito-aziendale-italia':   {'en': 'business-website-cost-italy',         'ru': 'skolko-stoit-sajt-v-italii'},
    'core-web-vitals-2026':                 {'en': 'core-web-vitals-2026',                'ru': 'core-web-vitals-2026'},
    'quanto-costa-ecommerce-italia':        {'en': 'ecommerce-cost-italy-2026',           'ru': 'skolko-stoit-internet-magazin'},
    'sito-lento-cause-costi':               {'en': 'slow-website-causes-fixes',           'ru': 'medlennyj-sajt-prichiny'},
    # Blog · Batch 1 — pubblicati in IT + EN. La versione RU del blog è un
    # batch separato con articoli propri (piano-blog.md, batch 5–6), non una
    # traduzione: fino ad allora questi articoli sono IT+EN-only (vedi
    # BLOG_IT_EN_ONLY: hreflang/switcher RU puntano all'indice /ru/blog/,
    # nessun 404). Gli slug RU pianificati restano qui per il batch futuro.
    'european-accessibility-act-ecommerce': {'en': 'eaa-ecommerce-risks',                 'ru': 'dostupnost-eaa-internet-magazin'},
    'llms-txt-cos-e':                       {'en': 'llms-txt-explained',                  'ru': 'chto-takoe-llms-txt'},
    'farsi-trovare-da-chatgpt-geo':         {'en': 'get-cited-by-chatgpt-geo',            'ru': 'kak-popast-v-chatgpt'},
    'check-up-sito-web-7-misure':           {'en': 'website-checkup-7-metrics',           'ru': 'chek-ap-sajta-7-pokazatelej'},
    'eeat-come-google-giudica-credibilita': {'en': 'eeat-how-google-judges-credibility',  'ru': 'eeat-kak-google-ocenivaet'},
    # Blog · Batch 2 — IT + EN (RU è un batch a sé: slug RU pianificati, IT+EN-only).
    'preventivo-sito-web-come-leggerlo':    {'en': 'website-quote-how-to-read-it',        'ru': 'kak-chitat-smetu-na-sajt'},
    'sito-web-in-3-settimane':              {'en': 'website-in-3-weeks',                  'ru': 'sajt-za-3-nedeli'},
    'restyling-o-sito-nuovo-5-domande':     {'en': 'redesign-or-new-website-5-questions', 'ru': 'redizajn-ili-novyj-sajt'},
    'impatto-ambientale-sito-web':          {'en': 'website-environmental-impact',        'ru': 'ekologicheskij-sled-sajta'},
    'dichiarazione-di-accessibilita-guida-2026': {'en': 'accessibility-statement-guide-2026', 'ru': 'deklaracija-o-dostupnosti-2026'},
    # Blog · Batch 3 — IT + EN (RU è un batch a sé: slug RU pianificati, IT+EN-only).
    'telegram-mini-app-business':           {'en': 'telegram-mini-app-for-business',       'ru': 'telegram-mini-app-dlja-biznesa'},
    'gestionale-su-misura-vs-excel':        {'en': 'custom-management-software-vs-excel',  'ru': 'gestionale-vs-excel'},
    'dati-strutturati-schema-org':          {'en': 'schema-org-structured-data-for-smes',  'ru': 'schema-org-mikrorazmetka'},
    'gamification-b2b':                      {'en': 'gamification-in-b2b',                  'ru': 'gejmifikacija-v-b2b'},
    'hosting-sito-web-italia':              {'en': 'website-hosting-italy-vs-cloud',       'ru': 'hosting-v-italii-ili-oblako'},
    # Blog · Batch 4 — IT + EN (RU è un batch a sé: slug RU pianificati, IT+EN-only).
    'seo-locale-milano':                    {'en': 'local-seo-milan',                     'ru': 'lokalnoe-seo-milan'},
    'google-business-profile-guida':        {'en': 'google-business-profile-guide',        'ru': 'google-business-profile-gid'},
    'hreflang-sito-multilingue':            {'en': 'hreflang-multilingual-website',        'ru': 'hreflang-mnogojazychnyj-sajt'},
    'sito-per-export':                      {'en': 'website-for-export',                   'ru': 'sajt-dlja-eksporta'},
    'manutenzione-wordpress':               {'en': 'wordpress-maintenance',                'ru': 'obsluzhivanie-wordpress'},
    # Sputnik area clienti + Lab Monitor — IT + EN (RU è un batch a sé).
    'area-clienti-agenzia-web':             {'en': 'web-agency-client-portal',             'ru': 'kabinet-klienta-veb-studii'},
    'monitoraggio-sito-dopo-lancio':        {'en': 'website-monitoring-after-launch',      'ru': 'monitoring-sajta-posle-zapuska'},
    # Blog · Batch 7 (seconda ondata) — IT + EN (RU è un batch a sé: slug RU pianificati, IT+EN-only).
    'perche-il-sito-non-converte':          {'en': 'why-your-website-doesnt-convert',      'ru': 'pochemu-sajt-ne-konvertiruet'},
    'landing-page-che-converte':            {'en': 'landing-page-that-converts',           'ru': 'landing-pejdzh-konversija'},
    'recensioni-riprova-sociale-onesta':    {'en': 'reviews-social-proof-done-right',      'ru': 'otzyvy-socialnoe-dokazatelstvo'},
    'whatsapp-business-pmi':                {'en': 'whatsapp-business-for-smes',           'ru': 'whatsapp-business-dlja-biznesa'},
    'copywriting-sito-web-prima-del-design': {'en': 'website-copywriting-before-design',    'ru': 'kopirajting-sajta-tekst-pered-dizajnom'},
    # Blog · Batch 8 (seconda ondata) — IT + EN (RU è un batch a sé: slug RU pianificati, IT+EN-only).
    'consent-mode-v2-cosa-cambia':          {'en': 'consent-mode-v2-what-changes',         'ru': 'consent-mode-v2-chto-menjaetsja'},
    'google-analytics-4-privacy-ue':        {'en': 'google-analytics-4-gdpr-eu',           'ru': 'google-analytics-4-gdpr'},
    'alternative-google-analytics-privacy': {'en': 'privacy-first-google-analytics-alternatives', 'ru': 'privacy-alternativy-google-analytics'},
    'cookie-policy-o-privacy-policy':       {'en': 'cookie-policy-vs-privacy-policy',       'ru': 'cookie-i-privacy-politika'},
    'backup-e-sicurezza-sito-web':          {'en': 'website-backup-and-security',           'ru': 'rezervnoe-kopirovanie-i-bezopasnost-sajta'},
    # Blog · Batch 9 (seconda ondata) — IT + EN (RU è un batch a sé: slug RU pianificati, IT+EN-only).
    'ai-overviews-google-restare-visibili': {'en': 'google-ai-overviews-stay-visible',      'ru': 'ai-overviews-google-vidimost'},
    'inp-metrica-core-web-vitals':          {'en': 'inp-core-web-vitals-metric',            'ru': 'inp-metrika-core-web-vitals'},
    'autorevolezza-tematica-batte-keyword': {'en': 'topical-authority-beats-keywords',      'ru': 'tematicheskij-avtoritet-seo'},
    'link-interni-seo-gratis':              {'en': 'internal-links-free-seo',               'ru': 'vnutrennie-ssylki-seo'},
    'immagini-velocita-webp-lazy-load':     {'en': 'image-optimization-webp-lazy-load',     'ru': 'optimizacija-izobrazhenij-sajta'},
    # Blog · Batch 10 (seconda ondata) — IT + EN (RU è un batch a sé: slug RU pianificati, IT+EN-only).
    'seo-locale-roma':                      {'en': 'local-seo-rome',                        'ru': 'lokalnoe-seo-rim'},
    'seo-locale-torino':                    {'en': 'local-seo-turin',                       'ru': 'lokalnoe-seo-turin'},
    'napoli-turismo-sito-multilingue':      {'en': 'naples-tourism-multilingual-website',   'ru': 'napoli-turizm-mnogojazychnyj-sajt'},
    'traduzione-madrelingua-vs-ai':         {'en': 'native-translation-vs-ai',              'ru': 'perevod-nositelem-vs-ai'},
    'roi-localizzazione-sito':              {'en': 'localization-roi',                      'ru': 'roi-lokalizacii-sajta'},
}

# Articoli del blog pubblicati solo in IT + EN in questa fase (la loro versione
# RU è un batch a sé, non una traduzione). Per questi, all_page_paths non emette
# una riga hreflang verso una pagina RU inesistente: la colonna RU rimanda
# all'indice /ru/blog/ (pagina reale), così switcher e hreflang restano validi.
BLOG_IT_EN_ONLY = {
    # SEO gap-fill
    'piattaforma-ecommerce-quale-scegliere',
    'ecommerce-checklist-prima-del-lancio',
    'cosa-include-sito-aziendale',
    'european-accessibility-act-ecommerce',
    'llms-txt-cos-e',
    'farsi-trovare-da-chatgpt-geo',
    'check-up-sito-web-7-misure',
    'eeat-come-google-giudica-credibilita',
    # Batch 2
    'preventivo-sito-web-come-leggerlo',
    'sito-web-in-3-settimane',
    'restyling-o-sito-nuovo-5-domande',
    'impatto-ambientale-sito-web',
    'dichiarazione-di-accessibilita-guida-2026',
    # Batch 3
    'telegram-mini-app-business',
    'gestionale-su-misura-vs-excel',
    'dati-strutturati-schema-org',
    'gamification-b2b',
    'hosting-sito-web-italia',
    # Batch 4
    'seo-locale-milano',
    'google-business-profile-guida',
    'hreflang-sito-multilingue',
    'sito-per-export',
    'manutenzione-wordpress',
    # Sputnik area clienti + Lab Monitor
    'area-clienti-agenzia-web',
    'monitoraggio-sito-dopo-lancio',
    # Batch 7 (seconda ondata)
    'perche-il-sito-non-converte',
    'landing-page-che-converte',
    'recensioni-riprova-sociale-onesta',
    'whatsapp-business-pmi',
    'copywriting-sito-web-prima-del-design',
    # Batch 8 (seconda ondata)
    'consent-mode-v2-cosa-cambia',
    'google-analytics-4-privacy-ue',
    'alternative-google-analytics-privacy',
    'cookie-policy-o-privacy-policy',
    'backup-e-sicurezza-sito-web',
    # Batch 9 (seconda ondata)
    'ai-overviews-google-restare-visibili',
    'inp-metrica-core-web-vitals',
    'autorevolezza-tematica-batte-keyword',
    'link-interni-seo-gratis',
    'immagini-velocita-webp-lazy-load',
    # Batch 10 (seconda ondata)
    'seo-locale-roma',
    'seo-locale-torino',
    'napoli-turismo-sito-multilingue',
    'traduzione-madrelingua-vs-ai',
    'roi-localizzazione-sito',
}

# Blog · Batch 5 — RU-only (scritti a mano in russo, senza specchio IT/EN;
# translate_pages.py ru è vietato per sempre). Speculare a BLOG_IT_EN_ONLY:
# la pagina esiste SOLO in RU. Per hreflang/switcher, IT ed EN puntano ai
# rispettivi indici blog (/blog/, /en/blog/) — pagine reali, nessun 404;
# RU punta all'articolo. Chiave = slug-foglia RU; valore = data (ISO) e
# copertina, usati da build_blog_schema_map (JSON-LD BlogPosting). Questi
# articoli NON stanno in BLOG_POSTS/BLOG_SLUGS: non hanno una versione
# italiana da cui derivare, il loro contenuto è nei pattern ru-blog-*.php.
BLOG_RU_ONLY = {
    'sajt-dlya-vyhoda-na-rynok-italii':       {'date': '2026-07-19', 'image': '/wp-content/themes/remarka-studio/assets/img/blog/batch5-mercato-cover.svg'},
    'seo-v-italii-po-russki':                 {'date': '2026-07-19', 'image': '/wp-content/themes/remarka-studio/assets/img/blog/batch5-seo-cover.svg'},
    'gdpr-dlya-russkoyazychnogo-biznesa-v-es': {'date': '2026-07-19', 'image': '/wp-content/themes/remarka-studio/assets/img/blog/batch5-gdpr-cover.svg'},
    'perevesti-ili-lokalizovat-sajt':         {'date': '2026-07-19', 'image': '/wp-content/themes/remarka-studio/assets/img/blog/batch5-loc-cover.svg'},
    'cena-sajta-v-italii':                    {'date': '2026-07-19', 'image': '/wp-content/themes/remarka-studio/assets/img/blog/batch5-cena-cover.svg'},
    # Batch 6 — RU-only (prodotti e fiducia, scritti a mano in russo).
    'telegram-prilozhenie-dlya-biznesa-v-evrope': {'date': '2026-07-20', 'image': '/wp-content/themes/remarka-studio/assets/img/blog/batch6-tg-cover.svg'},
    'kak-proverit-veb-studiyu':               {'date': '2026-07-20', 'image': '/wp-content/themes/remarka-studio/assets/img/blog/batch6-fiducia-cover.svg'},
    'zakon-o-dostupnosti-sajtov':             {'date': '2026-07-20', 'image': '/wp-content/themes/remarka-studio/assets/img/blog/batch6-eaa-cover.svg'},
    'sajt-v-chatgpt':                         {'date': '2026-07-20', 'image': '/wp-content/themes/remarka-studio/assets/img/blog/batch6-chatgpt-cover.svg'},
    'russkoyazychnaya-auditoriya-v-evrope':   {'date': '2026-07-20', 'image': '/wp-content/themes/remarka-studio/assets/img/blog/batch6-rus-cover.svg'},
    # Batch 11 — RU-only (vendite e fiducia, scritti a mano in russo).
    'pochemu-sajt-ne-prinosit-zayavok':       {'date': '2026-07-25', 'image': '/wp-content/themes/remarka-studio/assets/img/blog/batch11-utechki-cover.svg'},
    'otzyvy-i-reputaciya-v-italii':           {'date': '2026-07-25', 'image': '/wp-content/themes/remarka-studio/assets/img/blog/batch11-otzyvy-cover.svg'},
    'whatsapp-dlya-biznesa-v-evrope':         {'date': '2026-07-25', 'image': '/wp-content/themes/remarka-studio/assets/img/blog/batch11-whatsapp-cover.svg'},
    'reklama-ili-seo-s-chego-nachat':         {'date': '2026-07-25', 'image': '/wp-content/themes/remarka-studio/assets/img/blog/batch11-seo-reklama-cover.svg'},
    'kak-prinyat-oplatu-na-sajte':            {'date': '2026-07-25', 'image': '/wp-content/themes/remarka-studio/assets/img/blog/batch11-oplata-cover.svg'},
}


def slug_for(kind, it_slug, lang):
    """kind: section|single|service|case|tool|blog; lang: it|en|ru."""
    if lang == 'it':
        return it_slug
    table = {
        'section': SECTIONS, 'single': SINGLES, 'service': SERVICES_SLUGS,
        'case': CASES_SLUGS, 'tool': TOOLS_SLUGS, 'blog': BLOG_SLUGS,
    }[kind]
    return table[it_slug][lang]


def prefix(lang):
    return '' if lang == 'it' else f'/{lang}'


def paths_for(lang):
    """Готовые URL-хелперы для генератора."""
    p = prefix(lang)
    sec = {k: slug_for('section', k, lang) for k in SECTIONS}
    sng = {k: slug_for('single', k, lang) for k in SINGLES}
    return dict(
        home=f'{p}/' if p else '/',
        contatti=f'{p}/#contatti' if p else '/#contatti',
        servizi=f'{p}/{sec["servizi"]}/',
        casi=f'{p}/{sec["casi-studio"]}/',
        strumenti=f'{p}/{sec["strumenti"]}/',
        blog=f'{p}/{sec["blog"]}/',
        prezzi=f'{p}/{sng["prezzi"]}/',
        servizio=lambda s: f'{p}/{sec["servizi"]}/{slug_for("service", s, lang)}/',
        caso=lambda s: f'{p}/{sec["casi-studio"]}/{slug_for("case", s, lang)}/',
        strumento=lambda s: f'{p}/{sec["strumenti"]}/{slug_for("tool", s, lang)}/',
        articolo=lambda s: f'{p}/{sec["blog"]}/{slug_for("blog", s, lang)}/',
    )


def all_page_paths():
    """[(it_path, en_path, ru_path), ...] для hreflang-карты.

    Пути БЕЗ ведущего слеша (как get_page_by_path / page_uri WordPress).
    Первая строка — Home (пустой путь IT ↔ 'en' ↔ 'ru').
    """
    rows = [('', 'en', 'ru')]

    def row(it_path, en_path, ru_path):
        rows.append((it_path, f'en/{en_path}', f'ru/{ru_path}'))

    for it_slug, tr in SECTIONS.items():
        row(it_slug, tr['en'], tr['ru'])
    for it_slug, tr in SINGLES.items():
        row(it_slug, tr['en'], tr['ru'])
    for it_slug, tr in SERVICES_SLUGS.items():
        row(f'servizi/{it_slug}', f'{SECTIONS["servizi"]["en"]}/{tr["en"]}', f'{SECTIONS["servizi"]["ru"]}/{tr["ru"]}')
    for it_slug, tr in CASES_SLUGS.items():
        row(f'casi-studio/{it_slug}', f'{SECTIONS["casi-studio"]["en"]}/{tr["en"]}', f'{SECTIONS["casi-studio"]["ru"]}/{tr["ru"]}')
    for it_slug, tr in TOOLS_SLUGS.items():
        row(f'strumenti/{it_slug}', f'{SECTIONS["strumenti"]["en"]}/{tr["en"]}', f'{SECTIONS["strumenti"]["ru"]}/{tr["ru"]}')
    for it_slug, tr in BLOG_SLUGS.items():
        if it_slug in BLOG_IT_EN_ONLY:
            # RU non ancora pubblicato: rimanda all'indice /ru/blog/ (no 404).
            row(f'blog/{it_slug}', f'{SECTIONS["blog"]["en"]}/{tr["en"]}', SECTIONS["blog"]["ru"])
        else:
            row(f'blog/{it_slug}', f'{SECTIONS["blog"]["en"]}/{tr["en"]}', f'{SECTIONS["blog"]["ru"]}/{tr["ru"]}')
    # Blog · Batch 5 — RU-only: nessuna versione IT/EN. IT ed EN rimandano ai
    # loro indici blog (pagine reali, no 404), RU all'articolo. Appese DOPO la
    # riga indice 'blog' delle SECTIONS, così lo switcher sull'indice italiano
    # trova prima la riga giusta.
    for ru_slug in BLOG_RU_ONLY:
        row('blog', SECTIONS['blog']['en'], f'{SECTIONS["blog"]["ru"]}/{ru_slug}')
    return rows


def emit_php_lang_map(out_path):
    """Пишет inc/lang-map.php: карта путей для hreflang и переключателя."""
    rows = all_page_paths()
    lines = [
        '<?php',
        '/**',
        ' * Автогенерировано build-tools/lang.py — НЕ редактировать вручную.',
        ' * Карта соответствия путей страниц IT ↔ EN ↔ RU (без ведущего слеша).',
        ' */',
        'return array(',
    ]
    for it_p, en_p, ru_p in rows:
        lines.append(f"\tarray( 'it' => '{it_p}', 'en' => '{en_p}', 'ru' => '{ru_p}' ),")
    lines.append(');')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')


if __name__ == '__main__':
    import os
    out = os.path.join(os.path.dirname(__file__), '..', 'remarka-studio', 'inc', 'lang-map.php')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    emit_php_lang_map(out)
    print(f'lang-map.php: {len(all_page_paths())} righe')
