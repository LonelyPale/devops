import sys
import devops
from devops import cmd

class YumRepo:
    def install(self):
            if devops.os != "linux":
                print("Unsupported os: %s" % devops.os)
                sys.exit(1)
            
            if devops.arch != "x86_64" and devops.arch != "aarch64":
                print("Unsupported arch: %s" % devops.arch)
                sys.exit(1)
            
            if devops.release != "openeuler":
                print("Unsupported release: %s" % devops.release)
                sys.exit(1)
            
            url = ""
            if devops.arch == "x86_64":
                url = "https://repo.huaweicloud.com/repository/conf/openeuler_x86_64.repo"
            elif devops.arch == "aarch64":
                url = "https://repo.huaweicloud.com/repository/conf/openeuler_aarch64.repo"
            
            # todo: optimization
            cmd.run([
                "wget -O /etc/yum.repos.d/openEulerOS.repo %s" % url,
                "yum clean all",
                "yum makecache",
            ], multi_command=True)
