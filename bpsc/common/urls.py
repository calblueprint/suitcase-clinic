from django.conf.urls import patterns
from django.conf.urls import url

from bpsc.common.views import UserRegistrationView

urlpatterns = patterns(
    '',
    url(r'^register/$', UserRegistrationView.as_view(), name='user_registration')
)

