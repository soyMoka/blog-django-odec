# python manage.py runserver --settings=oportunidad_de_cambio.local_cj


from .settings import * 

DEBUG = True 
ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases






# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
# instalar libreria  pip install mysqlclient
# Actualizar requirements.txt (pip freeze > requirements.txt)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'OdeC',
        "USER": 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306', # Al no poner ninguno usa el por defecto.
    }
}






#--- Importamos la librería django_heroku y dejamos que haga su magia.---#

import django_on_heroku
django_on_heroku.settings(locals())

#------------------------------------------------------------------------#
