import platform
from devops import core

os = platform.system().lower()
arch = platform.machine().lower()
release = core.lsb_release()
