<?php

$s = "hoge\\nfuga\\t\"piyo\\n";

// $s_rep=preg_replace_callback('/\\\\(.)/', function($o){return "\\$o[1]";}, $s);
$s_rep=preg_replace_callback('/\\\\(.)/', 'replace_control_code', $s);

print_r($s_rep);

function replace_control_code($m) {
    print_r($m);
    switch ($m[0]) {
        case '\\n':
            return "\n";
        case '\\t':
            return "\t";
        default:
            return $m[0];
    }
}
