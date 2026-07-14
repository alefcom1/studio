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
}

# Имена клиентов — бренды, слаги не переводятся.
CASES_SLUGS = {
    s: {'en': s, 'ru': s}
    for s in ('arredamenti-colombo', 'cantina-serralta', 'tecnoidraulica', 'studio-legale-fontana')
}

TOOLS_SLUGS = {
    'test-velocita':      {'en': 'speed-test',       'ru': 'test-skorosti'},
    'check-gdpr':         {'en': 'gdpr-check',       'ru': 'proverka-gdpr'},
    'analisi-seo':        {'en': 'seo-audit',        'ru': 'seo-audit'},
    'roi-localizzazione': {'en': 'localization-roi', 'ru': 'roi-lokalizacii'},
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
