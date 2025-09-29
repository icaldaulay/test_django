import os
from .settings import *

# PythonAnywhere specific settings
DEBUG = False
ALLOWED_HOSTS = ['IcalDaulay.pythonanywhere.com']  # Sesuai username PythonAnywhere Anda

# Database - PythonAnywhere MySQL configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'IcalDaulay$twitter_db',
        'USER': 'IcalDaulay',
        'PASSWORD': 'ical1406',
        'HOST': 'IcalDaulay.mysql.pythonanywhere-services.com',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# Static files - Update path sesuai struktur folder Anda
STATIC_URL = '/static/'
STATIC_ROOT = '/home/IcalDaulay/test_django/twitter_project/staticfiles'

# Media files - Update path sesuai struktur folder Anda
MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/IcalDaulay/test_django/twitter_project/media'

# Security settings
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Session security
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Time zone
USE_TZ = True
TIME_ZONE = 'Asia/Jakarta'

print("✅ PythonAnywhere settings loaded successfully!")