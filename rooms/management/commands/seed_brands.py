from django.core.management.base import BaseCommand
from rooms import models as room_models


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--number", help="How many users do you want to create")

    def handle(self, *args, **options):
        brands = [
            "애플",
            "나이키",
            "아디다스",
            "구찌",
            "디올",
            "샤넬",
        ]
        for b in brands:
            room_models.Brand.objects.create(name=b)
        self.stdout.write(self.style.SUCCESS("brand created!"))