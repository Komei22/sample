# injection されるパターン
my $a = '$6$6aaa';
print `
echo "$a";
`;

# injectionされないパターン
my $a = '$6$6aaa';
print `
echo '$a';
`;

