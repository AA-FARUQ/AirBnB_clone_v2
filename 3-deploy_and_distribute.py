#!/usr/bin/python3
'''Creates and distributes an archive to web servers using deploy()'''

import os
from datetime import datetime
from fabric.api import env, local, put, run, runs_once


env.hosts = ['34.138.32.248', '3.226.74.205']


@runs_once
def create_archive():
    """Archives the static files."""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    current_time = datetime.now()
    archive_path = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        current_time.year,
        current_time.month,
        current_time.day,
        current_time.hour,
        current_time.minute,
        current_time.second
    )
    try:
        print("Packing web_static to {}".format9(archive_path))
        local("tar -cvzf {} web_static".format(archive_path))
        archize_size = os.stat(archive_path).st_size
        print("web_static packed: {} -> {} Bytes".format(archive_path, archize_size))
    except Exception:
        archive_path = None
    return archive_path


def deploy_static(archive_path):
    """Deploys the static files to the host servers.
    Args:
        archive_path (str): The path to the archived static files.
    """
    if not os.path.exists(archive_path):
        return False
    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)
    success = False
    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
        run("rm -rf /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        print('New version is now LIVE!')
        success = True
    except Exception:
        success = False
    return success


def deploy():
    """Archives and deploys the static files to the host servers.
    """
    archive_path = create_archive()
    return deploy_static(archive_path) if archive_path else False
