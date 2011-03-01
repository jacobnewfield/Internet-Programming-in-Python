import sys
sys.path.append('/home/jakenewf/django-projects')
sys.path.append('/home/jakenewf/django-projects/uwpyassignments')

from django.conf.urls.defaults import *

# Comment out the next two lines to disable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('views',
    (r'^$', 'index'),
    (r'^polls/', include('polls.urls')),
    (r'^families/', include('family.urls')),
    (r'^admin/', include(admin.site.urls)),
)
