
https://mirrors.huaweicloud.com/centos-altarch/7.9.2009/os/aarch64/Packages/firefox-68.10.0-1.el7.centos.aarch64.rpm

http://down.360safe.com/gc/browser360-cn-stable-10.4.1002.18-1.aarch64.rpm
http://down.360safe.com/gc/browser360-cn-stable-12.2.1070.0-1.aarch64.rpm

rpm  -ivh  google-chrome-stable_current_x86_64.rpm

sudo tar -C /usr/local/ -xzvf go1.15.6.linux-arm64.tar.gz
wget https://golang.google.cn/dl/go1.15.6.linux-arm64.tar.gz


export GOROOT=/usr/local/go
export GOPATH=/home/bruce/goProject 
export GOBIN=$GOPATH/bin
export PATH=$PATH:$GOROOT/bin
export PATH=$PATH:$GOPATH/bin

https://golang.google.cn/dl/
https://www.jianshu.com/p/33cf4f41cae9


federation.json
{
  "xpubs": [
    "937c478106e20dbbc2e22ee418733754dc8a9af6c227eab374ff3f48b574a23273a98400b8bc9dcd36276bf266e0f5a71b0a6420dc35b2ba534e9250013471c1"
  ],
  "quorum": 1
}


node_key.txt
c81af7000109871b49020fa8bdada0e463f8186573b508a8606c46895f710c50a60a9d422684b0db8dfe8e3573bb5b5659acdc0a4a722fca73fccd87bc3e9ec2


