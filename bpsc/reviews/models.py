from django.db import models

# Create your models here.
class Review(models.Model):
	service = models.CharField(max_length=50)
	rating = models.IntegerField()
	comments = models.TextField()
	reviewer = models.CharField(max_length=20)

