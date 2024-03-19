"""
Django settings for goatsmart project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ww=cheo_7t+9jl-62q#mldsk6*4i4k9opbg&$5oxr&zpv9g=6j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',    
    'user',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'goatsmart.urls'

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

WSGI_APPLICATION = 'goatsmart.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# import pyrebase

# # # config = {
# #   apiKey: "AIzaSyA11nBw9bitqtEUv5U-6ztPzuFaCHgrj_4",
# #   authDomain: "goatsmart-isis.firebaseapp.com",
# #   databaseURL: "https://goatsmart-isis-default-rtdb.firebaseio.com",
# #   projectId: "goatsmart-isis",
# #   storageBucket: "goatsmart-isis.appspot.com",
# #   messagingSenderId: "775920845294",
# #   appId: "1:775920845294:web:da1b415f2cdc03840f4eff",
# #   measurementId: "G-F3EDNBVSYF"
# # };

# config = {
#     "apiKey": "AIzaSyA11nBw9bitqtEUv5U-6ztPzuFaCHgrj_4",
#     "authDomain": "goatsmart-isis.firebaseapp.com",
#     "databaseURL": "https://goatsmart-isis-default-rtdb.firebaseio.com",
#     "projectId": "goatsmart-isis",
#     "storageBucket": "goatsmart-isis.appspot.com",
#     "messagingSenderId": "775920845294",
#     "appId": "1:775920845294:web:da1b415f2cdc03840f4eff",
#     "measurementId": "G-F3EDNBVSYF"
# }

# firebase = pyrebase.initialize_app(config)
# authe = firebase.auth()
# db = firebase.database()
