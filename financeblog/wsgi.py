"""
WSGI config for financeblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
>>>>>>> 30c7d3d263f020e02fa82aeeba7f2e4c7a4ec528
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'financeblog.settings')

application = get_wsgi_application()
