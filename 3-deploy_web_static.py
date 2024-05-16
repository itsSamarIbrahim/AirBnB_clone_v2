#!/usr/bin/python3
"""
A Fabric script (based on the file 2-do_deploy_web_static.py) that creates
and distributes an archive to your web servers, using the function deploy
"""
from os.path import exists, isdir
from fabric.api import put, run, local, env
from datetime import datetime


env_hosts = ['54.82.208.14', '54.161.250.120']


def do_pack():
    """
    Create a tar gzipped archive of the directory web_static
    """
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive = 'web_static_' + time + '.tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create is not None:
        return archive
    else:
        None

def do_deploy(archive_path):
    """
    Distributes an archive to your web servers, performs deployment steps.

    Args:
        archive_path (str): The path to the archive to be deployed.

    Returns:
        bool: True if deployment was successful, False otherwise.
    """
    if exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        no_extension = file_name.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_extension))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, no_extension))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}'.format(path, no_extension))
        run('rm -rf {}{}/web_static'.format(path, no_extension))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_extension))
        return True
    except Exception:
        return False

def deploy():
    """
    creates and distributes archives to the web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
