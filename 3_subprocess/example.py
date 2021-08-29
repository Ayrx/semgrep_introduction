import subprocess

def foo(s):
    subprocess.run(s, shell=True, check=True)

    subprocess.run(s, check=True, shell=True)
