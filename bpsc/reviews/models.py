from django.db import models
# Create your models here.

class EnableUsersToSeeReview(models.Model):
	access = models.BooleanField()

	def __unicode__(self):
		return "Access rights to reviews for public users: " + str(self.access)

class Review(models.Model):
	date = models.DateTimeField(auto_now_add=True)
	service = models.CharField(max_length=50)
	rating = models.IntegerField()
	comments = models.TextField(blank=True)
	reviewer = models.CharField(max_length=20, blank=True)

	def __unicode__(self):
		return "%(rating)d star review for %(service)s by %(reviewer)s, who says:  %(comments)s" %\
		 {"rating": self.rating, "service": self.service, "reviewer": self.reviewer, "comments":self.comments}

	def render_stars(self):
		result = ""
		for i in range(0, self.rating):
			result += "<span class='glyphicon glyphicon-star'></span>"
		for i in range(self.rating, 5):
			result += "<span class='glyphicon glyphicon-star-empty'></span>"
		return result


