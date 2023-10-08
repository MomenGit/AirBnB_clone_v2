#!/usr/bin/python3
"""Defines the function do_clean"""
from fabric.api import sudo, local, env

env.hosts = ['100.26.235.86', '100.26.153.227']


def do_clean(number=0):
    """Deletes out-of-date archives"""
    if number == 0:
        number = 1
    else:
        number = int(number)

    archives = local("ls ./versions", capture=True)
    archives = archives.split("\n")
    for i in range(len(archives) - number):
        local("rm ./versions/{}".format(archives[i]))

    versions = sudo("ls /data/web_static/releases")
    versions = versions.split("  ")
    for i in range(len(versions) - number):
        sudo("rm -rf /data/web_static/releases/{}".format(versions[i]))
