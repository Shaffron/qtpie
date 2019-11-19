import os

from django.core.exceptions import ImproperlyConfigured
from dotenv import (
    find_dotenv,
    load_dotenv,
)

load_dotenv(find_dotenv(), encoding='utf-8')

def get_env_variable(var_name, default=None):
    try:
        return os.environ[var_name]

    except KeyError:
        if default is None:
            error_msg = f'필수 환경 변수 {var_name}가 설정되지 않았습니다.'
            raise ImproperlyConfigured(error_msg)

        return default

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SECRET_KEY = get_env_variable('SECRET_KEY')

ALLOWED_HOSTS = ['*']

ADMINS = [
    (get_env_variable('ADMIN_NAME'), get_env_variable('ADMIN_EMAIL')),
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MY_APPS = [
    'account',
    'contemplate',
    'core',
]

THIRD_PARTY_APPS = [
    'django_crontab',
]

INSTALLED_APPS += MY_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'qtpie.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django_settings_export.settings_export',
            ],
        },
    },
]

APP_DIRS = True

WSGI_APPLICATION = 'qtpie.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_env_variable('DEFAULT_DB_NAME'),
        'USER': get_env_variable('DEFAULT_DB_USER'),
        'PASSWORD': get_env_variable('DEFAULT_DB_PASSWORD'),
        'HOST': get_env_variable('DEFAULT_DB_HOST'),
        'PORT': get_env_variable('DEFAULT_DB_PORT')
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

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'core/static'),
]

STATICFILES_VERSION = get_env_variable('STATICFILES_VERSION')

MEDIA_URL = '/media/'

MEDIA_ROOT = 'media'

# Crontab
CRONJOBS = [
    # crawling at monday ~ saturday 00:05 AM
    ('5 0 * * 1-6', 'core.cron.daily_crawling'),
]

# Export settings for template
SETTINGS_EXPORT = [
    'STATICFILES_VERSION',
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard' : {
            'format': '[%(asctime)s] [%(levelname)s] %(message)s (%(filename)s:%(lineno)d)',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
        'mail': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'standard',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': f'{BASE_DIR}/logs/django.log',
            'maxBytes': 10485760,
            'backupCount': 10,
            'formatter': 'standard',
        },
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler'
        }
    },
    'loggers': {
        '': {
            # root logger
            'handlers': ['file', 'console'],
            'level': 'INFO',
        },

        # ALLOWED_HOSTS alarm disable
        'django.security.DisallowedHost': {
            'handler': ['null'],
            'propagate': False,
        }
    }
}