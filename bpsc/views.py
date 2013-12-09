from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render

def search(request):     
	return render(request, 'search.html')

def survey(request):     
	return render(request, 'survey.html')

def home(request):
	return render(request, 'home.html')

def contact(request):
	return render(request, 'contact.html')

def server_error_500(request):
	return render(request, '500.html')

def server_error_404(request):
	return render(request, '404.html')
