import psycopg2
import time
from configparser import ConfigParser

config = ConfigParser()
config.read(['/etc/flant-testcase.conf'])

db_url = config.get('main', 'database')
db = psycopg2.connect(db_url)

def save_hit(url):
    crs = db.cursor()
    crs.execute('insert into hit (url) values (%(url)s)',
                {'url': url})
    crs.close()
    db.commit()

def application(env, start_response):
    url = env["PATH_INFO"]
    save_hit(url)
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    return ['{0}@{1}'.format(url, unicode(time.time()))]
