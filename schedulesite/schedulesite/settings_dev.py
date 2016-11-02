from schedulesite.settings_base import *

SECRET_KEY = 'some random string'

CALENDAR_DOMAIN = 'domain.com'
# Used by unit tests which also create 'a_credentials_file' used by the app
TEST_CALENDAR_ID = 'address@' + CALENDAR_DOMAIN

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DBS = {
    'sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },

    'postgresql': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'futuschedule',
        'HOST': 'localhost',
    },
}

# choose the DB
DATABASES = {'default': DBS['sqlite']}
del DBS
