"""
Production settings.

Every value below is required from the environment - there are no insecure
defaults. Set these as environment variables on the host (e.g. Railway's
"Variables" tab). DJANGO_ENV=production selects this module (see Procfile).
"""
import dj_database_url
from decouple import config

from .base import *  # noqa: F401,F403

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

CSRF_TRUSTED_ORIGINS = config('CSRF').split(',')

ALLOWED_HOSTS = config('ALLOWED_HOSTS').split(',')

CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS').split(',')

DATABASES = {'default': dj_database_url.config(default=config('DATABASE_URL'))}

# Django's MySQL backend is swapped for the mysql-connector-python driver.
if DATABASES['default']['ENGINE'] == 'django.db.backends.mysql':
    DATABASES['default']['ENGINE'] = 'mysql.connector.django'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": config("REDIS_URL"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}
