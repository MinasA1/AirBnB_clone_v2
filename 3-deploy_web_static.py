#!/usr/bin/python3
"""distributes archive to web servers"""
from fabric.operations import run, put, env, settings
from os.path import isdir as test
env.hosts = ['142.44.167.26', '144.217.246.235']
env.user = 'ubuntu'
time = local("$(date +%Y%m%d%H%M%S)")
archive_path = "versions/web_static_{}.tgz".format(time)
name = archive_path.split("/")[-1]


def deploy():
    """calls do_pack and do_deploy"""
    do_pack()


def do_pack():
    """create packet"""
    try:
        local("mkdir -p versions && tar -cvzf {} ./web_static"
              .format(archive_path))
        return name
    except:
        return False


def do_deploy(archive_path):
    """uploads to server"""
    if not (test(archive_path)):
        return False
    try:
        put(archive_path, "/tmp")
        path = "/data/web_static/releases/".format(name.split(".")[0])
        run("mkdir {0} && tar -xzf /tmp{1} -C {0}".format(path, name))
        run("rm /tmp/{} && rm -rf /data/web_static/current".format(name))
        run("ln -s {} /data/web_static/current".format(path))
        return True
    except:
        return False
