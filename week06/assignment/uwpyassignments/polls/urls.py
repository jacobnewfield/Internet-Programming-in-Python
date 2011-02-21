from django.conf.urls.defaults import *

# Comment out the next two lines to disable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('polls.views',
    (r'^$', 'index'),
    (r'^(?P<poll_id>\d+)/$', 'detail'),
    (r'^(?P<poll_id>\d+)/results/$', 'results'),
    (r'^(?P<poll_id>\d+)/vote/$', 'vote'),
    (r'^(?P<poll_id>\d+)/json/$', 'json_results'),
)
