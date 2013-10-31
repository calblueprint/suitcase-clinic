from django import forms
from django.forms.models import modelformset_factory
from bpsc.reviews.models import Review

# class ReviewForm(forms.Form):
# 	name = forms.CharField()
# 	message = forms.CharField(widget=forms.Textarea)

# 	def submit_review(self):
# 		# DO SOMETHING
# 	 	# SHOULD ADD THINGS TO REVIEW_LIST		
# 		pass

class ReviewForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ReviewForm, self).__init__(*args, **kwargs)
	class Meta:
		model = Review
		exclude = ('date')

	# DO NOT LET USERS CHANGE SERVICE