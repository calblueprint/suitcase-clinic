from django.conf.urls import patterns
from django.conf.urls import url

from bpsc.search.views import (
    HousingResourceListView, CommunityResourceListView,
    EmploymentResourceListView, LegalResourceListView,
    HousingResourceDetailView, CommunityResourceDetailView,
    EmploymentResourceDetailView, LegalResourceDetailView,
    HousingResourcePrintView, CommunityResourcePrintView,
    EmploymentResourcePrintView, LegalResourcePrintView,
    GovernmentResourceView, BatchHousingResourceDetailView
)

from bpsc.static_pages.views import (
    ResumeResourceView, CoverLetterResourceView,
    MentalResourceView, DentalResourceView,
    MedicalResourceView
)

urlpatterns = patterns(
    '',
    url(r'^housing/(?P<pk>\d+)/(?P<slug>[-\w\d]+)/$', HousingResourceDetailView.as_view(), name='housing_detail'),
    url(r'^housing/batch/(?P<pk>\d+)/(?P<slug>[-\w\d]+)/$', BatchHousingResourceDetailView.as_view(), name='batch_housing_detail'),
    url(r'^community/(?P<pk>\d+)/(?P<slug>[-\w\d]+)/$', CommunityResourceDetailView.as_view(), name='community_detail'),
    url(r'^community/mental/$', MentalResourceView.as_view(), name='community_mental'),
    url(r'^community/dental/$', DentalResourceView.as_view(), name='community_dental'),
    url(r'^community/medical/$', MedicalResourceView.as_view(), name='community_medical'),
    url(r'^employment/(?P<pk>\d+)/(?P<slug>[-\w\d]+)/$', EmploymentResourceDetailView.as_view(), name='employment_detail'),
    url(r'^employment/resume/$', ResumeResourceView.as_view(), name='employment_resume'),
    url(r'^employment/cover_letter/$', CoverLetterResourceView.as_view(), name='employment_cover_letter'),
    url(r'^legal/(?P<pk>\d+)/(?P<slug>[-\w\d]+)/$', LegalResourceDetailView.as_view(), name='legal_detail'),
    url(r'^housing/print/$', HousingResourcePrintView.as_view(), name='housing_print'),
    url(r'^community/print/$', CommunityResourcePrintView.as_view(), name='community_print'),
    url(r'^employment/print/$', EmploymentResourcePrintView.as_view(), name='employment_print'),
    url(r'^legal/print/$', LegalResourcePrintView.as_view(), name='legal_print'),
    url(r'^housing/$', HousingResourceListView.as_view(), name='housing_list'),
    url(r'^community/$', CommunityResourceListView.as_view(), name='community_list'),
    url(r'^employment/$', EmploymentResourceListView.as_view(), name='employment_list'),
    url(r'^legal/$', LegalResourceListView.as_view(), name='legal_list'),
    url(r'^government/$', GovernmentResourceView.as_view(), name='government'),
)
