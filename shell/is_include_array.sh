#!/bin/bash



_is_include_target()
{
    target=$1

    array="aaa bbb ccc"
    for a in $array; do
        if [ "$target" = "$a" ]; then
            return 0
        fi
    done
    return 1
}

# ret=`_is_include_target "bb"`  #returnの値が入るのではなくechoの標準出力が入る
# echo $ret
_is_include_target "aaa"
if [ $? -eq 0 ] && [ "hoge" = "hoge" ]; then
    echo success
else
    echo fail
fi
