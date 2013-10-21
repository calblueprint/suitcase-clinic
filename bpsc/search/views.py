# Create your views here.
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.views.generic import ListView

from bpsc.search.models import (
    Tag, HousingTag, CommunityTag, EmploymentTag, LegalTag,
    Resource, HousingResource, CommunityResource,
    EmploymentResource, LegalResource
)

class BaseResourceDetailView(DetailView):
    model = Resource

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        return get_object_or_404(self.model, pk=pk)

class HousingResourceDetailView(BaseResourceDetailView):
    model = HousingResource
    context_object_name = 'housing_resource'
    template_name = 'housing_resource_detail.html'


class CommunityResourceDetailView(BaseResourceDetailView):
    model = CommunityResource
    context_object_name = 'community_resource'
    template_name = 'community_resource_detail.html'


class EmploymentResourceDetailView(BaseResourceDetailView):
    model = EmploymentResource
    context_object_name = 'employment_resource'
    template_name = 'employment_resource_detail.html'


class LegalResourceDetailView(BaseResourceDetailView):
    model = LegalResource
    context_object_name = 'legal_resource'
    template_name = 'legal_resource_detail.html'

class BaseResourceListView(ListView):
    model = Resource
    tag = Tag

