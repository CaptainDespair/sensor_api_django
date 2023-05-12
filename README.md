# sensor_api_django
Django web application (DRF)

Данное Django web-приложение представляет собой API для CRUD-методов датчиков и зависимых событий.

Взаимодействие моделей происходит соответствующим образом:
![image](https://github.com/CaptainDespair/sensor_api_django/assets/105984453/a5bdf48e-cbb1-4d5e-b311-41506dc1afa4)

<h2>Задачи</h2>

  - CRUD операции для событий;
  
  - CRUD операции для датчиков;
  
  - Пагинация для событий;
  
  - Получение всех событий для конкретного датчика;
  
  - Фильтрацию событий по temperature и humidity (temperature_value, temperature_min, etc);
  
  - Выгрузка данных событий из JSON-файла в базу данных (если файл не *.JSON, либо поля не соответствуют, либо sensor_id не существует, запись события не произойдет);
  
  - Swagger/Redoc;

  - Dockerfile, docker-compose;
  
<h3>В разработке</h3>
 
 - Linter

 - CI/CD

 - TESTs

<h2>Обзор АПИ</h2>

<b><i>Апи для датчиков:</i></b>

        Удаление датчика: /sensor-delete/<str:pk>,
        Список датчиков: /sensor-list/,
        Создать датчик: /sensor-detail/<str:pk>,
        Получить события по датчику: /sensor-events/<str:pk>,
        Обновить датчик: /sensor-update/<str:pk>
        
<b><i>Апи для событий:</i></b>

        Список событий: /event-list/,
        Загрузка событий из json-файлов: /event-upload/,
        Создать событие: /event-detail/<str:pk>,
        Фильтрация событий: (example) humidity_min/max=? : /event-list/?humidity_min=*&&temperature_value=*&&...etc,
        view: temperature_value=?, temperature_min/max=?, humidity_value=?, humidity_min/max=?
        Обновить событие: /event-update/<str:pk>,
        Удалить событий: /event-delete/<str:pk>,
        Swagger: /swagger,
        Redoc: /redoc

        
# .env
#Django 

DJANGO_SECRET_KEY='<django_key>'

#PostgreSQL

NAME_DB='sensors_db'

POSTGRES_USER='postgres'

POSTGRES_PASSWORD='your_password'
  
POSTGRES_HOST='db'
  
POSTGRES_PORT='5432'

# Запуск приложения
1) Сначала вы должны создать в PostgreSQL базу данных с именем sensors_db или любое, в таком случае изменив NAME_DB в .env
2) >pip install -r requirements
3) .env - поставить свои настройки
4) >python manage.py makemigrations
5) >python manage.py migrate
6) >python manage.py runserver

# Запуск с помощью Docker
1) Создайте базу данных sensors_db в pgsql
2) .env - поставить свои настройки
3) >docker-compose up -d --build #билд сервиса
4) >docker-compose exec web python manage.py migrate --noinput #запуск миграций
5) >dicker-compose up #запускаем приложение
  
  
 # Стек
- Python3.11
  - Django
  - Django Rest Framework
  - psycopg2
  - json
  - yasg (Swagger)
- Postgres
- Docker
