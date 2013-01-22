## Задача
В репозитории представлено тестовое приложение, состоящее из двух частей - web-приложения и PgQ-консьюмера. Приложение сохраняет в СУБД "журнал запросов", PgQ-консьюмер обновляет статистку запросов. Web-приложение должно исполняться сервером приложений gunicorn.

Для выполнения задания необходимо:
* создать стартовые скрипты для всех элементов приложения - PgQ-тикера, PgQ-консьюмера и web-приложения,
* разработать и настроить схему разворачивания и обновления приложения из данного репозитория.

## Инициализация рабочего окружения
1. Создать базу, инициализировать её с помощью ```schema.sql```.
2. Разместить продуктивный конфиг в ```/etc/flant-testcase.conf```, шаблон в корне репозитория.
3. Подключить ```nginx.inc.conf``` к конфигурации nginx.

## Справочник команд
Все команды выполняются из корня репозитория.

### Запуск gunicorn с приложением
```
/usr/bin/gunicorn --bind localhost:5002 --worker-class egg:gunicorn#gevent --worker-connections 1 --workers 1 webapp:application
```

### Инициализация PgQ (выполняется один раз после создания базы)
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