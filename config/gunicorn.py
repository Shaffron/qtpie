from os import (
    cpu_count,
    path
)

PROJECT_DIR = path.abspath(path.dirname(__name__))

proc_name = 'qtpie'
bind = f'unix:{PROJECT_DIR}/run/gunicorn.sock'
worker_class = 'gevent'
workers = cpu_count() * 2 + 1
errorlog = f'/var/log/{proc_name}/gunicorn.error.log'
accesslog = f'/var/log/{proc_name}/gunicorn.access.log'
loglevel = 'info'