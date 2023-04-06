#!/usr/bin/python3

"""Fabric script to compress web_static in archive"""

from fabric.api import local
from datetime import datetime


def do_pack():

    """Create an archive from the contents of web_static folder."""

    now = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    path = "versions/web_static_{}.tgz".format(now)
    try:
        local('mkdir -p versions')
        local('tar -cvzf {} web_static'.format(path))
        return path
    except:
        return none
