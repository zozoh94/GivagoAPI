"""
Django settings for givagoapi project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

import environ
env = environ.Env() # set default values and casting
environ.Env.read_env() # reading .env file

ENV = env('ENV', default='DEV')
if ENV == 'PROD':    
    DEBUG = env('DEBUG', default=False)
else:
    DEBUG = env('DEBUG', default=True)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY', default='8sdszf9e@yjt)1v$0!^iq5vioc37tz2zr*4@0qz_=4=3+g=!6i')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

if ENV == 'PROD':
    ALLOWED_HOSTS = ['.givago.co',]
else:
    ALLOWED_HOSTS = ['*',]

SITE_ID = 1

AUTH_USER_MODEL = 'core.User'

# Application definition

INSTALLED_APPS = (
    'bootstrap_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'bootstrap3',
    'corsheaders',
    'allauth',
    'allauth.account',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'rest_auth.registration',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.twitter',
    'import_export',
    'subdomains',
    'embed_video',
    'taggit',
    'taggit_suggest',
    'taggit_serializer',
    'core',
    'advertisement',
    'sponsor',
    'give',
    'actfund'
)

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'subdomains.middleware.SubdomainURLRoutingMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsPostCsrfMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

DATABASES = {
    'default': env.db('DATABASE_URL', default='psql://givago@localhost/givago')
}

GEOIP_PATH = os.path.join(BASE_DIR, "core/geoip")
ALLOWED_COUNTRIES = ['GB']

ROOT_URLCONF = 'givagoapi.urls.api'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "core/templates"),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'givagoapi.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DAB_FIELD_RENDERER = 'django_admin_bootstrapped.renderers.BootstrapFieldRenderer'

from django.contrib import messages

MESSAGE_TAGS = {
            messages.SUCCESS: 'alert-success success',
            messages.WARNING: 'alert-warning warning',
            messages.ERROR: 'alert-danger error'
}


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'givagoapi.paginations.CustomPagination',
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'core.serializers.MyUserDetailsSerializer'
}

ACCOUNT_AUTHENTICATION_METHOD = "username_email"

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True

ACCOUNT_ADAPTER = 'core.adapter.MyAccountAdapter'

OLD_PASSWORD_FIELD_ENABLED = True

from allauth.account.signals import email_confirmation_sent, email_confirmed
from django.dispatch import receiver

@receiver(email_confirmation_sent)
def email_confirmation_sent_(confirmation, **kwargs):
    user = confirmation.email_address.user
    user.is_active = False
    user.save()

@receiver(email_confirmed)
def email_confirmed_(request, email_address, **kwargs):
    user = email_address.user
    user.is_active = True
    user.save()

EMAIL_BACKEND = env.email_url(
    'EMAIL_URL', default='consolemail://')
DEFAULT_FROM_EMAIL = 'noreply@givago.co'
DEFAULT_CONTACT_EMAIL = 'hello@givago.co'

STATICFILES_DIRS = (
    ( "bower_components", os.path.join(BASE_DIR, "bower_components")),
)

if ENV == 'PROD':
    STATIC_URL = "http://static.givago.co/"
    MEDIA_URL = "http://media.givago.co/"
else:
    STATIC_URL = "/static/"
    MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
STATIC_ROOT = os.path.join(BASE_DIR, "static")

SUBDOMAIN_URLCONFS = {
    'api': 'givagoapi.urls.api',
    'sponsor' : 'sponsor.urls',
    'admin' : 'givagoapi.urls.admin',
}

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'

SOCIALACCOUNT_PROVIDERS = \
    {'facebook':
       {'VERIFIED_EMAIL': True}}
SOCIALACCOUNT_ADAPTER = 'core.adapter.MySocialAccountAdapter'

PEANUTS_LAB_ACTFUND_APP_ID = '2b2ce92a9b0f82073d9bfdcd7bb5cb97'
PEANUTS_LAB_ACTFUND_TRANSACTION_ID = '2c80c533b21cc83e8f1bf813fd7fffd2'
PEANUTS_LAB_IPS = [
    '75.101.154.153',
    '54.243.235.176',
    '54.243.210.15',
    '54.243.204.6',
    '54.243.150.156',
    '54.243.150.126',
    '54.243.149.248',
    '54.243.149.247',
    '54.243.146.21',
    '54.243.143.97',
    '50.19.92.139',
    '50.17.194.132',
    '50.17.193.185',
    '50.17.191.62',
    '50.17.191.143',
    '50.17.190.69',
    '50.17.190.174',
    '50.17.189.251',
    '50.17.189.201',
    '50.17.189.138',
    '50.17.187.32',
    '50.17.187.218',
    '50.17.187.192',
    '50.17.187.145',
    '50.17.186.7',
    '50.17.186.39',
    '50.17.184.98',
    '50.17.184.153',
    '50.17.182.38',
    '50.17.182.19',
    '50.17.182.17',
    '50.17.181.130',
    '50.17.181.118',
    '50.17.181.11',
    '50.16.250.192',
    '50.16.249.58',
    '50.16.249.162',
    '50.16.245.185',
    '50.16.243.67',
    '50.16.241.60',
    '50.16.239.186',
    '50.16.236.39',
    '23.21.123.40',
    '184.73.254.159',
    '184.73.254.133',
    '184.73.250.161',
    '184.73.249.128',
    '184.73.244.77',
    '184.73.196.208',
    '184.73.166.67',
    '184.73.158.48',
    '184.73.153.111',
    '184.72.230.119',
    '184.72.222.51',
    '184.72.222.104',
    '184.72.221.219',
    '174.129.37.199',
    '174.129.242.30',
    '174.129.240.137',
    '174.129.238.17',
    '174.129.237.1',
    '174.129.22.190',
    '174.129.219.230',
    '174.129.209.23',
    '174.129.209.2',
    '107.22.164.69',
    '107.22.164.67',
    '107.22.164.59',
    '107.22.164.55',
    '107.22.164.53',
    '107.22.164.5',
    '107.22.162.83',
    '107.22.160.89',
    '107.22.160.31',
    '107.22.160.14',
    '107.20.248.88',
    '107.20.246.140',
    '107.20.235.89',
    '107.20.201.76',
    '107.20.152.198'
]

# Caches
environ.Env.CACHE_SCHEMES.update({'uwsgicache': 'uwsgicache.UWSGICache'})
CACHES = {
    'default': env.cache('CACHE_URL', default='locmemcache://givagoapi'),
}
