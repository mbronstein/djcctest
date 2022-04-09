# config/gunicorn.conf.py

bind = unix:/run/gunicorn.sock
wsgi_app= djcctest.wsgi:application
backlog = 2048

workers = 1
worker_class = 'sync'
worker_connections = 1000
timeout = 30
keepalive = 2
spew = False


daemon = False
raw_env = [
    DJANGO_SETTINGS_FILE=config.settings.production,
]

pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None

errorlog = '-'
loglevel = 'info'
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

proc_name = None


access - logfile - \
--workers
3 \
- -bind
unix: / run / gunicorn.sock \
    djcctest.wsgi: application
