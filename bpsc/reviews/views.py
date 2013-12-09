from django.views.generic import ListView
from django.views.generic import TemplateView
from bpsc.reviews.models import Review
from django.views.generic.edit import FormView
from django.db import models
from django.shortcuts import redirect
from bpsc.reviews.forms import ReviewForm
from django.shortcuts import render_to_response
from django.shortcuts import render

from django.forms.models import modelformset_factory
from django.forms.models import BaseModelFormSet

from django.contrib import messages

def reviews(request):
	return render(request, 'reviews.html')

class ReviewListView(ListView):
	template_name = 'reviews_list.html'
	model = Review

class SubmitReviewListView(TemplateView):
	template_name = 'base_submit_review.html'
	# form_class = ReviewForm
   
	def form_valid(self, form):
		form.submit_review()
		return super(FormView, self).form_valid(form)	

	def get_context_data(self, **kwargs):
		context = super(SubmitReviewListView, self).get_context_data(**kwargs)
		if self.request.method == "GET":
			context['reviewform'] = ReviewForm()
			return context
		else: # POST requests
			context['reviewform'] = ReviewForm(self.request.POST)
			return context

	# THIS FUNCION IS FOR POST VALIDATION
	def post(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		reviewform = context['reviewform']
		if reviewform.is_valid():
			reviewform.save()
			messages.success(request, 'Review was successfully submitted!')
			return redirect('/reviews/reviews')
		else:
			return self.render_to_response(context)

