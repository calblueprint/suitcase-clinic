# Create your views here.
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, FormView, ListView

from bpsc.search.models import (
    Tag, HousingTag, CommunityTag, EmploymentTag, LegalTag, Resource,
    HousingResource, CommunityResource, EmploymentResource, LegalResource
)

class BaseResourceDetailView(DetailView):
    model = Resource

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        return get_object_or_404(self.model, pk=pk)


class HousingResourceDetailView(BaseResourceDetailView):
    model = HousingResource
    context_object_name = 'resource'
    template_name = 'housing_resource_detail.html'


class CommunityResourceDetailView(BaseResourceDetailView):
    model = CommunityResource
    context_object_name = 'resource'
    template_name = 'community_resource_detail.html'


class EmploymentResourceDetailView(BaseResourceDetailView):
    model = EmploymentResource
    context_object_name = 'resource'
    template_name = 'employment_resource_detail.html'


class LegalResourceDetailView(BaseResourceDetailView):
    model = LegalResource
    context_object_name = 'resource'
    template_name = 'legal_resource_detail.html'

class BaseResourceListView(ListView):
    # Sorting will happen with Javascript on the frontend
    model = Resource
    tag = Tag

    def get_context_data(self, **kwargs):
        context = super(BaseResourceListView, self).get_context_data(**kwargs)
        # Retrieve all the related tags for this Resource
        context['tags'] = self.tag.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        # Use: <input type="checkbox" name="resources" value="{{ resource.id }}"/>
        # in template to render checkboxes next to each resource
        selected_resources = request.POST.getlist('resources')
        if not selected_resources:
            messages.error(request, 'No resources selected')
            context = self.get_context_data(object_list=self.object_list)
            return self.render_to_response(context)
        else:
            # TODO: Confirmation Page? Or on this page?
            confirm_url = request.build_absolute_uri() + 'print/'
            resource_params = '&'.join(['?resourceid=%s' % resource_id for resource_id in selected_resources])
            return redirect(confirm_url + resource_params)

class HousingResourceListView(BaseResourceListView):
    model = HousingResource
    context_object_name = 'resource_list'
    template_name = 'housing_resource_list.html'
    tag = HousingTag


class CommunityResourceListView(BaseResourceListView):
    model = CommunityResource
    context_object_name = 'resource_list'
    template_name = 'community_resource_list.html'
    tag = CommunityTag


class EmploymentResourceListView(BaseResourceListView):
    model = EmploymentResource
    context_object_name = 'resource_list'
    template_name = 'employment_resource_list.html'
    tag = EmploymentTag


class LegalResourceListView(BaseResourceListView):
    model = LegalResource
    context_object_name = 'resource_list'
    template_name = 'legal_resource_list.html'
    tag = LegalTag


class BaseResourcePrintView(ListView):
    model = Resource
    tag = Tag

    def get_queryset(self):
        resource_ids = self.request.GET.getlist('resourceid')
        queryset = self.model.objects.filter(pk__in=resource_ids)
        return queryset

    # TODO: Implement POST (printing)
    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return

class HousingResourcePrintView(ListView):
    model = HousingResource
    tag = HousingTag


class CommunityResourcePrintView(ListView):
    model = CommunityResource
    tag = CommunityTag


class EmploymentResourcePrintView(ListView):
    model = EmploymentResource
    tag = EmploymentTag


class LegalResourcePrintView(ListView):
    model = LegalResource
    tag = LegalTag
