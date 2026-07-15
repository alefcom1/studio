#!/usr/bin/env python3
"""
Генерирует полностраничные Gutenberg-паттерны Remarka Studio из data.py.

Запуск: python3 generate_pages.py
Пишет .php-файлы в wordpress/remarka-studio/patterns/pages/.
Категория паттернов — "remarka-pagine" (регистрируется в functions.php).

Зачем генератор, а не ручная разметка: блочная разметка WP — это
HTML-комментарии с JSON, очень многословные и легко ломаемые вручную
на масштабе 20+ страниц. Генератор гарантирует валидный JSON и
переиспользует один и тот же набор компонентов, что и секционные
паттерны (см. assets/css/remarka.css).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from blocks import (  # noqa: E402
    eyebrow, heading, paragraph, buttons, column, columns, group, section,
    raw_html, image, table, details_faq, stat_block, list_rows, checklist,
    metric_rows, browser_frame, case_screenshot_src, barra, barra_row,
    pull_quote, chapter, compare_table_row, pattern_header,
    case_shot, browser_frame_shot,
)
from data import SERVICES, CASES, CASES_BY_SLUG, TOOLS, CITY, CITIES, BLOG_POSTS, EXPORT_READY, WEB_APP, ADEGUAMENTO_EAA  # noqa: E402

OUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'remarka-studio', 'patterns', 'pages')
os.makedirs(OUT_DIR, exist_ok=True)


def write(slug, title, description, body):
    path = os.path.join(OUT_DIR, f'{slug}.php')
    content = pattern_header(title, slug, description, category='remarka-pagine') + body
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  {slug}.php')


def hero_interno(eyebrow_text, title, sub, extra_html='', stat=None):
    left = eyebrow(eyebrow_text) + heading(1, title, style='clamp(38px, 4.6vw, 64px)') + \
        paragraph(sub, color='grigio', size='medium', extra_style='max-width:640px;margin-top:24px') + extra_html
    if stat:
        right = raw_html(
            f'<div class="sr-stat" style="max-width:260px">'
            f'<span class="sr-stat__num" style="color:var(--sr-oltremare)">{stat[0]}</span>'
            f'<p style="margin-top:16px;font-size:15.5px;color:var(--sr-grigio)">{stat[1]}</p></div>'
        )
        inner = columns([column(left, width='62%', valign='center'), column(right, width='38%', valign='center')],
                         valign='center')
    else:
        inner = left
    return section(inner, classes='sr-section sr-hero')


# Link contestuali servizio → strumento gratuito (perelinkovka T2). Una riga
# sobria dentro la sezione prezzo del servizio, senza rompere la struttura.
SERVICE_TOOL_LINKS = {
    'siti-aziendali':       [('Obbligo di accessibilità (EAA dal 2025): verifica il vostro sito', '/strumenti/verifica-accessibilita/')],
    'e-commerce':           [('Obbligo di accessibilità (EAA dal 2025): verifica il vostro sito', '/strumenti/verifica-accessibilita/')],
    'restyling-migrazione': [('Misura l’impatto CO₂ del sito attuale', '/strumenti/impatto-co2/')],
    'seo-tecnica':          [('Analizza la SEO on-page della vostra pagina', '/strumenti/analisi-seo/'),
                             ('Verifica se il sito è pronto per l’AI', '/strumenti/sito-pronto-ai/'),
                             ('Misura i segnali E-E-A-T del sito', '/strumenti/segnali-eeat/')],
    'siti-multilingue':     [('Calcola il ROI della localizzazione', '/strumenti/roi-localizzazione/')],
}


# Prezzo lancio (owner 15.07.2026): −50% sui primi 5 progetti, solo sui tre
# prodotti "a scatola chiusa" (sito vetrina — solo nella tabella /prezzi/,
# non ha una pagina servizio propria — sito aziendale, e-commerce). Il testo
# è quello approvato dal titolare, usato alla lettera in ogni lingua.
LANCIO_SLUGS = {'siti-aziendali', 'e-commerce'}


def _lancio_banner_html():
    """Badge + riga + contatore promo. Avvolto in {{lancio}}…{{/lancio}}:
    il filtro the_content in functions.php lo mostra solo finché
    remarka_lancio_slots() > 0, e sostituisce {{lancio_slots}} col numero
    vero letto dall'option — niente redeploy quando la promo finisce."""
    return (
        '{{lancio}}'
        '<div class="sr-lancio-badge sr-mono">PREZZO LANCIO — PRIMI 5 PROGETTI</div>'
        '<p class="sr-lancio-line">Prezzo lancio sui primi 5 progetti: stesso contratto, stesse garanzie. '
        'Listino pieno dal 2027.</p>'
        '<p class="sr-lancio-counter sr-mono">Ne restano {{lancio_slots}} su 5.</p>'
        '{{/lancio}}'
    )


def _service_tool_links_html(slug):
    links = SERVICE_TOOL_LINKS.get(slug)
    if not links:
        return ''
    return ''.join(
        f'<p class="sr-card-link" style="margin-top:12px"><a href="{url}">{label} →</a></p>'
        for label, url in links
    )


def build_servizi_index():
    hero = section(eyebrow('Servizi') + heading(1, 'Sei cose che sappiamo fare bene', style='clamp(38px,4.6vw,64px)') +
                    paragraph('Ogni servizio nasce con lo stesso obiettivo: PageSpeed 90+ da contratto, prezzo chiuso, data fissa.',
                               color='grigio', size='medium'),
                    classes='sr-section sr-hero')

    cards = []
    for svc in SERVICES:
        card = (
            heading(3, svc['title'], accent_dot=False) +
            paragraph(svc['hero_sub'], color='grigio', size='small') +
            raw_html(f'<p class="sr-card-link" style="margin-top:16px"><a href="/servizi/{svc["slug"]}/">Scopri →</a></p>')
        )
        cards.append(group(card, classes='sr-card'))

    grid = section(group(''.join(cards), classes='', layout_type='grid', style='300px'), classes='sr-section')

    # Линии 2 и 3 концепции — отдельный блок «premium» под сеткой базовых услуг.
    premium_cards = ''.join(
        f'<div class="sr-card sr-card--carta"><p class="sr-eyebrow">{ey}</p>'
        f'<h3 class="wp-block-heading" style="font-size:22px">{t}</h3>'
        f'<p style="margin-top:12px;font-size:15.5px;color:var(--sr-grigio);line-height:1.6">{d}</p>'
        f'<p class="sr-card-link" style="margin-top:16px"><a href="{u}">Scopri →</a></p></div>'
        for ey, t, d, u in [
            ('Flagship', 'Export Ready', 'Il sito e la sua versione estera sotto un unico contratto: localizzazione da madrelingua, SEO internazionale, KPI per mercato.', '/servizi/export-ready/'),
            ('Prodotti digitali', 'Web app su misura', 'Aree clienti, configuratori, portali B2B e integrazioni: quando un sito non basta.', '/servizi/web-app/'),
            ('Obbligo di legge', 'Adeguamento EAA', 'Il vostro sito già online, portato allo standard WCAG 2.1 AA: audit, correzioni e dichiarazione di accessibilità. Obbligo di legge dal 2025.', '/servizi/adeguamento-eaa/'),
        ]
    )
    premium = section(
        eyebrow('Oltre il sito') + heading(2, 'Quando serve di più') +
        group(premium_cards, classes='', layout_type='grid', style='320px'),
        classes='sr-section sr-section--bianco',
    )
    write('servizi-index', 'Pagina — Servizi (elenco)', 'Elenco dei servizi con link alle pagine dettaglio + linee premium.',
          hero + grid + premium)


def build_servizio(svc):
    hero = hero_interno(svc['breadcrumb'], svc['hero_title'], svc['hero_sub'],
                         extra_html=buttons([
                             ('Richiedi preventivo in 24 ore', '/#contatti', None),
                             ('Vedi i casi studio', '/casi-studio/', 'outline'),
                         ], margin_top='36px'),
                         stat=(svc['hero_stat_value'], svc['hero_stat_label']))

    per_chi = section(
        columns([
            column(eyebrow('Per chi è') + heading(2, svc['per_chi_heading']), width='38%'),
            column(list_rows(svc['per_chi']), width='62%'),
        ]),
        classes='sr-section',
    )

    include = section(
        eyebrow('Cosa include') + heading(2, svc['include_heading']) + checklist(svc['include']),
        classes='sr-section sr-section--bianco',
    )

    # Mini-caso: un progetto REALE del gruppo Remarka (docs/copy-casi-studio.md),
    # non un cliente inventato — niente più barre prima/dopo fittizie, solo due
    # cifre verificabili sul progetto vivo (link_slug punta all'àncora della
    # scheda nel catalogo unico /casi-studio/#…).
    mc = svc['mini_caso']
    mini_caso = section(
        columns([
            column(eyebrow('Dal nostro catalogo') + heading(2, mc['cliente'], style='clamp(26px,3vw,34px)') +
                   raw_html(f'<p class="sr-mono" style="font-size:12.5px;color:var(--sr-grigio);margin-top:6px">{mc["progetto"]}</p>') +
                   paragraph(mc['testo'], size='base', extra_style='margin-top:16px;font-size:16px') +
                   raw_html(f'<p class="sr-card-link" style="margin-top:16px"><a href="{mc["link_slug"]}">Leggi il caso completo →</a></p>'),
                   width='55%'),
            column(raw_html(
                       f'<div class="sr-stat"><span class="sr-stat__num" style="font-size:clamp(30px,3vw,40px);color:var(--sr-oltremare)">{mc["stat1_value"]}</span>'
                       f'<p style="margin-top:8px;font-size:14px;color:var(--sr-grigio)">{mc["stat1_label"]}</p></div>'
                   ) +
                   raw_html(
                       f'<div class="sr-stat" style="margin-top:24px"><span class="sr-stat__num" style="font-size:clamp(30px,3vw,40px);color:var(--sr-oltremare)">{mc["stat2_value"]}</span>'
                       f'<p style="margin-top:8px;font-size:14px;color:var(--sr-grigio)">{mc["stat2_label"]}</p></div>'
                   ) +
                   raw_html(f'<p class="sr-mono" style="font-size:11px;letter-spacing:0.06em;color:var(--sr-grigio);margin-top:20px">{mc["caption"]}</p>'),
                   width='45%'),
        ], valign='center'),
        classes='sr-section',
    )

    lancio_html = raw_html(_lancio_banner_html()) if svc['slug'] in LANCIO_SLUGS else ''
    prezzo = section(
        eyebrow('Prezzo') +
        lancio_html +
        raw_html(f'<div class="sr-stat__num" style="font-size:clamp(36px,4vw,52px)">{svc["prezzo_range"]}</div>') +
        paragraph(svc['prezzo_lede'], color='grigio', size='base', extra_style='margin-top:14px;max-width:60ch') +
        paragraph('Cosa fa variare il prezzo', extra_style='margin-top:28px;font-weight:500;font-size:16px') +
        list_rows(svc['prezzo_note']) +
        raw_html(_service_tool_links_html(svc['slug'])) +
        raw_html('<p class="sr-card-link" style="margin-top:20px"><a href="/prezzi/">Confronta tutte le tariffe →</a></p>'),
        classes='sr-section sr-section--bianco',
    )

    faq = section(
        eyebrow(svc['faq_heading']) +
        group(''.join(
            raw_html(f'<div style="border-top:1px solid var(--sr-inchiostro);padding-top:20px">'
                      f'<h3 class="wp-block-heading" style="font-size:18px">{q}</h3>'
                      f'<p style="margin-top:10px;font-size:15px;color:var(--sr-grigio)">{a}</p></div>')
            for q, a in svc['faq']
        ), classes='', layout_type='grid', style='240px'),
        classes='sr-section',
    )

    cta = section(
        heading(2, 'Parliamo del vostro sito', style=None) +
        paragraph('Analisi gratuita del sito attuale, preventivo chiuso entro 24 ore dalla chiamata.',
                   color='grigio', size='medium', extra_style='margin-top:12px') +
        buttons([('Richiedi preventivo in 24 ore', '/#contatti', None),
                 ('Analizza il tuo sito — gratis', '/strumenti/test-velocita/', 'outline')],
                justify='center', margin_top='28px'),
        classes='sr-section sr-dark',
    )

    body = hero + per_chi + include + mini_caso + prezzo + faq + cta
    write(f'servizio-{svc["slug"]}', f'Pagina — Servizio: {svc["title"]}',
          f'Pagina completa del servizio {svc["title"]}: hero, per chi è, cosa include, mini caso, prezzo, FAQ, CTA.',
          body)


