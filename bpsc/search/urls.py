from django.conf.urls import patterns
from django.conf.urls import url

from bpsc.users.views import (
    HousingResourceListView, CommunityResourceListView,
    EmploymentResourceListView, LegalResourceListView,
    HousingResourceDetailView, CommunityResourceDetailView,
    EmploymentResourceDetailView, LegalResourceDetailView
)

urlpatterns = patterns(
    '',
    url(r'^housing/(?P<pk>\d+)/(?P<slug>[-\w\d]+/$', HousingResourceDetailView.as_view(), name='housing_detail'),
    url(r'^community/(?P<pk>\d+)/(?P<slug>[-\w\d]+/$', CommunityResourceDetailView.as_view(), name='community_detail'),
    url(r'^employment/(?P<pk>\d+)/(?P<slug>[-\w\d]+/$', EmploymentResourceDetailView.as_view(), name='employment_detail'),
    url(r'^legal/(?P<pk>\d+)/(?P<slug>[-\w\d]+/$', LegalResourceDetailView.as_view(), name='legal_detail'),
    url(r'^housing/$', HousingResourceListView.as_view(), name='housing_list'),
    url(r'^community/$', CommunityResourceListView.as_view(), name='community_list'),
    url(r'^employment/$', EmploymentResourceListView.as_view(), name='employment_list'),
    url(r'^legal/$', LegalResourceListView.as_view(), name='legal_list'),
)

