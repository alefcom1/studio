#!/usr/bin/env python3
"""Механический транслятор сгенерированных страниц IT → EN/RU.

Принцип: сгенерированные patterns/pages/*.php — единственный источник.
Для каждого файла:
  1) все hrefs локализуются по карте слагов (lang.py) — детерминированно;
  2) каждый ЦЕЛЬНЫЙ текстовый узел (между > и <) и значения видимых
     атрибутов (alt/aria-label/placeholder) заменяются по словарю
     it→lang, собранному из corpus_it.json + corpus_{lang}.json
     (переводы агентов) + CHROME (шаблонная микро-копия, переведена
     редактором) — замена только целиком, подстроки не трогаются;
  3) PHP-шапка: Title/Description переводятся, Slug получает префикс.

Все непереведённые узлы с итальянским текстом попадают в отчёт —
конвейер не даёт «тихих» пропусков.

Запуск: python3 translate_pages.py en|ru
Выход:  patterns/pages/{lang}-*.php + отчёт в stdout.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
import lang as L  # noqa: E402
from chrome_strings import CHROME  # noqa: E402

# Параметрические шаблоны генератора (составные строки с числами/именами).
PARAM_PATTERNS = {
    'en': [
        (re.compile(r'Prima: (\d+) su 100'), r'Before: \1 out of 100'),
        (re.compile(r'Dopo: (\d+) su 100'), r'After: \1 out of 100'),
        (re.compile(r'Screenshot del sito (.+)'), r'Screenshot of the \1 website'),
    ],
    'ru': [
        (re.compile(r'Prima: (\d+) su 100'), r'До: \1 из 100'),
        (re.compile(r'Dopo: (\d+) su 100'), r'После: \1 из 100'),
        (re.compile(r'Screenshot del sito (.+)'), r'Скриншот сайта \1'),
    ],
}

BASE = os.path.dirname(os.path.abspath(__file__))
PAGES = os.path.join(BASE, '..', 'remarka-studio', 'patterns', 'pages')
SCRATCH = os.path.join(BASE, 'i18n')

# Городские лендинги кроме Milano не переводим (piano-contenuti-seo §2).
SKIP = {'citta-monza', 'citta-bergamo', 'citta-brescia', 'citta-como'}


def collect_pairs(it_node, tr_node, out):
    """Рекурсивно собирает (it_string → translated_string) из двух
    структурно-идентичных JSON."""
    if isinstance(it_node, dict):
        for k in it_node:
            collect_pairs(it_node[k], tr_node[k], out)
    elif isinstance(it_node, (list, tuple)):
        for a, b in zip(it_node, tr_node):
            collect_pairs(a, b, out)
    elif isinstance(it_node, str) and isinstance(tr_node, str):
        it_s, tr_s = it_node.strip(), tr_node.strip()
        if it_s and it_s != tr_s:
            out[it_s] = tr_s


def build_dictionary(lang_code):
    with open(f'{SCRATCH}/corpus_it.json', encoding='utf-8') as f:
        it = json.load(f)
    with open(f'{SCRATCH}/corpus_{lang_code}.json', encoding='utf-8') as f:
        tr = json.load(f)
    d = {}
    collect_pairs(it, tr, d)
    for it_s, langs in CHROME.items():
        if langs.get(lang_code):
            d[it_s.strip()] = langs[lang_code]
    return d


def build_href_map(lang_code):
    """IT href → локализованный. Длинные пути первыми (детальные раньше
    секций), чтобы не съедать префиксы."""
    m = {}
    for it_slug in L.SERVICES_SLUGS:
        m[f'/servizi/{it_slug}/'] = L.paths_for(lang_code)['servizio'](it_slug)
    for it_slug in L.CASES_SLUGS:
        m[f'/casi-studio/{it_slug}/'] = L.paths_for(lang_code)['caso'](it_slug)
    for it_slug in L.TOOLS_SLUGS:
        m[f'/strumenti/{it_slug}/'] = L.paths_for(lang_code)['strumento'](it_slug)
    for it_slug in L.BLOG_SLUGS:
        m[f'/blog/{it_slug}/'] = L.paths_for(lang_code)['articolo'](it_slug)
    p = L.paths_for(lang_code)
    m['/servizi/'] = p['servizi']
    m['/casi-studio/'] = p['casi']
    m['/strumenti/'] = p['strumenti']
    m['/blog/'] = p['blog']
    m['/prezzi/'] = p['prezzi']
    m['/#contatti'] = p['contatti']
    for it_slug in L.SINGLES:
        if it_slug != 'prezzi':
            m[f'/{it_slug}/'] = f"/{lang_code}/{L.slug_for('single', it_slug, lang_code)}/"
    return dict(sorted(m.items(), key=lambda kv: -len(kv[0])))


TEXT_NODE = re.compile(r'>([^<>]+)<')
# alt/aria-label/placeholder: attributi visibili classici. data-verdict-*/
# data-label-*/data-err/data-audits-empty/data-caption*: stringhe dei widget
# strumenti (Remarka Lab, vedi contratto in assets/js/remarka.js prima di
# toolLocale()) — ogni pagina per-lingua porta le proprie in data-*, il JS le
# legge a runtime. data-sr-locale NON è qui: è un codice lingua tecnico,
# sostituito a parte (deterministico, non passa dal dizionario).
ATTRS = re.compile(
    r'\b(alt|aria-label|placeholder|data-verdict-[a-z0-9]+|data-label-[a-z-]+|'
    r'data-word-[a-z0-9]+|data-composite-[a-z0-9]+|data-calc-note|data-na-text|'
    r'data-ai-suffix|'
    r'data-err|data-audits-empty|data-caption[a-z-]*)="([^"]+)"'
)
SR_LOCALE = re.compile(r'data-sr-locale="it"')
HEADER_LINE = re.compile(r'^( \* (?:Title|Description): )(.+)$', re.M)

# Явно нетекстовые узлы: цифры, пунктуация, домены, метки-цифры.
NON_TEXT = re.compile(
    r'^[\d\s.,%€×+\-–—→←/():«»"\'’!?#…]*$|'
    r'^[a-z0-9.\-]+\.(it|com|biz|eu)$|^[a-z]$|^✓$|^★+$|^/0\d$'
)
# Эвристика «остался итальянский»: частотные итальянские слова.
ITALIAN_HINT = re.compile(
    r'\b(il|la|le|gli|dei|delle|della|del|che|per|con|una|un|non|più|sono|'
    r'è|sito|siti|nostro|vostro|ogni|anche|come|dopo|prima|senza|tutto|'
    r'settimane|mesi|giorno|prezzo|preventivo|richieste|consegna|pagine)\b',
    re.I,
)


def translate_file(path, d, href_map, lang_code, report):
    src = open(path, encoding='utf-8').read()

    for it_href, tr_href in href_map.items():
        src = src.replace(f'href="{it_href}"', f'href="{tr_href}"')

    quote_wrap = {'en': ('“', '”'), 'ru': ('«', '»')}[lang_code]

    def lookup(s):
        if s in d:
            return d[s]
        # Цитаты: генератор оборачивает строку корпуса в «…» — матчим
        # внутренность и заворачиваем в кавычки целевого языка.
        if s.startswith('«') and s.endswith('»'):
            inner = s[1:-1]
            if inner in d:
                return quote_wrap[0] + d[inner] + quote_wrap[1]
        # Параметрические шаблоны генератора.
        for pat, repl in PARAM_PATTERNS.get(lang_code, []):
            m2 = pat.fullmatch(s)
            if m2:
                return m2.expand(repl)
        return None

    def tr_text(m):
        raw = m.group(1)
        s = raw.strip()
        if not s or NON_TEXT.match(s):
            return m.group(0)
        tr = lookup(s)
        if tr is not None:
            return '>' + raw.replace(s, tr) + '<'
        if ITALIAN_HINT.search(s):
            report.append((os.path.basename(path), s))
        return m.group(0)

    src = TEXT_NODE.sub(tr_text, src)

    def tr_attr(m):
        s = m.group(2).strip()
        tr = lookup(s)
        if tr is not None:
            return f'{m.group(1)}="{tr}"'
        if s and not NON_TEXT.match(s) and ITALIAN_HINT.search(s):
            report.append((os.path.basename(path), f'[{m.group(1)}] {s}'))
        return m.group(0)

    src = ATTRS.sub(tr_attr, src)

    def tr_header(m):
        s = m.group(2).strip()
        return m.group(1) + d.get(s, s)

    src = HEADER_LINE.sub(tr_header, src)
    src = re.sub(r'( \* Slug: remarka-studio/)', rf'\g<1>{lang_code}-', src)

    # data-sr-locale="it" → codice lingua della pagina — deterministico,
    # fuori dal dizionario (non è testo editoriale, è l'API dei widget).
    src = SR_LOCALE.sub(f'data-sr-locale="{lang_code}"', src)

    if lang_code == 'en':
        # Американский формат чисел в видимом тексте: сначала десятичные
        # запятые → точки (1-2 цифры после), затем тысячные точки → запятые
        # (ровно 3 цифры после). Порядок важен; inline-стили не трогаем.
        def us_numbers(m):
            t = m.group(1)
            t = re.sub(r'(\d),(\d{1,2})(?!\d)', r'\1.\2', t)
            t = re.sub(r'(\d)\.(\d{3})(?!\d)', r'\1,\2', t)
            return '>' + t + '<'
        src = TEXT_NODE.sub(us_numbers, src)

        def us_numbers_attr(m):
            t = m.group(2)
            t = re.sub(r'(\d),(\d{1,2})(?!\d)', r'\1.\2', t)
            t = re.sub(r'(\d)\.(\d{3})(?!\d)', r'\1,\2', t)
            return f'{m.group(1)}="{t}"'
        src = ATTRS.sub(us_numbers_attr, src)
    return src


def main():
    lang_code = sys.argv[1]
    assert lang_code in ('en', 'ru')
    d = build_dictionary(lang_code)
    href_map = build_href_map(lang_code)
    report = []
    n = 0
    for fname in sorted(os.listdir(PAGES)):
        if not fname.endswith('.php') or fname.startswith(('en-', 'ru-')):
            continue
        slug = fname[:-4]
        if slug in SKIP:
            continue
        out = translate_file(os.path.join(PAGES, fname), d, href_map, lang_code, report)
        with open(os.path.join(PAGES, f'{lang_code}-{fname}'), 'w', encoding='utf-8') as f:
            f.write(out)
        n += 1
    print(f'{lang_code}: {n} файлов, словарь {len(d)} пар')
    if report:
        seen = set()
        print(f'\nНЕПЕРЕВЕДЕНО ({len(report)}):')
        for fn, s in report:
            key = s
            if key in seen:
                continue
            seen.add(key)
            print(f'  [{fn}] {s[:110]}')
        sys.exit(1)


if __name__ == '__main__':
    main()
