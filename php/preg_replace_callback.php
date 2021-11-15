<?php

$s="hoge\\nfuga";

$s_rep=preg_replace_callback('/\\\\(.)/', function($o){print_r($o); return $o[0];}, $s);
print_r($s_rep);
