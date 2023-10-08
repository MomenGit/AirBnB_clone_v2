#!/usr/bin/python3
"""Define the function do_pack"""
from fabric import operations as ops
from datetime import datetime


def do_pack():
    """
    generates a .tgz archive from the contents of the web_static folder
    of your AirBnB Clone repo
    """
    ops.local("mkdir -p versions")
    file_path = "versions/web_static_{}.tgz".format(
        datetime.utcnow().strftime("%Y%m%d%H%M%S"))
    tgz_file = ops.local(
        "tar -cvzf {} ./web_static".format(file_path), capture=True)
    if tgz_file.failed:
        return None
    else:
        return file_path
