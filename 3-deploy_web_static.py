#!/usr/bin/python3
"""This is a fabric script that does a full deployment to a webserver
"""

from fabric.api import env, put, cd, run, local
import os  # for file path checking
from datetime import datetime

env.hosts = ['3.85.41.84', '54.90.17.105']
env.user = 'ubuntu'
env.key_filename = ['~/.ssh/alx_ssh']


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


def do_deploy(archive_path):
    """function that deploys an archive to the remote server"""
    # check if path exists
    if not os.path.exists(archive_path):
        return False

    # steps to deploy
    remote_path = '/tmp/'
    # upload the local file to the remote path
    uploaded_file = put(archive_path, remote_path)[0]
    full_file_path = f'{remote_path}{os.path.basename(uploaded_file)}'

    # uncompress the archive to the folder
    # /data/web_static/releases/<archive filename without extension>
    path_to_decmp_archive = '/data/web_static/releases/'

    # get the filename without extension
    filename_no_ext = os.path.splitext(os.path.basename(full_file_path))[0]

    # Create the target directory if it doesn't exist
    run(f'mkdir -p {path_to_decmp_archive}{filename_no_ext}')

    # Extract the archive
    run(f'tar -xzf {full_file_path} -C \
            {path_to_decmp_archive}{filename_no_ext}')

    # Move contents one level up and remove the inner directory
    run(f'mv {path_to_decmp_archive}{filename_no_ext}/web_static/* \
            {path_to_decmp_archive}{filename_no_ext}/')
    run(f'rm -rf {path_to_decmp_archive}{filename_no_ext}/web_static')

    path_to_cur_release = '/data/web_static/current'

    # delete the archive from the web server
    run(f'sudo rm -rf {full_file_path}')

    # delete the symbolic link from the web server
    run(f'sudo rm -rf {path_to_cur_release}')

    # create a symbolic link to the new release without extension
    run(f'sudo ln -s {path_to_decmp_archive}{filename_no_ext} \
            {path_to_cur_release}')

    # restart nginx
    run('sudo service nginx restart')

    return True


def deploy():
    """
    Deploy the web static content to the servers
    """
    # Call the do_pack() function and store the path of the created archive
    try:
        archive_path = do_pack()
    except Exception as e:
        print((str(e)))
        return False

    # Return False if no archive has been created
    if not archive_path:
        return False

    # Call do_deploy(archive_path) func using the new path of new archive
    return do_deploy(archive_path)


if __name__ == '__main__':
    deploy()
