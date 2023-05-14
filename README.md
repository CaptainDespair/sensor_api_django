# sensor_api_django
Django web application (DRF)

Данное Django web-приложение представляет собой API для CRUD-методов датчиков и зависимых событий.

Взаимодействие моделей происходит соответствующим образом:

![image](https://github.com/CaptainDespair/sensor_api_django/assets/105984453/a5bdf48e-cbb1-4d5e-b311-41506dc1afa4)

<h2>Реализованные задачи</h2>

  - CRUD операции для событий;
  
  - CRUD операции для датчиков;
  
  - Пагинация для событий (drf pagination);
  
  - Получение всех событий для конкретного датчика (one2many);
  
  - Фильтрация событий по temperature и humidity (django-filter)
    -  /event-list/?temperature_value=...
    -  /event-list/?temperature_min=...
    -  /event-list/?temperature_max=...
    -  /event-list/?humidity_value=...
    -  /event-list/?humidity_min=...
    -  /event-list/?humidity_max=...
    -  и всевозможные взаимодействия через <b>&&</b>
  
  - Выгрузка данных событий из JSON-файла в бд:
      - если файл не JSON, либо поля не соответствуют, либо sensor_id не существует, запись события не произойдет.
      - файлы должны лежать в папке events-json, директорию и название файла можно переопределить в .env
      - /event-upload/ - возвращает 'Upload /dir/file/', если файл не поврежден и находится в папке (GET)
      - /event-upload/ - возвращает 'Json file is damaged or not found', если файл поврежден или не находится в папке (GET)
      - /event-upload/ - возвращает информацию об успешной/неуспешной загрузке events из JSON и ошибку (POST)
  
  - Swagger/Redoc;

  - Dockerfile, docker-compose;
  
  - Тесты на CRUD для модели Sensor;
  
<h3>В разработке</h3>
 
 - Linter

 - CI/CD

 - TESTs

<h2>Обзор АПИ</h2>

<b><i>Далее: /api/...</i></b>

<b><i>Апи для датчиков:</i></b>
         
        Список датчиков: /sensor-list/
        Создать датчик: /sensor-detail/<int:pk>
        Обновить датчик: /sensor-update/<int:pk>
        Удаление датчика: /sensor-delete/<int:pk>
        Получить события по датчику: /sensor-events/<int:pk>
      
<b><i>Апи для событий:</i></b>

        Список событий: /event-list/
        Фильтрация событий: (example) humidity_min/max=? : /event-list/?humidity_min=*&&temperature_value=*&&...etc
        view: temperature_value=?, temperature_min/max=?, humidity_value=?, humidity_min/max=?
        Создать событие: /event-detail/<int:pk>
        Обновить событие: /event-update/<int:pk>
        Удалить событие: /event-delete/<int:pk>
        Загрузка событий из json-файлов: /event-upload/
        Swagger: /swagger
        Redoc: /redoc

        
# .env
        #Django 
        DJANGO_SECRET_KEY='<django_key>'
        DEBUG=1
        DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

        #PostgreSQL
        DB_ENGINE='django.db.backends.postgresql_psycopg2'
        POSTGRES_DB='sensors_db'
        POSTGRES_USER='postgres'
        POSTGRES_PASSWORD='your_password'
        POSTGRES_HOST='127.0.0.1'
        POSTGRES_PORT='5432'
        
        #Json dir
        UPLOAD_FILE = 'events-json/events.json'

# Запуск приложения
1) Сначала вы должны создать в PostgreSQL базу данных с именем sensors_db или любое, в таком случае изменив POSTGRES_DB в .env
2) >pip install -r requirements
3) .env - поставить свои настройки
4) >python manage.py makemigrations sensors
5) >python manage.py migrate
6) >python manage.py runserver

# Запуск с помощью Docker
1) Создайте базу данных sensors_db в pgsql
2) .env - поставить свои настройки, <b><i>POSTGRES_HOST='db'</i></b> - обязательно, чтобы приложение подключилось к бд, которая запущена в контейнере с именем "db"
3) >docker-compose up -d --build #билд сервиса
4) >docker-compose exec sensor_api python manage.py migrate --noinput #запуск миграций
5) >docker-compose up #запускаем приложение

# Сроки по выполнению
- 11.05.2023-12.05.2023
  - API, swagger, docker

- 14.05.2023
  - docker-compose, tests (CRUD sensors)
  
 # Стек
- Python3.11
  - Django
  - Django Rest Framework
  - psycopg2
  - json
  - yasg (Swagger)
- Postgres
- Docker
