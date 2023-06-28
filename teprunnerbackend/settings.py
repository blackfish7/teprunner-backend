"""
Django settings for teprunnerbackend project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import datetime
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&_*8f-)+lcs2=0mm+b9*=_91wt9i^li7p%h0$2zzw%453q4!1_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',  # 跨域访问
    'user.apps.UserConfig',  # 用户模块
    'teprunner.apps.TeprunnerConfig',
    'channels',  # websocket
    'django_apscheduler',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # 跨域访问
]

ROOT_URLCONF = 'teprunnerbackend.urls'

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

WSGI_APPLICATION = 'teprunnerbackend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

# ---------------- 时区配置开始 ---------------------

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# ---------------- 时区配置结束 ---------------------

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# ---------------- 用户认证鉴权配置开始 ---------------------

AUTH_USER_MODEL = 'user.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'user.authentications.CustomJSONWebTokenAuthentication',
    ),
    'EXCEPTION_HANDLER': 'user.utils.custom_exception_handler',
    'DEFAULT_PAGINATION_CLASS': 'user.pagination.CustomPagination',
    'PAGE_SIZE': 10
}

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=30),
    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(hours=24),
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'user.utils.jwt_response_payload_handler',
    "JWT_AUTH_HEADER_PREFIX": "Bearer"
}

# ---------------- 用户认证鉴权配置开始 ---------------------

# ---------------- 跨域访问配置开始 ---------------------

ALLOWED_HOSTS = ["*"]

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = ()

# ---------------- 跨域访问配置结束 ---------------------


# ---------------- websocket配置开始 ---------------------
ASGI_APPLICATION = 'teprunnerbackend.asgi.application'  # ASGI应用配置

# 一种通信系统
CHANNEL_LAYERS = {
    "default": {
        # InMemoryChannelLayer 内存
        "BACKEND": "channels.layers.InMemoryChannelLayer",

        # RedisChannelLayer Redis（生产建议用这个）
        # "BACKEND": "channels_redis.core.RedisChannelLayer",
        # "CONFIG": {
        #     "hosts": [("127.0.0.1", 6379)],
        # },
    }
}
# ---------------- websocket配置结束 ---------------------

MENU_AUTH = {
    "管理员": [{"id": "teprunner", "name": "接口自动化", "access": True}, {"id": "console", "name": "后台管理", "access": True}],
    "测试": [{"id": "teprunner", "name": "接口自动化", "access": True}, {"id": "console", "name": "后台管理", "access": False}],
    "开发": [{"id": "teprunner", "name": "接口自动化", "access": True}, {"id": "console", "name": "后台管理", "access": False}]
}
