from .settings import *

DEBUG = True
ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['https://djong-grupo5.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd8ce45io054mhj',
        'USER': 'hnrbnceshsndyw',
        'PASSWORD': '75c94acc6cb1ecc1b0b9fb07b5f3127fb4955920cf8b4a8f0a2f1cd26e7372c0',
        'HOST': 'ec2-100-26-39-41.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

import django_heroku
django_heroku.settings(locals())