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
import re
import sys
from urllib.parse import quote

sys.path.insert(0, os.path.dirname(__file__))
from blocks import (  # noqa: E402
    eyebrow, heading, paragraph, buttons, column, columns, group, section,
    raw_html, image, table, details_faq, stat_block, list_rows, checklist,
    metric_rows, browser_frame, case_screenshot_src, barra, barra_row,
    pull_quote, chapter, compare_table_row, pattern_header,
    case_shot, browser_frame_shot,
)
from data import SERVICES, CASES, CASES_BY_SLUG, TOOLS, CITY, CITIES, BLOG_POSTS, EXPORT_READY, WEB_APP, ADEGUAMENTO_EAA, RECENSIONI_LAB, RECENSIONI_URL  # noqa: E402

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
                             ('Misura i segnali E-E-A-T del sito', '/strumenti/segnali-eeat/'),
                             ('Scoprite come l’AI legge davvero il vostro sito', '/strumenti/sito-letto-dallai/'),
                             ('Createvi un llms.txt in un minuto', '/strumenti/generatore-llms-txt/')],
    'siti-multilingue':     [('Calcola il ROI della localizzazione', '/strumenti/roi-localizzazione/'),
                             ('Provate se i vostri testi suonano madrelingua', '/strumenti/suona-madrelingua/')],
}


# Bottone "Analizza il tuo sito" di hero/CTA scuro (owner 17.07.2026: bottone
# contestuale, non più un unico link a test-velocità). Default: check-up
# completo. Contestuale solo dove esiste già uno strumento gratuito che
# risponde esattamente al servizio (non si inventano temi AI: nessuna pagina
# fuori da /strumenti/ ne parla oggi).
ANALYZE_CTA_DEFAULT = ('Analizza il tuo sito — gratis', '/strumenti/check-up-completo/')
ANALYZE_CTA_BY_SERVICE = {
    'siti-pwa':         ('Misura la velocità — gratis', '/strumenti/test-velocita/'),
    'seo-tecnica':      ('Analisi SEO — gratis', '/strumenti/analisi-seo/'),
    'siti-multilingue': ('Analisi SEO — gratis', '/strumenti/analisi-seo/'),
}


def analyze_cta_button(slug=None):
    """Ritorna la tripla (label, href, style) per il bottone "outline" di
    hero/CTA scuro. Un solo posto da aggiornare per default e contesti."""
    label, href = ANALYZE_CTA_BY_SERVICE.get(slug, ANALYZE_CTA_DEFAULT)
    return (label, href, 'outline')


# Riga di fiducia sotto i bottoni della card premium .sr-cta-band (redesign
# 18.07.2026, mockup approvato dal titolare). Testo fisso identico su tutte
# le 13 varianti della banda — niente icone SVG nel contenuto (wp_kses le
# taglierebbe), solo tipografia mono (vedi .sr-cta-band__trust in remarka.css).
CTA_TRUST_ITEMS = [
    ('100% gratuito', 'Nessun impegno'),
    ('Risposta in 24 ore', 'Preventivo dettagliato'),
    ('Dati al sicuro', 'Massima riservatezza'),
]


def cta_trust_row():
    items = ''.join(
        f'<div class="sr-cta-band__trust-item"><strong>{title}</strong><span>{sub}</span></div>'
        for title, sub in CTA_TRUST_ITEMS
    )
    return raw_html(f'<div class="sr-cta-band__trust">{items}</div>')


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


# Riga area clienti nelle pagine servizio (docs/piano-promo-cabinet-lab.md §3.5):
# ogni progetto include il cabinet — una riga sobria, stessa classe delle
# righe strumento, link alla pagina /area-clienti/ (localizzato dal conveyor).
AREA_CLIENTI_LINE = ('Ogni progetto include l’area clienti: fasi, approvazioni e file in un unico posto →')


def _area_clienti_line_html(margin_top='18px'):
    return (f'<p class="sr-card-link" style="margin-top:{margin_top}">'
            f'<a href="/area-clienti/">{AREA_CLIENTI_LINE}</a></p>')


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

    # Visual di direzione sulle card corrispondenti (manifest images/chatgpt):
    # immagini decorative (alt vuoto: il titolo della card è il testo).
    CARD_VISUALS = {
        'siti-aziendali': 'visual-sito-aziendale.webp',
        'e-commerce':     'visual-ecommerce.webp',
    }
    cards = []
    for svc in SERVICES:
        visual = CARD_VISUALS.get(svc['slug'])
        visual_html = (
            raw_html(f'<img class="sr-card__visual" src="/wp-content/themes/remarka-studio/assets/img/casi/{visual}" '
                     f'alt="" width="1200" height="800" loading="lazy" decoding="async"/>')
            if visual else ''
        )
        card = (
            visual_html +
            heading(3, svc['title'], accent_dot=False) +
            paragraph(svc['hero_sub'], color='grigio', size='small') +
            raw_html(f'<p class="sr-card-link" style="margin-top:16px"><a href="/servizi/{svc["slug"]}/">Scopri →</a></p>')
        )
        cards.append(group(card, classes='sr-card'))

    grid = section(group(''.join(cards), classes='', layout_type='grid', style='300px'), classes='sr-section')

    # Линии 2 и 3 концепции — отдельный блок «premium» под сеткой базовых услуг.
    premium_cards = ''.join(
        f'<div class="sr-card sr-card--carta">'
        + (f'<img class="sr-card__visual" src="/wp-content/themes/remarka-studio/assets/img/casi/{vis}" '
           f'alt="" width="1200" height="800" loading="lazy" decoding="async"/>' if vis else '')
        + f'<p class="sr-eyebrow">{ey}</p>'
        f'<h3 class="wp-block-heading" style="font-size:22px">{t}</h3>'
        f'<p style="margin-top:12px;font-size:15.5px;color:var(--sr-grigio);line-height:1.6">{d}</p>'
        f'<p class="sr-card-link" style="margin-top:16px"><a href="{u}">Scopri →</a></p></div>'
        for ey, t, d, u, vis in [
            ('Flagship', 'Export Ready', 'Il sito e la sua versione estera sotto un unico contratto: localizzazione da madrelingua, SEO internazionale, KPI per mercato.', '/servizi/export-ready/', None),
            ('Prodotti digitali', 'Web app su misura', 'Aree clienti, configuratori, portali B2B e integrazioni: quando un sito non basta.', '/servizi/web-app/', 'visual-webapp.webp'),
            ('Obbligo di legge', 'Adeguamento EAA', 'Il vostro sito già online, portato allo standard WCAG 2.1 AA: audit, correzioni e dichiarazione di accessibilità. Obbligo di legge dal 2025.', '/servizi/adeguamento-eaa/', None),
        ]
    )
    premium = section(
        eyebrow('Oltre il sito') + heading(2, 'Quando serve di più') +
        group(premium_cards, classes='', layout_type='grid', style='320px'),
        classes='sr-section sr-section--bianco',
    )

    # Polosa dei progetti (manifest images/chatgpt): tre schermate REALI dai
    # progetti del gruppo — techperevod.com, perevod4.ru, TMS interno. I file
    # servizi-*.webp portano già i margini chiari: si mostrano interi, mai
    # ritagliati (niente cover). Didascalie = domini/nomi veri, non inventati.
    proj_items = [
        ('servizi-techperevod.webp', 'techperevod.com', 'Schermata reale del sito techperevod.com'),
        ('servizi-perevod4-catalog.webp', 'perevod4.ru', 'Schermata reale del catalogo perevod4.ru'),
        ('servizi-tms.webp', 'TMS · interno', 'Schermata reale del TMS interno del gruppo'),
    ]
    proj_figs = ''.join(
        f'<figure class="sr-proj-strip__item"><img src="/wp-content/themes/remarka-studio/assets/img/casi/{img}" '
        f'alt="{alt}" width="960" height="640" loading="lazy" decoding="async"/>'
        f'<figcaption class="sr-mono">{label}</figcaption></figure>'
        for img, label, alt in proj_items
    )
    progetti = section(
        eyebrow('Dai progetti del gruppo') + heading(2, 'Interfacce vere, in produzione') +
        paragraph('Tre schermate dai progetti che il gruppo Remarka usa e mantiene ogni giorno — non mockup. '
                  'I casi completi, con i link ai siti vivi, sono nel catalogo.',
                   color='grigio', size='medium', extra_style='max-width:70ch') +
        raw_html(f'<div class="sr-proj-strip">{proj_figs}</div>') +
        raw_html('<p class="sr-card-link" style="margin-top:24px"><a href="/casi-studio/">Tutti i progetti, con i link vivi →</a></p>'),
        classes='sr-section',
    )

    # CTA di chiusura (owner 17.07.2026 — unificazione banner: pagina
    # commerciale, non ha senso l'asimmetria con strumenti-index/casi-studio/
    # prezzi, che un banner ce l'hanno). Stesso testo/stile riusato dalle
    # altre pagine (sr-cta-band), non un banner nuovo inventato.
    cta = section(
        heading(2, 'Parliamo del vostro sito', style=None) +
        paragraph('Analisi gratuita del sito attuale, preventivo chiuso entro 24 ore dalla chiamata.',
                   color='grigio', size='medium', extra_style='margin-top:12px') +
        buttons([('Richiedi preventivo in 24 ore', '/#contatti', None),
                 analyze_cta_button()],
                justify='center', margin_top='28px') +
        cta_trust_row(),
        classes='sr-section sr-cta-band',
    )
    write('servizi-index', 'Pagina — Servizi (elenco)', 'Elenco dei servizi con link alle pagine dettaglio, linee premium e polosa dei progetti reali.',
          hero + grid + premium + progetti + cta)


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
        eyebrow('Cosa include') + heading(2, svc['include_heading']) + checklist(svc['include']) +
        raw_html(_area_clienti_line_html()),
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
                 analyze_cta_button(svc['slug'])],
                justify='center', margin_top='28px') +
        cta_trust_row(),
        classes='sr-section sr-cta-band',
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
        ], justify='center', margin_top='28px') +
        cta_trust_row(),
        classes='sr-section sr-cta-band',
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
        ('Area clienti: fasi, approvazioni, fatture', [True, True, True]),
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
        buttons([('Richiedi preventivo dettagliato', '/#contatti', None)], justify='center', margin_top='28px') +
        cta_trust_row(),
        classes='sr-section sr-cta-band',
    )
    write('prezzi', 'Pagina — Prezzi (completa)',
          'Pagina prezzi con tabella comparativa completa (min-width 840px, scroll orizzontale su mobile).',
          hero + lancio_banner + table_section + market + variazioni + cta)


# ---------------------------------------------------------------- Strumenti

# Grafiche ritagliate dal macro-mockup owner 18.07.2026, v2 (sorgenti owner
# migliorate — foglio 11 carte 3x + hero dedicato, docs/piano-toolimg,
# nessun redisegno SVG — decisione owner finale, si ritaglia il PNG sorgente).
# Dimensioni display = 1/3 dei px del ritaglio (i sorgenti v2 sono ad alta
# risoluzione: divisore 3 tiene l'ingombro visivo vicino alla v1 dando
# nitidezza retina 3x); file in assets/img/tools/.
TOOLS_HERO_IMG = dict(file='tools-hero.webp', w=328, h=249,
                       alt='Dashboard del check-up con punteggio di salute 87 su 100 e grafico delle prestazioni')

TOOLS_CARD_IMG = {
    'test-velocita': dict(file='tool-test-velocita.webp', w=94, h=35,
                           alt='Grafico dell’andamento di velocità e tachimetro del punteggio PageSpeed'),
    'analisi-seo': dict(file='tool-analisi-seo.webp', w=99, h=38,
                         alt='Checklist SEO on-page e grafico di crescita della visibilità in ricerca'),
    'check-gdpr': dict(file='tool-check-gdpr.webp', w=107, h=38,
                        alt='Icone di verifica cookie, informative privacy e badge di conformità GDPR'),
    'roi-localizzazione': dict(file='tool-roi-localizzazione.webp', w=105, h=38,
                                alt='Grafico a barre crescenti con icona di ritorno economico della localizzazione'),
    'verifica-accessibilita': dict(file='tool-verifica-accessibilita.webp', w=99, h=38,
                                    alt='Icona di accessibilità con indicatori di conformità verificati'),
    'sito-pronto-ai': dict(file='tool-sito-pronto-ai.webp', w=107, h=40,
                            alt='Diagramma di segnali tecnici collegati e checklist di prontezza per l’AI'),
    'impatto-co2': dict(file='tool-impatto-co2.webp', w=105, h=35,
                         alt='Grafico dell’impronta di CO₂ generata dalle visite al sito'),
    'segnali-eeat': dict(file='tool-segnali-eeat.webp', w=98, h=35,
                          alt='Quattro icone dei pilastri E-E-A-T: esperienza, autorevolezza, verifica e affidabilità'),
    'sito-letto-dallai': dict(file='tool-sito-letto-dallai.webp', w=107, h=29,
                               alt='Blocchi di testo della pagina analizzati e icona a forma di occhio dell’AI'),
    'suona-madrelingua': dict(file='tool-suona-madrelingua.webp', w=105, h=23,
                               alt='Forma d’onda audio del testo con punteggio di naturalezza 92'),
    'generatore-llms-txt': dict(file='tool-generatore-llms-txt.webp', w=110, h=22,
                                 alt='Anteprima del file llms.txt generato automaticamente'),
}


