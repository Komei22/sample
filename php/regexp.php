<?php

// $s = "required heredoc maxlen=1000 blog_desc \"説明\" ex=\"hoge\\nfuga\"";
$s = "required heredoc maxlen=1000 blog_desc \"説明\" default=\"hoge\\nfuga\"\\tpiyo\\n\"";
// $s = "required heredoc maxlen=1000 blog_desc \"説明\" ex=\"hoge\\\\fuga\"";  // バックスラッシュを打ちたいパターン
$s_trim = trim($s);

preg_match_all('/(\\\\.|"(\\.|[^"])*"|\'(\\.|[^\'])*\'|\\S)+/', $s_trim, $m);
// print_r($m);

$args = [];
foreach ($m[0] as $l) {
    print_r($l);
    $args[] = preg_replace_callback(
        '/(\\\\(.)|"((\\.|[^"])*)"|\'((\\.|[^\'])*)\')/',
        function ($n) {
            print("\n------------\n");
            print_r($n);
            switch (substr($n[0],0,1)) {
                case '\\': return $n[2];
                case '"':
                    // print_r($n[3] . "\n");
                    $tmp = preg_replace_callback('/\\\\(.)/', function($o){print_r($o); return $o[0];}, $n[3]);
                    // print_r($tmp);
                    return $tmp;
                case "'": return preg_replace_callback('/\\\\(.)/', function($o){return $o[1];}, $n[5]);
            }
            print_r($n[0]);
            return $n[0];
        },
        $l
    );
}

print("\n===============================\n");
print_r($args);
print("\n===============================\n");
echo($args[5]);
