# /usr/bin/gunicorn --bind d3.local:5002 --worker-class egg:gunicorn#gevent --worker-connections 1 --workers 1 webapp:application

# sudo -u postgres pgqadm ./pgq.conf install
# sudo -u postgres pgqadm ./pgq.conf create admtc_queue
# sudo -u postgres pgqadm ./pgq.conf ticker 2> /dev/null
# sudo -u postgres pgqadm ./pgq.conf status

import psycopg2
from time import time

psycopg2_url = "user=d3 password=d3 host=localhost dbname=admtc"
db = psycopg2.connect(psycopg2_url)

def save_hit(url):
    crs = db.cursor()
    crs.execute('insert into hit (url) values (%(url)s)',
                {'url': url})
    crs.close()
    db.commit()

def application(env, start_response):
    status = '200 OK'
    headers = {'Content-Type': 'text/html; charset=utf-8'}
    url = env["PATH_INFO"]
    save_hit(url)
    start_response(status, headers.items())
    body = '{0}@{1}'.format(url, unicode(time()))
    return [body]