def _tool_img_html(img, style=None):
    src = f'/wp-content/themes/remarka-studio/assets/img/tools/{img["file"]}'
    style = style if style is not None else 'margin-top:14px;display:block;max-width:100%;height:auto'
    return (f'<img src="{src}" alt="{img["alt"]}" width="{img["w"]}" height="{img["h"]}" '
            f'loading="lazy" style="{style}"/>')


def _recensioni_section():
    """Recensioni reali dal lancio su Product Hunt (data.py:RECENSIONI_LAB).
    Citazioni in originale inglese su tutte le lingue — il conveyor le lascia
    intatte per costruzione (nessuna coppia nel dizionario). Nessun markup
    schema.org (self-serving reviews, vietate dalle linee guida Google)."""
    cards = ''.join(
        group(
            raw_html(f'<p class="sr-recensione__testo">«{r["testo"]}»</p>'
                     f'<p class="sr-mono sr-recensione__firma">{r["nome"]} · '
                     f'<a href="{RECENSIONI_URL}" target="_blank" rel="noopener">Product Hunt ↗</a></p>'),
            classes='sr-card sr-card--carta',
        )
        for r in RECENSIONI_LAB
    )
    return section(
        eyebrow('Dalla community') + heading(2, 'Cosa dice chi li ha provati') +
        paragraph('Le prime recensioni dal lancio su Product Hunt — citate in originale, con il permesso degli autori.',
                   color='grigio', size='medium', extra_style='max-width:70ch') +
        group(cards, classes='', layout_type='grid', style='300px'),
        classes='sr-section sr-section--bianco',
    )


def build_strumenti_index():
    hero = section(eyebrow('Remarka Lab · Strumenti gratuiti') + heading(1, 'Prima misurate, poi decidete', style='clamp(38px,4.6vw,64px)') +
                    paragraph('Strumenti professionali, gratuiti, senza registrazione.', color='grigio', size='medium'),
                    classes='sr-section sr-hero')

    # Check-up completo: posizione featured, prima della griglia dei singoli
    # strumenti (docs/piano-checkup-sito.md, scope M2).
    checkup = next(t for t in TOOLS if t['tipo'] == 'checkup')
    altri = [t for t in TOOLS if t['tipo'] != 'checkup']

    # Layout a due colonne (owner 18.07.2026 v2): testo+Prova a sinistra,
    # grafica hero a destra, centrata verticalmente da ≥640px; impilati su
    # mobile con la grafica sotto il testo (.sr-tools-feat, assets/css).
    featured = section(
        raw_html(
            '<div class="sr-card sr-card--carta sr-tools-feat" style="border-color:var(--sr-oltremare)">'
            '<div class="sr-tools-feat__text">'
            '<p class="sr-eyebrow" style="color:var(--sr-oltremare)">Novità · gratuito</p>'
            f'<h3 class="wp-block-heading" style="margin-top:10px">{checkup["titolo"]}</h3>'
            f'<p style="margin-top:10px;font-size:15.5px;color:var(--sr-grigio);max-width:60ch">{checkup["descrizione"]}</p>'
            f'<p class="sr-card-link" style="margin-top:18px"><a href="/strumenti/{checkup["slug"]}/">Prova →</a></p>'
            '</div>'
            f'<div class="sr-tools-feat__img">{_tool_img_html(TOOLS_HERO_IMG, style="display:block;max-width:100%;height:auto")}</div>'
            '</div>'
        ),
        classes='sr-section sr-section--bianco',
    )

    # Intro ai 3 nuovi strumenti AI (copy-ai-tools.md §7), prima della griglia:
    # stesso tono del resto del catalogo, nessuna promessa esagerata.
    ai_intro = section(
        paragraph(
            'Tre strumenti AI, nuovi. «Il vostro sito, letto dall’AI» vi mostra cosa '
            'capisce un assistente artificiale quando incontra la vostra home. «Suona '
            'madrelingua?» dice se i vostri testi in inglese o russo suonano nativi o '
            'sanno di traduzione — il nostro mestiere dal 2001. Il «Generatore di '
            'llms.txt» scrive per voi il file che spiega il sito agli assistenti AI, '
            'pronto da scaricare. Gratis, senza registrazione: è l’intelligenza '
            'artificiale al servizio del vostro sito, non del contrario.',
            color='grigio', size='base', extra_style='max-width:75ch',
        ),
        classes='sr-section sr-section--bianco',
    )

    cards = []
    for t in altri:
        img = TOOLS_CARD_IMG.get(t['slug'])
        card = (
            raw_html(f'<p class="sr-mono" style="color:var(--sr-oltremare);font-size:12px">{t["idx"]}</p>') +
            heading(3, t['titolo'], accent_dot=False) +
            paragraph(t['descrizione'], color='grigio', size='small') +
            (raw_html(_tool_img_html(img)) if img else raw_html('')) +
            raw_html(f'<p class="sr-card-link" style="margin-top:16px"><a href="/strumenti/{t["slug"]}/">Prova →</a></p>')
        )
        cards.append(group(card, classes='sr-card sr-card--carta'))

    grid = section(group(''.join(cards), classes='', layout_type='grid', style='240px'),
                    classes='sr-section sr-section--bianco')

    # Gratis vs Monitor (docs/piano-promo-cabinet-lab.md §4.4): àncora #monitor
    # linkata dalla home (strumenti-cards). lab.remarka.biz per ora chiede le
    # credenziali (piattaforma interna): il link c'è — decisione owner 18.07 —
    # ma il percorso commerciale resta /#contatti finché non apre la vetrina.
    monitor_free = group(
        eyebrow('Gratis · per tutti') +
        heading(3, 'Strumenti una tantum', accent_dot=False) +
        checklist([
            '12 check gratuiti: velocità, SEO, accessibilità, GDPR, AI, E-E-A-T, CO₂, ROI',
            'Risultato in circa un minuto, senza registrazione',
            'Ogni strumento indica cosa correggere — e il servizio giusto se serve una mano',
        ]),
        classes='sr-card sr-card--carta',
    )
    monitor_pro = group(
        eyebrow('Per i clienti · con l’assistenza') +
        heading(3, 'Remarka Lab · Monitor', accent_dot=False) +
        checklist([
            'Il sito osservato in continuo dopo il lancio: controlli periodici e uptime',
            'Core Web Vitals reali degli utenti, mese dopo mese',
            'Se un valore peggiora, lo vediamo noi — e interveniamo prima che diventi un problema',
        ]) +
        raw_html('<p class="sr-card-link" style="margin-top:16px"><a href="/blog/monitoraggio-sito-dopo-lancio/">Cosa misurare ogni mese: la guida al monitoraggio →</a></p>'
                 '<p class="sr-card-link" style="margin-top:8px"><a href="https://lab.remarka.biz/" target="_blank" rel="noopener">La piattaforma: lab.remarka.biz →</a></p>'
                 '<p class="sr-card-link" style="margin-top:8px"><a href="/#contatti">Incluso nei progetti con assistenza — parliamone →</a></p>'),
        classes='sr-card sr-card--carta',
    )
    monitor = section(
        eyebrow('Remarka Lab') + heading(2, 'Gratis oggi. Sotto controllo domani') +
        paragraph('Un punteggio si può misurare gratis, una volta. Tenerlo alto nel tempo è un lavoro — ed è il nostro: '
                  'per i clienti con assistenza attiva il sito resta osservato anche dopo il lancio, sulla stessa '
                  'piattaforma con cui costruiamo questi strumenti.',
                   color='grigio', size='medium', extra_style='max-width:75ch') +
        group(monitor_free + monitor_pro, classes='', layout_type='grid', style='320px'),
        classes='sr-section', anchor='monitor',
    )

    # CTA di chiusura (owner 17.07.2026 — unificazione banner: l'indice non
    # aveva mai una banda di contenuto, solo la .sr-footer-cta del footer;
    # rimossa quella, restava zero). Stesso testo/stile riusato dalle pagine
    # servizio/città/strumento (sr-cta-band), non un banner nuovo inventato.
    cta = section(
        heading(2, 'Parliamo del vostro sito', style=None) +
        paragraph('Analisi gratuita del sito attuale, preventivo chiuso entro 24 ore dalla chiamata.',
                   color='grigio', size='medium', extra_style='margin-top:12px') +
        buttons([('Richiedi preventivo in 24 ore', '/#contatti', None),
                 analyze_cta_button()],
                justify='center', margin_top='28px') +
        cta_trust_row(),
        classes='sr-section sr-cta-band',
    )
    write('strumenti-index', 'Pagina — Strumenti (elenco)',
          'Elenco degli strumenti gratuiti, con il check-up completo in evidenza, recensioni reali e la sezione Gratis/Monitor.',
          hero + featured + ai_intro + grid + _recensioni_section() + monitor + cta)


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

    <!-- Priorità PRIMA dei sette semafori (feedback lancio Product Hunt,
         19.07.2026: «a prioritized action list instead of dumping all results»
         — chi non è tecnico deve vedere subito da dove partire). -->
    <div data-sr-checkup-priorities-wrap style="margin-top:32px">
      <p class="sr-eyebrow">Da dove partire</p>
      <h2 class="wp-block-heading" style="font-size:clamp(24px,2.4vw,32px)">I 3 interventi che pesano di più</h2>
      <p style="margin:8px 0 20px;color:var(--sr-grigio);font-size:15.5px">Ordinati per impatto sul punteggio: quanto guadagnereste sistemandoli.</p>
      <div class="sr-priorities" data-sr-checkup-priorities></div>
    </div>

    <div style="margin-top:32px">
      <p class="sr-eyebrow">Le sette misure</p>
      <h2 class="wp-block-heading" style="font-size:clamp(24px,2.4vw,32px)">Sette semafori, un punteggio</h2>
      <div class="sr-dim-grid" style="margin-top:24px">{cards}</div>
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


# Widget dei 3 strumenti AI (Remarka Lab, docs/piano-ai-tools.md §6). Contratto
# data-* condiviso con assets/js/remarka.js (blocco "Remarka Lab — 3 strumenti
# AI"): data-sr-tool="ai-read|ai-suona|ai-llms", endpoint remarka_tool_ai.


def _widget_ai_read():
    return '''
<div class="sr-tool-widget sr-card" data-sr-tool="ai-read" data-sr-locale="it"
     data-ai-loading="L’AI sta leggendo il vostro sito…"
     data-ai-maintenance="Strumento in manutenzione."
     data-ai-limit="Avete raggiunto il limite di prove per oggi. Riprovate domani."
     data-ai-err="Lo strumento non è disponibile in questo momento. Riprovate tra poco.">
  <form data-sr-tool-form>
    <div class="sr-tool-row">
      <input type="text" placeholder="www.tuosito.it" class="sr-text-input" required />
      <button type="submit" class="wp-block-button__link" style="padding:17px 30px">Analizza</button>
    </div>
  </form>
  <p class="sr-tool-pending sr-mono" data-sr-tool-pending hidden>L’AI sta leggendo il vostro sito…<span class="sr-blink">…</span></p>
  <div class="sr-tool-result" data-sr-tool-result hidden>
    <p style="margin:0;font-size:17px;font-weight:500" data-sr-tool-verdict></p>
    <p class="sr-eyebrow" style="margin-top:24px">Citabilità AI</p>
    <div class="sr-tool-result__score">
      <span class="sr-mono" data-ai-citabilita>0</span><span class="sr-mono" style="font-size:18px;color:var(--sr-grigio)">/100</span>
    </div>
    <div class="sr-barra" style="height:10px"><div class="sr-barra__fill" data-ai-citabilita-fill style="width:0%"></div><span class="sr-barra__tick" style="left:75%"></span><span class="sr-barra__tick" style="left:50%"></span></div>
    <p class="sr-eyebrow" style="margin-top:28px">Le 3 mosse</p>
    <div data-ai-azioni>
      <template><div class="ai-azione"><span class="ai-azione-fai"></span><span class="ai-azione-arrow">→</span><span class="ai-azione-effetto"></span></div></template>
    </div>
    <p class="sr-disclaimer">Non salviamo il contenuto: è una lettura dell’AI, non un audit certificato.</p>

    <div class="sr-ai-lead">
      <p class="sr-eyebrow">Ricevete l’analisi completa via e-mail</p>
      <form data-ai-lead-form>
        <div class="sr-tool-row">
          <input type="email" class="sr-text-input" placeholder="La vostra e-mail" required />
          <button type="submit" class="wp-block-button__link" style="padding:15px 26px">Ricevi l’analisi completa</button>
        </div>
        <p style="margin-top:12px;font-size:13.5px"><label><input type="checkbox" data-ai-lead-consent required> Acconsento a essere ricontattato da Studio Remarka.</label></p>
        <input type="text" name="sr_ai_hp" class="sr-hp-field" tabindex="-1" autocomplete="off">
      </form>
      <p data-ai-lead-success hidden>Fatto: controllate la posta.</p>
      <p class="sr-form-error" data-ai-lead-error hidden>Lo strumento non è disponibile in questo momento. Riprovate tra poco.</p>
    </div>
  </div>
</div>'''


