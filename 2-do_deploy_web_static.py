#!/usr/bin/python3
# Fabric script to distribute an archive to a web server.
import os.path
from fabric.api import env, run, put
from fabric.colors import green

env.hosts = ["18.206.197.213", "3.83.238.214"]


def do_deploy(archive_path):
    """func to distribute archives to server.

    Args:
        archive_path (str): archive path.
    Returns:
        If files does not exist - False.
        Otherwise - True.
    """
    if os.path.isfile(archive_path) is False:
        return False

    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    print(f"[{env.host}] Executing task 'do_deploy'")
    print(f"[{env.host}] put: {archive_path} -> /tmp/{file}")
    print(run(f"mkdir -p /data/web_static/releases/{name}/"))
    print(run(f"tar -xzf /tmp/{file} -C /data/web_static/releases/{name}/"))
    print(run(f"rm /tmp/{file}"))
    print(run(f"mv /data/web_static/releases/{name}/web_static/* /data/web_static/releases/{name}/"))
    print(run(f"rm -rf /data/web_static/releases/{name}/web_static"))
    print(run(f"rm -rf /data/web_static/current"))
    print(run(f"ln -s /data/web_static/releases/{name}/ /data/web_static/current"))
    print(green("New version deployed!"))

    return True
