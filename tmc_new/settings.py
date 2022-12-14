"""
Django settings for tmc_new project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os

import pymysql as pymysql

pymysql.install_as_MySQLdb()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-inm1-d)u&zie_*1rk@*+zuucf*)-gg@75ku2^ezs7%^5gds*=e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['87.255.194.204', 'mdc.1312.kz', '127.0.0.1', '192.168.2.12']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tmc_new',
    'rest_framework',
    'corsheaders',

    'django_extensions',
    'crispy_forms',
    'apps.geo',
    'apps.crm',
    'apps.organizations',
    'apps.handbook',
    'apps.surveys',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:8080",
    "http://mdc.1312.kz:1002",
    "https://mdc.1312.kz:1002",
    "https://eu.cloudcall.kz",
    "http://localhost:8080",
    "http://192.168.2.5:8081",
]

ROOT_URLCONF = 'tmc_new.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

REST_FRAMEWORK = {
    'FORM_METHOD_OVERRIDE': None,
    'FORM_CONTENT_OVERRIDE': None,
    'FORM_CONTENTTYPE_OVERRIDE': None
}


WSGI_APPLICATION = 'tmc_new.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'bp_dev',
       'USER': 'postgres',
       'PASSWORD': 'lx3zui@U~ab|mT@{6d',
       'HOST': '194.110.55.62',
       'PORT': '5432',
   },
    'tmc': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'bpm_cc_hostedcc_ru',                      # Or path to database file if using sqlite3.
        'USER': 'bpm_cc_hostedcc_',                      # Not used with sqlite3.
        'PASSWORD': 'd7rHJDFK378',                  # Not used with sqlite3.
        'HOST': '185.102.73.206',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '33307',
    },
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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



STATICFILES_DIRS = [
    str(BASE_DIR / "static"),
]
STATIC_URL = "/static/"
STATIC_ROOT = str(BASE_DIR / "static_root")

MEDIA_ROOT = BASE_DIR / "static/media/"
MEDIA_URL = '/media/'



# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
