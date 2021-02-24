# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u0000006/data/www/annasoft.site/annasoft')
sys.path.insert(1, '/var/www/u0000006/data/annasoftenv/lib/python3.9/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'annasoft.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()