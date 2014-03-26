from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

def server_error_500(request):
	return render(request, '500.html')

def server_error_404(request):
	return render(request, '404.html')
