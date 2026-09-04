from decouple import config

DJANGO_ENV = config('DJANGO_ENV', default='local')

if DJANGO_ENV == 'production':
    from .production import *  # noqa: F401,F403
else:
    from .local import *  # noqa: F401,F403
