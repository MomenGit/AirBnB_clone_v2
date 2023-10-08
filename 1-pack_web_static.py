#!/usr/bin/python3
"""Define the function do_pack"""
from fabric import api
from datetime import datetime


def do_pack():
    """
    generates a .tgz archive from the contents of the web_static folder
    of your AirBnB Clone repo
    """
    api.local("mkdir versions")
    file_path = "versions/web_static_{}.tar".format(
        datetime.utcnow().strftime("%Y%m%d%H%M%S"))
    tar_file = api.local(
        "tar -cvzf {} ./web_static".format(file_path), capture=True)
    if tar_file.failed:
        return None
    else:
        return file_path
