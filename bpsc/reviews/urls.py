from django.conf.urls import patterns, urls
from bpsc.reviews import views

urlpatterns = patterns(
	'',
	url(r'^index/$', ReviewList.as_view()),#, name='index'),
	# url(r'^create/$', IndexView.as_view(), name='create'),
)