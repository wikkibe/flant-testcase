#!/usr/bin/python
import pgq
import sys

class Consumer(pgq.Consumer):
    def update_url_stat(self, db, url):
        crs = db.cursor()
        crs.execute('update stat set hits = hits + 1 where url = %(url)s',
                    {'url': url})
        if crs.rowcount == 0:
            crs.execute('insert into stat (url, hits) values (%(url)s, 1)',
                        {'url': url})

    def process_batch(self, db, batch_id, ev_list):
        for event in ev_list:
            self.update_url_stat(db, url=event.data)
            event.tag_done()

if __name__ == '__main__':
    Consumer('consumer', 'db', sys.argv[1:]).start()