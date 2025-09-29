# File: twitter_project/app_config/settings_pythonanywhere.py
import os
from .settings import *

# PythonAnywhere specific settings
DEBUG = False
ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']  # Ganti dengan username Anda

# Database - PythonAnywhere hanya support MySQL untuk free account
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'yourusername$twitter_db',  # Format: username$dbname
        'USER': 'yourusername',             # Username PythonAnywhere Anda
        'PASSWORD': 'your_db_password',     # Password database
        'HOST': 'yourusername.mysql.pythonanywhere-services.com',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = '/home/yourusername/twitter_project/staticfiles'

# Media files  
MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/yourusername/twitter_project/media'

# Security
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')