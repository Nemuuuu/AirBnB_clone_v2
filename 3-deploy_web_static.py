#!/usr/bin/python3
"""
fabric script that creates and distrubutes an archive to my server
"""
from fabric.contrib import files
from fabric.api import env, run , local
from fabric.operations import put
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

def do_deploy(archive_path):
    """ deploy """

    if not os.path.exists(archive_path):
        return False
    data_path = '/data/web_static/releases/'
    tmp = archive_path.split('.')[0]
    name = tmp.split('/')[1]
    dest = data_path + name
    try:
        put(archive_path, '/tmp')
        run('mkdir -p {}'.format(dest))
        run('tar -xzf /tmp/{}.tgz -C {}'.format(name, dest))
        run('rm -f /tmp/{}.tgz'.format(name))
        run('mv {}/web_static/* {}/'.format(dest, dest))
        run('rm -rf {}/web_static'.format(dest))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(dest))
        return True
    except:
        return False

def deploy():
    """full deploy"""
    
    path = do_pack()
    if path:
        return do_deploy(path)
    else:
        return False