# ---------------------------------------------------------------- Casi studio

CASE_FILTER_LABELS = [
    ('all', 'Tutti i progetti'),
    ('siti', 'Siti aziendali e vetrina'),
    ('webapp', 'Web app e prodotti'),
    ('seo', 'SEO tecnica e contenuti'),
    ('restyling', 'Restyling e marketing'),
]


def _case_shots_html(c):
    """Una scheda-caso può avere 1 screenshot, un board principale + 2 più
    piccoli (TMS) o una coppia affiancata (moscowtrans+techperevod)."""
    shots = c['shots']
    if len(shots) == 1:
        s = shots[0]
        return browser_frame_shot(c['url_label'], s['file'], c['alt'], s['caption'], mobile=s['mobile'])
    if c['slug'] == 'tms-perevod4':
        main, extra = shots[0], shots[1:]
        extra_html = ''.join(
            browser_frame_shot(c['url_label'], s['file'], c['alt'], s['caption'], mobile=False)
            for s in extra
        )
        return (browser_frame_shot(c['url_label'], main['file'], c['alt'], main['caption'], mobile=False) +
                raw_html(f'<div class="sr-case-card__shots-extra">{extra_html}</div>'))
    # Coppia affiancata (moscowtrans.ru + techperevod.com): due cornici uguali.
    return raw_html('<div class="sr-case-card__shots-extra">' + ''.join(
        browser_frame_shot(c['url_label'], s['file'], c['alt'], s['caption'], mobile=False)
        for s in shots
    ) + '</div>')


def build_casi_studio_index():
    hero = section(
        eyebrow('Casi studio') +
        heading(1, "Non un portfolio di clienti. I sistemi che abbiamo costruito per noi", style='clamp(38px,4.6vw,64px)') +
        paragraph(
            "Molte web agency mostrano loghi di clienti. Il gruppo Remarka lavora con le lingue dal 2001 — "
            "e dallo stesso anno costruisce siti: già nel 2002–2003 ne realizzava per aziende terze, e alcuni "
            "sono online ancora oggi (directindustry.com.ru · ivextrans.eu · beltran.by). Da allora abbiamo "
            "realizzato oltre 160 progetti; 28 sono oggi in manutenzione continua presso di noi. Studio Remarka "
            "è la vetrina nuova di questo lavoro, non il suo inizio.",
            color='grigio', size='medium', extra_style='margin-top:24px;max-width:74ch',
        ) +
        paragraph(
            "Qui sotto trovate i sistemi che il gruppo ha costruito per sé: per gestire il proprio lavoro, "
            "portare i propri servizi su Google, vendere in più lingue. Li usiamo ogni giorno, con i nostri "
            "soldi e la nostra reputazione in gioco — e quando lavorate con noi ricevete la stessa ingegneria. "
            "Ogni caso ha un link al progetto vivo: potete aprirlo, provarlo, misurarlo da soli. Nessun cliente "
            "inventato, nessun numero non verificabile.",
            color='grigio', size='medium', extra_style='margin-top:16px;max-width:74ch',
        ) +
        raw_html('<p class="sr-mono" style="margin-top:20px;font-size:12.5px;color:var(--sr-grigio)">Ogni scheda porta al progetto online. I punteggi e le metriche sono verificabili sul posto.</p>') +
        raw_html(
            '<div class="sr-case-filter" data-sr-case-filter-bar>' +
            ''.join(
                f'<button type="button" class="sr-case-filter__btn{" is-active" if key == "all" else ""}" '
                f'data-sr-case-filter="{key}" aria-pressed="{"true" if key == "all" else "false"}">{label}</button>'
                for key, label in CASE_FILTER_LABELS
            ) + '</div>'
        ) +
        raw_html('<p class="sr-mono" style="margin-top:14px;font-size:12px;color:var(--sr-grigio)">11 progetti del gruppo · filtra per tipo di lavoro</p>'),
        classes='sr-section sr-hero',
    )

    cards = []
    for i, c in enumerate(CASES):
        card_classes = 'sr-section sr-case-card' + (' sr-section--bianco' if i % 2 else '')
        card_body = columns([
            column(_case_shots_html(c), width='52%'),
            column(
                raw_html(f'<span class="sr-case-card__chip">{c["chip"]}</span>') +
                heading(2, c['titolo'], style='clamp(24px,2.6vw,32px)') +
                raw_html(f'<p class="sr-case-card__url" style="margin-top:10px"><a href="{c["url"]}" target="_blank" rel="noopener noreferrer">{c["url_label"]} ↗</a></p>') +
                paragraph(c['problema'], size='base', extra_style='margin-top:18px;font-size:15.5px') +
                paragraph(c['soluzione'], size='base', extra_style='margin-top:12px;font-size:15.5px') +
                raw_html(f'<p style="margin-top:16px;font-size:15.5px;font-weight:500">{c["risultato"]}</p>') +
                raw_html(f'<p class="sr-card-link" style="margin-top:18px"><a href="{c["cta_href"]}">{c["cta_testo"]} →</a></p>'),
                width='48%',
            ),
        ])
        cards.append(section(card_body, classes=card_classes, anchor=c['slug'], data_attrs={'data-cat': c['data_cat']}))

    cta = section(
        heading(2, 'Il prossimo sistema possiamo costruirlo per voi') +
        paragraph('Prima misuriamo cosa avete oggi, poi vi diciamo — con numeri e con una data in contratto — cosa possiamo fare.',
                   color='grigio', size='medium', extra_style='margin-top:12px') +
        buttons([
            ('Richiedi un preventivo in 24 ore', '/#contatti', None),
            ('Guarda tutti i servizi', '/servizi/', 'outline'),
        ], justify='center', margin_top='28px'),
        classes='sr-section sr-dark',
    )
    write('casi-studio-index', 'Pagina — Casi studio (elenco)',
          'Catalogo degli 11 casi studio reali del gruppo Remarka, con filtro per tipo di lavoro e link ai progetti vivi.',
          hero + ''.join(cards) + cta)


# ---------------------------------------------------------------- Prezzi

def build_prezzi():
    hero = section(
        eyebrow('Prezzi') + heading(1, 'Prezzi trasparenti. Nessuna sorpresa in corso d’opera', style='clamp(38px,4.6vw,64px)') +
        paragraph('Quanto costa un sito web? La tabella qui sotto è pubblica; il preventivo che firmate è un prezzo chiuso. '
                   'Se in corso d’opera serve altro, si concorda prima, per iscritto.',
                   color='grigio', size='medium') +
        raw_html('<div style="margin-top:40px;max-width:600px">') +
        raw_html(barra(100, height=6)) +
        raw_html('<p class="sr-mono" style="margin-top:10px;font-size:12px;color:var(--sr-grigio)">100% DEI PREVENTIVI 2025 CHIUSI AL PREZZO FIRMATO</p></div>'),
        classes='sr-section sr-hero',
    )

    lancio_banner = section(raw_html(_lancio_banner_html()), classes='sr-section')

    headers = [
        '',
        'Sito vetrina<br><span>{{listino}}€ 1.900–2.800{{/listino}}{{lancio}}<s class="sr-lancio-listino">€ 1.900–2.800</s> '
        '<strong class="sr-lancio-price">€ 950–1.400</strong>{{/lancio}}</span>',
        'Sito aziendale<br><span>{{listino}}€ 3.900–5.800{{/listino}}{{lancio}}<s class="sr-lancio-listino">€ 3.900–5.800</s> '
        '<strong class="sr-lancio-price">€ 1.950–2.900</strong>{{/lancio}}</span>',
        'E-commerce<br><span>{{listino}}€ 7.500–14.000{{/listino}}{{lancio}}<s class="sr-lancio-listino">€ 7.500–14.000</s> '
        '<strong class="sr-lancio-price">€ 3.750–7.000</strong>{{/lancio}}</span>',
    ]
    rows_data = [
        ('Pagine incluse', ['5', '15', 'Catalogo']),
        ('Lingue tradotte da madrelingua', ['1', '2', '2']),
        ('Design su misura, senza template', [True, True, True]),
        ('CMS per aggiornarlo da soli', [False, True, True]),
        ('PWA: offline e installabile', [False, True, True]),
        ('Catalogo, carrello e pagamenti', [False, False, True]),
        ('SEO tecnica e dati strutturati', ['base', 'completa', 'completa']),
        ('PageSpeed 90+ da contratto', [True, True, True]),
        ('Assistenza inclusa', ['12 mesi', '12 mesi', '12 mesi']),
        ('Consegna', ['2 sett.', '3 sett.', '6 sett.']),
    ]
    thead = '<tr>' + ''.join(f'<th>{h}</th>' for h in headers) + '</tr>'
    tbody = ''.join(compare_table_row(label, vals) for label, vals in rows_data)
    compare = raw_html(f'<div class="sr-compare-table"><table><thead>{thead}</thead><tbody>{tbody}</tbody></table></div>')

    table_section = section(
        compare +
        raw_html('<p class="sr-card-link" style="margin-top:20px;font-size:14.5px">'
                 '<a href="/servizi/adeguamento-eaa/">Sito già online? L’adeguamento all’European Accessibility Act '
                 'è un servizio a sé →</a></p>') +
        paragraph('Per confronto: le agenzie italiane chiedono in media € 2.500–8.000 per un sito aziendale '
                   'e € 5.000–20.000 per un e-commerce (listini pubblici 2026). Siamo nella stessa fascia — '
                   'con tre garanzie scritte nel contratto che altrove non trovate.',
                   color='grigio', size='base', extra_style='margin-top:28px;max-width:70ch') +
        paragraph('Fattura elettronica via SDI. Pagamento in tre tranche: 40 / 40 / 20.', color='grigio', size='small',
                   extra_style='margin-top:16px') +
        buttons([('Richiedi preventivo dettagliato', '/#contatti', None)], margin_top='20px'),
        classes='sr-section',
    )

    def _market_lancio(listino, lancio):
        return (f'{{{{listino}}}}{listino}{{{{/listino}}}}'
                f'{{{{lancio}}}}<s class="sr-lancio-listino">{listino}</s>'
                f'<span class="sr-lancio-price">{lancio}</span>{{{{/lancio}}}}')

    market_rows = [
        ('Sito vetrina', '€ 1.000–3.000', _market_lancio('€ 1.900–2.800', '€ 950–1.400'), '2–4 settimane', '2 settimane'),
        ('Sito aziendale', '€ 2.500–8.000', _market_lancio('€ 3.900–5.800', '€ 1.950–2.900'), '6–10 settimane', '3 settimane'),
        ('E-commerce', '€ 6.000–25.000', _market_lancio('€ 7.500–14.000', '€ 3.750–7.000'), '8–14 settimane', '6 settimane'),
    ]
    market_thead = ('<tr><th>Prodotto</th><th>Prezzo di mercato</th>'
                    '<th class="sr-market-table__uscol">Prezzo Remarka</th>'
                    '<th>Tempi di mercato</th>'
                    '<th class="sr-market-table__uscol">Tempi Remarka</th></tr>')
    market_tbody = ''.join(
        f'<tr><td class="sr-market-table__prod">{prod}</td>'
        f'<td>{mprice}</td><td class="sr-market-table__us sr-market-table__us--lancio">{rprice}</td>'
        f'<td>{mtime}</td><td class="sr-market-table__us">{rtime}</td></tr>'
        for prod, mprice, rprice, mtime, rtime in market_rows
    )
    market = section(
        heading(2, 'Prezzi e tempi, accanto a quelli di mercato') +
        paragraph('Le forbici di mercato vengono dai listini pubblici delle web agency italiane (2026). '
                   'Le nostre cifre sono quelle del contratto.',
                   color='grigio', size='medium', extra_style='margin-top:12px;max-width:70ch') +
        raw_html(f'<div class="sr-market-table" style="margin-top:40px"><table><thead>{market_thead}</thead>'
                 f'<tbody>{market_tbody}</tbody></table></div>') +
        paragraph('Forbici di mercato dai listini pubblici delle web agency italiane, 2026. '
                   'Analisi completa con le fonti nel nostro blog: '
                   '<a href="/blog/quanto-costa-sito-aziendale-italia/">«Quanto costa un sito aziendale in Italia»</a>.',
                   color='grigio', size='small', extra_style='margin-top:20px'),
        classes='sr-section',
    )

    variazioni = section(
        eyebrow('Cosa fa variare il prezzo') +
        paragraph('Tre voci, sempre le stesse. Le trovate esplicitate riga per riga nel preventivo.',
                   color='grigio', size='medium', extra_style='margin-bottom:24px') +
        list_rows([
            '<strong>Contenuti:</strong> pagine e schede oltre quelle incluse, servizi fotografici, testi da scrivere ex novo.',
            '<strong>Lingue:</strong> ogni lingua oltre quelle comprese, tradotta da madrelingua del gruppo Remarka.',
            '<strong>Integrazioni:</strong> gestionale, CRM, listini, sistemi di prenotazione o pagamento particolari.',
        ]),
        classes='sr-section sr-section--bianco',
    )

    cta = section(
        heading(2, 'Preventivo chiuso in 24 ore') +
        paragraph('Descriveteci il progetto: ricevete prezzo e data di consegna, entrambi vincolanti.',
                   color='grigio', size='medium', extra_style='margin-top:12px') +
        buttons([('Richiedi preventivo dettagliato', '/#contatti', None)], justify='center', margin_top='28px'),
        classes='sr-section sr-dark',
    )
    write('prezzi', 'Pagina — Prezzi (completa)',
          'Pagina prezzi con tabella comparativa completa (min-width 840px, scroll orizzontale su mobile).',
          hero + lancio_banner + table_section + market + variazioni + cta)


