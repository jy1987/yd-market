from django.core.management.base import BaseCommand
from rooms import models as room_models


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--number", help="How many delivery_term do you want to create"
        )

    def handle(self, *args, **options):
        delivery_term = [
            "3일이내배송",
            "7일이내배송",
            "10일이내배송",
        ]
        for d in delivery_term:
            room_models.DeliveryTerm.objects.create(name=d)
        self.stdout.write(self.style.SUCCESS("delivery_term created!"))