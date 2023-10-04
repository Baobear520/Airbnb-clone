import random
from datetime import datetime, timedelta
from typing import Any
from django.contrib.admin.utils import flatten
from django.core.management.base import BaseCommand, CommandParser
from django_seed import Seed
from reservations import models as reservation_models
from users import models as user_models
from rooms import models as room_models

NAME = 'reservations'

class Command(BaseCommand):

    help = f'This command creates {NAME}'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            '--number', default=2, type=int, help=f'How many {NAME} do you want to be created?')

    def handle(self, *args: Any, **options: Any) -> str | None:
        number = options.get('number')
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()

        seeder.add_entity(reservation_models.Reservation, number, {
            'status': lambda x: seeder.faker.word(ext_word_list=['Pending','Confirmed','Cancelled']),
            'guest': lambda x: random.choice(users),
            'check_in': lambda x: datetime.now(),
            'check_out': lambda x: datetime.now() + timedelta(days=random.randint(1, 31)),
            'room': lambda x: random.choice(rooms)
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{number} {NAME} created!'))