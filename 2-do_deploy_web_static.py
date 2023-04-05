#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that distributes an archive to your web servers 
"""
from fabric.api import env, put, run, sudo
from os.path import exists
import os

env.hosts = ['34.207.188.143', '100.25.160.228']

def do_deploy(archive_path):
    if not exists(archive_path):
        return False
    try:
        filename = os.path.basename(archive_path)
        dirname = os.path.splitext(filename)[0]

        put(archive_path, '/tmp')

        run('mkdir -p /data/web_static/releases/{}'.format(dirname))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(filename, dirname))
        run('rm /tmp/{}'.format(filename))
        run('sudo rm -f /data/web_static/current')
        run('sudo ln -s /data/web_static/releases/{}//data/web_static/current'.format(dirname))
        return True
    except:
        return False

