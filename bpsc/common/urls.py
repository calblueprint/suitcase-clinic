from django.conf.urls import patterns
from django.conf.urls import url

from bpsc.common.views import LoginView, LogoutView, UserRegistrationView

urlpatterns = patterns(
    '',
    url(r'^register/$', UserRegistrationView.as_view(), name='user_registration'),
    url(r'^login/$', LoginView.as_view(), name='user_login'),
    url(r'^logout/$', LogoutView.as_view(), name='user_logout'),
)

