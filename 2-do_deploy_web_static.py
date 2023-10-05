#!/usr/bin/python3
"""Compress and upload web static package to Web Servers
"""
from fabric.api import *
from datetime import datetime
from os import path

env.hosts = ["107.23.90.175", "100.25.21.55"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/school"

def do_deploy(archive_path):
    """Deploy web resources to server(s)"""
    try:
        if not (path.exists(archive_path)):
            return False
        put(archive_path, "/tmp/")

        timestamp = archive_path[-18:-4]
        run("sudo mkdir -p /data/web_static/releases/web_static_{}/"
            .format(timestamp))
