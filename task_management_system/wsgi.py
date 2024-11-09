"""
WSGI config for task_management_system project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_management_system.settings')

application = get_wsgi_application()



"""

BASE_DIR = Path(__file__).resolve().parent.parent
print('-------------------base dir in settings.py',BASE_DIR)
SECRET_KEY = 'django-insecure-x=d!k7@un=3-cm6n1)(4p#l^)$m+^i1ob_rerpsw=)l(#b=ii+'
DEBUG = True
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Karachi'
PASSWORD_RESET_TIMEOUT=900          # 900 Sec = 15 Min
LOGIN_URL = 'login'
USE_I18N = True
USE_TZ = True
WSGI_APPLICATION = 'NIMARFTS.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'account.User'
ROOT_URLCONF = 'NIMARFTS.urls'
CSRF_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_SAMESITE = "Lax"
CORS_ALLOW_CREDENTIALS = True
CORS_EXPOSE_HEADERS = ["Content-Type", "X-CSRFToken"]
CSRF_COOKIE_HTTP_ONLY = True
SESSION_COOKIE_SECURE = False
CSRF_USE_SESSIONS = True
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CSRF_COOKIE_SECURE = False
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'ALLOWALL'
SECURE_CONTENT_TYPE_NOSNIFF = True



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_elasticsearch_dsl',
    'corsheaders', ## for CORS/ also added middleware for cors
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'csp',
    'elastic',
    'pgfts',
    'django_celery_results', 
    'ElasticDocsManager',
    'RecordsManager',
    'account',
    'bookmark',
    'stats',
    'circles',
    'post',
    'notifications',
    'aijobs',
    'live',
    'actions',
    'STTLive',
    'django_filters',
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

CELERY_BROKER_URL = "redis://127.0.0.1:6379"


CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Karachi'
CELERY_RESULT_BACKEND = 'django-db'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


REDIS_HOST = 'localhost'

REDIS_PORT = 6379
REDIS_POOL = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT)


CELERY_BEAT_SCHEDULE = {
    'remove_compressed_media_files': {
        'task': 'RecordsManager.tasks.removeCompressedMediaFiles',
        'schedule': crontab(hour=0, minute=50),
    },
    'delete_old_notifications': {
        'task': 'notifications.tasks.removeOldNotifications',
        'schedule': crontab(hour=2, minute=15),  
    },
    'visualize_data_for_circle': {
        'task': 'circles.tasks.fetch_data_for_circle',
        'schedule': crontab(minute=0),
    },
    'visualize_data_for_department': {
        'task': 'circles.tasks.fetch_data_for_department',
        'schedule': crontab(minute=0),
    },
}

"""
