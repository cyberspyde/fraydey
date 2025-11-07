from pathlib import Path
import os.path, os
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
CSRF_TRUSTED_ORIGINS = ['https://fraydey.uz']

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('FRAYDEY_SECRET_KEY', 'django-insecure-demo-key-for-development-only-change-in-production')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Demo Mode Configuration
# Set to True to enable demo mode with pre-populated data and no database writes
DEMO_MODE = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'mnotes.apps.MnotesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'multiselectfield',
    'django_distill',  # Static site generator
]

DJANGORESIZED_DEFAULT_SIZE = [100, 100]
DJANGORESIZED_DEFAULT_QUALITY = 75
DJANGORESIZED_DEFAULT_KEEP_META = True
DJANGORESIZED_DEFAULT_FORCE_FORMAT = 'JPEG'
DJANGORESIZED_DEFAULT_FORMAT_EXTENSIONS = {'JPEG': ".jpg"}
DJANGORESIZED_DEFAULT_NORMALIZE_ROTATION = True

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'mnotes.demo_middleware.DemoModeMiddleware',  # Demo mode middleware
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MarketingNotes.urls'

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
                'mnotes.context_processors.demo_mode',  # Add demo mode context
            ],
        },
    },
]

WSGI_APPLICATION = 'MarketingNotes.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False

SESSION_COOKIE_AGE = 60 * 60 * 24 * 30

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATIC_URL = '/static/'

MEDIA_ROOT = BASE_DIR / 'media'

MEDIA_URL = '/media/'

STATICFILES_DIRS = [BASE_DIR / "static"]

# Django Distill settings for static site generation
DISTILL_DIR = BASE_DIR / 'dist'
DISTILL_PUBLISH = {
    'default': {
        'ENGINE': 'django_distill.backends.filesystem',
        'PATH': str(BASE_DIR / 'dist'),
        'PUBLIC_URL': '/',
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = 'login'


