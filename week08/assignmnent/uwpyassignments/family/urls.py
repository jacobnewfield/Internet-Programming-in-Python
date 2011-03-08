from django.conf.urls.defaults import *

# Comment out the next two lines to disable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('family.views',
    (r'^$', 'index'),
    (r'^(?P<family_id>\d+)/$', 'family'),
    (r'^contact/(?P<contact_id>\d+)/$', 'contact')
)
