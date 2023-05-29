from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret("DB_NAME"),
        'USER': get_secret("USER"),
        'PASSWORD': get_secret("PASSWORD"),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]
STATIC_ROOT = BASE_DIR.child('staticfiles')

MEDIAL_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')

#Configuración de email para correo electrónico
#EMAIL SETTINGS
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com' # tipo de correo con el que se enviará
EMAIL_HOST_USER = get_secret("EMAIL")
EMAIL_HOST_PASSWORD = get_secret("PASS_EMAIL")
EMAIL_PORT = 587 # Puerto de correos, normalemente en servidores ubuntú es 587
