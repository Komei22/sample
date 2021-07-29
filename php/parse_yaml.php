<?php

$yaml = '#cloud-config
hostname: foo
password: hoge
ssh_pwauth: True
chpasswd:
    expire: False
';

$user_data = yaml_parse($yaml);

var_dump($yaml);
var_dump($user_data);
