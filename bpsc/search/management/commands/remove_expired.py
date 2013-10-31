from django.core.management.base import BaseCommand, CommandError
from bpsc.search.models import *

import datetime


class Command(BaseCommand):
	help = 'Removes expired resources if they have an expiration date'

	def handle(self, *args, **options):
		pass