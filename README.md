## Справочник команд
Все команды выполняются из корня репозитория.

### Запуск gunicorn с приложением
```
/usr/bin/gunicorn --bind localhost:5002 --worker-class egg:gunicorn#gevent --worker-connections 1 --workers 1 webapp:application
```

### Инициализация PgQ
```
sudo -u postgres pgqadm ./pgq.conf install
sudo -u postgres pgqadm ./pgq.conf create flant_queue
sudo -u postgres pgqadm ./pgq.conf config flant_queue ticker_max_count=1 ticker_max_lag=1 ticker_idle_period=10
```

### Запуск PgQ-тикера
```
sudo -u postgres pgqadm ./pgq.conf ticker 2> /dev/null
```


### Запуск и останов PgQ-консьюмера
```
./consumer.py ./pgq.conf -d # start
./consumer.py ./pgq.conf -s # stop
```