# SECURITY WARNING: don't run with debug turned on in production!
from .base import *

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '127.0.0.1:8000', 'localhost:8000',
                 'employa-trail-backend-route-ans2sqb-dev.apps.sandbox-m3.1530.p1.openshiftapps.com']

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000"
]
