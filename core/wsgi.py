"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from core.settings import set_settings_env

from django.core.wsgi import get_wsgi_application

set_settings_env()

application = get_wsgi_application()
