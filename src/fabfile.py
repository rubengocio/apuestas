from fabric.api import env
from fabric.api import run, prefix
from fabric.context_managers import cd
from fabric.operations import sudo
from fab_tools.fab_settings import (
    USER, PASSWORD, PATH_PROJECT, PATH_PROJECT_SRC,
    PATH_VENV, PATH_VENV_ACTIVATE, getTerminalSize
)

def test():
    env.hosts = ["rgocio.tuxis.com.ar"]
    env.user = USER['test']
    env.password = PASSWORD['test']
    env.entorno = 'test'
    env.str_name = "Test"


def prod():
    env.hosts = ["rgocio.tuxis.com.ar"]
    env.user = USER['prod']
    env.password = PASSWORD['prod']
    env.entorno = 'prod'
    env.str_name = "Produccion"


def deploy():
    (width, height) = getTerminalSize()
    print '\n'*height
    DELIMITER = '-' * width
    print DELIMITER
    print "Host: %s" % env.host
    print "Entorno: %s" % env.str_name
    print "Usuario: %s" % env.user
    print DELIMITER
    confirmacion = raw_input('Continuar (s/n):')
    if confirmacion.lower() == 's':
        with cd(PATH_PROJECT[env.entorno]):
            run('git pull origin master')
        with cd(PATH_PROJECT_SRC[env.entorno]):
            run('find . -name \'*.pyc\' -delete')
            with prefix(PATH_VENV_ACTIVATE[env.entorno]):
                run('python manage.py migrate -v 1')
                run('rm static -R')
                run('python manage.py collectstatic -l --noinput')
        with cd(PATH_PROJECT[env.entorno]):
            run('chmod 777 %s' % PATH_PROJECT[env.entorno])


def restart_apache():
    sudo('service apache2 restart')