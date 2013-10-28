from django import forms

class ReviewForm(forms.Form):
	name = forms.CharField()
	message = forms.CharField(widget=forms.Textarea)

	def submit_review(self):
		# DO SOMETHING
		pass