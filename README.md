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
  
<h3>В разработке</h3>

 - Docker
 
 - Linter

 - CI/CD

 - TESTs

<h2>API_OverView</h2>

        "Delete sensor: /sensor-delete/<str:pk>",
        "List sensor: /sensor-list/",
        "Create sensor: /sensor-detail/<str:pk>",
        "Get sensor events: /sensor-events/<str:pk>",
        "Update sensor: /sensor-update/<str:pk>"

        "List event: /event-list/",
        "Upload *.json events: /event-upload/",
        "Create event: /event-detail/<str:pk>",
        "Filter event: /event-list/?humidity_min=*&&temperature_value=*&&...etc",
        "Update event: /event-update/<str:pk>",
        "Delete event: /event-delete/<str:pk>",
        "View swagger: /swagger",
        "View redoc: /redoc"

        
# .env
#Django 

DJANGO_SECRET_KEY='<django_key>'

#PostgreSQL

NAME_DB='sensors_db'

POSTGRES_USER='postgres'

POSTGRES_PASSWORD=<password>
  
POSTGRES_HOST='127.0.0.1'
  
POSTGRES_PORT='5432'

# Запуск приложения
1) Сначала вы должны создать в PostgreSQL базу данных с именем sensors_db или любое, в таком случае изменив NAME_DB в .env
2) >pip install -r requirements
3) .env - поставить свои настройки
4) >python manage.py makemigrations
5) >python manage.py migrate
6) >python manage.py runserver
  
 # Стек
- Python3.11
  - Django
  - Django Rest Framework
  - psycopg2
  - json
- Postgres
