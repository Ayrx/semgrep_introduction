import os

def foo(s):
    os.system("ls -lah")

    os.system(s)

    cmd = "whoami"
    os.system(cmd)

    os.popen(s)
