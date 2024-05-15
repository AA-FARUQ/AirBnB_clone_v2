#!/usr/bin/python3
'''
Fabric script to distribute an archive to web servers
'''

import os
from datetime import datetime
from fabric.api import env, local, put, run, runs_once

# Define the list of web server IPs
env.hosts = ['34.138.32.248', '3.226.74.205']


def pack_web_static():
    """Creates a compressed archive of the web_static folder.
    Returns:
        (str) Path to the packed archive.
    """
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
        print("Packing web_static to {}".format(archive_path))
        local("tar -cvzf {} web_static".format(archive_path))
        archize_size = os.stat(archive_path).st_size
        print("web_static packed: {} -> {} Bytes".format(archive_path, archize_size))
    except Exception as e:
        print("Error packing web_static:", e)
        archive_path = None
    return archive_path


@runs_once
def do_deploy(archive_path):
    """Deploys the static files to the host servers.
    Args:
        archive_path (str): The path to the archived static files.
    Returns:
        (bool) True if deployment is successful, Falseotherwise.
    """
    if not os.path.exists(archive_path):
        return False
    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)
    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
        run("rm -rf /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        print('New version deployed!')
        return True
    except Exception as e:
        print("Error deploying:", e)
    return False
