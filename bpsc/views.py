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
