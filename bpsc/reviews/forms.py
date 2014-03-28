from django import forms
from django.forms.models import modelformset_factory
from bpsc.reviews.models import Review
from django.forms import widgets


# List of services
SERVICES = ['Housing', 'Employment', 'Community Resources', 'Legal', 'Dental', 'Optometry', 'Medical']

class ReviewForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ReviewForm, self).__init__(*args, **kwargs)
		self.fields['service'].widget = widgets.Select(choices=[(s, s) for s in SERVICES])
	class Meta:
		model = Review
		exclude = ('date')
