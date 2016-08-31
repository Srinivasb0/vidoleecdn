"""
WSGI config for vidos project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vidos.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from dj_static import Cling, MediaCling
application = Cling(get_wsgi_application())
application = Cling(MediaCling(get_wsgi_application()))

