from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-vn2mcv$0!v0ss!dmbi_2zs%)vgc1lfxy+ok7c9@kpi^3-(jl_^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'relatorios',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portal_relatorios_vida.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'portal_relatorios_vida.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    # O banco padrão (Local) vai guardar os Usuários, Permissões e Sessões
    'default':{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },

    # O banco secundário será usado APENAS para leitura das views
    'viewsOracle': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'siga',
        'USER': 'sigaofc',
        'PASSWORD': 'sigaofc',
        'HOST': '173.29.21.7',
        'PORT': '1521',
        'CONN_MAX_AGE': 600,
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = 'static/'
import os 
# Diz ao Django onde ele deve juntar todas as imagens para o servidor ler
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Diz ao WhiteNoise para otimizar as imagens
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = '/login/' 
LOGOUT_URL = 'login'

# Configuração de logs de erro (produção)
import os 

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'detalhado': {
            'format': '[{asctime}] {levelname} [{name}:{lineno}] - {message}',
            'style': '{',
            'datefmt': '%d/%m/%Y %H:%M:%S',
        },
    },
    'handlers': {
        'arquivo_log': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'portal_erros.log'), #Nome do arquivo gerado
            'formatter': 'detalhado',
        },
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'detalhado',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['arquivo_log', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'relatorios': { # Captura erros específicos do app
            'handlers': ['arquivo_log', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}