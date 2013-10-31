from django.core.management.base import BaseCommand, CommandError
from bpsc.search.models import *


class Command(BaseCommand):
	help = 'Creates all tag objects to use for tagging resources'

	housing_tags = ['senior', 'veteran', 'hiv', 'disability', 'individual', 'family', 
					'youth', 'transitional', 'rental assistance', 'emergency', 'homeless', 
					'ami', 'section8', 'sro', 'studio', '1br', '1+br']

	community_tags = ['medical', 'dental', 'optometry', 'mental', 'shelter', 
					'shower', 'meals', 'miscellaneous']

	employment_tags = []
	
	legal_tags = ['low cost health', 'housing', 'emergency housing+meals', 
				'mental health', 'education', 'family', 'bankruptcy', 'immigration', 
				'employment', 'public', 'juvenile', 'gen civil', 'estate', 'dom violence', 
				'criminal', 'civil rights', 'car', 'business', 'attorney dispute']

	def set_housing_tags(self):
		HousingTag.objects.all().delete()
		for tag_name in Command.housing_tags:
			self.stdout.write('housing: ' + tag_name)
			tag = HousingTag()
			tag.tag_type = 'housing'
			tag.value = tag_name
			tag.save()

	def set_community_tags(self):
		CommunityTag.objects.all().delete()
		for tag_name in Command.community_tags:
			self.stdout.write('community: ' + tag_name)
			tag = CommunityTag()
			tag.tag_type = 'community'
			tag.value = tag_name
			tag.save()

	def set_employment_tags(self):
		EmploymentTag.objects.all().delete()
		for tag_name in Command.employment_tags:
			self.stdout.write('employment: ' + tag_name)
			tag = EmploymentTag()
			tag.tag_type = 'employment'
			tag.value = tag_name
			tag.save()

	def set_legal_tags(self):
		LegalTag.objects.all().delete()
		for tag_name in Command.legal_tags:
			self.stdout.write('legal: ' + tag_name)
			tag = LegalTag()
			tag.tag_type = 'legal'
			tag.value = tag_name
			tag.save()

	def handle(self, *args, **options):
		self.set_housing_tags()
		self.set_community_tags()
		self.set_employment_tags()
		self.set_legal_tags()