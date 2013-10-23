from django.conf.urls import *
from bpsc.views import search, survey, home, contact
from django.views.generic import TemplateView # Test

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bpsc.views.home', name='home'),
    # url(r'^bpsc/', include('bpsc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', home, name='home'),
    url(r'^survey/$', survey, name='survey'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^search/', include('bpsc.search.urls', app_name='search', namespace='search')),
    url(r'^users/', include('bpsc.users.urls', app_name='users', namespace='users')),
    #url(r'^reviews/', include('bpsc.reviews.urls', app_name='reviews', namespace='reviews')),
)
