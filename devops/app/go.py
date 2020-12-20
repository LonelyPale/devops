import sys
import devops
from devops import cmd
from devops.core import lonely

class Go(object):
    def install(self):
        if devops.os != "linux" or devops.os != "darwin":
            print("Unsupported os: %s" % devops.os)
            sys.exit(1)
        
        archs = {"x86_64":"amd64", "aarch64":"arm64"}
        if devops.arch not in archs:
            print("Unsupported arch: %s" % devops.arch)
            sys.exit(1)
        
        if cmd.cmd("go version").returncode == 0:
            print("go has been installed, please delete it first.")
            sys.exit(1)

        version = "1.15.6"
        go_file_name = "go%s.linux-%s.tar.gz" % (version, devops.arch)
        go_file = lonely.temp + "/" + go_file_name
        url = "https://golang.google.cn/dl/" + go_file_name
        lonely.mkdir()
        cmd.run([
            "wget -O %s %s" % (go_file, url),
            "tar -C %s -xzf %s" % (lonely.home, go_file),
        ], multi_command=True)
        self.env_add()
    
    def env_add(self):
        pass
