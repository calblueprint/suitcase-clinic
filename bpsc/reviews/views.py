from django.views.generic import ListView
from bpsc.reviews.models import Review
from django.views.generic.edit import FormView
from django.db import models
from bpsc.reviews import SubmitReviewForm
import datetime


class ReviewListView(ListView):
	template_name = 'reviews_list.html'
	model = Review

class SubmitReviewListView(FormView):
	template_name = 'submit_review.html'
	form_class = SubmitReviewForm
	success_url = '/reviews'

	def form_valid(self, form):
		form.submit_review()
		return super(ContactView, self).form_valid(form)
		
