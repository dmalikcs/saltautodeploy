from settings_base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'db_jenkins',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'dmalik5',
        'PASSWORD': 'unix123',
        'HOST': '192.168.1.102',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '5432',                      # Set to empty string for default.
        'OPTIONS': {'autocommit': True, }
    }
}

DEBUG = True
