# Create your views here.
from django.contrib import messages
from django.http import QueryDict
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, ListView

from bpsc.search.forms import ResourcePrintForm, MapForm
from bpsc.lib import send_suitcase_email
from bpsc.search.models import (
    Tag, HousingTag, CommunityTag, EmploymentTag, LegalTag, Resource,
    HousingResource, CommunityResource, EmploymentResource, LegalResource
)
from bpsc.wysiwyg.models import Post

from gmapi import maps
from gmapi.forms.widgets import GoogleMap
from django import forms
from django.shortcuts import render_to_response

class BaseResourceDetailView(DetailView):
    model = Resource

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        return get_object_or_404(self.model, pk=pk)

    def get_context_data(self, **kwargs):
        context = super(BaseResourceDetailView, self).get_context_data(**kwargs)

        gmap = maps.Map(opts = {
            'center': maps.LatLng(self.object.latitude, self.object.longitude),
            'mapTypeId': maps.MapTypeId.ROADMAP,
            'zoom': 12,
            'mapTypeControlOptions': {
                 'style': maps.MapTypeControlStyle.DROPDOWN_MENU
            },
        })

        marker = maps.Marker(opts = {
            'map': gmap,
            'position': maps.LatLng(self.object.latitude, self.object.longitude),
        })
        maps.event.addListener(marker, 'mouseover', 'myobj.markerOver')
        maps.event.addListener(marker, 'mouseout', 'myobj.markerOut')
        info = maps.InfoWindow({
            'content': 'Hello!',
            'disableAutoPan': True
        })
        info.open(gmap, marker)

        context['form'] = MapForm(initial={'map': gmap})
        return context

class HousingResourceDetailView(BaseResourceDetailView):
    model = HousingResource
    context_object_name = 'resource'
    template_name = 'housing_resource_detail.html'
    resource_type = 'Housing'


class CommunityResourceDetailView(BaseResourceDetailView):
    model = CommunityResource
    context_object_name = 'resource'
    template_name = 'community_resource_detail.html'
    resource_type = 'Community'


class EmploymentResourceDetailView(BaseResourceDetailView):
    model = EmploymentResource
    context_object_name = 'resource'
    template_name = 'employment_resource_detail.html'
    resource_type = 'Employment'


class LegalResourceDetailView(BaseResourceDetailView):
    model = LegalResource
    context_object_name = 'resource'
    template_name = 'legal_resource_detail.html'
    resource_type = 'Legal'

class BaseResourceListView(ListView):
    # Sorting will happen with Javascript on the frontend
    model = Resource
    tag = Tag
    resource_type = 'Base'

    def get_context_data(self, **kwargs):
        context = super(BaseResourceListView, self).get_context_data(**kwargs)
        tags = self.tag.objects.all()
        tag_dict = {t.tag_type: [] for t in tags}
        for t in tags:
            values_list = tag_dict.get(t.tag_type)
            values_list.append(t.value)
            tag_dict[t.tag_type] = values_list
        # Tags is a dictionary that maps a tag_type to all of its distinct values
        context['tags'] = tag_dict
        if self.request.method == 'POST':
            context['print_form'] = ResourcePrintForm(self.request.POST)
        else:
            context['print_form'] = ResourcePrintForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        # Use: <input type="checkbox" name="resources" value="{{ resource.id }}"/>
        # in template to render checkboxes next to each resource
        context = self.get_context_data(object_list=self.object_list)
        print_form = context['print_form']
        selected_resources = request.POST.getlist('resources')
        if print_form.is_valid():
            if not selected_resources:
                messages.error(request, 'No resources selected.')
                return self.render_to_response(context)
            # Eliminate any duplicate resource ids, possibly from selecting a listing of the week
            resource_params = '&'.join(['rid=%s' % resource_id for resource_id in sorted(set(selected_resources))])
            print_url = request.build_absolute_uri() + 'print/?' + resource_params
            for resource in context['resource_list']:
                resource.num_used += 1
                resource.save()
            email_context_dict = {
                'client_name': print_form.cleaned_data.get('client_name'),
                'client_phone': print_form.cleaned_data.get('client_phone'),
                'client_email': print_form.cleaned_data.get('client_email'),
                'resource_url': print_url,
                'resource_type': self.resource_type,
            }
            send_suitcase_email('print_resource.yml', email_context_dict,
                    [print_form.cleaned_data.get('user_email')])
            messages.success(request, 'Resources use logged successfully.')
            return redirect(print_url)
        else:
            messages.error(request, 'Error in client logging form. Please try again.')
            return self.render_to_response(context)

class HousingResourceListView(BaseResourceListView):
    model = HousingResource
    context_object_name = 'resource_list'
    template_name = 'housing_resource_list.html'
    resource_type = 'Housing'
    tag = HousingTag

class CommunityResourceListView(BaseResourceListView):
    model = CommunityResource
    context_object_name = 'resource_list'
    template_name = 'community_resource_list.html'
    resource_type = 'Community'
    tag = CommunityTag


class EmploymentResourceListView(BaseResourceListView):
    model = EmploymentResource
    context_object_name = 'resource_list'
    template_name = 'employment_resource_list.html'
    resource_type = 'Employment'
    tag = EmploymentTag

    def get_context_data(self, **kwargs):
        context = super(EmploymentResourceListView, self).get_context_data(**kwargs)
        context['listings_of_the_week'] = EmploymentResource.objects.filter(listing_of_the_week=True)
        return context


class LegalResourceListView(BaseResourceListView):
    model = LegalResource
    context_object_name = 'resource_list'
    template_name = 'legal_resource_list.html'
    resource_type = 'Legal'
    tag = LegalTag


class GovernmentResourceView(DetailView):
    model = Post
    context_object_name = 'resource'
    template_name = 'government_resource.html'
    resource_type = 'Government'

    def get_object(self, **kwargs):
        return Post.objects.get(url='search:government')


class BaseResourcePrintView(ListView):
    model = Resource
    context_object_name = 'resource_list'
    tag = Tag

    def dispatch(self, request, *args, **kwargs):
        self.is_logged = request.GET.get('logged') == 'true'
        return super(BaseResourcePrintView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        # Get the resources with the IDs in the url querystring
        resource_ids = self.request.GET.getlist('rid')
        queryset = self.model.objects.filter(pk__in=resource_ids)
        return queryset


class HousingResourcePrintView(BaseResourcePrintView):
    model = HousingResource
    template_name = 'housing_resource_print.html'
    list_url = 'search:housing_list'
    tag = HousingTag
    resource_type = 'Housing'


class CommunityResourcePrintView(BaseResourcePrintView):
    model = CommunityResource
    template_name = 'community_resource_print.html'
    list_url = 'search:community_list'
    tag = CommunityTag
    resource_type = 'Community'


class EmploymentResourcePrintView(BaseResourcePrintView):
    model = EmploymentResource
    template_name = 'employment_resource_print.html'
    list_url = 'search:employment_list'
    tag = EmploymentTag
    resource_type = 'Employment'


class LegalResourcePrintView(BaseResourcePrintView):
    model = LegalResource
    template_name = 'legal_resource_print.html'
    list_url = 'search:legal_list'
    tag = LegalTag
    resource_type = 'Legal'
