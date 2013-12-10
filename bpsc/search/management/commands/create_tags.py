from django.core.management.base import BaseCommand, CommandError
from bpsc.search.models import *


class Command(BaseCommand):
	help = 'Creates all tag objects to use for tagging resources'

	housing_tags = {'Category':['Senior', 'Veteran', 'HIV/AIDS', 'Disability', 'Individual', 'Family', 'Youth', 'Transitional', 'Rental Assistance', 'Emergency', 'Homeless'], 
					'Price':['AMI', 'Section 8', '400', '800', '1200'], 
					'Type of Housing':['SRO', 'Studio', '1 BR', '1+ BR'],
					'County':['Alameda', 'Contra Costa', 'San Francisco', 'Santa Clara', 'San Mateo', 'Marin', 'Solano', 'Napa', 'Other']}

	community_tags = {'Type of Service':['Medical', 'Dental', 'Optometry', 'Mental', 'Shelter', 'Shower', 'Meals', 'Miscellaneous'],
						'Location':['Alameda', 'Contra Costa', 'San Francisco', 'Santa Clara', 'San Mateo', 'Marin', 'Solano', 'Napa', 'Other'],
						'Health Insurance':['Yes', 'No', 'Unsure'],
						'Payment Type':['Free', 'Sliding Scale', 'Full Payment']}

	employment_tags = {}
	
	legal_tags = {'Type of Legal Service':['Low-Cost Health Services', 'Housing Law', 'Emergency Housing/Meals Resources', 
						'Mental Health Resources', 'Education Law', 'Family Law', 'Bankruptcy', 'Immigration', 
						'Employment Law/Worker\'s Rights', 'Public Benefits', 'Juvenile', 'General Civil', 'Estate Law', 'Domestic Violence', 
						'Criminal Law/Criminal Records', 'Civil Rights', 'Car Issues', 'Business Law', 'Attorney Disputes', 'Administrative Law',
						'Consumer Law']}

	def set_housing_tags(self):
		HousingTag.objects.all().delete()
		for tag_type, tag_list in Command.housing_tags.items():
			for tag_name in tag_list:
				self.stdout.write('housing: ' + tag_type + ": " + tag_name)
				tag = HousingTag()
				tag.tag_type = tag_type
				tag.value = tag_name
				tag.save()

	def set_community_tags(self):
		CommunityTag.objects.all().delete()
		for tag_type, tag_list in Command.community_tags.items():
			for tag_name in tag_list:
				self.stdout.write('community: ' + tag_type + ": " + tag_name)
				tag = CommunityTag()
				tag.tag_type = tag_type
				tag.value = tag_name
				tag.save()

	def set_employment_tags(self):
		EmploymentTag.objects.all().delete()
		for tag_type, tag_list in Command.employment_tags.items():
			for tag_name in tag_list:
				self.stdout.write('employment: ' + tag_type + ": " + tag_name)
				tag = EmploymentTag()
				tag.tag_type = tag_type
				tag.value = tag_name
				tag.save()

	def set_legal_tags(self):
		LegalTag.objects.all().delete()
		for tag_type, tag_list in Command.legal_tags.items():
			for tag_name in tag_list:
				self.stdout.write('legal: ' + tag_type + ": " + tag_name)
				tag = LegalTag()
				tag.tag_type = tag_type
				tag.value = tag_name
				tag.save()

	def handle(self, *args, **options):
		self.set_housing_tags()
		self.set_community_tags()
		self.set_employment_tags()
		self.set_legal_tags()


