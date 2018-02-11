**This project is developed on python 3.6


How to run the project

** Use virtual environment for isolated local development or use pipenv 

1. sudo pip install pipenv        # For Python version 2.7
2. sudo pip3 install pipenv       # For Python version 3.6
3. pipenv --python 3.6
4. touch Pipfile   # Put the name of dependent library there.
5. pipenv shell
6. pipenv install --dev
7. python manage.py makemigrations contact (Before running this command set database connection properly in settings.py file)
8. python manage.py migrate
9. python manage.py runserver_plus 0.0.0.0:8000 (For development)
10. gunicorn InterconnectionContact.wsgi:application -w 4 -b 0.0.0.0:8000 (For production with optional flag)**
11. curl -H "Content-Type: application/json" -X POST -d '{"first_name":"xyz","last_name":"xyz"}' http://localhost:8000/api/v1/contact/
12. Use any rest client such as Advanced Rest Client for getting data from rest url

** For Production you can use gunicorn or other wsgi compatible server

Please mail me for any help: rab.marjan@gmail.com
