from test_site.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
from test_site.settings import INSTALLED_APPS


SECRET_KEY = 'django-insecure-f^6h1+)!lo6n%6!$_up%x9p#pi4dp4y!ypmk@==4is62mn#w+h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

# INSTALLED_APPS = []

SITE_ID = 2


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS =[
    BASE_DIR / 'statics'
]

X_FRAME_OPTIONS = 'SAMEORIGIN'