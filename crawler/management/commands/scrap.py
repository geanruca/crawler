from django.core.management.base import BaseCommand
from crawler.spiders import AbsoluteBus


class Command(BaseCommand):
    help = 'Scrap buses information'

    def handle(self, *args, **options):
        AbsoluteBus.scrap()  # This is the first one
        self.stdout.write(self.style.SUCCESS('Successfully scrapped buses'))