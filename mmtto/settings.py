"""
Django settings for mmtto project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f=-9u9^0gq!-4vsfz+7q@^d&#r7&)(tbe!(3bwb+gj$go0&2-e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
#Instalacion de Paquetes Django.
#pip install django-import-export
#pip install django-ckeditor
#pip install Pillow
#pip install django-excel-response
#pip install six

# Application definition

INSTALLED_APPS = [
    'core',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'registration',
    'pages.apps.PagesConfig',
    'profiles',
    'monitoreo.apps.MonitoreoConfig',
    'oximetro.apps.OximetroConfig',
    'ambulancia.apps.AmbulanciaConfig',
    'anestesia.apps.AnestesiaConfig',
    'desfibrilador.apps.DesfibriladorConfig',
    'externo.apps.ExternoConfig',
    'incubadora.apps.IncubadoraConfig',
    'inventario.apps.InventarioConfig',
    'ventilador.apps.VentiladorConfig',
    'vital.apps.VitalConfig',
    'ssgg',
    'comunes',
    'proveedores',
    'licitacion',
    'ordenes',
    'infraestructura',
    'otautomotriz',
    'proyectos',
    'rrhh',
    'solicitudes',
    'costos',
    'clima',
    'industriales',
    'ordenestalleres',
    'solicitudestalleresabas',
    'roperiaconfeccion',
    'ropaexterno',
    'kilosservicio',
    'facturaroperia',
    'actas',
    'excel',
    'graficos',
    'pautas',
    'colisiones',
    'import_export',
    'gantt',
    'informe',
    'justificacion',
    'capacitacion',
    'bases',
    'control',
    'grafico',
    'messenger',
    'prevencion',
	'guia',
    'manuales',
    'covid',
	'hhee',
    'ambiente',
   
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mmtto.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mmtto.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#DATABASES = {
  #'default': {
# 'ENGINE': 'django.db.backends.mysql',
#  'NAME': 'bd_mmto',
#     'HOST': 'localhost',
#     'PORT': '3306',
#     'USER': 'Fernando',
#     'PASSWORD': 'Wolverine5597'
# }
#}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT= os.path.join(BASE_DIR, 'static')
# Media Files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
LOGOUT_REDIRECT_URL = 'home'