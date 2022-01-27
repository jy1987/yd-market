from django.core.management.base import BaseCommand
from rooms import models as room_models


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--number", help="How many delivery_from do you want to create"
        )

    def handle(self, *args, **options):
        delivery_from = [
            "해외배송",
            "국내배송",
        ]
        for d in delivery_from:
            room_models.DeliveryFrom.objects.create(name=d)
        self.stdout.write(self.style.SUCCESS("delivery_from created!"))