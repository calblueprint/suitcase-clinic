from django.db import models


class EnableUsersToSeeReview(models.Model):
    access = models.BooleanField('Reviews are Visible to Public')

    def __unicode__(self):
        return "Reviews are visible to public: " + str(self.access)

    class Meta:
        verbose_name = 'Toggle Visibility of Reviews to Public'
        verbose_name_plural = verbose_name


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