# ---------------------------------------------------------------- Strumenti

def build_strumenti_index():
    hero = section(eyebrow('Strumenti gratuiti') + heading(1, 'Prima misurate, poi decidete', style='clamp(38px,4.6vw,64px)') +
                    paragraph('Strumenti professionali, gratuiti, senza registrazione.', color='grigio', size='medium'),
                    classes='sr-section sr-hero')

    # Check-up completo: posizione featured, prima della griglia dei singoli
    # strumenti (docs/piano-checkup-sito.md, scope M2).
    checkup = next(t for t in TOOLS if t['tipo'] == 'checkup')
    altri = [t for t in TOOLS if t['tipo'] != 'checkup']

    featured = section(
        raw_html(
            '<div class="sr-card sr-card--carta" style="border-color:var(--sr-oltremare)">'
            '<p class="sr-eyebrow" style="color:var(--sr-oltremare)">Novità · gratuito</p>'
            f'<h3 class="wp-block-heading" style="margin-top:10px">{checkup["titolo"]}</h3>'
            f'<p style="margin-top:10px;font-size:15.5px;color:var(--sr-grigio);max-width:60ch">{checkup["descrizione"]}</p>'
            f'<p class="sr-card-link" style="margin-top:18px"><a href="/strumenti/{checkup["slug"]}/">Prova →</a></p>'
            '</div>'
        ),
        classes='sr-section sr-section--bianco',
    )

    cards = []
    for t in altri:
        card = (
            raw_html(f'<p class="sr-mono" style="color:var(--sr-oltremare);font-size:12px">{t["idx"]}</p>') +
            heading(3, t['titolo'], accent_dot=False) +
            paragraph(t['descrizione'], color='grigio', size='small') +
            raw_html(f'<p class="sr-card-link" style="margin-top:16px"><a href="/strumenti/{t["slug"]}/">Prova →</a></p>')
        )
        cards.append(group(card, classes='sr-card sr-card--carta'))

    grid = section(group(''.join(cards), classes='', layout_type='grid', style='240px'),
                    classes='sr-section sr-section--bianco')
    write('strumenti-index', 'Pagina — Strumenti (elenco)',
          'Elenco degli otto strumenti gratuiti, con il check-up completo in evidenza.', hero + featured + grid)


# Markup del widget per tipo di strumento — segue STRETTAMENTE il contratto
# data-* dichiarato in assets/js/remarka.js (blocco "CONTRATTO DATA-ATTRIBUTI").
# Ogni pagina IT porta le proprie stringhe di verdetto/etichetta nei data-*,
# con data-sr-locale="it". Riferimento markup: scratchpad/t1_widgets.html.

_TOOL_INPUT = ('<div class="sr-tool-row">'
               '<input type="text" placeholder="www.tuosito.it" class="sr-text-input" required />'
               '<button type="submit" class="wp-block-button__link" style="padding:17px 30px">{btn}</button>'
               '</div>')


def _widget_speed():
    return '''
<div class="sr-tool-widget sr-card" data-sr-tool="speed" data-sr-locale="it">
  <form data-sr-tool-form>
    <div class="sr-tool-row">
      <input type="text" placeholder="www.tuosito.it" class="sr-text-input" required />
      <button type="submit" class="wp-block-button__link" style="padding:17px 30px">Avvia il test</button>
    </div>
  <p class="sr-tool-pending sr-mono" data-sr-tool-pending hidden>Rilevazione Google in corso — mobile, può richiedere fino a 30 secondi<span class="sr-blink">…</span></p>
  <div class="sr-tool-result" data-sr-tool-result hidden>
    <p style="margin:0;font-size:14px;color:var(--sr-grigio)" data-sr-tool-url></p>
    <div class="sr-tool-result__score">
      <span class="sr-mono" data-sr-tool-score>0</span><span class="sr-mono" style="font-size:18px;color:var(--sr-grigio)">/100</span>
    </div>
    <div class="sr-barra" style="height:10px">
      <div class="sr-barra__fill" data-sr-tool-fill style="width:0%"></div>
      <span class="sr-barra__tick" style="left:90%"></span>
    </div>
    <div style="display:flex;justify-content:space-between;margin-top:8px;font-family:var(--sr-font-mono);font-size:11px;color:var(--sr-grigio)"><span>0</span><span>50</span><span>90</span><span>100</span></div>
    <p style="margin-top:20px;font-size:15.5px;color:var(--sr-grigio)" data-sr-tool-verdict></p>
    <div class="sr-tool-cwv">
      <div><p class="sr-eyebrow" style="margin-bottom:8px">LCP</p><p class="sr-tool-cwv-value sr-mono" data-sr-tool-lcp></p><p style="font-size:13.5px;color:var(--sr-grigio)">Tempo di caricamento del contenuto principale. Sotto i 2,5 s è considerato buono.</p></div>
      <div><p class="sr-eyebrow" style="margin-bottom:8px">INP</p><p class="sr-tool-cwv-value sr-mono" data-sr-tool-inp></p><p style="font-size:13.5px;color:var(--sr-grigio)">Reattività del sito al tocco. Sotto i 200 ms è considerato buono.</p></div>
      <div><p class="sr-eyebrow" style="margin-bottom:8px">CLS</p><p class="sr-tool-cwv-value sr-mono" data-sr-tool-cls></p><p style="font-size:13.5px;color:var(--sr-grigio)">Stabilità visiva durante il caricamento. Sotto 0,1 è considerato buono.</p></div>
    </div>
    <p class="sr-tool-caption sr-mono">Dati reali da Google PageSpeed Insights API — strategia mobile. LCP e CLS da analisi Lighthouse; INP da dati di campo Chrome UX quando disponibili.</p>
  </div>
  </form>
</div>'''


def _widget_score(tipo, btn, pending, suffix, verdict_good, verdict_mid, verdict_poor,
                  audits_empty, disclaimer=''):
    disc = (f'\n      <p class="sr-disclaimer">{disclaimer}</p>' if disclaimer else '')
    return f'''
<div class="sr-tool-widget sr-card" data-sr-tool="{tipo}" data-sr-locale="it"
     data-label-suffix="{suffix}"
     data-verdict-good="{verdict_good}"
     data-verdict-mid="{verdict_mid}"
     data-verdict-poor="{verdict_poor}"
     data-audits-empty="{audits_empty}"
     data-err="Non siamo riusciti a completare l’analisi. Riprovate tra qualche minuto.">
  <form data-sr-tool-form>
    {_TOOL_INPUT.format(btn=btn)}
  </form>
  <p class="sr-tool-pending sr-mono" data-sr-tool-pending hidden>{pending}<span class="sr-blink">…</span></p>
  <div class="sr-tool-result" data-sr-tool-result hidden>
    <p style="margin:0;font-size:14px;color:var(--sr-grigio)" data-sr-tool-url></p>
    <div class="sr-tool-result__score">
      <span class="sr-mono" data-sr-tool-score>0</span><span class="sr-mono" style="font-size:18px;color:var(--sr-grigio)">/100</span>
    </div>
    <div class="sr-barra" style="height:10px"><div class="sr-barra__fill" data-sr-tool-fill style="width:0%"></div><span class="sr-barra__tick" style="left:90%"></span></div>
    <p style="margin-top:20px;font-size:15.5px;color:var(--sr-grigio)" data-sr-tool-verdict></p>
    <ul class="sr-tool-audits" data-sr-tool-audits></ul>{disc}
  </div>
</div>'''


def _widget_co2():
    return '''
<div class="sr-tool-widget sr-card" data-sr-tool="co2" data-sr-locale="it"
     data-co2-average="0.8" data-co2-visits="10000"
     data-label-unit-year="kg CO₂e / anno"
     data-verdict-good="Sotto la media del web: pagina leggera, bene così."
     data-verdict-mid="Vicino alla media del web: c’è margine per alleggerire."
     data-verdict-poor="Sopra la media del web: pagina pesante, conviene ottimizzare."
     data-err="Non siamo riusciti a misurare il peso della pagina. Riprovate.">
  <form data-sr-tool-form>
    <div class="sr-tool-row">
      <input type="text" placeholder="www.tuosito.it" class="sr-text-input" required />
      <button type="submit" class="wp-block-button__link" style="padding:17px 30px">Misura l’impatto</button>
    </div>
  </form>
  <p class="sr-tool-pending sr-mono" data-sr-tool-pending hidden>Misurazione in corso<span class="sr-blink">…</span></p>
  <div class="sr-tool-result" data-sr-tool-result hidden>
    <p style="margin:0;font-size:14px;color:var(--sr-grigio)" data-sr-tool-url></p>
    <div class="sr-tool-result__score">
      <span class="sr-mono" data-sr-tool-grams>0 g</span>
    </div>
    <div class="sr-barra" style="height:10px;margin-top:8px"><div class="sr-barra__fill" data-sr-tool-fill style="width:0%"></div><span class="sr-barra__tick" style="left:50%"></span></div>
    <p style="margin-top:20px;font-size:15.5px;color:var(--sr-grigio)" data-sr-tool-verdict></p>
    <div class="sr-tool-cwv">
      <div><p class="sr-eyebrow" style="margin-bottom:8px">Peso pagina</p><p class="sr-tool-cwv-value sr-mono" data-sr-tool-weight></p></div>
      <div><p class="sr-eyebrow" style="margin-bottom:8px">Stima annua</p><p class="sr-tool-cwv-value sr-mono" data-sr-tool-year></p></div>
    </div>
    <p class="sr-tool-caption sr-mono">Modello Sustainable Web Design (co2.js, Apache-2.0). Stima per visita; anno calcolato su 10.000 visite/mese.</p>
  </div>
</div>'''


