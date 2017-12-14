#!/usr/bin/python3
"""archive web static folder"""
from fabric.operations import local


def do_pack():
    """create packet"""
    local("mkdir -p versions")
    local("tar -cvzf versions/web_static_$(date +%Y%m%d%H%M%S).tgz" +
          " ./web_static")
