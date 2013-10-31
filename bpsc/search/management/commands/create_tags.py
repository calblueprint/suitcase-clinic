from django.core.management.base import BaseCommand, CommandError
from bpsc.search.models import *


class Command(BaseCommand):
	help = 'Creates all tag objects to use for tagging resources'

	def handle(self, *args, **options):
		pass