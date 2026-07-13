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
    metric_rows, browser_frame, barra, barra_row, pull_quote, chapter,
    compare_table_row, pattern_header,
)
from data import SERVICES, CASES, TOOLS, CITY, CITIES, BLOG_POSTS, EXPORT_READY, WEB_APP  # noqa: E402

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


# ---------------------------------------------------------------- Servizio

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

    mc = svc['mini_caso']
    mini_caso = section(
        columns([
            column(eyebrow('Dal registro consegne') + heading(2, f"{mc['cliente']}, {mc['citta']}", style='clamp(26px,3vw,34px)') +
                   paragraph(mc['testo'], size='base', extra_style='margin-top:16px;font-size:16px') +
                   raw_html(f'<p class="sr-card-link" style="margin-top:16px"><a href="/casi-studio/{mc["link_slug"]}/">Leggi un caso completo →</a></p>'),
                   width='55%'),
            column(raw_html('<div style="display:flex;flex-direction:column;gap:20px">') +
                   raw_html(barra_row('Prima', str(mc['prima']), mc['prima'], muted=True)) +
                   raw_html(barra_row('Dopo', str(mc['dopo']), mc['dopo'], delay=150, verde_value=True)) +
                   raw_html(f'<p class="sr-mono" style="font-size:11.5px;letter-spacing:0.06em;color:var(--sr-grigio)">{mc["caption"]}</p>') +
                   raw_html('</div>'), width='45%'),
        ], valign='center'),
        classes='sr-section',
    )

    prezzo = section(
        eyebrow('Prezzo') +
        raw_html(f'<div class="sr-stat__num" style="font-size:clamp(36px,4vw,52px)">{svc["prezzo_range"]}</div>') +
        paragraph(svc['prezzo_lede'], color='grigio', size='base', extra_style='margin-top:14px;max-width:60ch') +
        paragraph('Cosa fa variare il prezzo', extra_style='margin-top:28px;font-weight:500;font-size:16px') +
        list_rows(svc['prezzo_note']) +
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

def build_casi_studio_index():
    hero = section(eyebrow('Casi studio') + heading(1, 'Risultati misurati, non promessi', style='clamp(38px,4.6vw,64px)'),
                    classes='sr-section sr-hero')

    cards = []
    for c in CASES:
        card_inner = (
            browser_frame('studioremarka.it', f'Screenshot del sito {c["cliente"]}') +
            raw_html(
                f'<a href="/casi-studio/{c["slug"]}/" style="color:inherit;text-decoration:none">'
                f'<h3 class="wp-block-heading" style="margin-top:20px">{c["cliente"]}</h3></a>'
            ) +
            raw_html(f'<p class="sr-mono" style="font-size:12px;letter-spacing:0.06em;text-transform:uppercase;color:var(--sr-grigio);margin-top:6px">{c["settore"]} · {c["citta"]} · {c["intervento"]}</p>') +
            raw_html(f'<p class="sr-mono" style="font-size:18px;color:var(--sr-oltremare);margin-top:10px">{c["key_metric"]}</p>') +
            raw_html('<div style="display:flex;flex-direction:column;gap:6px;margin-top:14px">') +
            raw_html(barra(c['prima'], muted=True, height=6)) +
            raw_html(barra(c['dopo'], delay=150, height=6)) +
            raw_html('</div>') +
            raw_html(f'<p class="sr-card-link" style="margin-top:16px"><a href="/casi-studio/{c["slug"]}/">Leggi il caso →</a></p>')
        )
        cards.append(group(card_inner, classes=''))

    grid = section(
        group(''.join(cards), classes='', layout_type='grid', style='280px') +
        paragraph('Punteggi Google PageSpeed su mobile — report disponibili su richiesta', classes='sr-mono',
                   extra_style='margin-top:40px;font-size:12px;color:var(--sr-grigio)'),
        classes='sr-section',
    )

    cta = section(
        heading(2, 'Il prossimo caso può essere il vostro') +
        paragraph('Prima misuriamo il sito attuale, poi vi diciamo — con numeri — cosa possiamo garantire.',
                   color='grigio', size='medium', extra_style='margin-top:12px') +
        buttons([('Analizza il tuo sito — gratis', '/strumenti/test-velocita/', None)], justify='center', margin_top='28px'),
        classes='sr-section sr-dark',
    )
    write('casi-studio-index', 'Pagina — Casi studio (elenco)',
          'Elenco dei casi studio in griglia 2×2 con metriche chiave e barre prima/dopo.',
          hero + grid + cta)


def build_caso_detail(c):
    hero = section(
        eyebrow(f'Casi studio / {c["cliente"]}') +
        heading(1, c['titolo'], style='clamp(34px,4.4vw,58px)') +
        raw_html(f'<p class="sr-mono" style="margin-top:20px;font-size:12.5px;letter-spacing:0.06em;color:var(--sr-grigio)">'
                  f'SETTORE {c["settore"].upper()} · SEDE {c["citta"].upper()} · INTERVENTO {c["intervento"].upper()} · ANNO {c["anno"]}</p>'),
        classes='sr-section sr-hero',
    )

    screenshot = section(browser_frame('studioremarka.it', f'Screenshot del sito {c["cliente"]}'), classes='sr-section')

    cap1 = section(chapter('01 — Problema',
                            paragraph(c['problema_testo'], size='base', extra_style='font-size:17px') +
                            group(''.join(
                                f'<div class="sr-stat"><span class="sr-stat__num" style="font-size:clamp(32px,3vw,44px);color:var(--sr-oltremare)">{v}</span>'
                                f'<p style="margin-top:10px;font-size:14.5px;color:var(--sr-grigio)">{l}</p></div>'
                                for v, l in c['problema_stats']),
                                classes='', layout_type='grid', style='160px')),
                    classes='sr-section')

    cap2 = section(chapter('02 — Soluzione',
                            paragraph(c['soluzione_testo'], size='base', extra_style='font-size:17px') +
                            list_rows(c['soluzione_interventi'])),
                    classes='sr-section sr-section--bianco')

    cap3_bars = raw_html('<div style="display:flex;flex-direction:column;gap:20px">') + \
        raw_html(barra_row('Prima', str(c['prima']), c['prima'], muted=True, height=10)) + \
        raw_html(barra_row('Dopo', str(c['dopo']), c['dopo'], delay=150, verde_value=True, height=10)) + \
        raw_html(f'<p class="sr-mono" style="font-size:11.5px;letter-spacing:0.06em;color:var(--sr-grigio)">{c["caption"]}</p>') + \
        raw_html('</div>')
    cap3 = section(chapter('03 — Risultati',
                            cap3_bars +
                            paragraph(c['risultati_testo'], size='base', extra_style='font-size:17px;margin-top:24px') +
                            group(''.join(
                                f'<div class="sr-stat"><span class="sr-stat__num" style="font-size:clamp(32px,3vw,44px);color:var(--sr-oltremare)">{v}</span>'
                                f'<p style="margin-top:10px;font-size:14.5px;color:var(--sr-grigio)">{l}</p></div>'
                                for v, l in c['risultati_stats']),
                                classes='', layout_type='grid', style='160px') +
                            pull_quote(c['quote'], c['attribuzione'])),
                    classes='sr-section')

    cta = section(
        heading(2, 'Numeri simili per il vostro settore', dot_char='?') +
        paragraph("L’analisi del sito attuale è gratuita e vi arriva come report scritto, con le priorità.",
                   color='grigio', size='medium', extra_style='margin-top:12px') +
        buttons([("Richiedi l’analisi gratuita", '/#contatti', None)], justify='center', margin_top='28px') +
        raw_html('<p class="sr-card-link" style="text-align:center;margin-top:20px"><a href="/casi-studio/">Altri casi studio →</a></p>'),
        classes='sr-section sr-dark',
    )

    write(f'caso-{c["slug"]}', f'Pagina — Caso: {c["cliente"]}',
          f'Caso studio dettagliato: {c["titolo"]}',
          hero + screenshot + cap1 + cap2 + cap3 + cta)


# ---------------------------------------------------------------- Prezzi

def build_prezzi():
    hero = section(
        eyebrow('Prezzi') + heading(1, 'Prezzi trasparenti. Nessuna sorpresa in corso d’opera', style='clamp(38px,4.6vw,64px)') +
        paragraph('La tabella qui sotto è pubblica; il preventivo che firmate è un prezzo chiuso. '
                   'Se in corso d’opera serve altro, si concorda prima, per iscritto.',
                   color='grigio', size='medium') +
        raw_html('<div style="margin-top:40px;max-width:600px">') +
        raw_html(barra(100, height=6)) +
        raw_html('<p class="sr-mono" style="margin-top:10px;font-size:12px;color:var(--sr-grigio)">100% DEI PREVENTIVI 2025 CHIUSI AL PREZZO FIRMATO</p></div>'),
        classes='sr-section sr-hero',
    )

    headers = ['', 'Sito vetrina<br><span>€ 1.900–2.800</span>', 'Sito aziendale<br><span>€ 3.900–5.800</span>',
               'E-commerce<br><span>€ 7.500–14.000</span>']
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
        ('Consegna', ['3 sett.', '5–7 sett.', '8–10 sett.']),
    ]
    thead = '<tr>' + ''.join(f'<th>{h}</th>' for h in headers) + '</tr>'
    tbody = ''.join(compare_table_row(label, vals) for label, vals in rows_data)
    compare = raw_html(f'<div class="sr-compare-table"><table><thead>{thead}</thead><tbody>{tbody}</tbody></table></div>')

    table_section = section(
        compare +
        paragraph('Per confronto: le agenzie italiane chiedono in media € 2.500–8.000 per un sito aziendale '
                   'e € 5.000–20.000 per un e-commerce (listini pubblici 2026). Siamo nella stessa fascia — '
                   'con tre garanzie scritte nel contratto che altrove non trovate.',
                   color='grigio', size='base', extra_style='margin-top:28px;max-width:70ch') +
        paragraph('Fattura elettronica via SDI. Pagamento in tre tranche: 40 / 40 / 20.', color='grigio', size='small',
                   extra_style='margin-top:16px') +
        buttons([('Richiedi preventivo dettagliato', '/#contatti', None)], margin_top='20px'),
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
          hero + table_section + variazioni + cta)


