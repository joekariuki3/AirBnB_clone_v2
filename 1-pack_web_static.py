#!/usr/bin/python3
"""
fab script to compress files from
web_static directory to a .tgz
compressed files
"""
from fabric.api import *
import datetime


def do_pack():
    """
    a fab funtion that takes the
    web_static folder and compress it
    and return path of the compressed file
    else return None
    """
    now = datetime.datetime.now()
    ymdh = "{}{}{}{}".format(now.year, now.month, now.day, now.hour)
    aFileName = "web_static_{}{}{}.tgz".format(ymdh, now.minute, now.second)
    local("mkdir -p versions")
    result = local("tar -cvzf versions/{} web_static".format(aFileName))
    if result.failed:
        return None
    path = local("realpath versions/{}".format(aFileName), capture=True)
    archivePath = path.stdout.strip()
    return archivePath
