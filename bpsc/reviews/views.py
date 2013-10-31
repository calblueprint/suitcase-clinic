from django.views.generic import ListView
from bpsc.reviews.models import Review
from django.views.generic.edit import FormView
from django.db import models
from django.shortcuts import redirect
from django.views.generic import TemplateView
from bpsc.reviews.forms import ReviewForm
from bpsc.reviews.models import Review
from django.shortcuts import render_to_response

from django.forms.models import modelformset_factory
from django.forms.models import BaseModelFormSet

services = ['feet', 'hair']

class ReviewListView(ListView):
	template_name = 'reviews_list.html'
	model = Review

class SubmitReviewListView(TemplateView):
	template_name = 'submit_review.html'
	# form_class = ReviewForm
   
	def form_valid(self, form):
		form.submit_review()
		return super(FormView, self).form_valid(form)	

	def get_context_data(self, **kwargs):
		context = super(SubmitReviewListView, self).get_context_data(**kwargs)
		Review_Formset = modelformset_factory(Review, form=ReviewForm, extra=len(services)) 
		if self.request.method == "GET":
			# a = Review_Formset()
			context['reviewformset'] = Review_Formset()
			# print(context['reviewformset'])
			for form, service in zip(context['reviewformset'], services):
				form.fields['service'].initial = service
			return context
		else: # POST requests
			data = {
				 'form-TOTAL_FORMS': u'1',
				 'form-INITIAL_FORMS': u'0',
				 'form-MAX_NUM_FORMS': u'',
				 'form-0-title': u'',
				 'form-0-pub_date': u'',
			}
			# context['reviewformset'] = Review_Formset(self.request.POST)
			context['reviewformset'] = Review_Formset(data, self.request.POST)
			return context

	# THIS FUNCION IS FOR POST VALIDATION
	def post(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		reviewformset = context['reviewformset']
		if reviewformset.is_valid():
			for entry in reviewformset:
				if entry.cleaned_data.get('rating') != None:
					entry.save()
			# SENDS USERS TO /REVIEWS/REVIEWS
			return redirect('/reviews/reviews')

			# NEED TO FIGURE OUT HOW TO FILTER

			# 	try:
			# 		if entry.cleaned_data.get('rating') != 'None': # and entry.cleaned_data.get('service') != 'None':
			# 			entry.save()
			# 			print "Successful"
			# 	except:
			# 		# Return 
			# 		print "Need to fill out rating and service!!"
			# 		return redirect('/reviews/submit')
			# # SENDS USERS TO /REVIEWS/REVIEWS
			# return redirect('/reviews/submit')
		else:
			return self.render_to_response(context)

