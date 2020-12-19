import sys
import devops
from devops import cmd

class Go(object):
    def install(self):
        if devops.os != "linux":
            print("Unsupported os: %s" % devops.os)
            sys.exit(1)
        
        archs = {"x86_64":"amd64", "aarch64":"arm64"}
        if devops.arch not in archs:
            print("Unsupported arch: %s" % devops.arch)
            sys.exit(1)

        version = "1.15.6"
        file = "go%s.linux-%s.tar.gz" % version,devops.arch
        url = "https://golang.google.cn/dl/" + file
        print(url)
