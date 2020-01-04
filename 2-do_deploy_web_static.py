#!/usr/bin/python3
"""Fabric script to generates a .tgz"""


from fabric.api import *
import os.path
from os import path
from datetime import datetime
from os.path import exists isfile


env.hosts = ['35.237.80.55', '35.231.185.233']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """ deploy a file to web servers"""
    if path.exists(archive_path) is False and not isfile(archive_path):
        return False
        try:
            upload = put(archive_path, '/tmp')
            name = archive_path.split('/')[1][:-4]
            run('sudo mkdir -p /data/web_static/releases/' + name + '/')
            run('sudo chown -R ubuntu:ubuntu /data')
            run('tar -xzf /tmp/' + name + '.tgz'
                ' -C /data/web_static/releases/' + name + '/')
            run('rm /tmp/' + name + '.tgz')
            run('mv /data/web_static/releases/' + name + '/web_static/* ' +
                '/data/web_static/releases/' + name + '/')
            run('rm -rf /data/web_static/releases/' + name + '/web_static')
            run('rm -rf /data/web_static/current')
            run('ln -sf /data/web_static/releases/' + name + '/ ' +
                '/data/web_static/current')
            print("New version deployed!")
            return True
        except:
            return False