def _widget_gdpr():
    return '''
<div class="sr-tool-widget sr-card" data-sr-tool="gdpr" data-sr-locale="it"
     data-label-cmp-yes="Cookie banner rilevato" data-label-cmp-no="Nessun cookie banner rilevato"
     data-label-policy-yes="Link a privacy/cookie policy presente" data-label-policy-no="Nessun link a privacy/cookie policy"
     data-label-trackers-clean="Nessun tracker nell’HTML iniziale"
     data-label-trackers-flag="Tracker attivi senza banner"
     data-label-trackers-ok="Tracker presenti (con banner)"
     data-label-external="{n} domini esterni caricano script"
     data-err="Non siamo riusciti a leggere il sito. Riprovate tra qualche minuto.">
  <form data-sr-tool-form>
    <div class="sr-tool-row">
      <input type="text" placeholder="www.tuosito.it" class="sr-text-input" required />
      <button type="submit" class="wp-block-button__link" style="padding:17px 30px">Controlla il sito</button>
    </div>
  </form>
  <p class="sr-tool-pending sr-mono" data-sr-tool-pending hidden>Lettura del sito in corso<span class="sr-blink">…</span></p>
  <div class="sr-tool-result" data-sr-tool-result hidden>
    <ul class="sr-gdpr-rows">
      <li><span class="sr-gdpr-key">Cookie banner</span><span data-sr-tool-cmp data-sr-flag></span></li>
      <li><span class="sr-gdpr-key">Policy</span><span data-sr-tool-policy data-sr-flag></span></li>
      <li><span class="sr-gdpr-key">Tracker</span><span data-sr-tool-trackers data-sr-flag></span></li>
      <li><span class="sr-gdpr-key">Script esterni</span><span data-sr-tool-external data-sr-flag></span></li>
    </ul>
    <p class="sr-disclaimer" data-sr-tool-disclaimer>Verifica indicativa, non una consulenza legale. Un audit GDPR completo richiede la verifica manuale di cookie, finalità e basi giuridiche.</p>
  </div>
</div>'''


def _widget_ai():
    return '''
<div class="sr-tool-widget sr-card" data-sr-tool="ai" data-sr-locale="it"
     data-label-yes="Sì" data-label-no="No" data-label-partial="Parziale"
     data-err="Non siamo riusciti a leggere il sito. Riprovate tra qualche minuto.">
  <form data-sr-tool-form>
    <div class="sr-tool-row">
      <input type="text" placeholder="www.tuosito.it" class="sr-text-input" required />
      <button type="submit" class="wp-block-button__link" style="padding:17px 30px">Verifica la prontezza AI</button>
    </div>
  </form>
  <p class="sr-tool-pending sr-mono" data-sr-tool-pending hidden>Verifica in corso<span class="sr-blink">…</span></p>
  <div class="sr-tool-result" data-sr-tool-result hidden>
    <div class="sr-tool-result__score">
      <span class="sr-mono" data-sr-tool-score>0/4</span>
    </div>
    <ul class="sr-gdpr-rows">
      <li><span class="sr-gdpr-key">llms.txt</span><span data-sr-tool-llms data-sr-flag></span></li>
      <li><span class="sr-gdpr-key">Crawler AI</span><span data-sr-tool-robots data-sr-flag></span></li>
      <li><span class="sr-gdpr-key">JSON-LD</span><span data-sr-tool-jsonld data-sr-flag></span></li>
      <li><span class="sr-gdpr-key">Sitemap</span><span data-sr-tool-sitemap data-sr-flag></span></li>
    </ul>
    <p class="sr-tool-caption sr-mono">Controlla llms.txt, l’accesso dei crawler AI (GPTBot, ClaudeBot, PerplexityBot, Google-Extended), i dati strutturati JSON-LD e la sitemap.</p>
  </div>
</div>'''


# Gli 8 segnali E-E-A-T (chiave data-sr-tool-*, etichetta di riga statica,
# stati good/warn/bad con relativa etichetta — docs/copy-eeat.md §3-bis).
# I segnali binari (nessun warn) ripetono la stessa etichetta good/bad due volte
# nell'attributo warn per semplicità del generatore: il JS non lo userà mai
# perché eeatComputeFlags non produce mai 'warn' per quei segnali.
_EEAT_SIGNALS = [
    ('https', 'Connessione HTTPS',
     'Connessione sicura (HTTPS)', None, 'Nessun HTTPS: connessione non sicura'),
    ('contatti', 'Contatti verificabili',
     'Contatti verificabili presenti', 'Solo un’email, nessun telefono o indirizzo', 'Nessun contatto verificabile'),
    ('legale', 'Identità legale (P.IVA)',
     'P.IVA / dati fiscali presenti', None, 'Nessuna P.IVA o identità legale'),
    ('policy', 'Privacy e cookie policy',
     'Privacy e cookie policy presenti', 'Presente solo una delle due policy', 'Nessuna privacy o cookie policy'),
    ('chisiamo', 'Pagina «Chi siamo»',
     'Pagina «Chi siamo» presente', None, 'Nessuna pagina «Chi siamo»'),
    ('portfolio', 'Portfolio / casi studio',
     'Portfolio o casi studio presenti', None, 'Nessun portfolio o caso studio'),
    ('schema', 'Dati strutturati (JSON-LD)',
     'Dati strutturati d’identità presenti', 'JSON-LD presente ma solo generico', 'Nessun dato strutturato JSON-LD'),
    ('profili', 'Profili esterni',
     'Profili esterni collegati', 'Un solo profilo esterno', 'Nessun profilo esterno collegato'),
]

_EEAT_AXES = [
    ('esperienza', 'Esperienza'),
    ('competenza', 'Competenza'),
    ('autorevolezza', 'Autorevolezza'),
    ('affidabilita', 'Affidabilità'),
]


def _widget_eeat():
    signal_attrs = ''
    signal_rows = ''
    for key, label, good, warn, bad in _EEAT_SIGNALS:
        signal_attrs += (f'\n     data-label-{key}-good="{good}"' +
                          (f' data-label-{key}-warn="{warn}"' if warn else '') +
                          f' data-label-{key}-bad="{bad}"')
        signal_rows += (f'<li><span class="sr-gdpr-key">{label}</span>'
                         f'<span data-sr-tool-{key} data-sr-flag></span></li>')

    axis_rows = ''.join(
        f'<li><span class="sr-gdpr-key">{label}</span>'
        f'<span data-sr-tool-axis-{key} data-sr-flag>—</span></li>'
        for key, label in _EEAT_AXES
    )

    return f'''
<div class="sr-tool-widget sr-card" data-sr-tool="eeat" data-sr-locale="it"
     data-verdict-good="Ottimo: i segnali di fiducia E-E-A-T sono presenti e leggibili nel codice. Ricordate che parliamo di segnali on-page, non del vostro E-E-A-T reale."
     data-verdict-buono="Buona base: la maggior parte dei segnali di fiducia c’è. Sistemate i pochi punti in giallo o rosso per completare il quadro."
     data-verdict-mid="A metà strada: diversi segnali di fiducia mancano o non sono leggibili. La lista qui sotto indica da dove partire."
     data-verdict-poor="Segnali deboli: la pagina espone pochi elementi di fiducia verificabili — che sono anche i più facili da aggiungere."
     data-notice="Il sito rende i contenuti via JavaScript: alcuni segnali potrebbero esistere ma non essere leggibili nell’HTML iniziale. Il punteggio è indicativo."
     data-label-nd="non rilevato (possibile rendering JavaScript)"{signal_attrs}
     data-err="Non siamo riusciti a leggere la pagina. Controllate l’indirizzo e riprovate tra qualche minuto.">
  <form data-sr-tool-form>
    <div class="sr-tool-row">
      <input type="text" placeholder="www.tuosito.it" class="sr-text-input" required />
      <button type="submit" class="wp-block-button__link" style="padding:17px 30px">Analizza i segnali di fiducia</button>
    </div>
  </form>
  <p class="sr-tool-pending sr-mono" data-sr-tool-pending hidden>Lettura del sito in corso<span class="sr-blink">…</span></p>
  <div class="sr-tool-result" data-sr-tool-result hidden>
    <p style="margin:0;font-size:14px;color:var(--sr-grigio)" data-sr-tool-url></p>
    <p class="sr-eyebrow" style="margin-top:4px">Punteggio E-E-A-T on-page</p>
    <div class="sr-tool-result__score">
      <span class="sr-mono" data-sr-tool-score>0</span><span class="sr-mono" style="font-size:18px;color:var(--sr-grigio)">/100</span>
    </div>
    <div class="sr-barra" style="height:10px"><div class="sr-barra__fill" data-sr-tool-fill style="width:0%"></div><span class="sr-barra__tick" style="left:90%"></span><span class="sr-barra__tick" style="left:75%"></span><span class="sr-barra__tick" style="left:50%"></span></div>
    <p style="margin-top:20px;font-size:15.5px;color:var(--sr-grigio)" data-sr-tool-verdict></p>
    <p class="sr-tool-notice" data-sr-tool-notice hidden></p>
    <div style="margin-top:28px">
      <p class="sr-eyebrow">I quattro pilastri</p>
      <ul class="sr-gdpr-rows">{axis_rows}</ul>
    </div>
    <div style="margin-top:28px">
      <p class="sr-eyebrow">Otto segnali di fiducia</p>
      <ul class="sr-gdpr-rows">{signal_rows}</ul>
    </div>
    <p class="sr-disclaimer" data-sr-tool-disclaimer>Misuriamo segnali on-page verificabili nel codice della pagina, non la vostra reputazione o competenza reale. Un punteggio alto non garantisce un giudizio E-E-A-T positivo da parte di Google.</p>
  </div>
</div>'''


def _widget_roi():
    return '''
<div class="sr-tool-widget sr-card" data-sr-tool="roi" data-sr-locale="it" data-roi-currency="€">
  <form data-sr-tool-form>
    <div class="sr-roi-grid">
      <label>Visite / mese<input type="number" class="sr-text-input" data-sr-roi-visits value="10000" min="0"></label>
      <label>Quota estera (%)<input type="number" class="sr-text-input" data-sr-roi-foreign value="20" min="0" max="100"></label>
      <label>Conversione (%)<input type="number" class="sr-text-input" data-sr-roi-conv value="2" min="0" max="100" step="0.1"></label>
      <label>Scontrino medio (€)<input type="number" class="sr-text-input" data-sr-roi-order value="80" min="0"></label>
      <label>Boost localizzazione (%)<input type="number" class="sr-text-input" data-sr-roi-boost value="40" min="0"></label>
    </div>
    <div class="sr-tool-row" style="margin-top:16px">
      <button type="submit" class="wp-block-button__link" style="padding:15px 28px">Ricalcola</button>
    </div>
  </form>
  <div class="sr-tool-result" data-sr-tool-result hidden>
    <div class="sr-roi-out">
      <div><p class="sr-eyebrow" style="margin-bottom:6px">Ricavo aggiuntivo / mese</p><p class="sr-mono" data-sr-roi-monthly>—</p></div>
      <div><p class="sr-eyebrow" style="margin-bottom:6px">Ricavo aggiuntivo / anno</p><p class="sr-mono" data-sr-roi-annual>—</p></div>
    </div>
    <p class="sr-disclaimer">Stima indicativa. Il boost di localizzazione (+40% conservativo) deriva da dati CSA Research sull’acquisto in lingua madre.</p>
  </div>
</div>'''


