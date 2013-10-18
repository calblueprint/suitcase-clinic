from django.views.generic import ListView
from bpsc.reviews.models import Review

class ReviewListView(ListView):
	template_name = 'reviews_list.html'
	model = Review