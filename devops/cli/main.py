#!/usr/bin/python3

import sys
import fire

from devops.app.go import Go
from devops.app.yum_repo import YumRepo

class Pipeline(object):
    def __init__(self):
        self.go = Go()
        self.yum_repo = YumRepo()

def main():
    fire.Fire(Pipeline)

if __name__ == '__main__':
    main()
