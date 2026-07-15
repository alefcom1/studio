<!--
Bundled third-party PDF stack for the check-up report (M3). All packages are
LGPL/MIT/BSD-style permissive licenses; each subdirectory keeps its own
LICENSE file from upstream. Pinned via Composer against packagist.org on
2026-07-15, then trimmed by hand (tests/, docs/, unused thecodingmachine/safe
generated functions, and dompdf's own bundled core fonts beyond the 3 DejaVu
files this theme needs removed) — see autoload.php for the replacement
autoloader that replaces vendor/composer's generated one.
-->

# Bundled PDF library versions

| Package | Version | License | Namespace |
|---|---|---|---|
| dompdf/dompdf | v3.1.5 | LGPL-2.1 | `Dompdf\` |
| dompdf/php-font-lib | 1.0.2 | LGPL-3.0 | `FontLib\` |
| dompdf/php-svg-lib | 1.0.2 | MIT | `Svg\` |
| masterminds/html5 | 2.10.1 | MIT | `Masterminds\` |
| sabberworm/php-css-parser | v9.4.0 | MIT | `Sabberworm\CSS\` |
| thecodingmachine/safe (trimmed) | v3.4.0 | MIT | `Safe\` |

Fonts: `dompdf/lib/fonts/DejaVuSans.ttf`, `DejaVuSans-Bold.ttf`,
`DejaVuSansMono.ttf` (Bitstream Vera / DejaVu license, embedded — Cyrillic
coverage). Registered at render time in `inc/checkup-report-pdf.php` into a
writable font-cache directory under `wp_upload_dir()`, because dompdf's
`FontMetrics::registerFont()` needs to write there; the theme's own copy of
the .ttf files stays read-only.

`safe/` keeps only the 4 function files (`iconv`, `pcre`, `classobj`,
`special_cases`) and 4 exception classes that
`sabberworm/php-css-parser` actually calls (`Safe\iconv`, `Safe\preg_match`,
`Safe\preg_match_all`, `Safe\preg_replace`, `Safe\preg_split`,
`Safe\class_alias`) — trimmed from ~80 upstream files covering extensions
this project never touches (curl, ldap, gmp, …).
