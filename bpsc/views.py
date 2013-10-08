from django.http import HttpResponse

def search(request):     
	return HttpResponse("Search page")

def survey(request):     
	return HttpResponse("Survey page")

def home(request):
	return HttpResponse("Home page")