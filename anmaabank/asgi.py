"""
ASGI config for anmaabank project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
import django.core.handlers.wsgi
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "anmaabank.settings")

application = get_asgi_application()

application = django.core.handlers.wsgi.WSGIHandler()