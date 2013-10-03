from django.conf.urls.defaults import *
from mysite.views import hello

urlpatterns = patterns('',
    ('^/$', home), )
    ('^survey/$', survey), )
    ('^search/$', search), )
