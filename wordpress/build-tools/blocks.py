"""
Gutenberg block-markup helpers for generating Remarka Studio page patterns.

Каждая функция возвращает валидную строку блочной разметки WordPress
(HTML-комментарии `<!-- wp:... -->` + JSON-атрибуты через json.dumps,
без ручного экранирования кавычек — источник ошибок в предыдущих
хендрайтен-паттернах).
"""
import json


def _attrs(d):
    if not d:
        return ''
    return ' ' + json.dumps(d, ensure_ascii=False, separators=(',', ':'))


def eyebrow(text, extra_class=''):
    cls = ('sr-eyebrow ' + extra_class).strip()
    return (f'<!-- wp:paragraph {{"className":"{cls}"}} -->\n'
            f'<p class="{cls}">{text}</p>\n'
            f'<!-- /wp:paragraph -->\n')


def heading(level, text, accent_dot=True, style=None, dot_char='.'):
    """level: 1-6. style: optional inline font-size, e.g. 'clamp(38px, 4.6vw, 64px)'.
    dot_char: carattere colorato finale (default '.', usare '?' per le domande)."""
    dot = f'<span class="sr-accent-dot">{dot_char}</span>' if accent_dot else ''
    a = {"level": level} if level != 2 else {}
    if style:
        a.setdefault("style", {}).setdefault("typography", {})["fontSize"] = style
    tag = f'h{level}'
    style_attr = f' style="font-size:{style}"' if style else ''
    return (f'<!-- wp:heading{_attrs(a)} -->\n'
            f'<{tag} class="wp-block-heading"{style_attr}>{text}{dot}</{tag}>\n'
            f'<!-- /wp:heading -->\n')


def paragraph(text, classes='', color=None, size=None, extra_style=None):
    cls_parts = [c for c in classes.split() if c]
    color_cls = f'has-{color}-color has-text-color' if color else ''
    size_cls = f'has-{size}-font-size' if size else ''
    all_cls = ' '.join([c for c in cls_parts + [color_cls, size_cls] if c])
    attrs = {}
    if all_cls:
        attrs['className'] = ' '.join(cls_parts) if cls_parts else None
    if color:
        attrs['textColor'] = color
    if size:
        attrs['fontSize'] = size
    attrs = {k: v for k, v in attrs.items() if v}
    style_attr = f' style="{extra_style}"' if extra_style else ''
    class_attr = f' class="{all_cls}"' if all_cls else ''
    return (f'<!-- wp:paragraph{_attrs(attrs)} -->\n'
            f'<p{class_attr}{style_attr}>{text}</p>\n'
            f'<!-- /wp:paragraph -->\n')


def buttons(items, justify=None, gap='14px', margin_top=None):
    """items: list of (text, href, style) style in (None,'outline','whatsapp')"""
    layout = {"type": "flex", "justifyContent": justify} if justify else None
    style = {"spacing": {"blockGap": gap}}
    if margin_top:
        style["spacing"]["margin"] = {"top": margin_top}
    outer_attrs = {"style": style}
    if layout:
        outer_attrs["layout"] = layout
    inner = []
    for text, href, btn_style in items:
        cls = ''
        if btn_style == 'outline':
            cls = 'is-style-outline'
        elif btn_style == 'whatsapp':
            cls = 'sr-btn-whatsapp'
        battrs = {"className": cls} if cls else {}
        wrapper_cls = f' {cls}' if cls else ''
        target = ' target="_blank" rel="noopener noreferrer"' if href.startswith('http') else ''
        inner.append(
            f'<!-- wp:button{_attrs(battrs)} -->\n'
            f'<div class="wp-block-button{wrapper_cls}"><a class="wp-block-button__link wp-element-button" href="{href}"{target}>{text}</a></div>\n'
            f'<!-- /wp:button -->\n'
        )
    style_attr = f' style="margin-top:{margin_top}"' if margin_top else ''
    return (f'<!-- wp:buttons{_attrs(outer_attrs)} -->\n'
            f'<div class="wp-block-buttons"{style_attr}>' + ''.join(inner) + '</div>\n'
            f'<!-- /wp:buttons -->\n')


def column(html, width=None, valign=None):
    attrs = {}
    if width:
        attrs['width'] = width
    if valign:
        attrs['verticalAlignment'] = valign
    style = f' style="flex-basis:{width}"' if width else ''
    valign_cls = ' is-vertically-aligned-center' if valign else ''
    return (f'<!-- wp:column{_attrs(attrs)} -->\n'
            f'<div class="wp-block-column{valign_cls}"{style}>{html}</div>\n'
            f'<!-- /wp:column -->\n')


