#!/usr/bin/python3
# Fabric script to distribute an archive to a web server.
import os.path
from fabric.api import env, run, put
from fabric.colors import green, red

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

    print(green("Executing task 'do_deploy'"))

    # Upload the archive
    print(run(f"put: {archive_path} -> /tmp/{file}"))

    # Remove the old directory
    print(run(f"run: rm -rf /data/web_static/releases/{name}/"))

    # Create the new directory
    print(run(f"run: mkdir -p /data/web_static/releases/{name}/"))

    # Extract the archive
    print(run(f"run: tar -xzf /tmp/{file} -C /data/web_static/releases/{name}/"))

    # Remove the temporary archive
    print(run(f"run: rm /tmp/{file}"))

    # Move the contents of the extracted folder
    print(run(f"run: mv /data/web_static/releases/{name}/web_static/* "
               f"/data/web_static/releases/{name}/"))

    # Remove the old symbolic link
    print(run(f"run: rm -rf /data/web_static/releases/{name}/web_static"))

    # Remove the old current directory
    print(run(f"run: rm -rf /data/web_static/current"))

    # Create a new symbolic link
    print(run(f"run: ln -s /data/web_static/releases/{name}/ /data/web_static/current"))

    print(green("New version deployed!"))

    return True