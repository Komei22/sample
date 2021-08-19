dd of=fd0.img if=/dev/zero bs=1k count1440

hdiutil mount -mountpoint fd0 fd0.img

touch fd0/meta-data
cat << EOS > fd0/user-data
#cloud-config
hostname: "hoge"
password: "fuga"
EOS

hdiutil unmount fd0
