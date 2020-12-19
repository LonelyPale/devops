import sys
import subprocess

def run(command, exit_code=True, multi_command=False):
    if multi_command and (isinstance(command, tuple) or isinstance(command, list)):
        rets = []
        for c in command:
            rets.append(cmd(c, exit_code))
        return rets
    else:
        return cmd(command, exit_code)

def cmd(command, exit_code=False):
    ret = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8", timeout=10)
    if len(ret.stdout) > 0:
        print(ret.stdout)
    if len(ret.stderr) > 0:
        print(ret.stderr)
    if exit_code and ret.returncode != 0:
        sys.exit(1)
    return ret
