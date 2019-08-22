#배포환경

from mysite.settings.common import *

DEBUG = False

ALLOWED_HOSTS = ['13.59.202.149', ]

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}