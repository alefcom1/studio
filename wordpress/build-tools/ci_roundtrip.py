#!/usr/bin/env python3
"""CI round-trip: перегенерировать репрезентативный набор страниц и убедиться,
что вывод генератора совпадает с закоммиченными паттернами.

Ловит главную граблю проекта: кто-то поправил сгенерированную страницу в
patterns/** руками вместо data.py + генератора. После этого скрипта CI делает
`git diff --exit-code -- wordpress/remarka-studio/patterns`: если появился дифф,
значит рассинхрон — сборка красная.

Специально НЕ вызывает main() generate_pages.py (он регенерирует всё и плодит
strays — запрещён правилами проекта). Только точечные, самодостаточные билдеры,
которые не создают лишних файлов.
"""
import os
import sys

# Генератор пишет файлы по путям относительно каталога build-tools.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import generate_pages as g  # noqa: E402
import data  # noqa: E402


def main() -> int:
    # Индексные страницы — самодостаточны, без побочных файлов.
    g.build_strumenti_index()
    g.build_blog_index()

    # Одна флагманская городская страница (офисный бранч) — покрывает
    # build_city_flagship, самый сложный билдер.
    roma = next((c for c in data.CITIES if c.get('slug') == 'roma'), None)
    if roma is not None:
        g.build_city_flagship(roma)

    print('round-trip: перегенерированы strumenti-index, blog-index, citta-roma')
    return 0


if __name__ == '__main__':
    sys.exit(main())
