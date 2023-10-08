#!/usr/bin/python3
"""
fab script to compress files from
web_static directory to a .tgz compressed files
then distribute the compressed files to our servers
using only one function now deploy()
"""
from fabric.api import *
import datetime
from os.path import exists

env.hosts = ['ubuntu@54.90.5.38', 'ubuntu@52.3.242.109']


@runs_once
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


def do_deploy(archive_path):
    """
    do_deploy distributes an archive to
    webservers to /tmp/ dir using the path passed to it
    them uncompress it and remove the compessed file
    then sets the moved files to be served by the servers
    """
    if not exists(archive_path):
        return False
    FullFileName = archive_path.split("/")[-1]
    fileName = FullFileName.split(".")[0]
    upload = put("{}".format(archive_path), "/tmp/")
    if upload.failed:
        return False
    unarchiveD = "/data/web_static/releases/{}".format(fileName)
    mkUnarchiveDest = run("mkdir -p {}".format(unarchiveD))
    unarchive = run("tar -xzf /tmp/{} -C {}".format(FullFileName, unarchiveD))
    # move files from subfolder to the main folder
    run("mv {}/web_static/* {}".format(unarchiveD, unarchiveD))
    # remove the subfolder
    run("rm -rf {}/web_static".format(unarchiveD))
    if unarchive.failed:
        return False
    rmArchive = run("rm -rf /tmp/{}".format(FullFileName))
    if rmArchive.failed:
        return False
    rmSmLink = run("rm -rf /data/web_static/current")
    if rmSmLink.failed:
        return False
    smTarget = "/data/web_static/releases/{}".format(fileName)
    smName = "/data/web_static/current"
    newSmLink = run("ln -sf {} {}".format(smTarget, smName))
    if newSmLink.failed:
        return False
    return True


def deploy():
    """
    Creates an achive using do_pack(),
    then uses do_deploy(path) to move the
    archive files to the servers
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    returnValue = do_deploy(archive_path)
    return returnValue


def do_clean(number=0):
    """
    perform a cleaning opration
    by removing old archives and specifing
    latest one to keep
    locally and remote
    """
    number = int(number)
    versionList = local("ls -t versions/", capture=True).split("\n")
    RemoteVersionList = run("ls -t /data/web_static/releases/").split()
    # remove ones to keep
    if number == 0 or number == 1:
        versionList.remove(versionList[0])
        RemoteVersionList.remove(RemoteVersionList[0])
    if number > 1:
        for i in range(number):
            if len(versionList) > 0:
                versionList.remove(versionList[0])
            if len(RemoteVersionList) > 0:
                RemoteVersionList.remove(RemoteVersionList[0])

    for archive in versionList:
        rmUnwanted = local("rm -fR versions/{}".format(archive))
    for a in RemoteVersionList:
        rmUnwanted = run("sudo rm -fR /data/web_static/releases/{}".format(a))
