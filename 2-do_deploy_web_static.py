#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that distributes an archive to your web servers 
"""
from fabric.api import env, put, run, sudo
from os.path import exists
import os

env.hosts = ['34.207.188.143', '100.25.160.228']

def do_deploy(archive_path):
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

