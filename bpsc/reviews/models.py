from django.db import models

# Create your models here.
class Review(models.Model):
	date = models.DateTimeField()
	service = models.CharField(max_length=50)
	rating = models.IntegerField()
	comments = models.TextField()
	reviewer = models.CharField(max_length=20)

	def __unicode__(self):
		return "%(rating)d star review for %(service)s by %(reviewer)s, who says:  %(comments)s" %\
		 {"rating": self.rating, "service": self.service, "reviewer": self.reviewer, "comments":self.comments}
