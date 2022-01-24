from django.core.management.base import BaseCommand
from rooms import models as room_models


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--number", help="How many users do you want to create")

    def handle(self, *args, **options):
        nation = [
            "미국",
            "일본",
            "중국",
            "홍콩",
            "프랑스",
            "영국",
            "독일",
        ]
        for n in nation:
            room_models.Nation.objects.create(name=n)
        self.stdout.write(self.style.SUCCESS("Nation created!"))