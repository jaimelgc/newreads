"""
Local development settings.

Runs against SQLite and an in-memory cache, so `python manage.py runserver`
works out of the box with no external services (MySQL, Redis) and no .env
file required. Create backend/.env if you want to override any of these.
"""
from decouple import config

from .base import *  # noqa: F401,F403
from .base import BASE_DIR

SECRET_KEY = config('SECRET_KEY', default='django-insecure-local-dev-key-do-not-use-in-production')

DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*').split(',')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# Wide open so the Vite dev server can call the API without extra setup.
CORS_ALLOW_ALL_ORIGINS = True
