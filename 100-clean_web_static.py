#!/usr/bin/python3
"""
Fabric script that cleans up the local archives and the web servers
"""
from fabric.api import env, sudo, local
env.hosts = ['54.84.162.208', '54.175.225.209']


def do_clean(number=0):
    """Function to clean up archives"""
    number = int(number)
    if number == 0:
        number = 1
    number += 1
    local("ls -d -1tr versions/* | tail -n +{} | \
          xargs -d '\n' rm -f --".format(number))
    sudo("ls -d -1tr /data/web_static/releases/* | tail -n +{} | \
        xargs -d '\n' rm -rf --".format(number))
