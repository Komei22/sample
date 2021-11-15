<?php

$yaml = '#cloud-config
hostname: foo
password: hoge
ssh_pwauth: True
chpasswd:
    expire: False
';

$yaml_abnormal = '#cloud-config
hostname: foopassword: hoge
ssh_pwauth: True
chpasswd:
    expire: False
';

$parsed_yaml = yaml_parse($yaml);

// var_dump($yaml);
var_dump($parsed_yaml);

if ($parsed_yaml == false) {
    var_dump("parse error");
}
