#!/usr/local/bin/perl
use JSON;
use Encode;

# my $meta_data_hash = {'instance-id'=> 1};
# my $meta_data_json = decode('utf-8', encode_json($meta_data_hash));
my $meta_data_json = decode('utf-8', encode_json({'instance-id' => 1}));
print $meta_data_json;