def columns(cols_html, gap='32px', valign=None, extra_class=''):
    attrs = {"style": {"spacing": {"blockGap": {"left": gap}}}}
    if valign:
        attrs['verticalAlignment'] = valign
    cls = ('sr-cascade ' + extra_class).strip()
    attrs['className'] = cls
    valign_cls = ' are-vertically-aligned-center' if valign else ''
    return (f'<!-- wp:columns{_attrs(attrs)} -->\n'
            f'<div class="wp-block-columns{valign_cls} {cls}">' + ''.join(cols_html) + '</div>\n'
            f'<!-- /wp:columns -->\n')


def group(html, classes='', layout_type='constrained', tag=None, style=None, anchor=None):
    """layout_type: 'constrained' | 'grid' | 'flow'. Il markup renderizzato porta
    sempre la classe is-layout-* corrispondente (come farebbe Gutenberg), così il
    grid non dipende dall'attributo JSON — funziona anche in anteprime statiche."""
    attrs = {"className": classes, "layout": {"type": layout_type}}
    grid_style_attr = ''
    if layout_type == 'grid':
        min_width = style or '260px'
        attrs['layout'] = {"type": "grid", "minimumColumnWidth": min_width}
        grid_style_attr = f' style="--sr-grid-min:{min_width}"'
    if tag:
        attrs['tagName'] = tag
    if anchor:
        attrs['anchor'] = anchor
    tagname = tag or 'div'
    anchor_attr = f' id="{anchor}"' if anchor else ''
    class_attr = ' '.join(c for c in ['wp-block-group', f'is-layout-{layout_type}', classes] if c)
    return (f'<!-- wp:group{_attrs(attrs)} -->\n'
            f'<{tagname} class="{class_attr}"{anchor_attr}{grid_style_attr}>' + html + f'</{tagname}>\n'
            f'<!-- /wp:group -->\n')


def section(inner_html, classes='sr-section', anchor=None):
    attrs = {"tagName": "section", "className": classes,
             "layout": {"type": "constrained", "contentSize": "1240px"}}
    if anchor:
        attrs["anchor"] = anchor
    anchor_attr = f' id="{anchor}"' if anchor else ''
    return (f'<!-- wp:group{_attrs(attrs)} -->\n'
            f'<section class="wp-block-group is-layout-constrained {classes}"{anchor_attr}>' + inner_html + '</section>\n'
            f'<!-- /wp:group -->\n')


def raw_html(html):
    return f'<!-- wp:html -->\n{html}\n<!-- /wp:html -->\n'


PLACEHOLDER_IMG_SRC = '/wp-content/themes/remarka-studio/assets/img/placeholder-browser.svg'


def image(alt='', src=None):
    # src vuoto (`src=""`) non sopravvive a wp_insert_post() senza utente
    # loggato (wp_kses lo rimuove): serve un URL reale, anche per un
    # placeholder. Resta un vero blocco Immagine: sostituibile dal
    # proprietario del sito con lo screenshot reale via editor a blocchi.
    src = src or PLACEHOLDER_IMG_SRC
    return (f'<!-- wp:image {{"sizeSlug":"large"}} -->\n'
            f'<figure class="wp-block-image size-large"><img src="{src}" alt="{alt}"/></figure>\n'
            f'<!-- /wp:image -->\n')


def table(headers, rows):
    thead = '<tr>' + ''.join(f'<th>{h}</th>' for h in headers) + '</tr>'
    tbody = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in row) + '</tr>' for row in rows)
    return (f'<!-- wp:table -->\n'
            f'<figure class="wp-block-table"><table><thead>{thead}</thead><tbody>{tbody}</tbody></table></figure>\n'
            f'<!-- /wp:table -->\n')


def details_faq(items):
    """items: list of (question, answer)"""
    out = []
    for q, a in items:
        out.append(
            '<!-- wp:details -->\n'
            f'<details class="wp-block-details"><summary>{q}</summary>'
            f'<!-- wp:paragraph -->\n<p>{a}</p>\n<!-- /wp:paragraph --></details>\n'
            '<!-- /wp:details -->\n'
        )
    return ''.join(out)


