from devops import cmd

class Go(object):
    def install(self):
        cmd.run("ls")
        cmd.run("pwd")
        cmd.run("echo 123")

        print("install")
