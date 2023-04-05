#!usr/bin/python3
""" helps to compress files using fabric library """
from fabric.api import *
from datetime import datetime
import os

def do_pack():
    """ compressing files in archive """

    now = datetime.now().strftime('%Y%m%d%H%M%S')
    local('mkdir -p versions')
    file_name = 'web_static_{}.tgz'.format(now)
    archive_path = os.path.join("versions", file_name)
    check = local('tar -cvzf {} web_static'.format(archive_path))
    if check.failed:
        return None
    else:
        return archive_path
