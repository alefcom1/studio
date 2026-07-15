<?php
/**
 * Minimal PSR-4 autoloader for the bundled dompdf stack, replacing
 * Composer's generated autoloader so the theme ships only the files that
 * `inc/checkup-report-pdf.php` actually uses instead of a full vendor/ tree
 * (no tests, no dev tooling, no unused thecodingmachine/safe functions).
 * See VERSIONS.md in this directory for exact pinned versions and licenses.
 */

if ( defined( 'REMARKA_DOMPDF_AUTOLOAD_LOADED' ) ) {
	return;
}
define( 'REMARKA_DOMPDF_AUTOLOAD_LOADED', true );

$remarka_dompdf_lib_dir = __DIR__;

$remarka_dompdf_prefixes = array(
	'Dompdf\\'           => $remarka_dompdf_lib_dir . '/dompdf/src/',
	'FontLib\\'          => $remarka_dompdf_lib_dir . '/php-font-lib/src/FontLib/',
	'Svg\\'              => $remarka_dompdf_lib_dir . '/php-svg-lib/src/Svg/',
	'Masterminds\\'      => $remarka_dompdf_lib_dir . '/html5/src/',
	'Sabberworm\\CSS\\'  => $remarka_dompdf_lib_dir . '/css-parser/src/',
	'Safe\\Exceptions\\' => $remarka_dompdf_lib_dir . '/safe/exceptions/',
);

spl_autoload_register(
	function ( $class ) use ( $remarka_dompdf_lib_dir, $remarka_dompdf_prefixes ) {
		// Cpdf.php lives outside src/, in dompdf's own lib/ (Composer classmap
		// entry in the upstream package, replicated here by hand).
		if ( 'Dompdf\\Cpdf' === $class ) {
			require $remarka_dompdf_lib_dir . '/dompdf/lib/Cpdf.php';
			return;
		}
		foreach ( $remarka_dompdf_prefixes as $prefix => $base_dir ) {
			if ( 0 !== strpos( $class, $prefix ) ) {
				continue;
			}
			$relative = substr( $class, strlen( $prefix ) );
			$file     = $base_dir . str_replace( '\\', '/', $relative ) . '.php';
			if ( is_file( $file ) ) {
				require $file;
				return;
			}
		}
	}
);

// thecodingmachine/safe: PHP functions cannot be autoloaded, so the handful
// that sabberworm/php-css-parser actually calls (iconv, preg_*, class_alias)
// are required eagerly. Trimmed from ~80 upstream files to the 4 used.
require_once $remarka_dompdf_lib_dir . '/safe/functions/iconv.php';
require_once $remarka_dompdf_lib_dir . '/safe/functions/pcre.php';
require_once $remarka_dompdf_lib_dir . '/safe/functions/classobj.php';
require_once $remarka_dompdf_lib_dir . '/safe/functions/special_cases.php';
