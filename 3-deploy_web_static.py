#!/usr/bin/python3
"""
fabric script that creates and distrubutes an archive to my server
"""
from fabric.contrib import files
from fabric.api import env, run , local, put
from fabric.operations import put
from datetime import datetime
import os


env.hosts = ['54.234.69.13', '100.26.9.245']


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


def do_deploy(archive_path):
    """Distribute the archive to the web servers."""

    if archive_path is None or os.path.isfile(archive_path) is False:
        return False

    try:
        a_name = archive_path.split('/')[-1]
        put('{}'.format(archive_path), '/tmp/{}'.format(a_name))
        name_target = a_name.split('.')[0]
        full_target = "/data/web_static/releases/{}".format(name_target)
        run('mkdir -p {}'.format(full_target))
        run("tar -xzf /tmp/{} -C {}".format(a_name, full_target))
        run('rm /tmp/{}'.format(a_name))
        run('mv {}/web_static/* {}/'.format(full_target, full_target))
        run('rm -Rf {}/web_static'.format(full_target))
        run('rm -Rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(full_target))
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
