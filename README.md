video: https://www.youtube.com/watch?v=c-QsfbznSXI&t=795s&ab_channel=TechWithTim

```
// create virtual env
> python3 -m venv env

// activate virtual env
> source env/bin/activate

// install packages from txt file
> pip install -r requirements.txt

// create django admin
> django-admin startproject backend
> cd backend

// create app
> py manage.py startapp api

// create migration files
> py manage.py makemigrations

// apply migrations
> py manage.py migrate

// run server
> py manage.py runserver

// browser
http://127.0.0.1:8000/api/user/register/
http://127.0.0.1:8000/api/token/
http://127.0.0.1:8000/api/token/refresh/
http://127.0.0.1:8000/api/notes/
http://127.0.0.1:8000/api/notes/delete/<id>