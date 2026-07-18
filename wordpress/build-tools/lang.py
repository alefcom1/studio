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

# I casi studio (docs/copy-casi-studio.md, deck §8.3) non hanno più pagine
# dedicate /casi-studio/<slug>/: vivono come schede con àncora nel catalogo
# unico (IT: casi-studio-index.php, EN: en-casi-studio-index.php, RU:
# ru-casi-studio-index.php — narrativa a sé). Niente slug da tradurre.
CASES_SLUGS = {}

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
}

# Articoli del blog pubblicati solo in IT + EN in questa fase (la loro versione
# RU è un batch a sé, non una traduzione). Per questi, all_page_paths non emette
# una riga hreflang verso una pagina RU inesistente: la colonna RU rimanda
# all'indice /ru/blog/ (pagina reale), così switcher e hreflang restano validi.
BLOG_IT_EN_ONLY = {
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
