import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from faker.proxy import Faker
from users import models as user_models
from rooms import models as room_models


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many rooms do you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        fake = Faker(["ko_KR"])
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        all_nation = room_models.Nation.objects.all()
        all_brand = room_models.Brand.objects.all()
        all_categories = room_models.Category.objects.all()
        # print(all_users, all_nation)
        name = [
            "아이폰10",
            "아이폰11",
            "아이폰12",
        ]
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: random.choice(name),
                "brand": lambda x: random.choice(all_brand),
                "categories": lambda x: random.choice(all_categories),
                "host": lambda x: random.choice(all_users),
                "nation": lambda x: random.choice(all_nation),
                "price": lambda x: random.randint(100000, 150000),
                "discount_rate": lambda x: random.randint(5, 20),
                "description": lambda x: fake.address(),
            },
        )
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        colors = room_models.ItemColor.objects.all()
        for pk in created_clean:
            room = room_models.Room.objects.get(pk=pk)
            for i in range(3, random.randint(5, 6)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"room_photos/clothe{random.randint(1, 2)}.jpeg",
                )

            for c in colors:
                magic_number = random.randint(0, 10)
                if magic_number % 2 == 0:
                    room.color.add(c)
        self.stdout.write(self.style.SUCCESS(f"{number} rooms are created!"))