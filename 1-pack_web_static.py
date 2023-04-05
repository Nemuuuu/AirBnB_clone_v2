#!usr/bin/python3
""" helps to compress files using fabric library """
from fabric.api import *
from datetime import datetime

def do_pack():
    """ compressing files in archive """
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    local('mkdir -p versions')
    file_name = 'versions/web_static_'+now+'.tgz'
    check = local('tar -czvf {} web_static_'.format(file_name))
    if check.failed:
        return None
    else:
        return file_name
