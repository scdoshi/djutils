###############################################################################
## Imports
###############################################################################
from django.core.management.base import BaseCommand
from djutils.signals import after_syncdb


###############################################################################
## Command
###############################################################################
class Command(BaseCommand):
    help = 'sends after_syncdb signal'

    def handle(self, *args, **options):
        after_syncdb.send(sender=self)
