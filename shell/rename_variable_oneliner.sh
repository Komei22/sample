rg -I -o "rem\(\d+" | sort | uniq | sed "s/(/ /g" | awk '{print $1"("$2")/"($2 / 16)"rem"}' | xargs -I@ sed "s/@/g" case/*.txt
