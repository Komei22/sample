#!/usr/local/bin/perl

use strict;
use YAML::Tiny;
use Data::Dumper;

my $yaml = '#cloud-config
hostname: foo
password: hoge
ssh_pwauth: True
chpasswd:
    expire: False
';

my $data = YAML::Tiny->new;
$data = YAML::Tiny->read_string($yaml);
print $yaml;
print Dumper($data);

print $data->[0]->{password};
