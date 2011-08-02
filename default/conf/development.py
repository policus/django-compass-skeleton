from conf.common import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'default',
        'USER': 'default',
        'PASSWORD': 'default',
        'HOST': '',
        'PORT': '',
    }
}

INTERNAL_IPS = ('127.0.0.1', 'active.lo',)

# include debug_toolbar
INSTALLED_APPS += ('debug_toolbar',)
MIDDLEWARE_CLASSES +=('debug_toolbar.middleware.DebugToolbarMiddleware',)