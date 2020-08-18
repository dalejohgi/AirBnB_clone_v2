#!/usr/bin/python3
"""Compress web static folder into a tgz file"""

from datetime import datetime
from fabric.api import *


env.user = "ubuntu"


def do_pack():
    """Compress web static folder into a tgz file"""
    local("mkdir -p versions")
    date = datetime.now()
    now = date.strftime("%Y%m%d%H%M%S")
    tgz_file = "web_static_{}.tgz".format(now)
    try:
        local("tar -cvzf versions/{}\
              ~/AirBnB_clone_v2/web_static".format(tgz_file))
        return "versions/{}".format(tgz_file)
    except:
        return None