# Le 7 dimensioni del check-up completo, nell'ordine del peso (docs/copy-checkup.md
# §1.1/§2.3): (chiave-JS, etichetta, "Peso N", didascalia motore, 4 frasi di
# rilievo Eccellente/Buono/Da migliorare/Critico). Le 4 frasi diventano gli
# attributi data-verdict-0..3 letti da remarka.js (initCheckupTool).
_CHECKUP_DIMS = [
    ('perf', 'Prestazioni', 'Peso 25', 'Google PageSpeed', [
        'Il sito è rapido su mobile: rispetta gli standard Google.',
        'Velocità buona; restano margini misurabili su qualche pagina.',
        'Nella media del web, ma lontano dagli standard consigliati.',
        'Il sito è lento su mobile: gran parte dei visitatori abbandona prima del caricamento.',
    ]),
    ('seo', 'SEO', 'Peso 20', 'Google PageSpeed', [
        'Basi tecniche on-page in ordine: nessun ostacolo all’indicizzazione.',
        'Struttura solida; poche correzioni per completare le basi.',
        'Alcuni elementi on-page mancano o sono duplicati.',
        'Qualcosa ostacola l’indicizzazione: da sistemare prima di tutto.',
    ]),
    ('a11y', 'Accessibilità', 'Peso 15', 'WCAG 2.1 / EAA', [
        'Poche o nessuna barriera: sito fruibile secondo WCAG 2.1 AA.',
        'Buon livello; restano barriere minori da rimuovere.',
        'Diverse barriere rilevate: contrasti, etichette, navigazione.',
        'Barriere gravi: il sito è difficile da usare per molte persone (obbligo EAA).',
    ]),
    ('gdpr', 'Privacy e cookie', 'Peso 15', 'Verifica indicativa · non legale', [
        'Banner, informative e tracker in ordine nell’HTML iniziale.',
        'Impianto presente; un paio di punti da verificare a mano.',
        'Mancano elementi o alcuni tracker vanno governati meglio.',
        'Tracker attivi senza banner o policy assenti: rischio concreto col Garante.',
    ]),
    ('bp', 'Best practice', 'Peso 10', 'Google PageSpeed', [
        'Sito tecnicamente pulito: HTTPS, console senza errori, librerie aggiornate.',
        'Buon livello tecnico; qualche avviso da chiudere.',
        'Diversi avvisi tecnici: sicurezza, errori console, immagini.',
        'Problemi tecnici diffusi che indeboliscono affidabilità e sicurezza.',
    ]),
    ('ai', 'Pronto per l’AI', 'Peso 10', '4 segnali tecnici', [
        '4 segnali su 4: il sito è leggibile e citabile dai modelli AI.',
        '3 segnali su 4: manca poco alla piena prontezza AI.',
        '2 segnali su 4: dati strutturati o sitemap da completare.',
        '0–1 segnali: i modelli AI faticano a leggere e citare il sito.',
    ]),
    ('co2', 'Impatto CO₂', 'Peso 5', 'Modello SWD', [
        'Pagina leggera: emissioni sotto la media del web.',
        'Vicino alla media; c’è margine per alleggerire.',
        'Sopra la media: la pagina è pesante da caricare.',
        'Molto sopra la media: pagina pesante, costo ambientale e di velocità.',
    ]),
]


def _checkup_dim_card(key, label, weight, engine, verdicts):
    extra = '<span class="sr-dim-card__extra" data-sr-dim-extra></span>' if key == 'ai' else ''
    verdict_attrs = ' '.join(f'data-verdict-{i}="{v}"' for i, v in enumerate(verdicts))
    # «Approfondisci →» verso lo strumento dedicato: tutte le dimensioni tranne
    # 'bp' (best practice non ha una pagina strumento propria). L'href lo
    # calcola remarka.js (mappa dim→percorso per lingua, lang-map.php) dopo un
    # rendering con punteggio; l'etichetta viene da data-more-label sulla
    # wrapper del widget (fallback IT in JS).
    more = ('\n  <p class="sr-dim-card__more"><a data-sr-dim-more hidden target="_self">Approfondisci →</a></p>'
            if key != 'bp' else '')
    return f'''<div class="sr-card sr-dim-card" data-sr-dim="{key}" {verdict_attrs}>
  <div class="sr-dim-card__head"><p class="sr-eyebrow" style="margin:0">{label}</p><span class="sr-dim-card__weight">{weight}</span></div>
  <div class="sr-dim-card__score"><span class="sr-dim-card__score-value" data-sr-tool-score>—</span><span class="sr-dim-card__score-suffix">/100</span>{extra}</div>
  <div class="sr-barra" style="height:8px;margin-top:12px"><div class="sr-barra__fill" data-sr-tool-fill style="width:0%"></div></div>
  <p class="sr-dim-card__word" data-sr-dim-word></p>
  <p class="sr-dim-card__findings" data-sr-tool-verdict></p>
  <p class="sr-dim-card__engine sr-mono">{engine}</p>{more}
</div>'''


def _widget_checkup():
    cards = ''.join(_checkup_dim_card(*d) for d in _CHECKUP_DIMS)
    return f'''
<div class="sr-tool-widget sr-card sr-checkup" data-sr-tool="checkup" data-sr-locale="it"
     data-word-0="Eccellente" data-word-1="Buono" data-word-2="Da migliorare" data-word-3="Critico"
     data-composite-0="Sito in salute eccellente" data-composite-1="Sito in buona salute"
     data-composite-2="Sito da migliorare" data-composite-3="Sito a rischio"
     data-label-suffix=" — analisi mobile"
     data-calc-note="Calcolato su {{n}} misurazioni su 7."
     data-na-text="Non siamo riusciti a misurare questo aspetto: il sito ha rifiutato la lettura o il servizio Google era saturo."
     data-err="Non siamo riusciti a completare il check-up. Riprovate tra qualche minuto."
     data-ai-suffix=" / 4 segnali"
     data-more-label="Approfondisci →">
  <form data-sr-tool-form>
    <div class="sr-tool-row">
      <input type="text" placeholder="www.ilvostrosito.it" class="sr-text-input" required />
      <button type="submit" class="wp-block-button__link" style="padding:17px 30px">Analizza il sito — gratis</button>
    </div>
  </form>
  <p class="sr-tool-pending sr-mono" data-sr-tool-pending hidden>Analisi in corso su sette fronti — può richiedere fino a 30 secondi<span class="sr-blink">…</span></p>

  <div class="sr-tool-result" data-sr-tool-result hidden>

    <div class="sr-checkup-incomplete" data-sr-checkup-incomplete hidden>
      <h3 class="wp-block-heading">Check-up incompleto</h3>
      <p>Riprovate tra qualche minuto: alcune misure non hanno risposto (il servizio Google potrebbe essere saturo, oppure il sito ha rifiutato la lettura).</p>
      <button type="button" class="wp-block-button__link" data-sr-checkup-retry>Riprova</button>
    </div>

    <div data-sr-checkup-composite>
      <p class="sr-eyebrow">Salute del sito</p>
      <div class="sr-checkup-composite">
        <div class="sr-gauge" data-sr-gauge>
          <div class="sr-gauge__num"><span class="sr-gauge__num-value" data-sr-gauge-num>0</span><span class="sr-gauge__num-suffix">/100</span></div>
        </div>
        <div>
          <p class="sr-mono sr-checkup-url" data-sr-checkup-url></p>
          <h2 class="wp-block-heading sr-checkup-label" data-sr-checkup-label></h2>
          <p class="sr-checkup-method-note">Media pesata di 7 misure. Prestazioni, SEO, accessibilità e best practice arrivano da Google PageSpeed Insights; privacy, prontezza AI e impatto CO₂ dalle verifiche di Studio Remarka.</p>
          <p class="sr-mono sr-checkup-calc" data-sr-checkup-calc></p>
        </div>
      </div>
    </div>

    <div style="margin-top:32px">
      <p class="sr-eyebrow">Le sette misure</p>
      <h2 class="wp-block-heading" style="font-size:clamp(24px,2.4vw,32px)">Sette semafori, un punteggio</h2>
      <div class="sr-dim-grid" style="margin-top:24px">{cards}</div>
    </div>

    <div data-sr-checkup-priorities-wrap style="margin-top:32px">
      <p class="sr-eyebrow">Le priorità</p>
      <h2 class="wp-block-heading" style="font-size:clamp(24px,2.4vw,32px)">I 3 interventi che pesano di più</h2>
      <p style="margin:8px 0 20px;color:var(--sr-grigio);font-size:15.5px">Ordinati per impatto sul punteggio: quanto guadagnereste sistemandoli.</p>
      <div class="sr-priorities" data-sr-checkup-priorities></div>
    </div>

    <div data-sr-checkup-form-wrap style="margin-top:32px">
      <div class="sr-card sr-checkup-lead">
        <p class="sr-eyebrow">Report completo</p>
        <h2 class="wp-block-heading" style="font-size:clamp(22px,2.6vw,28px)">Il report completo, in PDF</h2>
        <p style="margin-top:10px;color:var(--sr-grigio);font-size:15.5px;line-height:1.6">Vi inviamo l’analisi integrale: una pagina per ognuna delle sette dimensioni, tutte le criticità rilevate e le raccomandazioni in ordine di impatto.</p>
        <ul class="sr-tool-audits" style="margin-top:18px">
          <li>Il punteggio di salute con i sette semafori</li>
          <li>Una pagina per dimensione: punteggio, cosa abbiamo trovato, cosa fare</li>
          <li>I tre interventi prioritari con le contromisure</li>
          <li>«Cosa faremmo noi» e i riferimenti di Studio Remarka</li>
        </ul>
        <form data-sr-checkup-report-form style="margin-top:24px">
          <p class="sr-hp-field" aria-hidden="true"><label>Sito web<input type="text" name="sr_checkup_hp" tabindex="-1" autocomplete="off"></label></p>
          <div class="sr-tool-row">
            <input type="email" placeholder="nome@vostraazienda.it" class="sr-text-input" required />
            <button type="submit" class="wp-block-button__link" style="padding:15px 26px">Inviatemi il report PDF</button>
          </div>
          <label class="sr-consent"><input type="checkbox" data-sr-checkup-consent required /><span>Ho letto la <a href="/privacy/">privacy policy</a> e acconsento all’invio del report e a essere ricontattato.</span></label>
          <label class="sr-consent"><input type="checkbox" data-sr-checkup-consent-monthly /><span>Inviatemi ogni mese il monitoraggio dei Core Web Vitals di questo sito.</span></label>
          <p class="sr-mono" data-sr-checkup-success hidden style="margin-top:16px;color:var(--sr-verde)">Fatto. Il report è in viaggio verso la vostra casella: se non arriva entro qualche minuto, controllate lo spam o scriveteci.</p>
          <p class="sr-form-error" data-sr-checkup-error hidden>Non siamo riusciti a inviare il report. Riprovate tra poco o scriveteci: ve lo mandiamo a mano.</p>
        </form>
        <p class="sr-mono" style="margin-top:20px;font-size:11px;color:var(--sr-grigio);opacity:.85">Niente spam. Usiamo l’indirizzo solo per il report ed eventuale ricontatto. Studio Remarka S.r.l., P.IVA GE 302230994.</p>
      </div>
    </div>

  </div>
</div>'''


