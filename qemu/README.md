# qemuの検証環境（mac）

## qemuなどのインストール

```
brew install qemu
brew install mkfs.fat
```

## 検証した内容
### ゲストからホストOSにfd使って書き込めてしまう問題
ホストOSで以下のコマンドを実行し、VMを起動
```
sudo qemu-system-x86_64 -m 2G -enable-kvm -nographic \
  -drive file=data/ubuntu-20.04-server-cloudimg-amd64.img,format=qcow2 \
  -fda fd0.img
```
ゲストにログインして以下のコマンドで、fd0に書き込む
```
sudo mount /dev/fd0 /mnt
sudo touch /mnt/a.txt
sudo umount /mnt
```

この問題への対処策としてはfd0をreadonlyの状態で起動すること。具体的には以下のようなパラメータでvmをあげると良い

```

qemu-system-x86_64 -m 2G -nographic \
  -drive file=ubuntu20.04-cloudimg.img,format=qcow2 \
  -drive file=fd0.img,index=0,if=floppy,readonly
```
