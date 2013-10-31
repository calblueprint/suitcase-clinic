from django.conf.urls import patterns
from django.conf.urls import url

from bpsc.reviews.views import *

urlpatterns = patterns(
	'',
	url(r'^reviews/$', ReviewListView.as_view(), name='reviews_list'),
	# url(r'^new/$', NewReviewView.as_view(), name='new'),
    url(r'^$', reviews, name='reviews'),
	url(r'^submit/$', SubmitReviewListView.as_view()),
)