def build_tool_widget(tool):
    tipo = tool['tipo']
    if tipo == 'speed':
        return _widget_speed()
    if tipo == 'seo':
        return _widget_score('seo', 'Analizza la SEO', 'Analisi Google in corso', ' — SEO on-page',
                             'Ottimo: le basi SEO on-page sono a posto.',
                             'SEO nella media: ci sono correzioni concrete da fare.',
                             'SEO on-page carente: è la priorità da sistemare.',
                             'Nessun problema SEO rilevante rilevato.')
    if tipo == 'a11y':
        return _widget_score('a11y', 'Verifica l’accessibilità', 'Analisi in corso', ' — accessibilità',
                             'Ottimo: le barriere principali sono già rimosse.',
                             'Accessibilità nella media: alcune barriere restano.',
                             'Accessibilità carente: barriere importanti per gli utenti.',
                             'Nessuna barriera rilevante rilevata.',
                             disclaimer='Controllo automatico (Lighthouse): copre parte dei criteri WCAG 2.1 AA. La conformità EAA richiede anche verifica manuale.')
    if tipo == 'co2':
        return _widget_co2()
    if tipo == 'gdpr':
        return _widget_gdpr()
    if tipo == 'ai':
        return _widget_ai()
    if tipo == 'roi':
        return _widget_roi()
    if tipo == 'checkup':
        return _widget_checkup()
    if tipo == 'eeat':
        return _widget_eeat()
    raise ValueError(f'tipo strumento sconosciuto: {tipo}')


def build_tool(tool):
    """Pagina completa di uno strumento: hero, widget (per tipo, contratto T1),
    «Come funziona» (3 passi), FAQ (3), CTA verso il servizio pertinente,
    blocco «Gli altri strumenti gratuiti» (gli altri 6).
    Il check-up completo (tipo 'checkup') è l'orchestratore delle altre 7
    misure: eyebrow dedicato invece di «Strumento gratuito /NN» e nessuna
    sezione «Come migliorare» (non prevista dal copy deck — docs/copy-checkup.md)."""
    eyebrow_text = 'Check-up completo · gratuito' if tool['tipo'] == 'checkup' else f'Strumento gratuito {tool["idx"]}'
    hero = section(
        eyebrow(eyebrow_text) + heading(1, tool['hero_titolo'], style='clamp(34px,4vw,52px)') +
        paragraph(tool['hero_sub'], color='grigio', size='medium', extra_style='max-width:100%'),
        classes='sr-section sr-hero',
    )

    widget_section = section(raw_html(build_tool_widget(tool)), classes='sr-section')

    passi = ''.join(
        f'<div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">{i:02d}</p>'
        f'<p style="font-weight:500;margin-top:8px">{t}</p>'
        f'<p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">{d}</p></div>'
        for i, (t, d) in enumerate(tool['come_funziona'], start=1)
    )
    come_funziona = section(
        eyebrow('Come funziona') + heading(2, 'Tre passaggi, nessuna registrazione') +
        group(passi, classes='', layout_type='grid', style='240px'),
        classes='sr-section sr-section--bianco',
    )

    # Sezione metodologia: cosa misura (davvero) il test — motore e segnali.
    m_h2, m_paras = tool['metodologia']
    metodologia = section(
        eyebrow('Il metodo') + heading(2, m_h2) +
        ''.join(paragraph(p, size='base', extra_style='font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px')
                for p in m_paras),
        classes='sr-section',
    )

    # Sezione lettura del risultato: punteggi, fasce, falsi allarmi.
    l_h2, l_paras = tool['lettura']
    lettura = section(
        eyebrow('Leggere il risultato') + heading(2, l_h2) +
        ''.join(paragraph(p, size='base', extra_style='font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px')
                for p in l_paras),
        classes='sr-section sr-section--bianco',
    )

    faq = section(
        eyebrow('Tre domande tipiche') + details_faq(tool['faq']),
        classes='sr-section',
    )

    # Sezione «come migliorare»: metodi concreti a griglia + link contestuali
    # (servizio + articolo blog). Va dopo la FAQ, prima della CTA. Opzionale:
    # il check-up completo non ne ha una propria nel copy deck (orchestra le
    # 7 sezioni «migliorare» già presenti nelle pagine dei singoli strumenti).
    mig = tool.get('migliorare')
    if mig:
        mig_cards = ''.join(
            f'<div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">{i:02d}</p>'
            f'<p style="font-weight:500;margin-top:8px">{t}</p>'
            f'<p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">{d}</p></div>'
            for i, (t, d) in enumerate(mig['punti'], start=1)
        )
        mig_links = ''.join(
            f'<p class="sr-card-link" style="margin-top:12px"><a href="{url}">{label} →</a></p>'
            for label, url in mig['links']
        )
        migliorare = section(
            eyebrow('Come migliorare') + heading(2, mig['h2']) +
            paragraph(mig['intro'], color='grigio', size='base',
                      extra_style='font-size:17px;line-height:1.75;max-width:75ch;margin-top:12px') +
            group(mig_cards, classes='', layout_type='grid', style='240px') +
            raw_html(f'<div style="margin-top:24px;display:flex;flex-direction:column;'
                     f'gap:8px;align-items:flex-start">{mig_links}</div>'),
            classes='sr-section sr-section--bianco',
        )
    else:
        migliorare = ''

    cta_data = tool['cta']
    cta_heading = cta_data['heading'].rstrip()
    cta_dot = '?' if cta_heading.endswith('?') else '.'
    cta = section(
        heading(2, cta_heading.rstrip('?.'), dot_char=cta_dot) +
        paragraph(cta_data['testo'], color='grigio', size='medium', extra_style='margin-top:12px') +
        buttons(cta_data['buttons'], justify='center', margin_top='28px'),
        classes='sr-section sr-dark',
    )

    altri = [t for t in TOOLS if t['slug'] != tool['slug']]
    rows = ''.join(
        f'<div><span class="sr-mono" style="color:var(--sr-oltremare)">{o["idx"]}</span>'
        f'<a href="/strumenti/{o["slug"]}/" style="color:var(--sr-inchiostro);font-size:15.5px">{o["titolo"]}</a>'
        f'<span class="sr-mono" style="color:var(--sr-oltremare)">→</span></div>'
        for o in altri
    )
    altri_section = section(
        eyebrow('Gli altri strumenti gratuiti') + raw_html(f'<div class="sr-servizi-rows">{rows}</div>'),
        classes='sr-section sr-section--bianco',
    )

    write(f'strumento-{tool["slug"]}', f'Pagina — Strumento: {tool["titolo"]}',
          f'Strumento gratuito {tool["titolo"]}: widget interattivo, come funziona, FAQ, CTA.',
          hero + widget_section + come_funziona + metodologia + lettura + faq + migliorare + cta + altri_section)


# ---------------------------------------------------------------- Città

def build_city(c):
    """Городской лендинг под «realizzazione siti web {città}». Каждый город —
    свой кейс, свои отзывы с гео-привязкой и свой FAQ (piano-contenuti-seo §2:
    содержательные страницы, не клоны)."""
    hero = section(
        eyebrow(c['eyebrow']) + heading(1, f'Realizzazione siti web a {c["nome"]}', style='clamp(38px,4.6vw,64px)') +
        paragraph(c['sub'], color='grigio', size='medium') +
        buttons([('Richiedi preventivo in 24 ore', '/#contatti', None),
                 ('Analizza il tuo sito — gratis', '/strumenti/test-velocita/', 'outline')], margin_top='28px') +
        stat_block(str(c['progetti']), f'progetti consegnati a {c["nome"]} e provincia dal {c["dal"]}', '', counter=True),
        classes='sr-section sr-hero',
    )

    servizi_rows = ''.join(
        f'<div><span style="font-size:16px;font-weight:500;color:var(--sr-inchiostro)">{s["title"]}</span>'
        f'<a href="/servizi/{s["slug"]}/" class="sr-mono" style="color:var(--sr-oltremare)">→</a></div>'
        for s in SERVICES
    )
    # H2 con la parola chiave locale (SEO on-page): Milano ha una chiave
    # propria («web agency Milano»), gli altri la forma naturale del servizio.
    servizi_heading = (f'Web agency {c["nome"]}: sei servizi, una garanzia'
                       if c['slug'] == 'milano'
                       else f'Realizzazione siti web a {c["nome"]}, e non solo')
    servizi = section(
        eyebrow('Cosa facciamo') + heading(2, servizi_heading) +
        raw_html(f'<div class="sr-servizi-rows" style="margin-top:32px">{servizi_rows}</div>'),
        classes='sr-section sr-section--bianco',
    )

    # Il caso non è un cliente locale: è un progetto REALE del gruppo Remarka
    # (docs/copy-casi-studio.md) — stessa ingegneria, ovunque sia il cliente.
    local_case = CASES_BY_SLUG[c['case_slug']]
    case_alt = local_case['alt']  # stringa già coperta dal corpus (CASES) — niente concatenazioni non traducibili
    main_shot = local_case['shots'][0]
    caso = section(
        columns([
            column(browser_frame_shot(c['case_url_label'], main_shot['file'], case_alt, main_shot['caption'], mobile=main_shot['mobile']), width='55%'),
            column(eyebrow(c['case_eyebrow']) + heading(3, c['case_title'], accent_dot=False) +
                   paragraph(local_case['risultato'], color='grigio', size='base', extra_style='margin-top:12px') +
                   raw_html(f'<p class="sr-card-link" style="margin-top:20px"><a href="/casi-studio/#{local_case["slug"]}">Leggi il caso completo →</a></p>'),
                   width='45%'),
        ], valign='center'),
        classes='sr-section',
    )

    # Прозрачный прайс-блок прямо на городской странице (формат, который
    # ранжируется по «costo sito web {città}» — см. piano-contenuti-seo §3.A).
    prezzi_rows = ''.join(
        f'<div><span style="font-size:16px;font-weight:500;color:var(--sr-inchiostro)">{t}</span>'
        f'<span class="sr-mono" style="color:var(--sr-oltremare)">{p}</span></div>'
        for t, p in [('Sito vetrina', '€ 1.900–2.800'), ('Sito aziendale', '€ 3.900–5.800'), ('E-commerce', '€ 7.500–14.000')]
    )
    prezzi_local = section(
        eyebrow('Prezzi chiari, anche qui') +
        heading(2, f'Quanto costa un sito web a {c["nome"]}', dot_char='?') +
        raw_html(f'<div class="sr-servizi-rows" style="margin-top:32px">{prezzi_rows}</div>') +
        paragraph('Prezzo chiuso nel preventivo, PageSpeed 90+ e data di consegna scritti nel contratto. Gli stessi prezzi pubblici, ovunque siate.',
                   color='grigio', size='base', extra_style='margin-top:24px') +
        raw_html('<p class="sr-card-link" style="margin-top:12px"><a href="/prezzi/">Confronta tutte le tariffe →</a></p>'),
        classes='sr-section sr-section--bianco',
    )

    if c.get('has_office'):
        dove = section(
            raw_html('<div class="sr-dove-siamo">') +
            raw_html('<div class="sr-dove-siamo__map" aria-hidden="true"></div>') +
            group(
                eyebrow('Dove siamo') +
                paragraph(c['indirizzo'], extra_style='margin-top:12px;font-size:16px') +
                raw_html(f'<p class="sr-mono" style="margin-top:8px;font-size:13px;color:var(--sr-grigio)">{c["metro"]}</p>') +
                paragraph(c['orari'], color='grigio', size='base', extra_style='margin-top:16px') +
                raw_html(f'<p class="sr-mono" style="margin-top:6px;font-size:14px">{c["telefono"]}</p>'),
                classes='sr-card',
            ) + raw_html('</div>'),
            classes='sr-section',
        )
    else:
        dove = section(
            eyebrow(f'Come lavoriamo con {c["nome"]}') +
            heading(2, 'Vicini quanto serve') +
            paragraph(c['vicino'], color='grigio', size='medium', extra_style='margin-top:16px;max-width:70ch'),
            classes='sr-section',
        )

    rec_cards = ''.join(
        f'<div class="sr-card"><p class="sr-mono" style="color:var(--sr-oltremare)">★★★★★</p>'
        f'<p style="margin-top:14px;font-size:15.5px;line-height:1.6">«{q}»</p>'
        f'<p class="sr-mono" style="margin-top:16px;font-size:13px;color:var(--sr-grigio)">{a}</p></div>'
        for q, a in c['recensioni']
    )
    recensioni = section(
        eyebrow(f'Dicono di noi, da {c["nome"]} e dintorni') + heading(2, 'Recensioni Google verificate') +
        raw_html('<p class="sr-mono" style="margin:16px 0 32px;color:var(--sr-oltremare)">★ 4,9 · 47 recensioni</p>') +
        group(rec_cards, classes='', layout_type='grid', style='260px'),
        classes='sr-section' + ('' if c.get('has_office') else ' sr-section--bianco'),
    )

    faq = section(
        eyebrow('Domande da ' + c['nome']) +
        details_faq(c['faq']),
        classes='sr-section',
    )

    cta = section(
        heading(2, 'Parliamo del vostro progetto') +
        paragraph('Primo incontro gratuito, da voi in azienda. Preventivo chiuso entro 24 ore.',
                   color='grigio', size='medium', extra_style='margin-top:12px') +
        buttons([('Richiedi preventivo in 24 ore', '/#contatti', None),
                 ('WhatsApp Business', 'https://wa.me/390000000000', 'whatsapp')], justify='center', margin_top='28px'),
        classes='sr-section sr-dark',
    )
    write(f'citta-{c["slug"]}', f'Pagina — Città: {c["nome"]}',
          f'Landing locale «realizzazione siti web {c["nome"].lower()}»: servizi, caso, prezzi, recensioni, FAQ.',
          hero + servizi + caso + prezzi_local + dove + recensioni + faq + cta)


