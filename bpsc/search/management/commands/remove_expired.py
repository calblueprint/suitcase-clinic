from django.core.management.base import BaseCommand, CommandError
from bpsc.search.models import HousingResource, EmploymentResource, CommunityResource

import datetime


class Command(BaseCommand):
	help = 'Removes expired resources if they have an expiration date'

	def remove_expired_housing(self):
		today = datetime.date.today()
		all_housing = HousingResource.objects.all()
		for resource in all_housing:
			age = (today - resource.posted).days
			if age > 42 and age < 90:
				resource.outdated = True
				resource.save()
			elif age >= 90:
				resource.delete()


	# def remove_expired_employment(self):
	# 	today = datetime.date.today()
	# 	all_employment = EmploymentResource.objects.all()
	# 	for resource in all_employment:
	# 		age = (today - resource.posted).days
	# 		if age > 36 and age < 90:
	# 			resource.outdated = True
	# 			resource.save()
	# 		elif age >= 90:
	# 			resource.delete()

	def set_community_outdated(self):
		today = datetime.date.today()
		all_community = CommunityResource.objects.all()
		for resrouce in all_community:
			age = (today - resource.posted).days
			if age >= 180:
				resource.outdated = True
				resource.save()

	def handle(self, *args, **options):
		self.set_community_outdated()
		# self.remove_expired_employment()
		self.remove_expired_housing()