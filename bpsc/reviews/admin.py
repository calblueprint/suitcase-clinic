from django.contrib import admin
from bpsc.reviews.models import Review, EnableUsersToSeeReview

admin.site.register(Review)
admin.site.register(EnableUsersToSeeReview)