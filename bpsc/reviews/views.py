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
		# Review_Formset = modelformset_factory(Review, form=ReviewForm, extra=len(services)) 
		if self.request.method == "GET":
			# a = Review_Formset()
			# print(context['reviewformset'])
			context['reviewform'] = ReviewForm()
			# print(context['reviewformset'])
			# for form, service in zip(context['reviewform'], services):
			# 	form.field['service'].initial = service
			return context
		else: # POST requests
			# data = {
			# 	 'form-TOTAL_FORMS': u'5',
			# 	 'form-INITIAL_FORMS': u'5',
			# 	 'form-MAX_NUM_FORMS': u'6',
			# 	 'form-0-title': u'TITLE1',
			# 	 'form-0-pub_date': u'',
			# }
			context['reviewform'] = ReviewForm(self.request.POST)
			# context['reviewform'] = Review_Formset(data, self.request.POST)
			return context

	# THIS FUNCION IS FOR POST VALIDATION
	def post(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		reviewform = context['reviewform']
		if reviewform.is_valid():
			# try:
			reviewform.save()
			# messages.success(request, 'Review was successfully submitted!')
			messages.success(request, 'Review was successfully submitted!')
			return redirect('/reviews/reviews')

		#except:

			
			# SENDS USERS TO /REVIEWS/REVIEWS
			

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

