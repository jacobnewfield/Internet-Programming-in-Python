import os, sys
sys.path.append('/home/jakenewf/django-projects')
os.environ['DJANGO_SETTINGS_MODULE'] = 'uwpyassignments.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
