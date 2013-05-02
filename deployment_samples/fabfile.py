from fabric.api import *

import os

def prod():
    """Select the prod environment for future commands."""
    raise NotImplementedError

def dev():
    """Select the dev environment for future commands."""
    env.hosts = ['dev.open511.ca']
    env.user = 'michael'
    _env_init()
    env.base_dir = os.path.join(env.home_dir, 'sites', 'open511')

def _env_init():
    env.home_dir = '/home/' + env.user
    env.python = os.path.join(env.home_dir, '.virtualenvs', 'open511', 'bin', 'python')
    env.base_dir = os.path.join(env.home_dir, 'app')
    env.pip = env.python.replace('bin/python', 'bin/pip')
    
def deploy(ref='master'):
    """Perform all the steps in a standard deployment"""
    pull(ref)
    update_requirements()
    syncdb()
    update_statics()
    reload_code()
    
def pull(ref='master'):
    """Update the git repository to the given branch or tag"""
    with cd(env.base_dir):
        run('git fetch')
        run('git fetch --tags')
        run('git checkout %s' % ref)
    
        is_tag = (ref == run('git describe --all %s' % ref).strip())
        if not is_tag:
            run('git pull origin %s' % ref)
                    
def reload_code():
    """Send gunicorn a signal to restart its Python processes"""
    with cd(env.base_dir):
        run('kill -HUP `cat gunicorn.pid`')

def update_requirements():
    """Update Python dependencies"""
    with cd(env.base_dir):
        run(env.pip + ' install -r requirements.txt')

def syncdb():
    """Update database tables"""
    with cd(env.base_dir):
        run(env.python + ' manage.py syncdb --noinput')
        #run(env.python + ' manage.py migrate')
        
def update_statics():
    """Tell Django staticfiles to update said files."""
    with cd(env.base_dir):
        run(env.python + ' manage.py collectstatic --noinput')

def manage(cmd):
    with cd(env.base_dir):
        run(env.python + ' manage.py %s' % cmd)

def shell():
    manage('shell_plus')
