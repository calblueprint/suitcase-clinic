from django.http import HttpResponse
from django.shortcuts import render

def search(request):     
	return HttpResponse("Search page")

def survey(request):     
	return HttpResponse("Survey page")

def home(request):
	# Test rendering of .html pages
	return render(request, '/Users/vincenttian/Desktop/workspace/Blueprint/bpsc/templates/home.html')
	# return HttpResponse("Home page")

def contact(request):
	return HttpResponse("Contact page")
