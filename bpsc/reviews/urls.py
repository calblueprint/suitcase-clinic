from django.conf.urls import patterns
from django.conf.urls import url

from bpsc.reviews.views import ReviewListView

urlpatterns = patterns(
	'',
	url(r'^reviews/$', ReviewListView.as_view(), name='reviews'),
)