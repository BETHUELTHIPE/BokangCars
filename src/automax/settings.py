

import os
import environ
from pathlib import Path
from distutils.util import strtobool

from django.contrib.messages import constants as messages

# Intialize Environ
env = environ.Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "64x_huhh3q5x)sk!=4ww=r!l68ak6#ho4%1ig*z=s&i*3mklxj"


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if env('DJANGOAPPMODE') == 'Debug' else False
print(f'Application running in debug mode: {DEBUG}')

ALLOWED_HOSTS = ['', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'localflavor',
    'crispy_forms',
    'django_filters',
    'main',
    'users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = 'automax.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'automax.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

#if env('USEDEBUGDB') == 'True':
    #DATABASES = {
        #'default': {
            #'ENGINE': 'django.db.backends.sqlite3',
            #'NAME': BASE_DIR / 'db.sqlite3',
       # }
   # }
#else:
DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd6h9bbu5hklr75',
        'USER': 'ufl1un3t33mqod',
        'PASSWORD': 'p3bf3af752ed31f9773a9050374aed850955a4aa390c93d8989a997b78ecc4a72',
        'HOST': 'c2fdaem59i7d3.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Login Settings
LOGIN_REDIRECT_URL = '/home/'
LOGIN_URL = '/login/'

# Messages Settings
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Media Files (Uploaded Files)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#AWS_ACCESS_KEY_ID = env('BUCKETEER_AWS_ACCESS_KEY_ID')
#AWS_SECRET_ACCESS_KEY = env('BUCKETEER_AWS_SECRET_ACCESS_KEY')
#AWS_S3_REGION_NAME = env('BUCKETEER_AWS_REGION')
#AWS_STORAGE_BUCKET_NAME = env('BUCKETEER_BUCKET_NAME')

# Django Crispy Form Settings
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Email Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Replace 'smtp.example.com' with your SMTP server
EMAIL_PORT = 587  # Corrected port
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'moukangwebethuel@gmail'  # Enter your email address
EMAIL_HOST_PASSWORD = '@Beth23498812'  # Enter your email password
DEFAULT_FROM_EMAIL = 'moukangwebethuel@gmail'  # Set default sender email address

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
