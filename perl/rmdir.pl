#!/usr/local/bin/perl
$tmp_dir = "tmp_dir";
mkdir($tmp_dir);

print "mkdir $tmp_dir\n";

open FH, ">$tmp_dir/tmp";
print FH "tmp";
close FH;


print "touch $tmp_dir/tmp\n";

# rmdirは削除対象のディレクトリにパーミッションがない or ファイルが存在する場合は削除が失敗する
rmdir($tmp_dir) or die "$tmp_dir を削除できません";
