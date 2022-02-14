import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from faker.proxy import Faker
from users import models as user_models
from rooms import models as room_models


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many users do you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        fake = Faker(["ko_KR"])
        seeder = Seed.seeder()
        all_nation = room_models.Nation.objects.all()
        all_brand = room_models.Brand.objects.all()
        all_categories = room_models.Category.objects.all()
        seeder.add_entity(
            user_models.User,
            number,
            {
                "is_staff": False,
                "username": lambda x: fake.name(),
                "brand": lambda x: random.choice(all_brand),
                "categories": lambda x: random.choice(all_categories),
                "nation": lambda x: random.choice(all_nation),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} users are created!"))