# ---------------------------------------------------------------- Strumenti

def build_strumenti_index():
    hero = section(eyebrow('Strumenti gratuiti') + heading(1, 'Prima misurate, poi decidete', style='clamp(38px,4.6vw,64px)') +
                    paragraph('Strumenti professionali, gratuiti, senza registrazione.', color='grigio', size='medium'),
                    classes='sr-section sr-hero')

    cards = []
    for t in TOOLS:
        card = (
            raw_html(f'<p class="sr-mono" style="color:var(--sr-oltremare);font-size:12px">{t["idx"]}</p>') +
            heading(3, t['titolo'], accent_dot=False) +
            paragraph(t['descrizione'], color='grigio', size='small') +
            raw_html(f'<p class="sr-card-link" style="margin-top:16px"><a href="/strumenti/{t["slug"]}/">Prova →</a></p>')
        )
        cards.append(group(card, classes='sr-card sr-card--carta'))

    grid = section(group(''.join(cards), classes='', layout_type='grid', style='240px'),
                    classes='sr-section sr-section--bianco')
    write('strumenti-index', 'Pagina — Strumenti (elenco)', 'Elenco dei quattro strumenti gratuiti.', hero + grid)


def build_strumento_test_velocita():
    t = TOOLS[0]
    hero = section(
        eyebrow(f'Strumento gratuito {t["idx"]}') + heading(1, t['hero_titolo'], style='clamp(34px,4vw,52px)') +
        paragraph(t['hero_sub'], color='grigio', size='medium', extra_style='max-width:100%'),
        classes='sr-section sr-hero',
    )

    widget = raw_html(f'''
<div class="sr-tool-widget sr-card">
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
</div>''')

    widget_section = section(widget, classes='sr-section')

    cta = section(
        heading(2, 'Vuoi che sistemiamo noi questi problemi', dot_char='?') +
        paragraph('Report gratuito con le cause, le priorità e un preventivo chiuso: 90+ garantito da contratto.',
                   color='grigio', size='medium', extra_style='margin-top:12px') +
        buttons([("Richiedi l’analisi completa", '/#contatti', None)], justify='center', margin_top='28px'),
        classes='sr-section sr-dark',
    )

    altri = TOOLS[1:]
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

    write('strumento-test-velocita', 'Pagina — Strumento: Test velocità',
          'Strumento interattivo con demo di analisi PageSpeed (punteggio, LCP/INP/CLS simulati).',
          hero + widget_section + cta + altri_section)


