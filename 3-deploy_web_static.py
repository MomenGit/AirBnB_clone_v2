#!/usr/bin/python3
"""Defines the function deploy"""
from fabric.api import env, put, local, run
from os.path import exists
from datetime import datetime

env.hosts = ['100.26.235.86	', '100.26.153.227']


def do_pack():
    """
    generates a .tgz archive from the contents of the web_static folder
    of your AirBnB Clone repo
    """
    local("mkdir -p versions")
    file_path = "versions/web_static_{}.tgz".format(
        datetime.utcnow().strftime("%Y%m%d%H%M%S"))
    tgz_file = local(
        "tar -cvzf {} ./web_static".format(file_path), capture=True)
    if tgz_file.failed:
        return None
    else:
        return file_path


def do_deploy(archive_path):
    """Distributes an archive to hosting web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split('/')[-1]
        version_name = file_name.split('.')[0]
        version_path = "/data/web_static/releases/{}".format(version_name)
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(version_path))
        run("tar -xzf /tmp/{} -C {}/".format(file_name, version_path))
        run("rm /tmp/{}".format(file_name))
        run("mv {0}/web_static/* {0}/".format(version_path))
        run("rm -rf {}/web_static".format(version_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(version_path))
        return True
    except Exception as e:
        return False


def deploy():
    """Creates and distributes an archive to hosting web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    op = do_deploy(archive_path)
    return op
