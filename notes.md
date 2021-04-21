# 2021-04-21
docker pull bytom/bytom
docker run -v $HOME/.bytom:/root/.bytom bytom/bytom:latest bytomd init --chain_id=solonet
docker run -d --net=host --log-opt max-size=50m --name=bytomd -v $HOME/.bytom:/root/.bytom bytom/bytom:latest bytomd node --auth.disable
curl localhost:9888/net-info

# old
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

curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
/bin/zsh -c "$(curl -fsSL https://gitee.com/cunkai/HomebrewCN/raw/master/Homebrew.sh)"
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)

https://raw.githubusercontent.com/LonelyPale/devops/main/test/test.py
https://151.101.108.133/LonelyPale/devops/main/test/test.py
https://199.232.96.133/LonelyPale/devops/main/test/test.py

curl --proto '=https' --tlsv1.2 -sSf https://raw.githubusercontent.com/LonelyPale/devops/main/test/test.py
curl -fsSL https://raw.githubusercontent.com/LonelyPale/devops/main/test/test.py

curl http://39.104.181.232/test/test.py
curl http://39.104.181.232/test/test.py | python3
python3 -c "$(curl http://39.104.181.232/test/test.py)"

vscode://vscode.github-authentication/did-authenticate?windowid=1&code=2d724ddf23a6f4c9cbdc&state=903bc6cb-746b-4227-a13c-3749c540bbf9


GET /LonelyPale/devops/main/test/test.py HTTP/1.1
Host: raw.githubusercontent.com
Connection: keep-alive
Cache-Control: max-age=0
sec-ch-ua: "Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"
sec-ch-ua-mobile: ?0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,ja;q=0.8
If-None-Match: W/"1214f6ea6fc8e042b9d626392d5e1c9be2f15ebe9f55117427f44ed35714cd08"


