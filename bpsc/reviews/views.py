from django.views.generic import ListView
from bpsc.reviews import Review

class ReviewList(ListView):
	model = Review