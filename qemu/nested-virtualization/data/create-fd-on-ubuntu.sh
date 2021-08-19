#!/bin/bash
# $HOMEで実行する

mkdir fd0
dd of=fd0.img if=/dev/zero bs=1KiB count=1440
mkfs.fat -n CIDATA fd0.img
sudo mount -o loop fd0.img fd0
sudo cp meta-data user-data fd0
sudo umount fd0
