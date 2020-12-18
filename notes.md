
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

