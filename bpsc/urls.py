from django.conf.urls import *
from django.contrib import admin
from django.conf.urls.defaults import handler404, handler500
from bpsc.views import search, survey, home, contact
from bpsc.users.views import LoginView, LogoutView
from bpsc.views import HomePageView

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^search/', include('bpsc.search.urls', app_name='search', namespace='search')),
    url(r'^reviews/', include('bpsc.reviews.urls', app_name='reviews', namespace='reviews')),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^$', HomePageView.as_view(), name='home'),
)

handler500 = 'bpsc.views.server_error_500'
handler404 = 'bpsc.views.server_error_404'
