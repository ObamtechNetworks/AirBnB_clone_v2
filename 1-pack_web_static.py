#!/usr/bin/python3
"""This module defines a fabric script that generates a tgz archive
Archive is generated from the contents of web_static folder
"""

# import fabric commands
from fabric.api import local
from datetime import datetime


def do_pack():
    """packs a folder content into archives"""
    # target directory
    src_folder = "web_static"

    # destination folder
    dest_folder = "versions"

    # generate timestamp for the archive name
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    # set the archive name
    archive_name = f'web_static_{timestamp}.tgz'

    # run local commands - create the directory
    local(f'mkdir -p {dest_folder}')

    result = local(f'tar -czvf {dest_folder}/{archive_name} {src_folder}')

    if result.succeeded:
        path = f'{dest_folder}/{archive_name}'
        return path
    else:
        return None
