"""
WSGI config for schedulesite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import sys
sys.path.append("/opt/app/schedulesite")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
