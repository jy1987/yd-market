from django.core.management.base import BaseCommand
from rooms import models as room_models


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--number", help="How many users do you want to create")

    def handle(self, *args, **options):
        colors = [
            "블랙",
            "화이트",
            "레드",
            "그레이",
            "블루",
            "옐로우",
            "베이지",
        ]
        for c in colors:
            room_models.ItemColor.objects.create(name=c)
        self.stdout.write(self.style.SUCCESS("Colors created!"))