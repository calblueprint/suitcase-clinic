import datetime

from django.core.management.base import BaseCommand

from bpsc.search.models import BatchHousingResource, CommunityResource


class Command(BaseCommand):
	help = 'Removes expired resources if they have an expiration date'

	def remove_expired_housing(self):
		today = datetime.date.today()
		all_housing = BatchHousingResource.objects.all()
		for resource in all_housing:
			age = (today - resource.posted).days
			if age > 42 and age < 90:
				resource.outdated = True
				resource.save()
			elif age >= 90:
				resource.delete()

	def set_community_outdated(self):
		today = datetime.date.today()
		all_community = CommunityResource.objects.all()
		for resource in all_community:
			age = (today - resource.posted).days
			if age >= 180:
				resource.outdated = True
				resource.save()

	def handle(self, *args, **options):
		self.set_community_outdated()
		self.remove_expired_housing()
