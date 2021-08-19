sudo qemu-system-x86_64 -m 2G -enable-kvm -nographic \
  -drive file=data/ubuntu-20.04-server-cloudimg-amd64.img,format=qcow2 \
  -fda fd0.img
