from django.conf.urls import patterns
from django.conf.urls import url

from bpsc.users.views import LoginView, LogoutView, UserRegistrationView

urlpatterns = patterns(
    '',
    url(r'^register/$', UserRegistrationView.as_view(), name='register'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
)

