#!/usr/bin/python3
"""distributes archive to web servers"""
from fabric.operations import run, put, env
from os.path import isdir as test
env.hosts = ['142.44.167.26', '144.217.246.235']


def do_deploy(archive_path):
    """uploads to server"""
    if not (test(archive_path)):
        return False
    try:
        put(archive_path, "/tmp")
        name = archive_path.split("/")[-1]
        path = "/data/web_static/releases/{}".format(name.split(".")[0])
        run("mkdir {}".format(path))
        run("tar -xzf /tmp{} -C {}".format(name, path))
        run("rm -rf /tmp/{} ".format(name))
        rune("rm -rf /data/web_static/current".format(name))
        run("ln -s {} /data/web_static/current".format(path))
        return True
    except:
        return False