# ---------------------------------------------------------------- Export Ready (линия 2)

def build_export_ready():
    e = EXPORT_READY
    hero = hero_interno(e['eyebrow'], e['hero_title'], e['hero_sub'],
                         extra_html=buttons([
                             ('Richiedi preventivo in 24 ore', '/#contatti', None),
                             ('Calcola il ROI della localizzazione', '/strumenti/roi-localizzazione/', 'outline'),
                         ], margin_top='36px'),
                         stat=(e['hero_stat_value'], e['hero_stat_label']))

    problema = section(
        columns([
            column(eyebrow('Il problema') + heading(2, e['problema_heading']), width='38%'),
            column(paragraph(e['problema_testo'], size='base', extra_style='font-size:17px'), width='62%'),
        ]),
        classes='sr-section',
    )

    garanzie = section(
        eyebrow('Garanzie') + heading(2, e['garanzie_heading']) + checklist(e['garanzie']),
        classes='sr-section sr-section--bianco',
    )

    formati_cards = ''.join(
        f'<div class="sr-card"><h3 class="wp-block-heading" style="font-size:22px">{nome}</h3>'
        f'<p class="sr-mono" style="font-size:24px;color:var(--sr-oltremare);margin-top:12px">{prezzo}</p>'
        f'<p style="margin-top:14px;font-size:15.5px;color:var(--sr-grigio);line-height:1.6">{desc}</p></div>'
        for nome, prezzo, desc in e['formati']
    )
    formati = section(
        eyebrow('Due formati') + heading(2, 'Un mercato o una strategia') +
        group(formati_cards, classes='', layout_type='grid', style='320px') +
        paragraph('Prezzo chiuso nel preventivo, come per tutti i nostri servizi. Fattura elettronica, pagamento in tre tranche.',
                   color='grigio', size='small', extra_style='margin-top:24px'),
        classes='sr-section',
    )

    proc_rows = ''.join(
        f'<div class="sr-step"><p class="sr-mono" style="color:var(--sr-oltremare)">{n}</p>'
        f'<p style="font-weight:500;margin-top:8px">{t}</p>'
        f'<p style="font-size:14.5px;color:var(--sr-grigio);margin-top:8px">{d}</p></div>'
        for n, t, d in e['processo']
    )
    processo = section(
        eyebrow('Come lavoriamo') + heading(2, 'Quattro passaggi, un contratto') +
        group(proc_rows, classes='', layout_type='grid', style='240px'),
        classes='sr-section sr-section--bianco',
    )

    faq = section(
        eyebrow('Tre domande tipiche') + details_faq(e['faq']),
        classes='sr-section',
    )

    cta = section(
        heading(2, 'Il vostro prossimo mercato parla un’altra lingua', dot_char='?') +
        paragraph('Analisi gratuita del sito attuale e del mercato target. Preventivo chiuso entro 24 ore.',
                   color='grigio', size='medium', extra_style='margin-top:12px') +
        buttons([('Richiedi preventivo in 24 ore', '/#contatti', None)], justify='center', margin_top='28px'),
        classes='sr-section sr-dark',
    )
    write('servizio-export-ready', 'Pagina — Servizio: Export Ready',
          'Flagship: sito + versione estera sotto un unico contratto, localizzazione da madrelingua, KPI per mercato.',
          hero + problema + garanzie + formati + processo + faq + cta)


# ---------------------------------------------------------------- Web app (линия 3)

def build_web_app():
    w = WEB_APP
    hero = hero_interno(w['eyebrow'], w['hero_title'], w['hero_sub'],
                         extra_html=buttons([
                             ('Richiedi preventivo in 24 ore', '/#contatti', None),
                             ('Vedi i casi studio', '/casi-studio/', 'outline'),
                         ], margin_top='36px'),
                         stat=(w['hero_stat_value'], w['hero_stat_label']))

    per_chi = section(
        columns([
            column(eyebrow('Per chi è') + heading(2, w['per_chi_heading']), width='38%'),
            column(list_rows(w['per_chi']), width='62%'),
        ]),
        classes='sr-section',
    )

    formati_cards = ''.join(
        f'<div class="sr-card"><h3 class="wp-block-heading" style="font-size:22px">{nome}</h3>'
        f'<p class="sr-mono" style="font-size:24px;color:var(--sr-oltremare);margin-top:12px">{prezzo}</p>'
        f'<p style="margin-top:14px;font-size:15.5px;color:var(--sr-grigio);line-height:1.6">{desc}</p></div>'
        for nome, prezzo, desc in w['formati']
    )
    formati = section(
        eyebrow('Due formati') + heading(2, 'Perimetro chiuso o crescita per iterazioni') +
        group(formati_cards, classes='', layout_type='grid', style='320px'),
        classes='sr-section sr-section--bianco',
    )

    prove = section(
        columns([
            column(eyebrow('Product Lab') + heading(2, w['prove_heading']), width='38%'),
            column(paragraph(w['prove_testo'], size='base', extra_style='font-size:17px'), width='62%'),
        ]),
        classes='sr-section',
    )

    faq = section(
        eyebrow('Tre domande tipiche') + details_faq(w['faq']),
        classes='sr-section sr-section--bianco',
    )

    cta = section(
        heading(2, 'Raccontateci il processo da automatizzare') +
        paragraph('Analisi gratuita e un preventivo chiuso: perimetro, prezzo e data, tutti e tre nel contratto.',
                   color='grigio', size='medium', extra_style='margin-top:12px') +
        buttons([('Richiedi preventivo in 24 ore', '/#contatti', None)], justify='center', margin_top='28px'),
        classes='sr-section sr-dark',
    )
    write('servizio-web-app', 'Pagina — Servizio: Web app su misura',
          'Linea Prodotti digitali: web app, aree clienti, configuratori. MVP Sprint e Product Build.',
          hero + per_chi + formati + prove + faq + cta)


# ---------------------------------------------------------------- Adeguamento EAA
# Servizio «speciale» (docs/copy-eaa.md): niente mini_caso (nessun caso
# inventato per un obbligo di legge), blocchi processo/garanzie propri —
# stesso trattamento di Export Ready/Web app, non build_servizio().

def build_adeguamento_eaa():
    e = ADEGUAMENTO_EAA
    hero = hero_interno(e['eyebrow'], e['hero_title'], e['hero_sub'],
                         extra_html=buttons([
                             ('Richiedi l’audit di accessibilità', '/#contatti', None),
                             ('Verifica subito il tuo sito', '/strumenti/verifica-accessibilita/', 'outline'),
                         ], margin_top='36px'),
                         stat=(e['hero_stat_value'], e['hero_stat_label']))

    per_chi = section(
        columns([
            column(eyebrow('Per chi è') + heading(2, e['per_chi_heading']), width='38%'),
            column(list_rows(e['per_chi']), width='62%'),
        ]),
        classes='sr-section',
    )

    include = section(
        eyebrow('Cosa include') + heading(2, e['include_heading']) + checklist(e['include']),
        classes='sr-section sr-section--bianco',
    )

    week_cols = ''.join(
        f'<div class="sr-week"><p class="sr-week-chip sr-no-margin">{settimana}</p>'
        f'<div class="sr-week__steps"><div class="sr-week__step">'
        f'<p class="sr-step__head sr-no-margin"><span class="sr-step-num">{i:02d}</span></p>'
        f'<h4>{passo}</h4><p>{testo}</p></div></div></div>'
        for i, (settimana, passo, testo) in enumerate(e['processo'], start=1)
    )
    processo = section(
        eyebrow('Come lavoriamo') + heading(2, e['processo_heading']) +
        raw_html(f'<div class="sr-weeks sr-cascade">{week_cols}</div>') +
        raw_html(f'<p class="sr-eyebrow" style="margin-top:44px">{e["processo_note"]}</p>'),
        classes='sr-section sr-section--bianco',
    )

    prezzo_link_label, prezzo_link_url = e['prezzo_link']
    prezzo = section(
        columns([
            column(eyebrow('Prezzo') + heading(2, 'Prezzo chiuso, dopo l’audit') +
                   raw_html(f'<p class="sr-mono" style="font-size:32px;color:var(--sr-oltremare);margin-top:16px">{e["prezzo_range"]}</p>') +
                   paragraph(e['prezzo_lede'], size='base', extra_style='margin-top:16px;font-size:16px') +
                   raw_html(f'<p class="sr-card-link" style="margin-top:20px"><a href="{prezzo_link_url}">{prezzo_link_label} →</a></p>'),
                   width='50%'),
            column(eyebrow('Cosa fa variare il prezzo') + list_rows(e['prezzo_note']), width='50%'),
        ]),
        classes='sr-section',
    )

    garanzie = section(
        eyebrow('Garanzie') + heading(2, e['garanzie_heading']) + checklist(e['garanzie']),
        classes='sr-section sr-section--bianco',
    )

    fonti_links = ''.join(
        f'<p class="sr-card-link" style="margin-top:8px;font-size:14px">'
        f'<a href="{url}" target="_blank" rel="noopener noreferrer nofollow">{label} →</a></p>'
        for label, url in e['fonti']
    )
    faq = section(
        eyebrow('Domande frequenti') + details_faq(e['faq']) +
        raw_html('<div style="margin-top:32px">') +
        list_rows(e['fatti'] + ['Standard di riferimento: <strong>WCAG 2.1 livello AA</strong>.']) +
        raw_html(fonti_links) +
        paragraph(e['disclaimer'], color='grigio', size='small', extra_style='margin-top:20px') +
        raw_html('</div>'),
        classes='sr-section',
    )

    cta = section(
        heading(2, e['cta']['heading']) +
        paragraph(e['cta']['testo'], color='grigio', size='medium', extra_style='margin-top:12px') +
        buttons(e['cta']['buttons'], justify='center', margin_top='28px'),
        classes='sr-section sr-dark',
    )
    write('servizio-adeguamento-eaa', 'Pagina — Servizio: Adeguamento EAA',
          'Servizio conformità European Accessibility Act: audit, correzioni, dichiarazione di accessibilità e verifica finale WCAG 2.1 AA.',
          hero + per_chi + include + processo + prezzo + garanzie + faq + cta)


