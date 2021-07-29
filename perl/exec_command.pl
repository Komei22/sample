#!/usr/local/bin/perl

# execution commandのテスト
my $path="piyo";
# my $cmd = "
# echo \"$path/hoge\"
# echo \"hoge\"
# ";

my $cmd = "
date
echo 'waiting'
# sleep 5
date
";

$_ = `$cmd`;

# print "\n--------exec command------------\n".$cmd;
# print "--------stdout------------\n";
# print $out;
# print "--------\$?------------\n";
# print $?;

# ----------------------------------------------------
# if文のテスト
# if (! -f "./a" || ! -f "./b") {
	# die "Fail create cloud-init data";
# }

# my $our2 = `
# curl -l
# `;
# print $?
