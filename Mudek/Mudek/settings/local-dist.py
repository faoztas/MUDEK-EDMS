# Local Django
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/validators/

AUTH_PASSWORD_VALIDATORS = []

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Domain
DOMAIN_BACKEND = 'http://127.0.0.1:8000'

# Email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