# ---------------------------------------------------------------- Chi siamo / legal

def build_chi_siamo():
    hero = section(
        eyebrow('Chi siamo') +
        heading(1, 'Un gruppo che lavora con le lingue e il web dal 2001', style='clamp(34px,4vw,52px)') +
        paragraph(
            'Studio Remarka nasce all’interno del gruppo Remarka, agenzia di traduzioni attiva dal 2001. '
            'Applichiamo la stessa precisione contrattuale alla velocità dei siti che progettiamo: numeri misurati, non promesse commerciali.',
            color='grigio', size='medium', extra_style='max-width:100%'),
        classes='sr-section sr-hero',
    )
    write('chi-siamo', 'Pagina — Chi siamo', 'Storia dello studio e del gruppo Remarka.', hero)


def build_legal_page(slug, title, eyebrow_text, body_text):
    hero = section(
        eyebrow(eyebrow_text) + heading(1, title, style='clamp(30px,3.6vw,44px)') +
        paragraph(body_text, size='base', extra_style='margin-top:20px;font-size:16px'),
        classes='sr-section sr-hero',
    )
    write(slug, f'Pagina — {title}', f'Testo segnaposto per {title}: da sostituire con testo legale definitivo.', hero)


# ---------------------------------------------------------------- Blog

def build_blog_index():
    hero = section(eyebrow('Blog') + heading(1, 'Appunti tecnici, in italiano', style='clamp(38px,4.6vw,64px)') +
                    paragraph('Niente marketing travestito da articolo: solo quello che impariamo consegnando siti veloci.',
                               color='grigio', size='medium'),
                    classes='sr-section sr-hero')

    rows = ''.join(
        f'<a href="/blog/{p["slug"]}/" class="sr-blog-row" style="color:inherit">'
        f'<span class="sr-blog-date">{p["data"]}</span>'
        f'<span class="sr-blog-body"><span style="font-family:var(--sr-font-display);font-weight:500;font-size:26px">{p["titolo"]}</span>'
        f'<span style="font-size:15.5px;color:var(--sr-grigio)">{p["estratto"]}</span></span></a>'
        for p in BLOG_POSTS
    )
    list_section = section(raw_html(rows), classes='sr-section')
    write('blog-index', 'Pagina — Blog (elenco)', 'Elenco articoli, riga data + titolo + estratto.', hero + list_section)


def blog_figure(fig, cover=False):
    """Иллюстрация статьи (фирменный SVG). cover=True — обложка под H1
    (без подписи, с рамкой), иначе — схема/диаграмма с mono-подписью.
    loading=lazy, max-width:100% (адаптив), alt переводится конвейером."""
    margin = '8px 0 8px' if cover else '36px 0 8px'
    cap = ''
    if not cover and fig.get('caption'):
        cap = (f'<figcaption class="sr-mono" style="margin-top:12px;font-size:12.5px;'
               f'letter-spacing:0.04em;color:var(--sr-grigio);max-width:75ch">{fig["caption"]}</figcaption>')
    return raw_html(
        f'<figure class="wp-block-image size-large" style="margin:{margin}">'
        f'<img src="{fig["src"]}" alt="{fig["alt"]}" loading="lazy" '
        f'style="max-width:100%;height:auto;display:block;border:1px solid var(--sr-bordo)"/>'
        f'{cap}</figure>'
    )


def _blog_section_links(links):
    # Link contestuali dentro una sezione: interni (perelinkovka: servizio/
    # strumento/articolo vicino — href localizzato dal conveyor) oppure esterni
    # a fonti autorevoli (http(s): target _blank rel noopener, fuori dalla mappa
    # href, restano invariati in EN). Ogni etichetta è un nodo di testo intero.
    out = ''
    for label, url in links:
        attrs = ' target="_blank" rel="noopener"' if url.startswith('http') else ''
        out += (f'<p class="sr-card-link" style="margin-top:14px">'
                f'<a href="{url}"{attrs}>{label} →</a></p>')
    return out


def _blog_fonti(fonti):
    """Blocco «Fonti» in chiusura d'articolo (requisito titolare 15.07): elenco
    di 3–5 prime fonti autorevoli, ognuna con un link esterno (target _blank
    rel noopener) e una frase di contesto. Etichetta e nota sono nodi di testo
    interi e distinti (nessun frammento con trattino), tradotti dal conveyor."""
    items = ''.join(
        f'<li style="margin-top:16px;line-height:1.55">'
        f'<a href="{url}" target="_blank" rel="noopener">{label}</a>'
        f'<span style="display:block;font-size:14.5px;color:var(--sr-grigio);margin-top:4px">{nota}</span>'
        f'</li>'
        for label, url, nota in fonti
    )
    return (
        heading(2, 'Fonti', style='clamp(24px,2.6vw,32px)') +
        paragraph('Le cifre e le affermazioni di questo articolo vengono da qui. Sono prime fonti, non riassunti: apritele e verificate.',
                  size='base', extra_style='font-size:16px;line-height:1.7;max-width:75ch;margin-top:8px') +
        raw_html(f'<ul style="list-style:none;padding:0;margin:20px 0 0;border-top:1px solid var(--sr-bordo)">'
                 f'{items}</ul>')
    )


def build_blog_post(p):
    hero = section(
        raw_html(f'<p class="sr-mono" style="color:var(--sr-grigio);font-size:13px">{p["data"]}</p>') +
        heading(1, p['titolo'], accent_dot=False, style='clamp(32px,4vw,48px)') +
        (blog_figure(p['cover'], cover=True) if p.get('cover') else ''),
        classes='sr-section',
    )

    # Полноформатная статья: intro + секции (h2 + абзацы + опц. список +
    # опц. диаграмма + опц. контекстные ссылки). Короткий формат (только
    # corpo) остаётся для старых заглушек.
    inner = ''
    if p.get('sezioni'):
        inner += paragraph(p['corpo'], size='base', extra_style='font-size:18px;line-height:1.75;max-width:75ch')
        for sez in p['sezioni']:
            inner += heading(2, sez['titolo'], style='clamp(24px,2.6vw,32px)')
            for par in sez.get('paragrafi', []):
                inner += paragraph(par, size='base', extra_style='font-size:17px;line-height:1.75;max-width:75ch;margin-top:16px')
            if sez.get('lista'):
                inner += list_rows(sez['lista'])
            if sez.get('figura'):
                inner += blog_figure(sez['figura'])
            if sez.get('links'):
                inner += raw_html(_blog_section_links(sez['links']))
    else:
        inner += paragraph(p['corpo'], size='base', extra_style='font-size:17px;line-height:1.7')

    if p.get('fonti'):
        inner += _blog_fonti(p['fonti'])

    if p.get('cta'):
        label, url = p['cta']
        inner += raw_html(f'<p class="sr-card-link" style="margin-top:32px"><a href="{url}">{label} →</a></p>')

    body = section(
        inner + buttons([('← Tutti gli articoli', '/blog/', 'outline')], margin_top='40px'),
        classes='sr-section',
    )
    write(f'blog-{p["slug"]}', f'Pagina — Articolo: {p["titolo"]}', f'Articolo blog: {p["titolo"]}', hero + body)


# Mesi abbreviati italiani (campo `data` di BLOG_POSTS) → numero, per ISO 8601.
_MESI_IT = {'GEN': '01', 'FEB': '02', 'MAR': '03', 'APR': '04', 'MAG': '05', 'GIU': '06',
            'LUG': '07', 'AGO': '08', 'SET': '09', 'OTT': '10', 'NOV': '11', 'DIC': '12'}


def _blog_iso_date(data_str):
    """'15 LUG 2026' → '2026-07-15'."""
    giorno, mese, anno = data_str.split()
    return f'{anno}-{_MESI_IT[mese.upper()]}-{int(giorno):02d}'


def build_blog_schema_map():
    """Genera inc/blog-schema-map.php: mappa slug-foglia (IT/EN/RU) →
    {date ISO, image} per l'hook JSON-LD BlogPosting (functions.php). Un'unica
    fonte di verità (BLOG_POSTS + lang.BLOG_SLUGS), niente duplicazione a mano.
    L'headline non sta qui: l'hook usa get_the_title() (già localizzato dalla
    pagina), così non si duplicano i titoli — RU compreso. dateModified è
    gestito dall'hook. Gli articoli solo-IT+EN (batch 1) non emettono la
    riga RU: la pagina RU non esiste ancora (piano-blog batch 5–6)."""
    import lang as L  # noqa: E402
    RETROFIT = '2026-07-15'  # ретрофит-проход: обновлены все статьи (dateModified)
    lines = [
        '<?php',
        '/**',
        ' * Автогенерировано build-tools/generate_pages.py:build_blog_schema_map() —',
        ' * НЕ редактировать вручную. Карта slug-статьи → дата публикации (ISO) и',
        ' * обложка, для JSON-LD BlogPosting (см. remarka_blog_posting_schema).',
        ' */',
        'return array(',
        f"\t'_modified' => '{RETROFIT}',",
        "\t'posts' => array(",
    ]
    seen = set()  # dedup: alcuni slug coincidono tra lingue (es. core-web-vitals-2026)
    for p in BLOG_POSTS:
        it_slug = p['slug']
        iso = _blog_iso_date(p['data'])
        image = p['cover']['src'] if p.get('cover') else ''
        slugs = [it_slug, L.BLOG_SLUGS[it_slug]['en']]
        if it_slug not in L.BLOG_IT_EN_ONLY:
            slugs.append(L.BLOG_SLUGS[it_slug]['ru'])
        for leaf in slugs:
            if leaf in seen:
                continue
            seen.add(leaf)
            lines.append(f"\t\t'{leaf}' => array( 'date' => '{iso}', 'image' => '{image}' ),")
    lines.append('\t),')
    lines.append(');')
    out = os.path.join(os.path.dirname(__file__), '..', 'remarka-studio', 'inc', 'blog-schema-map.php')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    print(f'  blog-schema-map.php: {sum(1 for _ in BLOG_POSTS)} articoli')


def main():
    print('Servizi:')
    build_servizi_index()
    for svc in SERVICES:
        build_servizio(svc)
    build_export_ready()
    build_web_app()
    build_adeguamento_eaa()

    print('Casi studio:')
    build_casi_studio_index()

    print('Prezzi:')
    build_prezzi()

    print('Strumenti:')
    build_strumenti_index()
    for tool in TOOLS:
        build_tool(tool)

    print('Città:')
    for c in CITIES:
        build_city(c)

    print('Chi siamo e pagine legali:')
    build_chi_siamo()
    build_legal_page('privacy', 'Privacy policy', 'Privacy policy',
                      'Contenuto legale da redigere con un consulente privacy prima del lancio. I dati raccolti tramite il modulo contatti restano nell’Unione Europea, come indicato nel sito, e non vengono ceduti a terzi per finalità di profilazione.')
    build_legal_page('cookie-policy', 'Cookie policy', 'Cookie policy',
                      'Usiamo solo cookie tecnici necessari al funzionamento del sito. Nessun cookie di profilazione o tracciamento pubblicitario è attivo senza consenso esplicito. Contenuto legale completo da redigere con un consulente privacy prima del lancio.')
    build_legal_page('cookie-preferenze', 'Preferenze cookie', 'Preferenze cookie',
                      'Il sito usa solo cookie tecnici necessari: non esistono al momento preferenze facoltative da gestire. Questa pagina sarà ampliata se in futuro verranno introdotti cookie di terze parti.')

    print('Blog:')
    build_blog_index()
    for p in BLOG_POSTS:
        build_blog_post(p)

    print('\nFatto.')


if __name__ == '__main__':
    main()