def build_strumento_placeholder(tool):
    """Le altre 3 card di /strumenti/ rimandano a pagine reali anche prima che
    lo strumento sia implementato — placeholder onesto invece di link rotti."""
    hero = section(
        eyebrow(f'Strumento gratuito {tool["idx"]}') + heading(1, tool['hero_titolo'], style='clamp(34px,4vw,52px)') +
        paragraph(tool['hero_sub'], color='grigio', size='medium', extra_style='max-width:100%'),
        classes='sr-section sr-hero',
    )

    placeholder = group(
        eyebrow('In arrivo') +
        paragraph('Questo strumento è in fase di sviluppo. Nel frattempo richiedete un’analisi gratuita: vi rispondiamo entro un giorno lavorativo.',
                   size='medium') +
        buttons([('Richiedi analisi gratuita', '/#contatti', None)], margin_top='20px'),
        classes='sr-card',
    )
    placeholder_section = section(raw_html('<div style="text-align:center;max-width:640px;margin:0 auto">') + placeholder + raw_html('</div>'),
                                   classes='sr-section')

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
          f'Placeholder onesto per lo strumento {tool["titolo"]} (non ancora implementato).',
          hero + placeholder_section + altri_section)


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
    servizi = section(
        eyebrow('Cosa facciamo') + heading(2, 'Sei servizi, un’unica garanzia') +
        raw_html(f'<div class="sr-servizi-rows" style="margin-top:32px">{servizi_rows}</div>'),
        classes='sr-section sr-section--bianco',
    )

    local_case = next(x for x in CASES if x['slug'] == c['case_slug'])
    caso = section(
        columns([
            column(browser_frame(c['case_url_label'], f'Screenshot del sito {local_case["cliente"]}'), width='55%'),
            column(eyebrow(c['case_eyebrow']) + heading(3, c['case_title'], accent_dot=False) +
                   paragraph(local_case['risultati_testo'], color='grigio', size='base', extra_style='margin-top:12px') +
                   raw_html('<div style="display:flex;flex-direction:column;gap:10px;margin-top:24px">') +
                   raw_html(barra(local_case['prima'], muted=True, height=6)) +
                   raw_html(barra(local_case['dopo'], delay=150, height=6)) +
                   raw_html('</div>') +
                   raw_html(f'<p class="sr-card-link" style="margin-top:20px"><a href="/casi-studio/{local_case["slug"]}/">Leggi il caso completo →</a></p>'),
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


def build_blog_post(p):
    hero = section(
        raw_html(f'<p class="sr-mono" style="color:var(--sr-grigio);font-size:13px">{p["data"]}</p>') +
        heading(1, p['titolo'], accent_dot=False, style='clamp(32px,4vw,48px)'),
        classes='sr-section',
    )
    body = section(
        paragraph(p['corpo'], size='base', extra_style='font-size:17px;line-height:1.7') +
        buttons([('← Tutti gli articoli', '/blog/', 'outline')], margin_top='32px'),
        classes='sr-section',
    )
    write(f'blog-{p["slug"]}', f'Pagina — Articolo: {p["titolo"]}', f'Articolo blog: {p["titolo"]}', hero + body)


def main():
    print('Servizi:')
    build_servizi_index()
    for svc in SERVICES:
        build_servizio(svc)
    build_export_ready()
    build_web_app()

    print('Casi studio:')
    build_casi_studio_index()
    for c in CASES:
        build_caso_detail(c)

    print('Prezzi:')
    build_prezzi()

    print('Strumenti:')
    build_strumenti_index()
    build_strumento_test_velocita()
    for tool in TOOLS[1:]:
        build_strumento_placeholder(tool)

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
