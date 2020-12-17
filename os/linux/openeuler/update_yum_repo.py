#!/usr/bin/python3

import sys
import platform
import subprocess

def cmd(command):
    ret = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8", timeout=10)
    if len(ret.stdout) > 0:
        print(ret.stdout)
    if len(ret.stderr) > 0:
        print(ret.stderr)
    return ret

def lsb_release():
    ret = cmd("cat /etc/openEuler-release")
    if ret.returncode == 0:
        #print("success:", ret)
        if ret.stdout.lower().find("openeuler") > -1:
            return "openeuler"
        else:
            return "unknown"
    else:
        #print("failure:", ret)
        return "unknown"

def update_yum_repo():
    sys_os = platform.system().lower()
    sys_arch = platform.machine().lower()
    sys_release = lsb_release()

    if sys_os != "linux":
        print("Unsupported os: %s" % sys_os)
        return False
    
    if sys_arch != "x86_64" and sys_arch != "aarch64":
        print("Unsupported arch: %s" % sys_arch)
        return False
    
    if sys_release != "openeuler":
        print("Unsupported release: %s" % sys_release)
        return False
    
    url = ""
    if sys_arch == "x86_64":
        url = "https://repo.huaweicloud.com/repository/conf/openeuler_x86_64.repo"
    elif sys_arch == "aarch64":
        url = "https://repo.huaweicloud.com/repository/conf/openeuler_aarch64.repo"
    
    # todo: optimization
    cmd("wget -O /etc/yum.repos.d/openEulerOS.repo %s" % url)
    cmd("yum clean all")
    cmd("yum makecache")

    return True

if __name__ == '__main__':
    if update_yum_repo():
        sys.exit(0)
    else:
        sys.exit(1)
