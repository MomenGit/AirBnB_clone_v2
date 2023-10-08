#!/usr/bin/python3
"""Defines the function do_deploy"""
from fabric.api import env, put, sudo
from os.path import exists

# env.hosts = ['100.26.235.86', '100.26.153.227']
# env.user = "ubuntu"
# env.key = "~/.ssh/id_rsa_alx"


def do_deploy(archive_path):
    """Distributes an archive to hosting web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split('/')[-1]
        version_name = file_name.split('.')[0]
        version_path = "/data/web_static/releases/{}/".format(version_name)
        put(archive_path, "/tmp/")
        sudo("mkdir -p {}".format(version_path))
        sudo("tar -xzf /tmp/{} -C {}/".format(file_name, version_path))
        sudo("rm /tmp/{}".format(file_name))
        sudo("mv {0}web_static/* {0}".format(version_path))
        sudo("rm -rf {}web_static".format(version_path))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s {} /data/web_static/current".format(version_path))
        print("New version deployed!")
        return True
    except Exception as e:
        return False
