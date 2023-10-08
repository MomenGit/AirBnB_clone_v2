#!/usr/bin/python3
"""Defines the function do_clean"""
from fabric.api import env, put, local, sudo
from os.path import exists
from datetime import datetime

env.hosts = ['100.26.235.86', '100.26.153.227']


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
        sudo("mkdir -p {}".format(version_path))
        sudo("tar -xzf /tmp/{} -C {}/".format(file_name, version_path))
        sudo("rm /tmp/{}".format(file_name))
        sudo("mv {0}/web_static/* {0}/".format(version_path))
        sudo("rm -rf {}/web_static".format(version_path))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s {}/ /data/web_static/current".format(version_path))
        print("New version deployed!")
        return True
    except Exception as e:
        return False


archive_path = do_pack()


def deploy():
    """Creates and distributes an archive to hosting web servers"""
    if archive_path is None:
        return False
    op = do_deploy(archive_path)
    return op


def do_clean_local(number=0):
    """Deletes out-of-date archives"""
    if number == 0:
        number = 1
    else:
        number = int(number)
    archives = local("ls ./versions", capture=True)
    archives = archives.split("\n")
    archives_length = len(archives) - number
    for i in range(archives_length):
        local("rm ./versions/{}".format(archives[i]))


def do_clean_remote(number=0):
    """Deletes out-of-date versions"""
    if number == 0:
        number = 1
    else:
        number = int(number)
    versions = sudo("ls /data/web_static/releases")
    versions = versions.split("  ")
    versions_length = len(versions) - number
    for i in range(versions_length):
        sudo("rm -rf /data/web_static/releases/{}".format(versions[i]))


def do_clean(number=0):
    """Deletes out-of-date archives and out-of-date versions"""
    do_clean_local(number=number)
    do_clean_remote(number=number)
