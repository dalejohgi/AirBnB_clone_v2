#!/usr/bin/python3
"""Compress web static folder into a tgz file"""

from datetime import datetime
from fabric.api import *
from os.path import exists


env.user = "ubuntu"
env.hosts = [
    '34.74.50.241',
    '34.75.65.52',
]


def do_pack():
    """Compress web static folder into a tgz file"""
    local("mkdir -p versions")
    date = datetime.now()
    now = date.strftime("%Y%m%d%H%M%S")
    tgz_file = "versions/web_static_{}.tgz".format(now)
    try:
        local("tar -cvzf {} web_static".format(tgz_file))
        return (tgz_file)
    except:
        return None


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if exists(archive_path):
        try:
            put(archive_path, '/tmp/')
            tgz_file = archive_path.split('/')[-1]
            file = tgz_file.split('.')[0]
            archive_folder = '/data/web_static/releases/{}/'.format(file)
            run('mkdir -p {}'.format(archive_folder))
            run('tar -xvzf /tmp/{} -C {}'.format(tgz_file, archive_folder))
            run('rm /tmp/{}'.format(tgz_file))
            run('mv {}web_static/* {}'.format(archive_folder, archive_folder))
            run('rm -rf {}web_static'.format(archive_folder))
            run('rm -rf /data/web_static/current')
            run('ln -s {} /data/web_static/current'.format(archive_folder))
            return True
        except:
            return False
    else:
        return False


def deploy():
    """creates and distributes an archive to web servers."""
    path = do_pack()
    if not path:
        return False
    else:
        value = do_deploy(path)
        return value
