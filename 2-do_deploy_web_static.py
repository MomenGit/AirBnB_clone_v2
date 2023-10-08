#!/usr/bin/python3
"""Defines the function do_deploy"""
from fabric.api import env, put, run, local, sudo
from os.path import exists

env.hosts = ['100.26.235.86	', '100.26.153.227']


def do_deploy(archive_path):
    """Distributes an archive to hosting web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split('/')[-1]
        version_name = file_name.split('.')[0]
        version_path = "/data/web_static/releases/{}/".format(version_name)
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(version_path))
        run("tar -xzf /tmp/{} -C {}/".format(file_name, version_path))
        run("rm /tmp/{}".format(file_name))
        run("mv {0}web_static/* {0}".format(version_path))
        run("rm -rf {}web_static".format(version_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(version_path))
        return True
    except Exception as e:
        return False