def stat_block(value, label, desc='', color='oltremare', counter=False):
    counter_cls = ' sr-counter' if counter else ''
    color_style = 'var(--sr-oltremare-chiaro)' if color == 'chiaro' else (
        'var(--sr-verde)' if color == 'verde' else 'var(--sr-oltremare)')
    desc_html = f'<p style="margin-top:8px;font-size:15px;color:var(--sr-grigio)">{desc}</p>' if desc else ''
    inner = (
        f'<span class="sr-stat__num{counter_cls}" style="color:{color_style}">{value}</span>'
        f'<p style="margin-top:16px;font-weight:500">{label}</p>{desc_html}'
    )
    return raw_html(f'<div class="sr-stat">{inner}</div>')


def list_rows(items):
    """items: list of strings -> a) b) c)…"""
    letters = 'abcdefghijklmnopqrstuvwxyz'
    rows = ''.join(
        f'<div><span class="sr-mono">{letters[i]}</span><span>{text}</span></div>'
        for i, text in enumerate(items)
    )
    return raw_html(f'<div class="sr-list-rows">{rows}</div>')


def checklist(items):
    rows = ''.join(f'<div><span class="sr-mono">✓</span><span>{t}</span></div>' for t in items)
    return raw_html(f'<div class="sr-checklist">{rows}</div>')


def metric_rows(items):
    """items: list of (value, text)"""
    rows = ''.join(f'<div><span class="sr-mono">{v}</span><span>{t}</span></div>' for v, t in items)
    return raw_html(f'<div class="sr-metric-rows">{rows}</div>')


def browser_frame(url_label, alt_text, src=None):
    bar = (f'<div class="sr-browser__bar"><span class="sr-browser__dot"></span>'
           f'<span class="sr-browser__dot"></span><span class="sr-browser__dot"></span>'
           f'<span class="sr-browser__url">{url_label}</span></div>')
    return group(raw_html(bar) + image(alt_text, src=src), classes='sr-browser')


def case_screenshot_src(case_slug):
    """Мокап-скриншоты кейсов (сгенерированы Playwright'ом, лежат в теме).
    Владелец заменяет реальными через редактор блоков (кнопка «Sostituisci»)."""
    return f'/wp-content/themes/remarka-studio/assets/img/caso-{case_slug}.jpg'


def barra(target, delay=0, muted=False, height=10, aria_label=None):
    fill_cls = 'sr-barra__fill sr-barra__fill--muted' if muted else 'sr-barra__fill'
    aria = f' role="img" aria-label="{aria_label}"' if aria_label else ' aria-hidden="true"'
    return (f'<div class="sr-barra" style="height:{height}px" data-sr-target="{target}%" '
            f'data-sr-delay="{delay}"{aria}><div class="{fill_cls}"></div></div>')


def barra_row(label, value, target, delay=0, muted=False, verde_value=False, height=8):
    val_cls = 'sr-barra-row__val sr-barra-row__val--verde' if verde_value else 'sr-barra-row__val'
    row = (f'<div class="sr-barra-row"><span class="sr-eyebrow" style="margin:0">{label}</span>'
           f'<span class="{val_cls}">{value}</span></div>')
    return row + barra(target, delay=delay, muted=muted, height=height,
                        aria_label=f'{label}: {value} su 100')


def pull_quote(text, attribution):
    return raw_html(
        f'<blockquote class="sr-pull-quote"><p>«{text}»</p><cite>{attribution}</cite></blockquote>'
    )


def chapter(number_label, content_html):
    return raw_html(f'<div class="sr-chapter"><p class="sr-chapter__label">{number_label}</p>'
                     f'<div class="sr-chapter__content">') + content_html + raw_html('</div></div>')


def compare_table_row(label, values):
    cells = []
    for v in values:
        if v is True:
            cells.append('<td><span class="sr-yes">✓</span></td>')
        elif v is False:
            cells.append('<td><span class="sr-no">—</span></td>')
        else:
            cells.append(f'<td>{v}</td>')
    return f'<tr><td>{label}</td>' + ''.join(cells) + '</tr>'


def pattern_header(title, slug, description, viewport=1400, category='remarka'):
    return (f'<?php\n/**\n * Title: {title}\n * Slug: remarka-studio/{slug}\n'
            f' * Categories: {category}\n * Description: {description}\n'
            f' * Viewport Width: {viewport}\n */\n?>\n')
