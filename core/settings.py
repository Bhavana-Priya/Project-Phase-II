from pathlib import Path
import os
#import django_heroku

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-d*2eog&xs-3+50xd0c(i+636^(fs38*si4df68-fn80%kf#+%%'

DEBUG = True
LOGIN_URL = '/login/'
AUTH_USER_MODEL = 'app.User'  # Replace 'app' with your actual app name if different
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]
MONGO_URI = 'mongodb+srv://Priya_Sharma:EItoPPX5sqbIF0sT@cluster0.gcjsnpe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
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

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "priyasharma98533@gmail.com"  # Replace with your email
EMAIL_HOST_PASSWORD = "wdus ttui ofhj muag"  # Use an App Password (not your real password)

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
DATABASES = {
    'default': {
        'ENGINE': 'djongo',  # Ensure you have installed `djongo`
        'NAME': 'Stock_Prediction',
        'ENFORCE_SCHEMA': False,
        'HOST': 'localhost',  # Or your MongoDB host
        'PORT': 27017,        # Default MongoDB port
        'CLIENT': {
            'host': 'mongodb+srv://Priya_Sharma:EItoPPX5sqbIF0sT@cluster0.gcjsnpe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0',  # Change if using a cloud MongoDB
        }
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'app/static',  
]
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_URL = '/static/'

# For development
import os
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#django_heroku.settings(locals())