from django.conf.urls import patterns
from django.conf.urls import url

from bpsc.reviews.views import *

urlpatterns = patterns(
	'',
	url(r'^reviews/$', ReviewListView.as_view(), name='reviews'),
	# url(r'^new/$', NewReviewView.as_view(), name='new'),
	url(r'^submit/$', SubmitReviewListView.as_view()),
)