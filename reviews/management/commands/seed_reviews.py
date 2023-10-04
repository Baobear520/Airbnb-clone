import random
from typing import Any
from django.contrib.admin.utils import flatten
from django.core.management.base import BaseCommand, CommandParser
from django_seed import Seed
from reviews import models as review_models
from users import models as user_models
from rooms import models as room_models


class Command(BaseCommand):

    help = 'This command creates reviews'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            '--number', default=2, type=int, help='How many reviews do you want to be created?')

    def handle(self, *args: Any, **options: Any) -> str | None:
        number = options.get('number')
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()

        seeder.add_entity(review_models.Review, number, {
            'accuracy': lambda x: random.randint(1, 5),
            'communication': lambda x: random.randint(1, 5),
            'cleanliness': lambda x: random.randint(1, 5),
            'location': lambda x: random.randint(1, 5),
            'check_in': lambda x: random.randint(1, 5),
            'value': lambda x: random.randint(1, 5),
            'user': lambda x: random.choice(users),
            'room': lambda x: random.choice(rooms)
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{number} reviews created!'))