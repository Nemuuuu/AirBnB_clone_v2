#!usr/bin/python3
""" """
from fabric.api import local
from datetime import datetime

def do_pack():
    try:
        now = datetime.now().strftime('%Y%m%d%H%M%S')
        local('mkdir -p version')
        file_name = 'versions/web_static_'+now+'.tgz'
        local('tar -cvzf {} web_static_' format(file_ame))
        return file_name
    except:
        return None
