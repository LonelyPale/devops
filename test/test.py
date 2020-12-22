#!/usr/bin/python3
 
#sites = ["Baidu", "Google","Runoob","Taobao"]
sites = []
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

#exec(open("/Users/wyb/.bash_profile").read())
import os, sys
os.environ['a1'] = 'a'*10
os.environ.update(os.environ)
print(os.environ['a1'])

import subprocess
# subprocess.run(". /tmp/test.sh", executable="/bin/sh")
#subprocess.run(". /tmp/test.sh")

os.execl('/bin/bash', '/bin/bash', '/tmp/test.sh', '&& echo $$')
