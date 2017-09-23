**This project is developed on python 3.6


How to run the project

** Use virtual environment for isolated local development

1. pip install -r requirement.txt
2. python manage.py makemigrations contact (Before running this command set database connection properly in settings.py file)
3. python manage.py migrate
4. python manage.py runserver_plus localhost:8000 (For development)
5. gunicorn InterconnectionContact.wsgi:application -w 4 -b localhost:8000 (For production with optional flag)**
6. curl -H "Content-Type: application/json" -X POST -d '{"first_name":"xyz","last_name":"xyz"}' http://localhost:8000/api/v1/contact/
7.Use any rest client such as Advanced Rest Client for getting data from rest url

** For Production you can use gunicorn or other wsgi compatible server

Please mail me for any help: rab.marjan@gmail.com
