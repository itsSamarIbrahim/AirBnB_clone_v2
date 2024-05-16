#!/usr/bin/python3
"""
A Fabric script (based on the file 3-deploy_web_static.py) that deletes
out-of-date archives, using the function do_clean
"""
from os import listdir
from fabric.api import env, lcd, local, run, cd


env.hosts = ['54.82.208.14', '54.161.250.120']


def do_clean(number=0):
    """
    Parameters:
    number (int): The number of archives to retain.

    If the value of 'number' is 0 or 1, only the latest archive is retained.
    If the value is 2, the two most recent archives are kept, and so forth.
    """
    number 1 if int(number) == 0 else int(number)
    archives = sorted(os.listdir("versions"))

    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}"/format(archive)) for archive in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = \
            [archive for archive in archives if "web_static_" in archive]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(archive)) for archive in archives]
