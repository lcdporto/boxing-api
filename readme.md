Dependencies

* Virtual Env
* Pip
* Python 3

How to Create a Project From Scratch

// create virtual environment with python 3
$ virtualenv -p python3 env

// activate the virtual environment

$ source /env/bin/activate

// install django
$ pip install django

// install django rest framework
$ pip install djangorestframework

// install django cors headers

$ pip install django-cors-headers

// create a new django project in the pwd with name boxing
$ django-admin startproject boxing .

// create a new django app
$ cd boxing
$ django-admin startapp api

// edit settings.py

* change database engine and name (optional)
* add to installed apps

    'rest_framework',
    'corsheaders',
    'boxing.api',

* add rest frameword configuration

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'PAGE_SIZE': 25
}

* add to middleware classes

    'corsheaders.middleware.CorsMiddleware',

* add cors configuration

CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = (
    'localhost:8000',
)

* apply changes to database

$ ./manage.py migrate

* create super user

$ ./manage.py createsuperuser

// configure routing inside urls.py @todo
// create a viewset @todo
// create a model @todo

// update schema
$ ./manage.py makemigrations

// update the database
$ ./manage.py migrate

/ runserver, bind server to ip 127.0.o.1 0and port 8080
$ ./manage.py runserver 127.0.0.1:8080
