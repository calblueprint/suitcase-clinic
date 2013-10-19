from django.views.generic import ListView
from bpsc.reviews.models import Review
from django.views.generic.edit import FormView

class ReviewListView(ListView):
	template_name = 'reviews_list.html'
	model = Review