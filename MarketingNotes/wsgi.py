"""
WSGI config for MarketingNotes project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""
from whitenoise import WhiteNoise
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MarketingNotes.settings')

application = get_wsgi_application()

AUTOREFRESH = True

application = WhiteNoise(application, root='c:/Users/Peter/Django/MarketingNotes/mnotes/static')
application.add_files('c:/Users/Peter/Django/MarketingNotes/media', prefix='media/')