import os
import sys
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'api.Account'

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'boxing.api',
    'rest_framework_swagger'
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('boxing.api.permissions.IsAdminOrReadOnly',),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'PAGE_SIZE': sys.maxsize
}

# required by rest_framework_swagger
TEMPLATE_LOADERS = (
    'django.template.loaders.eggs.Loader',
)

SWAGGER_SETTINGS = {
    'is_authenticated': True,
    'info': {
        'contact': 'ricardolobo@audienciazero.org',
        'description': 'Boxing is an application built to provide a faster and easier way to find objects in the Laboratory.',
        'title': 'Boxing API'
    }
}

# AUTHENTICATION - JWT CONFIGURATION
# For the official docs see: http://getblimp.github.io/django-rest-framework-jwt/
JWT_AUTH = {
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': timedelta(hours=5),
    'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=15)
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
)

# django-cors settings
# for info on django-cors settings https://github.com/ottoyiu/django-cors-headers
CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = True # when set to True allows the use of cookies
CORS_ORIGIN_WHITELIST = ('boxing.audienciazero.net',)

ROOT_URLCONF = 'boxing.urls'

WSGI_APPLICATION = 'boxing.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'boxing.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_ROOT = '/var/www/boxing-api/boxing/api/static/'
STATIC_URL = '/static/'

# media settings
# used to store images submitted by the users
MEDIA_ROOT = STATIC_ROOT + 'media/'
MEDIA_URL = STATIC_URL + 'media/'
