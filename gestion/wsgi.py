"""
WSGI config for gestion project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

import sys
sys.path.insert(0, '/home/dani/Documentos/practica-Imp/iaw_gestionGN')
from aplicacion.app import app as application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gestion.settings")


application = get_wsgi_application()

