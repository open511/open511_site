import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

try:
    NUM_CPUS = os.sysconf('SC_NPROCESSORS_ONLN')
except:
    NUM_CPUS = 2

bind = '127.0.0.1:10132'

workers = (NUM_CPUS * 2) + 1

pidfile = os.path.join(BASE_DIR, '..', 'gunicorn.pid')

#worker_class = 'gevent'
errorlog = os.path.join(BASE_DIR, '..', 'logs', 'gunicorn-error.log')

proc_name = 'open511'