def _widget_ai_suona():
    return '''
<div class="sr-tool-widget sr-card" data-sr-tool="ai-suona" data-sr-locale="it"
     data-ai-loading="L’AI sta valutando il testo…"
     data-ai-maintenance="Strumento in manutenzione."
     data-ai-limit="Avete raggiunto il limite di prove per oggi. Riprovate domani."
     data-ai-err="Lo strumento non è disponibile in questo momento. Riprovate tra poco."
     data-ai-err-short="Incollate almeno una frase."
     data-ai-badge-yes="Suona nativo" data-ai-badge-no="Si sente la traduzione">
  <form data-sr-tool-form>
    <div class="sr-ai-lang">
      <span class="sr-eyebrow">Lingua del testo:</span>
      <div class="sr-pill-group">
        <label class="sr-pill"><input type="radio" class="sr-pill__input" name="text_lang" value="en" checked><span>Inglese</span></label>
        <label class="sr-pill"><input type="radio" class="sr-pill__input" name="text_lang" value="ru"><span>Russo</span></label>
      </div>
    </div>
    <textarea class="sr-text-input" data-ai-suona-text placeholder="Incollate qui il testo da valutare (max ~2.000 caratteri)…" maxlength="2000" required></textarea>
    <p class="sr-ai-counter" data-ai-counter>0 / 2000</p>
    <div class="sr-tool-row">
      <button type="submit" class="wp-block-button__link" style="padding:15px 28px">Valuta il testo</button>
    </div>
  </form>
  <p class="sr-tool-pending sr-mono" data-sr-tool-pending hidden>L’AI sta valutando il testo…<span class="sr-blink">…</span></p>
  <div class="sr-tool-result" data-sr-tool-result hidden>
    <p style="margin:0;font-size:15.5px" data-sr-tool-verdict></p>
    <p class="sr-ai-badge" data-ai-badge data-sr-flag style="margin-top:12px"></p>
    <p class="sr-eyebrow" style="margin-top:20px">Naturalezza</p>
    <div class="sr-tool-result__score">
      <span class="sr-mono" data-ai-punteggio>0</span><span class="sr-mono" style="font-size:18px;color:var(--sr-grigio)">/100</span>
    </div>
    <div class="sr-barra" style="height:10px"><div class="sr-barra__fill" data-ai-punteggio-fill style="width:0%"></div><span class="sr-barra__tick" style="left:75%"></span><span class="sr-barra__tick" style="left:50%"></span></div>
    <p style="margin-top:16px"><span class="sr-eyebrow">Registro</span><br><span data-ai-registro></span></p>
    <p class="sr-eyebrow" style="margin-top:28px">3 correzioni</p>
    <div data-ai-correzioni>
      <template><div class="ai-correzione"><p><span class="sr-eyebrow">Prima</span><br><span class="ai-correzione-prima"></span></p><p><span class="sr-eyebrow">Dopo</span><br><span class="ai-correzione-dopo"></span></p><p class="ai-correzione-perche"></p></div></template>
    </div>
    <p class="sr-disclaimer">Non salviamo il testo: è una lettura dell’AI, non un audit certificato.</p>
  </div>
</div>'''


