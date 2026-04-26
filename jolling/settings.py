"""
Django settings for jolling project.
"""

import os
from juntagrico import defaults

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('JUNTAGRICO_SECRET_KEY')

DEBUG = os.environ.get("JUNTAGRICO_DEBUG", 'False')=='True'

if not DEBUG:
    ALLOWED_HOSTS = ['my.jolling.de', 'jolling.juntagrico.science']


# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {'format': '[%(asctime)s] %(levelname)s %(message)s'}
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'WARNING',
        },
    },
}


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'juntagrico.apps.JuntagricoAdminConfig',
    'jolling',
    'juntagrico',
    'import_export',
    'polymorphic',
    'adminsortable2',
    'impersonate',
    'crispy_forms',
    'crispy_bootstrap4',
    'django_select2',
    'djrichtextfield',
]

ROOT_URLCONF = 'jolling.urls'

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('JUNTAGRICO_DATABASE_ENGINE','django.db.backends.sqlite3'), 
        'NAME': os.environ.get('JUNTAGRICO_DATABASE_NAME','jolling.db'), 
        'USER': os.environ.get('JUNTAGRICO_DATABASE_USER'), #''junatagrico', # The following settings are not used with sqlite3:
        'PASSWORD': os.environ.get('JUNTAGRICO_DATABASE_PASSWORD'), #''junatagrico',
        'HOST': os.environ.get('JUNTAGRICO_DATABASE_HOST'), #'localhost', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': os.environ.get('JUNTAGRICO_DATABASE_PORT', False), #''', # Set to empty string for default.
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.request',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'juntagrico.context_processors.vocabulary',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ],
            'debug' : True
        },
    },
]

WSGI_APPLICATION = 'jolling.wsgi.application'


LANGUAGE_CODE = 'de'
CURRENCY = "EUR"

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

DATE_INPUT_FORMATS =['%d.%m.%Y',]

AUTHENTICATION_BACKENDS = (
    'juntagrico.util.auth.AuthenticateWithEmail',
    'django.contrib.auth.backends.ModelBackend'
)


MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'impersonate.middleware.ImpersonateMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
]

EMAIL_BACKEND='juntagrico.backends.email.EmailBackend'

EMAIL_HOST = os.environ.get('JUNTAGRICO_EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('JUNTAGRICO_EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('JUNTAGRICO_EMAIL_PASSWORD')
EMAIL_PORT = int(os.environ.get('JUNTAGRICO_EMAIL_PORT', '25' ))
EMAIL_USE_TLS = os.environ.get('JUNTAGRICO_EMAIL_TLS', 'False')=='True'
EMAIL_USE_SSL = os.environ.get('JUNTAGRICO_EMAIL_SSL', 'False')=='True'

ADMINS = [
    ('Admin', os.environ.get('JUNTAGRICO_ADMIN_EMAIL')),
    ('Juntagrico', os.environ.get('JUNTAGRICO_DS_EMAIL'))
]
MANAGERS = ADMINS

WHITELIST_EMAILS = ['']

def whitelist_email_from_env(var_env_name):
    email = os.environ.get(var_env_name)
    if email:
        WHITELIST_EMAILS.append(email.replace('@gmail.com', '(\+\S+)?@gmail.com'))


if DEBUG is True:
    for key in os.environ.keys():
        if key.startswith("JUNTAGRICO_EMAIL_WHITELISTED"):
            whitelist_email_from_env(key)
            


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

IMPERSONATE = {
    'REDIRECT_URL': '/my/profile',
}

IMPORT_EXPORT_EXPORT_PERMISSION_CODE = 'view'

LOGIN_REDIRECT_URL = "/"

"""
    File & Storage Settings
"""
STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage',
    },
}

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

MEDIA_ROOT = 'media'

"""
     Richtext Settings
"""

DJRICHTEXTFIELD_CONFIG = defaults.richtextfield_config(LANGUAGE_CODE)

"""
     Crispy Settings
"""
CRISPY_TEMPLATE_PACK = 'bootstrap4'

"""
     juntagrico Settings
"""
ORGANISATION_NAME = "Jolling e.G."
ORGANISATION_LONG_NAME = "Jolling e.G."
ORGANISATION_ADDRESS = {"name":"Jolling e.G.", 
            "street" : "Jolling",
            "number" : "14",
            "zip" : "83093",
            "city" : "Bad Endorf",
            "extra" : ""}
ORGANISATION_BANK_CONNECTION = {
            "IBAN" : "DE07 7116 0000 0008 1860 49",
            "BIC" : "GENODEF1VRR",
            "NAME" : "Volksbank Raiffeisenbank Rosenheim-Chiemsee eG",
            "ESR" : ""}
CONTACTS = {
    'general': "info@jolling.de"
}
ORGANISATION_WEBSITE = "www.jolling.de"
ADMINPORTAL_NAME = "my.jolling.de"
ADMINPORTAL_SERVER_URL = "my.jolling.de"
SHARE_PRICE = "100"
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")


# Staging
if os.environ.get('JUNTAGRICO_STAGING') == '1':
    ALLOWED_HOSTS.append('jolling-staging.juntagrico.science')
    EMAIL_BACKEND = "django.core.mail.backends.dummy.EmailBackend"
