#!/bin/bash

sudo apt-get update
# metadata userdataの作成に使うツール
sudo apt-get install -y cloud-image-utils
# qemu関連ツールのインストール
sudo apt-get install -y qemu-kvm qemu-utils ovmf

# ubuntu20.04イメージの取得
wget https://cloud-images.ubuntu.com/releases/20.04/release/ubuntu-20.04-server-cloudimg-amd64.img /home/vagrant/data/ubuntu-20.04-server-cloudimg-amd64.img
