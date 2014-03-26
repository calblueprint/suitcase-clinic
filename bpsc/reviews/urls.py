from django.conf.urls import patterns
from django.conf.urls import url

from bpsc.reviews.views import ReviewListView, SubmitReviewListView

urlpatterns = patterns('',
	url(r'^submit/$', SubmitReviewListView.as_view(), name='submit_review'),
	url(r'^$', ReviewListView.as_view(), name='reviews_list'),
)
