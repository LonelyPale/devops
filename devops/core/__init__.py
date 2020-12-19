from devops import cmd

def lsb_release():
    ret = cmd.run("cat /etc/openEuler-release")
    if ret.returncode == 0:
        #print("success:", ret)
        if ret.stdout.lower().find("openeuler") > -1:
            return "openeuler"
        else:
            return "unknown"
    else:
        #print("failure:", ret)
        return "unknown"
