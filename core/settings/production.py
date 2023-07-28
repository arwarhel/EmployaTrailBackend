# SECURITY WARNING: don't run with debug turned on in production!
from decouple import config

from .base import *

DEBUG = False

ALLOWED_HOSTS = ['employatrail.pythonanywhere.com',
                 'employatrailbackend-arwa-rhel-dev.apps.sandbox-m2.ll9k.p1.openshiftapps.com']

CORS_ALLOWED_ORIGINS = [
    "https://employatrail.pythonanywhere.com",
    "https://employatrailbackend-arwa-rhel-dev.apps.sandbox-m2.ll9k.p1.openshiftapps.com"
]
