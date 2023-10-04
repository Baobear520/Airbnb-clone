import random
from typing import Any
from django.contrib.admin.utils import flatten
from django.core.management.base import BaseCommand, CommandParser
from django_seed import Seed
from lists import models as list_models
from users import models as user_models
from rooms import models as room_models

NAME = 'lists'

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

        seeder.add_entity(list_models.List, number, {
            'user': lambda x: random.choice(users)
        })
        
        created = seeder.execute()
        cleared = flatten(list(created.values()))
        for pk in cleared:
            wish_list = list_models.List.objects.get(pk=pk)
            to_add = rooms[random.randint(1, 15):random.randint(16, 50)]
            wish_list.rooms.add(*to_add)
        self.stdout.write(self.style.SUCCESS(f'{number} {NAME} created!'))