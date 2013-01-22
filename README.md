# /usr/bin/gunicorn --bind d3.local:5002 --worker-class egg:gunicorn#gevent --worker-connections 1 --workers 1 webapp:application

# sudo -u postgres pgqadm ./pgq.conf install
# sudo -u postgres pgqadm ./pgq.conf create admtc_queue
# sudo -u postgres pgqadm ./pgq.conf ticker 2> /dev/null
# sudo -u postgres pgqadm ./pgq.conf status
# sudo -u postgres pgqadm ./pgq.conf config admtc_queue ticker_max_count=1 ticker_max_lag=1 ticker_idle_period=10
# ./consumer.py ./pgq.conf -d
# ./consumer.py ./pgq.conf -s