def _widget_ai_llms():
    return '''
<div class="sr-tool-widget sr-card" data-sr-tool="ai-llms" data-sr-locale="it"
     data-ai-loading="L’AI sta scrivendo il vostro llms.txt…"
     data-ai-maintenance="Strumento in manutenzione."
     data-ai-limit="Avete raggiunto il limite di prove per oggi. Riprovate domani."
     data-ai-err="Lo strumento non è disponibile in questo momento. Riprovate tra poco."
     data-ai-copy-done="Copiato">
  <form data-sr-tool-form>
    <div class="sr-pill-group">
      <label class="sr-pill"><input type="radio" class="sr-pill__input" name="ai_llms_mode" value="form" checked><span>Compila i campi</span></label>
      <label class="sr-pill"><input type="radio" class="sr-pill__input" name="ai_llms_mode" value="url"><span>Ho solo l’indirizzo</span></label>
    </div>
    <div data-ai-llms-form style="margin-top:16px">
      <p><label class="sr-eyebrow" style="display:block;margin-bottom:6px">Nome del sito / attività</label><input type="text" name="ai_llms_nome" class="sr-text-input" style="width:100%;box-sizing:border-box" required></p>
      <p><label class="sr-eyebrow" style="display:block;margin-bottom:6px">Di cosa vi occupate</label><textarea name="ai_llms_cosa" class="sr-text-input" style="min-height:90px" required></textarea></p>
      <p><label class="sr-eyebrow" style="display:block;margin-bottom:6px">Pagine chiave (una per riga)</label><textarea name="ai_llms_pagine" class="sr-text-input" style="min-height:90px"></textarea></p>
    </div>
    <div data-ai-llms-url hidden style="margin-top:16px">
      <div class="sr-tool-row">
        <input type="text" name="ai_llms_url" placeholder="www.tuosito.it" class="sr-text-input">
      </div>
    </div>
    <div class="sr-tool-row" style="margin-top:16px">
      <button type="submit" class="wp-block-button__link" style="padding:15px 28px">Analizza</button>
    </div>
  </form>
  <p class="sr-tool-pending sr-mono" data-sr-tool-pending hidden>L’AI sta scrivendo il vostro llms.txt…<span class="sr-blink">…</span></p>
  <div class="sr-tool-result" data-sr-tool-result hidden>
    <p style="font-size:15.5px" data-sr-tool-verdict></p>
    <div class="sr-ai-llms-output">
      <textarea class="sr-ai-llms-textarea" data-ai-llms-output readonly></textarea>
    </div>
    <div class="sr-ai-llms-actions">
      <button type="button" class="wp-block-button__link" data-ai-copy>Copia</button>
      <span class="sr-btn-outline"><button type="button" class="wp-block-button__link" data-ai-download>Scarica llms.txt</button></span>
    </div>
    <p class="sr-disclaimer" data-ai-llms-note></p>
    <p class="sr-disclaimer">Non salviamo i dati: è una lettura dell’AI, non un audit certificato.</p>
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
    if tipo == 'ai-read':
        return _widget_ai_read()
    if tipo == 'ai-suona':
        return _widget_ai_suona()
    if tipo == 'ai-llms':
        return _widget_ai_llms()
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
        buttons(cta_data['buttons'], justify='center', margin_top='28px') +
        cta_trust_row(),
        classes='sr-section sr-cta-band',
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

    # Recensioni reali (Product Hunt) — solo sull'orchestratore check-up:
    # è lo strumento recensito e la pagina più visitata del Lab.
    recensioni = _recensioni_section() if tool['tipo'] == 'checkup' else ''

    write(f'strumento-{tool["slug"]}', f'Pagina — Strumento: {tool["titolo"]}',
          f'Strumento gratuito {tool["titolo"]}: widget interattivo, come funziona, FAQ, CTA.',
          hero + widget_section + come_funziona + metodologia + lettura + recensioni + faq + migliorare + cta + altri_section)


# ---------------------------------------------------------------- Città

def office_dove_siamo(indirizzo, maps_share_url, aria_label, office_testo, office_nota):
    """Blocco «Dove siamo» dei tre uffici REALI (Milano/Torino/Roma, indirizzi
    pubblici owner 17.07.2026 — piano-geo-citta.md). Due colonne (riusa
    `.sr-dove-siamo`, prima un riquadro decorativo vuoto):
      - sinistra `.sr-mappa`: mappa click-to-load, GDPR-safe — nessuna
        richiesta a Google Maps finché non si preme «Apri la mappa» (nessun
        iframe/script nel markup iniziale, lo inserisce assets/js/remarka.js
        #11 al click, stile in assets/css/remarka.css). `role="region"` +
        `aria-label` invece del vecchio `role="img"`: il pannello ora contiene
        un bottone interattivo, `role="img"` lo nasconderebbe alla a11y tree;
      - destra `.sr-card`: NAP testuale (funziona anche senza JS) — ragione
        sociale, indirizzo pubblico, «solo su appuntamento», testo ufficio,
        nota ATT (le schede Maps di questi uffici sono registrate a nome di
        ATT · Agenzia di Traduzione Tecnica, altro brand del gruppo che
        condivide l'ufficio — lo spieghiamo, non lo nascondiamo), contatti,
        link esterno alla scheda proprietaria (stesso share-link della mappa)
        e CTA. LocalBusiness-schema: remarka_office_local_business_schema()
        in functions.php, sugli stessi tre slug (+ le due varianti /milan/ EN/RU).
    """
    query = quote(f'Studio Remarka, {indirizzo}')
    mappa = raw_html(
        f'<div class="sr-mappa" role="region" aria-label="{aria_label}" data-sr-mappa data-sr-mappa-query="{query}">'
        '<div class="sr-mappa__cta" data-sr-mappa-cta>'
        '<span class="sr-btn-outline"><button type="button" class="wp-block-button__link" data-sr-mappa-btn>Apri la mappa</button></span>'
        '<p class="sr-disclaimer" style="margin-top:12px">Il pulsante carica una mappa di Google: nessuna richiesta a Google finché non lo attivate.</p>'
        '</div></div>'
    )
    card = group(
        eyebrow('Dove siamo') +
        raw_html(f'<p style="margin-top:12px;font-size:16px"><strong>Studio Remarka S.r.l.</strong><br>{indirizzo}</p>') +
        raw_html('<p class="sr-mono" style="margin-top:8px;font-size:13px;color:var(--sr-grigio)">Solo su appuntamento</p>') +
        paragraph(office_testo, color='grigio', size='base', extra_style='margin-top:16px') +
        paragraph(office_nota, color='grigio', size='base', extra_style='margin-top:12px') +
        raw_html('<p class="sr-mono" style="margin-top:16px;font-size:14px">Tel./WhatsApp +39 347 83 11141 · info@remarka.biz</p>') +
        raw_html(f'<p class="sr-card-link" style="margin-top:16px"><a href="{maps_share_url}" target="_blank" rel="noopener noreferrer">Apri in Google Maps →</a></p>') +
        raw_html('<p class="sr-card-link" style="margin-top:4px"><a href="/#contatti">Fissa un appuntamento →</a></p>'),
        classes='sr-card',
    )
    return raw_html('<div class="sr-dove-siamo">') + mappa + card + raw_html('</div>')


def build_city(c):
    """Городской лендинг под «realizzazione siti web {città}». Каждый город —
    свой кейс, свои отзывы с гео-привязкой и свой FAQ (piano-contenuti-seo §2:
    содержательные страницы, не клоны)."""
    hero = section(
        eyebrow(c['eyebrow']) + heading(1, f'Realizzazione siti web a {c["nome"]}', style='clamp(38px,4.6vw,64px)') +
        paragraph(c['sub'], color='grigio', size='medium') +
        buttons([('Richiedi preventivo in 24 ore', '/#contatti', None),
                 analyze_cta_button()], margin_top='28px') +
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
            eyebrow(c['office_eyebrow']) + heading(2, c['office_heading']) +
            office_dove_siamo(c['office_indirizzo'], c['office_maps_url'], c['office_aria'], c['office_testo'], c['office_nota']),
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
                 ('WhatsApp Business', 'https://wa.me/393478311141', 'whatsapp')], justify='center', margin_top='28px') +
        cta_trust_row(),
        classes='sr-section sr-cta-band',
    )
    write(f'citta-{c["slug"]}', f'Pagina — Città: {c["nome"]}',
          f'Landing locale «realizzazione siti web {c["nome"].lower()}»: servizi, caso, prezzi, recensioni, FAQ.',
          hero + servizi + caso + prezzi_local + dove + recensioni + faq + cta)


def build_city_flagship(c):
    """Città flagship (Roma, Torino): le uniche due con un ufficio REALE del
    gruppo (batch G1a). Pagina più profonda di build_city(): scena-lead,
    profilo di settore con cifre e fonti ufficiali, blocco «quali siti servono»
    (4 abbinamenti settore→servizio→caso), ufficio come differenziatore centrale
    CON indirizzo pubblico e mappa click-to-load (batch U1, indirizzi owner
    17.07.2026 — office_dove_siamo(), LocalBusiness-schema in functions.php).
    Nessun blocco recensioni inventate: sulle pagine flagship l'E-E-A-T si
    regge su fatti verificabili (piano-geo-citta §2)."""
    hero = section(
        eyebrow(c['eyebrow']) + heading(1, f'Realizzazione siti web a {c["nome"]}', style='clamp(38px,4.6vw,64px)') +
        paragraph(c['sub'], color='grigio', size='medium') +
        buttons([('Richiedi preventivo in 24 ore', '/#contatti', None),
                 analyze_cta_button()], margin_top='28px') +
        stat_block(str(c['progetti']), c['stat_label'], '', counter=True),
        classes='sr-section sr-hero',
    )

    # Scena-lead: un business locale tipico, in stile blog (numeri, non aggettivi).
    lead_paras = ''.join(
        paragraph(p, color='grigio', size='medium', extra_style='margin-top:16px;max-width:75ch')
        for p in c['lead']
    )
    lead = section(
        eyebrow(c['lead_eyebrow']) + heading(2, c['lead_heading']) + lead_paras,
        classes='sr-section sr-section--bianco',
    )

    # Profilo di settore con cifre reali e fonti ufficiali (Camera di Commercio,
    # ISTAT/enti) — verificate via WebSearch 07.2026, ogni numero linkato.
    settore = section(
        eyebrow(c['settore_eyebrow']) + heading(2, c['settore_heading']) +
        paragraph(c['settore_intro'], color='grigio', size='medium', extra_style='margin-top:16px;max-width:75ch') +
        metric_rows(c['settore_metrics']) +
        paragraph(c['settore_nota'], color='grigio', size='base', extra_style='margin-top:24px;max-width:75ch'),
        classes='sr-section',
    )

    servizi_rows = ''.join(
        f'<div><span style="font-size:16px;font-weight:500;color:var(--sr-inchiostro)">{s["title"]}</span>'
        f'<a href="/servizi/{s["slug"]}/" class="sr-mono" style="color:var(--sr-oltremare)">→</a></div>'
        for s in SERVICES
    )
    servizi = section(
        eyebrow('Cosa facciamo') + heading(2, c['servizi_heading']) +
        raw_html(f'<div class="sr-servizi-rows" style="margin-top:32px">{servizi_rows}</div>'),
        classes='sr-section sr-section--bianco',
    )

    # «Quali siti servono»: 4 abbinamenti settore→servizio→caso reale.
    pairing_cards = ''.join(
        '<div class="sr-card">'
        f'<p class="sr-mono" style="color:var(--sr-oltremare)">{p["eyebrow"]}</p>'
        f'<h3 style="margin-top:12px;font-size:20px;line-height:1.3">{p["titolo"]}</h3>'
        f'<p style="margin-top:12px;font-size:15.5px;line-height:1.6;color:var(--sr-grigio)">{p["testo"]}</p>'
        f'<p class="sr-card-link" style="margin-top:16px"><a href="{p["service_href"]}">{p["service_label"]} →</a></p>'
        f'<p class="sr-card-link" style="margin-top:4px"><a href="/casi-studio/#{p["case_slug"]}">Vedi il caso: {CASES_BY_SLUG[p["case_slug"]]["url_label"]} →</a></p>'
        '</div>'
        for p in c['pairings']
    )
    pairings = section(
        eyebrow('Su misura, non a stampino') + heading(2, c['pairings_heading']) +
        paragraph(c['pairings_intro'], color='grigio', size='medium', extra_style='margin-top:16px;max-width:75ch') +
        group(pairing_cards, classes='', layout_type='grid', style='460px'),
        classes='sr-section',
    )

    local_case = CASES_BY_SLUG[c['case_slug']]
    main_shot = local_case['shots'][0]
    caso = section(
        columns([
            column(browser_frame_shot(c['case_url_label'], main_shot['file'], local_case['alt'], main_shot['caption'], mobile=main_shot['mobile']), width='55%'),
            column(eyebrow(c['case_eyebrow']) + heading(3, c['case_title'], accent_dot=False) +
                   paragraph(local_case['risultato'], color='grigio', size='base', extra_style='margin-top:12px') +
                   raw_html(f'<p class="sr-card-link" style="margin-top:20px"><a href="/casi-studio/#{local_case["slug"]}">Leggi il caso completo →</a></p>'),
                   width='45%'),
        ], valign='center'),
        classes='sr-section sr-section--bianco',
    )

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
        raw_html('<p class="sr-card-link" style="margin-top:12px"><a href="/prezzi/">Confronta tutte le tariffe →</a></p>') +
        raw_html(f'<p class="sr-card-link" style="margin-top:4px"><a href="{c["tool_link"][1]}">{c["tool_link"][0]} →</a></p>'),
        classes='sr-section',
    )

    # Presenza locale. Due rami, scelti dalla presenza del campo 'office_heading':
    #  - città con ufficio REALE (Roma, Torino, batch G1a): blocco ufficio,
    #    differenziatore centrale, con indirizzo pubblico (owner 17.07.2026) e
    #    mappa click-to-load GDPR-safe — vedi office_dove_siamo().
    #  - città SENZA ufficio (batch G1b): blocco «Come lavoriamo», formula onesta
    #    (uffici a Milano, Torino e Roma; altrove video o incontro su
    #    appuntamento, veniamo noi). Nessun ufficio/indirizzo/«team locale»
    #    inventato. La chiave focus è portata da role="region"+aria-label.
    if c.get('office_heading'):
        office = section(
            eyebrow(c['office_eyebrow']) + heading(2, c['office_heading']) +
            raw_html('<div style="margin-top:28px">') +
            office_dove_siamo(c['office_indirizzo'], c['office_maps_url'], c['office_aria'], c['office_testo'], c['office_nota']) +
            raw_html('</div>'),
            classes='sr-section sr-section--bianco',
        )
    else:
        office = section(
            eyebrow(c['presenza_eyebrow']) + heading(2, c['presenza_heading']) +
            paragraph(c['presenza_testo'], color='grigio', size='medium', extra_style='margin-top:16px;max-width:75ch') +
            raw_html(f'<div role="region" aria-label="{c["presenza_aria"]}" style="margin-top:24px">') +
            group(
                paragraph(c['presenza_nota'], color='grigio', size='base') +
                raw_html('<p class="sr-card-link" style="margin-top:16px"><a href="/#come-lavoriamo">Come lavoriamo, passo per passo →</a></p>') +
                raw_html('<p class="sr-card-link" style="margin-top:4px"><a href="/dove-lavoriamo/">Dove lavoriamo, in tutta Italia →</a></p>') +
                raw_html('<p class="sr-card-link" style="margin-top:4px"><a href="/#contatti">Fissa una videochiamata o un incontro →</a></p>'),
                classes='sr-card',
            ) + raw_html('</div>'),
            classes='sr-section sr-section--bianco',
        )

    faq = section(
        eyebrow('Domande da ' + c['nome']) + details_faq(c['faq']),
        classes='sr-section',
    )

    cta = section(
        heading(2, c['cta_heading']) +
        paragraph(c['cta_testo'], color='grigio', size='medium', extra_style='margin-top:12px') +
        buttons([('Richiedi preventivo in 24 ore', '/#contatti', None),
                 ('WhatsApp Business', 'https://wa.me/393478311141', 'whatsapp')], justify='center', margin_top='28px') +
        cta_trust_row(),
        classes='sr-section sr-cta-band',
    )
    # Descrizione onesta: le città con ufficio (Roma/Torino) restano invariate;
    # quelle senza ufficio non devono dichiararne uno (byte-identici per Roma/Torino).
    _presenza_desc, _presenza_voce = ('ufficio in città', 'ufficio') if c.get('office_heading') else ('senza ufficio', 'come lavoriamo')
    write(f'citta-{c["slug"]}', f'Pagina — Città: {c["nome"]}',
          f'Landing locale «realizzazione siti web {c["nome"].lower()}» (flagship, {_presenza_desc}): '
          f'scena, profilo di settore con fonti, servizi, casi, prezzi, {_presenza_voce}, FAQ.',
          hero + lead + settore + servizi + pairings + caso + prezzi_local + office + faq + cta)


def build_dove_lavoriamo():
    """Hub di navigazione «Dove lavoriamo» (batch G1b-2). Nessuna focus-key:
    pagina navigazionale. Racconta il modello (tre uffici REALI a Milano,
    Torino e Roma — solo su appuntamento — e lavoro in tutta Italia: video,
    incontri da voi, consegna documenti con corriere BRT/Poste/DHL), mostra le
    tre schede ufficio con indirizzo e link alle città flagship, e la griglia
    di tutte le 17 landing città raggruppate per macro-area (Nord/Centro/Sud
    e Isole). Registrata in deploy-import (page_map) e linkata dal footer
    (etichetta «Dove operiamo») e dai blocchi «Come lavoriamo» delle città."""
    hero = section(
        eyebrow('Studio Remarka · In tutta Italia') +
        heading(1, 'Dove lavoriamo', style='clamp(38px,4.6vw,64px)') +
        paragraph('Tre uffici veri — Milano, Torino e Roma, solo su appuntamento — e progetti in tutta Italia. '
                  'Dove non abbiamo un ufficio lavoriamo allo stesso modo: analisi e avanzamento in videochiamata, '
                  'un ambiente di prova online che vedete aggiornarsi ogni venerdì e, su appuntamento, veniamo noi da voi. '
                  'I documenti stampati — traduzioni giurate, contratti, materiali — li recapitiamo in tutta Italia in '
                  '24–48 ore con corriere BRT, Poste Italiane o DHL.',
                  color='grigio', size='medium'),
        classes='sr-section sr-hero',
    )

    uffici_data = [
        ('Milano', 'Vicolo Privato Lavandai, 2a — 20144', '/milano/'),
        ('Torino', 'Corso Regina Margherita, 94 — 10153', '/torino/'),
        ('Roma', 'Via Flaminia, 122 — 00196', '/roma/'),
    ]
    uffici_cards = ''.join(
        '<div class="sr-card">'
        f'<p class="sr-mono" style="color:var(--sr-oltremare)">{nome}</p>'
        f'<p style="margin-top:12px;font-size:16px"><strong>Studio Remarka S.r.l.</strong><br>{ind}</p>'
        '<p class="sr-mono" style="margin-top:8px;font-size:13px;color:var(--sr-grigio)">Solo su appuntamento</p>'
        f'<p class="sr-card-link" style="margin-top:16px"><a href="{href}">Siti web a {nome} →</a></p>'
        '</div>'
        for nome, ind, href in uffici_data
    )
    uffici = section(
        eyebrow('I nostri uffici') + heading(2, 'Tre indirizzi veri, su appuntamento') +
        paragraph('Le schede Google Maps di questi uffici sono registrate a nome di ATT · Agenzia di Traduzione '
                  'Tecnica, l’altro marchio del gruppo che condivide gli stessi spazi. Riceviamo solo su '
                  'appuntamento: il primo incontro non si paga.',
                   color='grigio', size='base', extra_style='margin-top:16px;max-width:75ch') +
        group(uffici_cards, classes='', layout_type='grid', style='300px'),
        classes='sr-section sr-section--bianco',
    )

    # Griglia di TUTTE le 17 città, per macro-area. I link puntano agli slug
    # piatti già registrati in page_map (build_city / build_city_flagship).
    gruppi = [
        ('Nord', [('Milano', '/milano/'), ('Torino', '/torino/'), ('Genova', '/genova/'),
                  ('Monza', '/monza/'), ('Bergamo', '/bergamo/'), ('Brescia', '/brescia/'),
                  ('Como', '/como/'), ('Bologna', '/bologna/'), ('Verona', '/verona/'),
                  ('Padova', '/padova/'), ('Venezia', '/venezia/')]),
        ('Centro', [('Roma', '/roma/'), ('Firenze', '/firenze/')]),
        ('Sud e Isole', [('Napoli', '/napoli/'), ('Bari', '/bari/'),
                         ('Palermo', '/palermo/'), ('Catania', '/catania/')]),
    ]
    area_cards = ''
    for titolo, cs in gruppi:
        links = ''.join(
            f'<li style="margin:0"><a href="{href}" style="font-size:16px">{nome}</a></li>'
            for nome, href in cs
        )
        area_cards += (
            '<div class="sr-card">'
            f'<p class="sr-mono" style="color:var(--sr-oltremare)">{titolo}</p>'
            f'<ul style="list-style:none;margin:14px 0 0;padding:0;display:flex;flex-wrap:wrap;gap:10px 20px">{links}</ul>'
            '</div>'
        )
    citta = section(
        eyebrow('Le città con cui lavoriamo') + heading(2, 'Diciassette città, un unico metodo') +
        paragraph('Ogni città ha la sua pagina, con il profilo di settore, i casi e le domande locali. Dove non c’è '
                  'un ufficio, lavoriamo in video o veniamo noi da voi su appuntamento — la stessa data in contratto '
                  'e lo stesso prezzo chiuso, ovunque siate.',
                  color='grigio', size='medium', extra_style='margin-top:16px;max-width:75ch') +
        group(area_cards, classes='', layout_type='grid', style='320px'),
        classes='sr-section',
    )

    cta = section(
        heading(2, 'Parliamo del vostro progetto') +
        paragraph('Primo incontro gratuito, in videochiamata o da voi su appuntamento. Preventivo chiuso entro 24 ore.',
                   color='grigio', size='medium', extra_style='margin-top:12px') +
        buttons([('Richiedi preventivo in 24 ore', '/#contatti', None),
                 ('WhatsApp Business', 'https://wa.me/393478311141', 'whatsapp')], justify='center', margin_top='28px') +
        cta_trust_row(),
        classes='sr-section sr-cta-band',
    )

    write('dove-lavoriamo', 'Pagina — Dove lavoriamo',
          'Hub di navigazione: uffici del gruppo (Milano, Torino, Roma) e tutte le città con cui lavora Studio Remarka.',
          hero + uffici + citta + cta)


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
            column(paragraph(e['problema_testo'], size='base', extra_style='font-size:17px') +
                   raw_html('<figure class="sr-hero-visual" style="margin-top:24px">'
                            '<img src="/wp-content/themes/remarka-studio/assets/img/lingue-processo-madrelingua.webp" '
                            'alt="Schema del percorso editoriale: sorgente, revisione, versioni locali" '
                            'width="1200" height="800" loading="lazy" decoding="async"/></figure>'),
                   width='62%'),
        ]),
        classes='sr-section',
    )

    garanzie = section(
        eyebrow('Garanzie') + heading(2, e['garanzie_heading']) + checklist(e['garanzie']) +
        raw_html(_area_clienti_line_html()),
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
                   color='grigio', size='small', extra_style='margin-top:24px') +
        raw_html('<p class="sr-card-link" style="margin-top:12px"><a href="/strumenti/suona-madrelingua/">Provate se i vostri testi suonano madrelingua →</a></p>'),
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
        buttons([('Richiedi preventivo in 24 ore', '/#contatti', None)], justify='center', margin_top='28px') +
        cta_trust_row(),
        classes='sr-section sr-cta-band',
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
            column(paragraph(w['prove_testo'], size='base', extra_style='font-size:17px') +
                   raw_html(_area_clienti_line_html(margin_top='14px')), width='62%'),
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
        buttons([('Richiedi preventivo in 24 ore', '/#contatti', None)], justify='center', margin_top='28px') +
        cta_trust_row(),
        classes='sr-section sr-cta-band',
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
        eyebrow('Cosa include') + heading(2, e['include_heading']) + checklist(e['include']) +
        raw_html(_area_clienti_line_html()),
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
        buttons(e['cta']['buttons'], justify='center', margin_top='28px') +
        cta_trust_row(),
        classes='sr-section sr-cta-band',
    )
    write('servizio-adeguamento-eaa', 'Pagina — Servizio: Adeguamento EAA',
          'Servizio conformità European Accessibility Act: audit, correzioni, dichiarazione di accessibilità e verifica finale WCAG 2.1 AA.',
          hero + per_chi + include + processo + prezzo + garanzie + faq + cta)


# ---------------------------------------------------------------- Area clienti
# Pagina trust (docs/piano-promo-cabinet-lab.md): non vende un servizio, vende
# la trasparenza del processo — il cabinet su cab.remarka.biz è incluso in ogni
# progetto. Nome pubblico IT «area clienti» (mai «CAB»: per un italiano è il
# Codice di Avviamento Bancario — piano-cabinet-k1 §10.2).

def build_area_clienti():
    hero = hero_interno(
        'Area clienti', 'Il progetto, nero su bianco',
        'Ogni progetto Remarka include l’accesso all’area clienti: la fase del lavoro visibile ogni giorno, '
        'approvazioni e file in un unico posto — in italiano, inglese o russo.',
        extra_html=buttons([
            ('Accedi all’area clienti', 'https://cab.remarka.biz/', None),
            ('Non siete ancora clienti? Parliamone', '/#contatti', 'outline'),
        ], margin_top='36px'),
        stat=('8', 'fasi del progetto, visibili in ogni momento — dal brief al lancio'),
    )

    passi = [
        ('Passo 1', 'Entrate senza password',
         'Inserite la vostra e-mail: vi mandiamo un link di accesso monouso, valido 15 minuti. '
         'Niente password da ricordare, niente password da rubare.'),
        ('Passo 2', 'Vedete a che punto siamo',
         'Il progetto avanza su 8 fasi, dal brief al lancio: quella corrente è sempre evidenziata. '
         'Non serve chiedere «a che punto siamo?» — si vede.'),
        ('Passo 3', 'Approvate e scaricate',
         'Bozze e testi si approvano con un click, con data e nome; file e fatture restano archiviati. '
         'Ogni domanda ha un filo tracciato, non una e-mail persa.'),
    ]
    week_cols = ''.join(
        f'<div class="sr-week"><p class="sr-week-chip sr-no-margin">{chip}</p>'
        f'<div class="sr-week__steps"><div class="sr-week__step">'
        f'<p class="sr-step__head sr-no-margin"><span class="sr-step-num">{i:02d}</span></p>'
        f'<h4>{titolo}</h4><p>{testo}</p></div></div></div>'
        for i, (chip, titolo, testo) in enumerate(passi, start=1)
    )
    come_funziona = section(
        eyebrow('Come funziona') + heading(2, 'Tre passaggi, zero password') +
        raw_html(f'<div class="sr-weeks sr-cascade">{week_cols}</div>'),
        classes='sr-section sr-section--bianco',
    )

    feature_cards = [
        ('/01', 'Fasi del progetto',
         'Dal brief al lancio, 8 fasi con la corrente evidenziata: l’avanzamento si vede a colpo d’occhio, ogni giorno.'),
        ('/02', 'Approvazioni con storico',
         'Bozze e testi da approvare o rimandare con un commento. Ogni decisione resta agli atti: chi, cosa, quando.'),
        ('/03', 'File in un unico posto',
         'I materiali del progetto — bozze, consegne, documenti — sempre scaricabili. E potete caricare i vostri: loghi, testi, foto.'),
        ('/04', 'Fatture e stato dei pagamenti',
         'Numero, data, importo e stato di ogni fattura, con il PDF scaricabile. Niente da chiedere, niente da cercare.'),
        ('/05', 'Richieste tracciate',
         'Ogni domanda apre un filo con storico e risposta: niente e-mail perse tra le caselle di tre persone.'),
        ('/06', 'Tre lingue',
         'Interfaccia e notifiche in italiano, inglese o russo: ognuno del vostro team la usa nella propria lingua.'),
    ]
    cards = ''.join(
        group(
            raw_html(f'<p class="sr-mono" style="color:var(--sr-oltremare);font-size:12px">{idx}</p>') +
            heading(3, titolo, accent_dot=False) +
            paragraph(testo, color='grigio', size='small'),
            classes='sr-card sr-card--carta',
        )
        for idx, titolo, testo in feature_cards
    )
    dentro = section(
        eyebrow('Cosa trovate dentro') + heading(2, 'Tutto il progetto, in un posto solo') +
        group(cards, classes='', layout_type='grid', style='240px'),
        classes='sr-section',
    )

    perche = section(
        columns([
            column(eyebrow('Perché l’abbiamo costruita') +
                   heading(2, 'Costruita da noi, come i siti che vendiamo') +
                   paragraph(
                       'Sviluppiamo web app per i clienti — e l’area clienti è la nostra: stessa piattaforma, '
                       'stessi standard, stesso design. Nessun gestionale di terzi: i dati restano su server '
                       'nell’Unione Europea e ne raccogliamo solo il minimo necessario per lavorare insieme.',
                       size='base', extra_style='margin-top:16px;font-size:16px') +
                   raw_html('<p class="sr-card-link" style="margin-top:16px"><a href="/blog/area-clienti-agenzia-web/">'
                            'Cosa pretendere dall’area clienti di qualunque agenzia: la guida →</a></p>'),
                   width='50%'),
            column(eyebrow('Sicurezza e privacy') + checklist([
                'Accesso senza password: link monouso via e-mail, valido 15 minuti',
                'Sessioni revocabili e registro degli accessi',
                'Dati su server nell’Unione Europea (Germania), GDPR by design',
                'Solo i dati necessari: e-mail, nome, lingua — nient’altro',
            ]), width='50%'),
        ]),
        classes='sr-section sr-section--bianco',
    )

    faq = section(
        eyebrow('Domande frequenti') + details_faq([
            ('Quanto costa l’area clienti?',
             'Niente: è inclusa in ogni progetto Remarka, dal sito vetrina all’e-commerce.'),
            ('Serve installare qualcosa?',
             'No. Funziona dal browser, anche dal telefono. Entrate con la vostra e-mail: niente password, niente app da installare.'),
            ('In che lingua è l’interfaccia?',
             'Italiano, inglese o russo: la scegliete voi, e ogni membro del vostro team può usarne una diversa.'),
            ('Chi vede i vostri dati?',
             'Solo voi e noi. Ogni cliente vede esclusivamente i propri progetti; i dati stanno su server nell’Unione Europea e non li cediamo a terzi.'),
        ]),
        classes='sr-section',
    )

    cta = section(
        heading(2, 'Parliamo del vostro sito', style=None) +
        paragraph('Analisi gratuita del sito attuale, preventivo chiuso entro 24 ore dalla chiamata.',
                   color='grigio', size='medium', extra_style='margin-top:12px') +
        buttons([('Richiedi preventivo in 24 ore', '/#contatti', None),
                 analyze_cta_button()],
                justify='center', margin_top='28px') +
        cta_trust_row(),
        classes='sr-section sr-cta-band',
    )

    write('area-clienti', 'Pagina — Area clienti',
          'L’area clienti su cab.remarka.biz: fasi del progetto, approvazioni, file e fatture. Inclusa in ogni progetto.',
          hero + come_funziona + dentro + perche + faq + cta)


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


def _legal_list(items):
    lis = ''.join(f'<li>{it}</li>' for it in items)
    return f'<!-- wp:list -->\n<ul class="wp-block-list">{lis}</ul>\n<!-- /wp:list -->\n'


def _legal_blocks(blocks):
    """blocks: lista di tuple ('p'|'h3'|'ul'|'raw', valore)."""
    out = ''
    for kind, val in blocks:
        if kind == 'p':
            out += paragraph(val, size='base',
                             extra_style='margin-top:14px;font-size:16px;line-height:1.7;max-width:760px')
        elif kind == 'h3':
            out += heading(3, val, accent_dot=False, style='19px')
        elif kind == 'ul':
            out += _legal_list(val)
        elif kind == 'raw':
            out += raw_html(val)
    return out


def build_legal_from_data(slug, d):
    """Pagina legale ricca (privacy / cookie policy / preferenze) da una
    struttura dati: hero + sezioni h2 con paragrafi ed elenchi. Testo scritto a
    mano nelle tre lingue (niente traduzione automatica sui testi legali)."""
    hero = (
        eyebrow(d['eyebrow']) +
        heading(1, d['h1'], style='clamp(30px,3.6vw,44px)') +
        paragraph(d['intro'], size='base',
                  extra_style='margin-top:20px;font-size:16px;line-height:1.7;max-width:760px')
    )
    if d.get('updated'):
        hero += paragraph(d['updated'],
                          extra_style='margin-top:10px;font-size:14px;color:var(--sr-grigio)')
    body = section(hero, classes='sr-section sr-hero')
    for h2, blocks in d['sections']:
        body += section(heading(2, h2) + _legal_blocks(blocks), classes='sr-section')
    write(slug, f'Pagina — {d["title"]}', d['description'], body)


def _cookie_reset_html(label, done):
    return (
        '<div class="sr-cookie-reset">'
        f'<button type="button" class="wp-block-button__link wp-element-button" data-sr-cookie-reset>{label}</button>'
        f'<p class="sr-cookie-reset__done" data-sr-cookie-reset-done hidden>{done}</p>'
        '</div>'
    )


def build_all_legal():
    """Genera privacy / cookie-policy / cookie-preferenze in IT, EN e RU
    (9 file). I contenuti vivono in LEGAL_CONTENT più sotto."""
    for base_slug, langs in LEGAL_CONTENT.items():
        for lang, prefix in (('it', ''), ('en', 'en-'), ('ru', 'ru-')):
            build_legal_from_data(prefix + base_slug, langs[lang])


# --------------------------------------------------- Contenuto pagine legali
#
# Testi scritti a mano nelle tre lingue (i testi legali non passano da
# translate_pages.py). Dicono SOLO quello che il sito fa davvero: modulo
# contatti, strumenti gratuiti (lead), area clienti cab.remarka.biz, log del
# server; responsabili reali (Hetzner in Germania, Brevo nell'UE, Google
# PageSpeed API, Anthropic API); mappe Google click-to-load. Nessun DPO
# inventato, nessun numero di registro inventato. Data di aggiornamento in alto.

LEGAL_UPDATED = {
    'it': 'Ultimo aggiornamento: 18 luglio 2026',
    'en': 'Last updated: 18 July 2026',
    'ru': 'Последнее обновление: 18 июля 2026',
}

LEGAL_CONTENT = {
    'privacy': {
        'it': {
            'title': 'Privacy policy', 'eyebrow': 'Privacy policy', 'h1': 'Privacy policy',
            'updated': LEGAL_UPDATED['it'],
            'description': 'Come trattiamo i dati personali su questo sito: quali raccogliamo, perché, a chi li affidiamo e come esercitare i vostri diritti.',
            'intro': 'Questa pagina spiega, senza giri di parole, quali dati raccogliamo quando usate questo sito, perché lo facciamo e come potete chiederci di cancellarli. Raccogliamo il minimo indispensabile: nessuna profilazione pubblicitaria, nessuna vendita di dati a terzi.',
            'sections': [
                ('Chi tratta i vostri dati', [
                    ('p', 'Il titolare del trattamento è Studio Remarka S.r.l. (P.IVA GE 302230994). Ci trovate in tre uffici, su appuntamento: Milano — Vicolo Privato Lavandai 2a, 20144; Torino — Corso Regina Margherita 94, 10153; Roma — Via Flaminia 122, 00196. Per qualsiasi domanda sui vostri dati scriveteci a info@remarka.biz: risponde una persona, non un modulo.'),
                ]),
                ('Quali dati raccogliamo e perché', [
                    ('p', 'Trattiamo solo i dati che ci servono per rispondervi o per farvi usare gli strumenti gratuiti.'),
                    ('h3', 'Modulo di contatto e richiesta di preventivo'),
                    ('ul', [
                        'Cosa: il vostro nome, un recapito (email o telefono) e il testo del messaggio, più eventuali allegati che scegliete di caricare.',
                        'Perché: per rispondervi e prepararvi un preventivo. Base giuridica: la vostra richiesta (misure precontrattuali).',
                        'Le richieste ci arrivano via email; non le usiamo per inviarvi pubblicità.',
                    ]),
                    ('h3', 'Strumenti gratuiti e check-up del sito'),
                    ('ul', [
                        'Cosa: l’indirizzo del sito che analizzate e, se chiedete il report via email, il vostro indirizzo email; registriamo anche il punteggio ottenuto e la lingua della pagina.',
                        'Perché: per generarvi l’analisi, inviarvi il PDF e — solo se lo avete acconsentito — ricontattarvi con un’offerta o un promemoria. Base giuridica: il vostro consenso, revocabile in qualsiasi momento.',
                        'Conserviamo queste richieste in un archivio interno di potenziali clienti.',
                    ]),
                    ('h3', 'Area clienti (cab.remarka.biz)'),
                    ('ul', [
                        'Cosa: email, nome, lingua preferita e, nei log di accesso, l’indirizzo IP e il browser (user-agent) usati per entrare. Non salviamo password: si entra con un link temporaneo inviato via email.',
                        'Perché: per darvi accesso ai vostri progetti. Base giuridica: l’esecuzione del contratto di servizio.',
                        'L’area clienti è riservata a chi lavora già con noi.',
                    ]),
                    ('h3', 'Log tecnici del server'),
                    ('ul', [
                        'Cosa: gli indirizzi IP e le richieste che ogni server web registra per funzionare e difendersi dagli abusi.',
                        'Perché: sicurezza e diagnostica. Base giuridica: il nostro legittimo interesse a tenere il sito online e sicuro.',
                    ]),
                ]),
                ('A chi affidiamo i dati', [
                    ('p', 'Per far funzionare il sito ci appoggiamo ad alcuni fornitori, che trattano i dati solo per nostro conto. I dati dei moduli e dell’area clienti restano nell’Unione Europea:'),
                    ('ul', [
                        'Hetzner — hosting del sito su server in Germania (UE).',
                        'Brevo — invio delle email transazionali (risposte, report PDF, link di accesso all’area clienti); fornitore con sede nell’UE.',
                    ]),
                    ('p', 'Due funzioni tecniche comunicano un dato a un fornitore con sede fuori dall’UE, ma solo quando siete voi ad avviarle e limitatamente a quanto segue:'),
                    ('ul', [
                        'Google PageSpeed Insights API — quando misurate velocità o SEO di una pagina, inviamo a Google soltanto l’indirizzo di quella pagina, per ottenere il punteggio. Nessun vostro dato personale.',
                        'Anthropic (Claude API) — gli strumenti basati su AI inviano ad Anthropic il testo o l’indirizzo che voi stessi incollate, solo quando premete il pulsante, per generare il risultato. Quei contenuti non vengono usati per addestrare modelli.',
                    ]),
                    ('p', 'Non cediamo i vostri dati a terzi per finalità di marketing.'),
                ]),
                ('Mappe e contenuti esterni', [
                    ('p', 'Le mappe di Google si caricano solo se le richiedete voi: mostriamo un’anteprima e la mappa interattiva parte — con la relativa connessione a Google — soltanto dopo che avete cliccato. Finché non cliccate, il vostro browser non contatta Google Maps.'),
                ]),
                ('Per quanto tempo teniamo i dati', [
                    ('ul', [
                        'Richieste dal modulo contatti: il tempo necessario a gestire la richiesta e gli adempimenti conseguenti.',
                        'Lead dagli strumenti gratuiti: finché sono utili al ricontatto o finché non ne chiedete la cancellazione.',
                        'Area clienti: i log di accesso per 12 mesi; l’account finché dura la collaborazione. Alla chiusura, o su vostra richiesta, i dati collegati vengono eliminati a cascata.',
                        'Log tecnici del server: per un periodo breve, poi sovrascritti.',
                    ]),
                ]),
                ('I vostri diritti', [
                    ('p', 'Sui vostri dati potete esercitare i diritti previsti dal GDPR: accesso, rettifica, cancellazione, limitazione, opposizione e portabilità. Potete revocare in qualsiasi momento un consenso già dato, senza togliere validità a quanto fatto prima.'),
                    ('p', 'Per esercitarli basta un’email a info@remarka.biz: ce ne occupiamo noi, anche per l’area clienti (esportazione o cancellazione a cascata). Se pensate che qualcosa non vada, potete rivolgervi al Garante per la protezione dei dati personali.'),
                ]),
                ('Aggiornamenti a questa pagina', [
                    ('p', 'Se cambieremo strumenti o finalità, aggiorneremo questa pagina e la data indicata in alto.'),
                ]),
            ],
        },
        'en': {
            'title': 'Privacy policy', 'eyebrow': 'Privacy policy', 'h1': 'Privacy policy',
            'updated': LEGAL_UPDATED['en'],
            'description': 'How we handle personal data on this site: what we collect, why, who we entrust it to, and how to exercise your rights.',
            'intro': 'This page explains, plainly, what data we collect when you use this website, why we do it, and how you can ask us to delete it. We collect the bare minimum: no advertising profiling, no selling of data to third parties.',
            'sections': [
                ('Who processes your data', [
                    ('p', 'The data controller is Studio Remarka S.r.l. (VAT GE 302230994). You can meet us at three offices, by appointment: Milan — Vicolo Privato Lavandai 2a, 20144; Turin — Corso Regina Margherita 94, 10153; Rome — Via Flaminia 122, 00196. For any question about your data, write to info@remarka.biz: a person replies, not a form.'),
                ]),
                ('What we collect and why', [
                    ('p', 'We only process the data we need to reply to you or let you use the free tools.'),
                    ('h3', 'Contact form and quote request'),
                    ('ul', [
                        'What: your name, one contact detail (email or phone) and the message text, plus any attachments you choose to upload.',
                        'Why: to reply and prepare a quote. Legal basis: your request (pre-contractual steps).',
                        'Requests reach us by email; we do not use them to send you advertising.',
                    ]),
                    ('h3', 'Free tools and site check-up'),
                    ('ul', [
                        'What: the address of the site you analyse and, if you ask for the report by email, your email address; we also record the score obtained and the page language.',
                        'Why: to generate your analysis, send you the PDF and — only if you consented — get back to you with an offer or a reminder. Legal basis: your consent, which you can withdraw at any time.',
                        'We keep these requests in an internal list of prospective clients.',
                    ]),
                    ('h3', 'Client area (cab.remarka.biz)'),
                    ('ul', [
                        'What: email, name, preferred language and, in the access logs, the IP address and browser (user-agent) used to log in. We do not store passwords: you sign in with a temporary link sent by email.',
                        'Why: to give you access to your projects. Legal basis: performance of the service contract.',
                        'The client area is reserved for people already working with us.',
                    ]),
                    ('h3', 'Server technical logs'),
                    ('ul', [
                        'What: the IP addresses and requests that every web server records in order to run and to defend against abuse.',
                        'Why: security and diagnostics. Legal basis: our legitimate interest in keeping the site online and secure.',
                    ]),
                ]),
                ('Who we entrust the data to', [
                    ('p', 'To run the site we rely on a few providers, which process data only on our behalf. Data from the forms and the client area stays within the European Union:'),
                    ('ul', [
                        'Hetzner — site hosting on servers in Germany (EU).',
                        'Brevo — sending transactional emails (replies, PDF reports, client-area sign-in links); an EU-based provider.',
                    ]),
                    ('p', 'Two technical features send one piece of data to a provider based outside the EU, but only when you trigger them and limited to the following:'),
                    ('ul', [
                        'Google PageSpeed Insights API — when you measure a page’s speed or SEO, we send Google only that page’s address, to obtain the score. None of your personal data.',
                        'Anthropic (Claude API) — the AI-based tools send Anthropic the text or address you paste in yourself, only when you press the button, to generate the result. That content is not used to train models.',
                    ]),
                    ('p', 'We do not pass your data to third parties for marketing purposes.'),
                ]),
                ('Maps and external content', [
                    ('p', 'Google maps load only if you ask for them: we show a preview, and the interactive map starts — with its connection to Google — only after you click. Until you click, your browser does not contact Google Maps.'),
                ]),
                ('How long we keep the data', [
                    ('ul', [
                        'Contact-form requests: for as long as needed to handle the request and any resulting obligations.',
                        'Leads from the free tools: as long as they are useful for follow-up, or until you ask for their deletion.',
                        'Client area: access logs for 12 months; the account for as long as the collaboration lasts. On closure, or at your request, the linked data is deleted in cascade.',
                        'Server technical logs: for a short period, then overwritten.',
                    ]),
                ]),
                ('Your rights', [
                    ('p', 'Over your data you can exercise the rights granted by the GDPR: access, rectification, erasure, restriction, objection and portability. You can withdraw a consent already given at any time, without affecting what was done before.'),
                    ('p', 'To exercise them, just email info@remarka.biz: we handle it, including for the client area (export or cascade deletion). If you think something is wrong, you can contact the Italian data protection authority (Garante).'),
                ]),
                ('Updates to this page', [
                    ('p', 'If we change tools or purposes, we will update this page and the date shown at the top.'),
                ]),
            ],
        },
        'ru': {
            'title': 'Политика конфиденциальности', 'eyebrow': 'Конфиденциальность',
            'h1': 'Политика конфиденциальности',
            'updated': LEGAL_UPDATED['ru'],
            'description': 'Как мы обрабатываем персональные данные на этом сайте: что собираем, зачем, кому доверяем и как реализовать ваши права.',
            'intro': 'Эта страница простыми словами объясняет, какие данные мы собираем, когда вы пользуетесь сайтом, зачем это делаем и как попросить их удалить. Собираем только необходимый минимум: без рекламного профилирования и без продажи данных третьим лицам.',
            'sections': [
                ('Кто обрабатывает ваши данные', [
                    ('p', 'Оператор обработки — Studio Remarka S.r.l. (НДС-номер GE 302230994). Нас можно встретить в трёх офисах по предварительной записи: Милан — Vicolo Privato Lavandai 2a, 20144; Турин — Corso Regina Margherita 94, 10153; Рим — Via Flaminia 122, 00196. По любым вопросам о ваших данных пишите на info@remarka.biz: отвечает человек, а не форма.'),
                ]),
                ('Какие данные мы собираем и зачем', [
                    ('p', 'Мы обрабатываем только те данные, которые нужны, чтобы ответить вам или дать воспользоваться бесплатными инструментами.'),
                    ('h3', 'Форма обратной связи и запрос сметы'),
                    ('ul', [
                        'Что: ваше имя, контакт (email или телефон) и текст сообщения, а также файлы, которые вы решите приложить.',
                        'Зачем: чтобы ответить и подготовить смету. Правовое основание: ваш запрос (преддоговорные меры).',
                        'Запросы приходят к нам по email; мы не используем их для рекламных рассылок.',
                    ]),
                    ('h3', 'Бесплатные инструменты и проверка сайта'),
                    ('ul', [
                        'Что: адрес сайта, который вы анализируете, и — если вы запрашиваете отчёт по email — ваш адрес email; мы также сохраняем полученный балл и язык страницы.',
                        'Зачем: чтобы сформировать анализ, отправить PDF и — только с вашего согласия — связаться с предложением или напоминанием. Правовое основание: ваше согласие, которое можно отозвать в любой момент.',
                        'Эти запросы мы храним во внутренней базе потенциальных клиентов.',
                    ]),
                    ('h3', 'Личный кабинет (cab.remarka.biz)'),
                    ('ul', [
                        'Что: email, имя, предпочитаемый язык и — в журнале входов — IP-адрес и браузер (user-agent), с которых выполнен вход. Пароли не храним: вход по временной ссылке, отправленной на email.',
                        'Зачем: чтобы дать вам доступ к вашим проектам. Правовое основание: исполнение договора об оказании услуг.',
                        'Кабинет доступен только тем, кто уже работает с нами.',
                    ]),
                    ('h3', 'Технические журналы сервера'),
                    ('ul', [
                        'Что: IP-адреса и запросы, которые любой веб-сервер записывает для работы и защиты от злоупотреблений.',
                        'Зачем: безопасность и диагностика. Правовое основание: наш законный интерес держать сайт онлайн и в безопасности.',
                    ]),
                ]),
                ('Кому мы доверяем данные', [
                    ('p', 'Чтобы сайт работал, мы пользуемся несколькими подрядчиками, которые обрабатывают данные только по нашему поручению. Данные из форм и кабинета остаются в Европейском союзе:'),
                    ('ul', [
                        'Hetzner — хостинг сайта на серверах в Германии (ЕС).',
                        'Brevo — отправка транзакционных писем (ответы, PDF-отчёты, ссылки для входа в кабинет); подрядчик с местонахождением в ЕС.',
                    ]),
                    ('p', 'Две технические функции передают один элемент данных подрядчику за пределами ЕС, но только когда вы сами их запускаете и только в следующем объёме:'),
                    ('ul', [
                        'Google PageSpeed Insights API — когда вы измеряете скорость или SEO страницы, мы передаём Google лишь адрес этой страницы, чтобы получить балл. Никаких ваших персональных данных.',
                        'Anthropic (Claude API) — инструменты на основе ИИ передают Anthropic текст или адрес, которые вы сами вставляете, только когда вы нажимаете кнопку, чтобы получить результат. Эти материалы не используются для обучения моделей.',
                    ]),
                    ('p', 'Мы не передаём ваши данные третьим лицам в маркетинговых целях.'),
                ]),
                ('Карты и внешний контент', [
                    ('p', 'Карты Google загружаются только по вашему запросу: мы показываем превью, а интерактивная карта — вместе с соответствующим соединением с Google — запускается лишь после клика. Пока вы не кликнули, ваш браузер не обращается к Google Maps.'),
                ]),
                ('Сколько мы храним данные', [
                    ('ul', [
                        'Запросы из формы обратной связи: столько, сколько нужно для обработки запроса и связанных с этим обязанностей.',
                        'Лиды из бесплатных инструментов: пока они полезны для повторного контакта или пока вы не попросите удалить.',
                        'Кабинет: журналы входов — 12 месяцев; учётная запись — пока длится сотрудничество. При завершении или по вашему запросу связанные данные удаляются каскадно.',
                        'Технические журналы сервера: короткий срок, затем перезапись.',
                    ]),
                ]),
                ('Ваши права', [
                    ('p', 'В отношении своих данных вы можете реализовать права по GDPR: доступ, исправление, удаление, ограничение, возражение и переносимость. Ранее данное согласие можно отозвать в любой момент — это не отменяет законность обработки до отзыва.'),
                    ('p', 'Чтобы воспользоваться правами, достаточно письма на info@remarka.biz: мы всё сделаем сами, в том числе по кабинету (экспорт или каскадное удаление). Если считаете, что что-то не так, вы можете обратиться в надзорный орган по защите данных.'),
                ]),
                ('Обновления этой страницы', [
                    ('p', 'Если мы поменяем инструменты или цели обработки, мы обновим эту страницу и дату вверху.'),
                ]),
            ],
        },
    },
    'cookie-policy': {
        'it': {
            'title': 'Cookie policy', 'eyebrow': 'Cookie policy', 'h1': 'Cookie policy',
            'updated': LEGAL_UPDATED['it'],
            'description': 'I cookie tecnici di questo sito: a cosa servono, quali sono e come cambiare la vostra scelta in qualsiasi momento.',
            'intro': 'Questa pagina elenca i cookie tecnici del sito — quelli necessari al suo funzionamento — e i servizi esterni che si attivano solo su vostra azione. Il banner vi chiede una scelta semplice; qui trovate che cosa c’è dietro.',
            'sections': [
                ('Cosa sono i cookie tecnici', [
                    ('p', 'I cookie tecnici sono piccoli file (o voci di memoria del browser) che servono a far funzionare il sito: ricordare una scelta, tenere aperta una sessione. Per legge non richiedono consenso preventivo, ma ve li elenchiamo lo stesso, per trasparenza.'),
                ]),
                ('Quali usiamo davvero', [
                    ('ul', [
                        'Scelta sui cookie: quando accettate o rifiutate dal banner, salviamo la vostra scelta nella memoria del browser (localStorage), così il banner non ricompare a ogni visita. Nessun dato lascia il vostro dispositivo.',
                        'Sessione e login di WordPress: cookie tecnici attivi solo per chi entra nell’area di amministrazione del sito (lo staff). Un visitatore normale non li riceve.',
                        'Area clienti (cab.remarka.biz): un cookie di sessione tecnico (cab_session), impostato solo dopo il login, per tenervi autenticati. È strettamente necessario e non richiede consenso.',
                    ]),
                ]),
                ('Servizi esterni, solo su vostra azione', [
                    ('p', 'Alcune funzioni contattano un servizio esterno soltanto quando siete voi ad attivarle, non prima:'),
                    ('ul', [
                        'Le mappe di Google partono solo dopo che cliccate sull’anteprima.',
                        'Gli strumenti basati su AI inviano il testo o l’URL che incollate solo quando premete il pulsante.',
                    ]),
                ]),
                ('Come cambiare la vostra scelta', [
                    ('p', 'Potete rivedere la vostra scelta in qualsiasi momento dalla pagina Preferenze cookie: un clic azzera la selezione salvata e fa ricomparire il banner. In alternativa, potete cancellare i dati del sito dalle impostazioni del vostro browser.'),
                ]),
            ],
        },
        'en': {
            'title': 'Cookie policy', 'eyebrow': 'Cookie policy', 'h1': 'Cookie policy',
            'updated': LEGAL_UPDATED['en'],
            'description': 'The technical cookies on this site: what they do, which ones they are, and how to change your choice at any time.',
            'intro': 'This page lists the site’s technical cookies — the ones needed for it to work — and the external services that start only when you act. The banner asks you a simple choice; here is what sits behind it.',
            'sections': [
                ('What technical cookies are', [
                    ('p', 'Technical cookies are small files (or browser-storage entries) that make the site work: remembering a choice, keeping a session open. By law they do not require prior consent, but we list them anyway, for transparency.'),
                ]),
                ('What we actually use', [
                    ('ul', [
                        'Cookie choice: when you accept or decline from the banner, we save your choice in the browser’s storage (localStorage), so the banner does not reappear on every visit. No data leaves your device.',
                        'WordPress session and login: technical cookies active only for those who log into the site’s admin area (staff). A regular visitor never receives them.',
                        'Client area (cab.remarka.biz): a technical session cookie (cab_session), set only after login, to keep you authenticated. It is strictly necessary and requires no consent.',
                    ]),
                ]),
                ('External services, only on your action', [
                    ('p', 'Some features contact an external service only when you trigger them, not before:'),
                    ('ul', [
                        'Google maps start only after you click the preview.',
                        'The AI-based tools send the text or URL you paste only when you press the button.',
                    ]),
                ]),
                ('How to change your choice', [
                    ('p', 'You can review your choice at any time from the Cookie preferences page: one click clears the saved selection and brings the banner back. Alternatively, you can clear the site’s data from your browser settings.'),
                ]),
            ],
        },
        'ru': {
            'title': 'Политика cookie', 'eyebrow': 'Политика cookie', 'h1': 'Политика cookie',
            'updated': LEGAL_UPDATED['ru'],
            'description': 'Технические cookie этого сайта: зачем они нужны, какие именно и как изменить свой выбор в любой момент.',
            'intro': 'На этой странице — технические cookie сайта (те, что нужны для его работы) и внешние сервисы, которые включаются только по вашему действию. Баннер предлагает простой выбор; здесь описано, что за ним стоит.',
            'sections': [
                ('Что такое технические cookie', [
                    ('p', 'Технические cookie — это небольшие файлы (или записи в памяти браузера), которые нужны, чтобы сайт работал: запомнить выбор, держать открытой сессию. По закону они не требуют предварительного согласия, но мы всё равно перечисляем их — ради прозрачности.'),
                ]),
                ('Что мы действительно используем', [
                    ('ul', [
                        'Выбор по cookie: когда вы принимаете или отклоняете через баннер, мы сохраняем ваш выбор в памяти браузера (localStorage), чтобы баннер не появлялся при каждом визите. Никакие данные не покидают ваше устройство.',
                        'Сессия и вход в WordPress: технические cookie, активные только для тех, кто входит в административную часть сайта (сотрудники). Обычный посетитель их не получает.',
                        'Личный кабинет (cab.remarka.biz): технический cookie сессии (cab_session), устанавливается только после входа, чтобы держать вас авторизованным. Строго необходим и не требует согласия.',
                    ]),
                ]),
                ('Внешние сервисы — только по вашему действию', [
                    ('p', 'Некоторые функции обращаются к внешнему сервису только тогда, когда вы сами их запускаете, не раньше:'),
                    ('ul', [
                        'Карты Google запускаются только после клика по превью.',
                        'Инструменты на основе ИИ передают текст или URL, которые вы вставили, только когда вы нажимаете кнопку.',
                    ]),
                ]),
                ('Как изменить свой выбор', [
                    ('p', 'Пересмотреть выбор можно в любой момент на странице «Настройки cookie»: один клик сбрасывает сохранённый выбор и возвращает баннер. Также можно очистить данные сайта в настройках браузера.'),
                ]),
            ],
        },
    },
    'cookie-preferenze': {
        'it': {
            'title': 'Preferenze cookie', 'eyebrow': 'Preferenze cookie', 'h1': 'Preferenze cookie',
            'updated': LEGAL_UPDATED['it'],
            'description': 'Gestisci la tua scelta sui cookie tecnici: azzera la selezione salvata e fai ricomparire il banner.',
            'intro': 'I cookie tecnici su cui si regge il sito non si possono disattivare senza comprometterne il funzionamento di base. Qui potete azzerare la scelta salvata nel banner — e farla di nuovo.',
            'sections': [
                ('La vostra scelta attuale', [
                    ('p', 'Alla prima visita il banner vi ha chiesto se accettare o rifiutare. Quella scelta è salvata nella memoria del vostro browser. Se volete rivederla — per rileggere il banner o ripartire da zero — azzeratela qui:'),
                    ('raw', _cookie_reset_html('Reimposta le preferenze cookie', 'Fatto: la scelta è stata azzerata. Il banner ricomparirà.')),
                ]),
                ('Cosa succede quando azzerate', [
                    ('p', 'Il pulsante cancella solo la vostra scelta salvata su questo dispositivo. Al prossimo caricamento di una pagina il banner ricomparirà e potrete decidere di nuovo. Nessun altro dato viene toccato.'),
                    ('p', 'Per i dettagli su quali cookie usiamo, trovate tutto nella Cookie policy.'),
                ]),
            ],
        },
        'en': {
            'title': 'Cookie preferences', 'eyebrow': 'Cookie preferences', 'h1': 'Cookie preferences',
            'updated': LEGAL_UPDATED['en'],
            'description': 'Manage your choice about technical cookies: clear the saved selection and bring the banner back.',
            'intro': 'The technical cookies this site relies on cannot be turned off without breaking basic functionality. What you can do here is clear your saved banner choice and make it appear again.',
            'sections': [
                ('Your current choice', [
                    ('p', 'On your first visit the banner asked whether to accept or decline. That choice is saved in your browser’s storage. If you want to review it — to read the banner again or start over — clear it here:'),
                    ('raw', _cookie_reset_html('Reset cookie preferences', 'Done: your choice has been cleared. The banner will appear again.')),
                ]),
                ('What happens when you clear it', [
                    ('p', 'The button clears only your choice saved on this device. On the next page load the banner will reappear and you can decide again. No other data is touched.'),
                    ('p', 'For details on which cookies we use, everything is in the Cookie policy.'),
                ]),
            ],
        },
        'ru': {
            'title': 'Настройки cookie', 'eyebrow': 'Настройки cookie', 'h1': 'Настройки cookie',
            'updated': LEGAL_UPDATED['ru'],
            'description': 'Управляйте выбором по техническим cookie: сбросьте сохранённый выбор и верните баннер.',
            'intro': 'Технические cookie, на которых держится сайт, нельзя отключить, не сломав его базовую работу. Здесь можно сбросить сохранённый выбор в баннере — и сделать его заново.',
            'sections': [
                ('Ваш текущий выбор', [
                    ('p', 'При первом визите баннер спросил, принять или отклонить. Этот выбор сохранён в памяти вашего браузера. Если хотите пересмотреть его — перечитать баннер или начать заново — сбросьте его здесь:'),
                    ('raw', _cookie_reset_html('Сбросить настройки cookie', 'Готово: выбор сброшен. Баннер появится снова.')),
                ]),
                ('Что происходит при сбросе', [
                    ('p', 'Кнопка удаляет только ваш выбор, сохранённый на этом устройстве. При следующей загрузке страницы баннер появится снова, и вы сможете решить заново. Никакие другие данные не затрагиваются.'),
                    ('p', 'Подробности о том, какие cookie мы используем, есть в Политике cookie.'),
                ]),
            ],
        },
    },
}


# ---------------------------------------------------------------- Blog

# Rubriche dell'indice blog (richiesta del titolare 17.07, redesign indice:
# «In evidenza» + filtro a chip). Chiave = valore del campo `tema` di ogni
# dict in BLOG_POSTS (data.py) → usato sia come data-cat delle righe sia
# come data-sr-case-filter dei bottoni. Etichette EN in
# chrome_strings.py:CHROME_BLOG_INDEX.
BLOG_RUBRICHE = [
    ('seo', 'SEO e visibilità AI'),
    ('norme', 'Norme e accessibilità'),
    ('decisioni', 'Prezzi e decisioni'),
    ('prodotti', 'Tecnologie che vendono'),
    ('prestazioni', 'Velocità e sostenibilità'),
]


def build_blog_index():
    hero = section(eyebrow('Blog') + heading(1, 'Appunti tecnici, in italiano', style='clamp(38px,4.6vw,64px)') +
                    paragraph('Niente marketing travestito da articolo: solo quello che impariamo consegnando siti veloci.',
                               color='grigio', size='medium'),
                    classes='sr-section sr-hero')

    # Ordine: dalla più recente (richiesta del titolare 17.07) — i batch
    # vengono APPESI a BLOG_POSTS, quindi senza sort i nuovi finirebbero in
    # fondo. Sort stabile: articoli dello stesso giorno restano nell'ordine
    # del batch.
    posts_sorted = sorted(BLOG_POSTS, key=lambda p: _blog_iso_date(p['data']), reverse=True)

    # «In evidenza»: le 2 uscite più recenti come card grandi (copertina SVG,
    # data, titolo, estratto, freccia) — vetrina sopra il catalogo completo.
    # Le stesse 2 storie restano ANCHE come riga nell'elenco sotto (la
    # vetrina non sostituisce il catalogo).
    feat_posts = [p for p in posts_sorted if p.get('cover')][:2]
    feat_cards = ''.join(
        f'<a href="/blog/{p["slug"]}/" class="sr-blog-feat-card">'
        f'<img src="{p["cover"]["src"]}" alt="{p["cover"]["alt"]}" loading="lazy" class="sr-blog-feat-card__img"/>'
        f'<span class="sr-blog-feat-card__body">'
        f'<span class="sr-blog-feat-card__date sr-mono">{p["data"]}</span>'
        f'<span class="sr-blog-feat-card__title">{p["titolo"]}</span>'
        f'<span class="sr-blog-feat-card__excerpt">{p["estratto"]}</span>'
        f'<span class="sr-blog-feat-card__arrow">→</span>'
        f'</span></a>'
        for p in feat_posts
    )
    featured = section(
        eyebrow('In evidenza') +
        raw_html(f'<div class="sr-blog-feat-grid">{feat_cards}</div>'),
        classes='sr-section sr-section--bianco',
    )

    # Filtro a chip per rubrica: stessa meccanica/classi del filtro casi
    # studio (CASE_FILTER_LABELS più sopra, assets/js/remarka.js
    # initCaseFilter()) — generalizzato per riconoscere anche
    # .sr-blog-row[data-cat] oltre a .sr-case-card[data-cat], senza toccare
    # il comportamento sui casi studio.
    chip_btns = (
        '<button type="button" class="sr-case-filter__btn is-active" '
        'data-sr-case-filter="all" aria-pressed="true">Tutti</button>' +
        ''.join(
            f'<button type="button" class="sr-case-filter__btn" '
            f'data-sr-case-filter="{key}" aria-pressed="false">{label}</button>'
            for key, label in BLOG_RUBRICHE
        )
    )
    chips = raw_html(f'<div class="sr-case-filter" data-sr-case-filter-bar>{chip_btns}</div>')

    rows = ''.join(
        f'<a href="/blog/{p["slug"]}/" class="sr-blog-row" data-cat="{p["tema"]}" style="color:inherit">'
        f'<span class="sr-blog-date">{p["data"]}</span>'
        f'<span class="sr-blog-body"><span style="font-family:var(--sr-font-display);font-weight:500;font-size:26px">{p["titolo"]}</span>'
        f'<span style="font-size:15.5px;color:var(--sr-grigio)">{p["estratto"]}</span></span></a>'
        for p in posts_sorted
    )
    list_section = section(chips + raw_html(rows), classes='sr-section')
    write('blog-index', 'Pagina — Blog (elenco)',
          'Indice blog: 2 articoli più recenti in evidenza, filtro a chip per rubrica, elenco completo per data.',
          hero + featured + list_section)


_THEME_DIR = os.path.join(os.path.dirname(__file__), '..', 'remarka-studio')
_THEME_URL_PREFIX = '/wp-content/themes/remarka-studio/'


def _svg_dims(src):
    """width/height (int, int) letti dal viewBox (o dagli attributi width/
    height) di un SVG locale del tema, per gli attributi HTML width/height
    dell'<img> (audit "elementi immagine senza width/height espliciti" —
    senza questi attributi il browser non può riservare lo spazio prima del
    caricamento → CLS). None se `src` non è un SVG locale del tema o il
    file/attributo manca — in quel caso il chiamante omette gli attributi
    invece di scriverne di sbagliati."""
    if not src.startswith(_THEME_URL_PREFIX) or not src.lower().endswith('.svg'):
        return None
    path = os.path.join(_THEME_DIR, src[len(_THEME_URL_PREFIX):])
    try:
        with open(path, 'r', encoding='utf-8') as fh:
            head = fh.read(2000)
    except OSError:
        return None
    m = re.search(
        r'<svg\b[^>]*\bviewBox=["\']\s*[\d.+-]+\s+[\d.+-]+\s+([\d.]+)\s+([\d.]+)\s*["\']',
        head,
    )
    if not m:
        m = re.search(
            r'<svg\b[^>]*\bwidth=["\'](\d+(?:\.\d+)?)["\'][^>]*\bheight=["\'](\d+(?:\.\d+)?)["\']',
            head,
        )
    if not m:
        return None
    return int(round(float(m.group(1)))), int(round(float(m.group(2))))


def blog_figure(fig, cover=False):
    """Иллюстрация статьи (фирменный SVG). cover=True — обложка под H1
    (без подписи, с рамкой), иначе — схема/диаграмма с mono-подписью.
    loading=lazy, max-width:100% (адаптив), alt переводится конвейером.
    width/height — dal viewBox del file SVG (_svg_dims), per il CLS."""
    margin = '8px 0 8px' if cover else '36px 0 8px'
    cap = ''
    if not cover and fig.get('caption'):
        cap = (f'<figcaption class="sr-mono" style="margin-top:12px;font-size:12.5px;'
               f'letter-spacing:0.04em;color:var(--sr-grigio);max-width:75ch">{fig["caption"]}</figcaption>')
    dims = _svg_dims(fig['src'])
    size_attrs = f' width="{dims[0]}" height="{dims[1]}"' if dims else ''
    return raw_html(
        f'<figure class="wp-block-image size-large" style="margin:{margin}">'
        f'<img src="{fig["src"]}" alt="{fig["alt"]}"{size_attrs} loading="lazy" '
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

    body = section(inner, classes='sr-section')

    # CTA di chiusura (owner 17.07.2026 — unificazione banner: prima gli
    # articoli non avevano NESSUNA banda di contenuto, solo la .sr-footer-cta
    # del footer; rimossa quella, restava zero. Stesso testo/stile della CTA
    # servizi/città/strumenti (sr-cta-band), non un secondo banner diverso.
    cta = section(
        heading(2, 'Parliamo del vostro sito', style=None) +
        paragraph('Analisi gratuita del sito attuale, preventivo chiuso entro 24 ore dalla chiamata.',
                   color='grigio', size='medium', extra_style='margin-top:12px') +
        buttons([('Richiedi preventivo in 24 ore', '/#contatti', None),
                 analyze_cta_button()],
                justify='center', margin_top='28px') +
        cta_trust_row(),
        classes='sr-section sr-cta-band',
    )

    torna = section(
        buttons([('← Tutti gli articoli', '/blog/', 'outline')], justify='center'),
        classes='sr-section',
    )
    write(f'blog-{p["slug"]}', f'Pagina — Articolo: {p["titolo"]}', f'Articolo blog: {p["titolo"]}',
          hero + body + cta + torna)


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
    RETROFIT = '2026-07-18'  # ultima rigenerazione della mappa (dateModified); batch 4 pubblicato oggi
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
        if c.get('flagship'):
            build_city_flagship(c)
        else:
            build_city(c)

    print('Chi siamo e pagine legali:')
    build_chi_siamo()
    build_all_legal()

    print('Blog:')
    build_blog_index()
    for p in BLOG_POSTS:
        build_blog_post(p)

    print('\nFatto.')


if __name__ == '__main__':
    main()
