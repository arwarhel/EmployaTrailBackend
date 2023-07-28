# SECURITY WARNING: don't run with debug turned on in production!
from decouple import config

from .base import *

DEBUG = False

ALLOWED_HOSTS = ['employatrail.pythonanywhere.com',
                 'employa-trail-backend-route-ans2sqb-dev.apps.sandbox-m3.1530.p1.openshiftapps.com']

CORS_ALLOWED_ORIGINS = [
    "https://employatrail.pythonanywhere.com",
]
