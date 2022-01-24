from django.core.management.base import BaseCommand
from rooms import models as room_models


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--number", help="How many users do you want to create")

    def handle(self, *args, **options):
        categories = [
            "가전제품",
            "스마트폰",
            "화장품",
            "건강식품",
            "의류",
        ]
        for c in categories:
            room_models.Category.objects.create(name=c)
        self.stdout.write(self.style.SUCCESS("category created!"))