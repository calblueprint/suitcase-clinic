from django.conf.urls import *
from django.contrib import admin

from bpsc.views import search, survey, home, contact

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^survey/$', survey, name='survey'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^search/', include('bpsc.search.urls', app_name='search', namespace='search')),
    url(r'^users/', include('bpsc.users.urls', app_name='users', namespace='users')),
    url(r'^reviews/', include('bpsc.reviews.urls', app_name='reviews', namespace='reviews')),
    url(r'^admin/doccl/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
)
