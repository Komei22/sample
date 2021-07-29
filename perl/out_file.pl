
my $file = './hoge/a.txt';
my $txt = 'hoge';
open my $fh, '>', $file;
print $fh $txt;
close $fh
