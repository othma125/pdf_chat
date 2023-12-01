#!/usr/bin/python3
"""mysql server distribution must be 5.7.x"""
from fabric.api import env, run

import os.path

env.user = 'ubuntu'
env.hosts = ["54.146.65.131"]
env.key_filename = "~/.ssh/school"

def do_deploy(archive_path):
    run('cd pdf_chat')
    run('git pull')
    run('./reload_gunicorn_no_downtime')