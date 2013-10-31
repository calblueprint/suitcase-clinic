from django.db import models

# Create your models here.
class Review(models.Model):
	date = models.DateTimeField(auto_now_add=True)
	service = models.CharField(max_length=50)
	rating = models.IntegerField(blank=True)
	comments = models.TextField(blank=True)
	reviewer = models.CharField(max_length=20, blank=True)

	def __unicode__(self):
		return "%(rating)d star review for %(service)s by %(reviewer)s, who says:  %(comments)s" %\
		 {"rating": self.rating, "service": self.service, "reviewer": self.reviewer, "comments":self.comments}


	# aggregate to get average review
"""
class ReviewForm(ModelForm):
	class Meta:
		model = Review
"""


