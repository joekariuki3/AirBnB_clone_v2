#!/usr/bin/python3
"""
fab script to compress files from
web_static directory to a .tgz compressed files
then distribute the compressed files to our servers
"""
from fabric.api import *
import datetime
from os.path import exists

env.hosts = ['ubuntu@54.90.5.38', 'ubuntu@52.3.242.109']


def do_pack():
    """
    a fab funtion that takes the
    web_static folder and compress it
    and return path of the compressed file
    else return None
    """
    now = datetime.datetime.now()
    ymd = f"{now.year}{now.month}{now.day}"
    archiveFileName = f"web_static_{ymd}{now.hour}{now.minute}{now.second}.tgz"
    local("mkdir -p versions")
    result = local(f"tar -cvzf versions/{archiveFileName} web_static")
    if result.succeeded:
        return local(f"realpath {archiveFileName}")


def do_deploy(archive_path):
    """
    do_deploy distributes an archive to
    webservers to /tmp/ dir using the path passed to it
    them uncompress it and remove the compessed file
    then sets the moved files to be served by the servers
    """
    if exists(archive_path):
        FullFileName = archive_path.split("/")[-1]
        fileName = FullFileName.split(".")[0]
        upload = put(f"{archive_path}", "/tmp/")
        if upload.succeeded:
            unarchiveDest = f"/data/web_static/releases/{fileName}"
            mkUnarchiveDest = run(f"mkdir -p {unarchiveDest}")
            unarchive = run(f"tar -xzf /tmp/{FullFileName} -C {unarchiveDest}")
            # move files from subfolder to the main folder
            run(f"mv {unarchiveDest}/web_static/* {unarchiveDest}")
            # remove the subfolder
            run(f"rm -rf {unarchiveDest}/web_static")
            if unarchive.succeeded:
                rmArchive = run(f"rm -rf /tmp/{FullFileName}")
                if rmArchive.succeeded:
                    rmSmLink = run("rm -rf /data/web_static/current")
                    if rmSmLink.succeeded:
                        smTarget = f"/data/web_static/releases/{fileName}"
                        smName = f"/data/web_static/current"
                        newSmLink = run(f"ln -sf {smTarget} {smName}")
                        if newSmLink.succeeded:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
