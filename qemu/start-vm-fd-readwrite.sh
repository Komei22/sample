qemu-system-x86_64 -m 2G -nographic \
  -drive file=ubuntu20.04-cloudimg.img,format=qcow2 \
  -fda fd0.img
