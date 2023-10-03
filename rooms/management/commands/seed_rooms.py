import random
from typing import Any
from django.contrib.admin.utils import flatten
from django.core.management.base import BaseCommand, CommandParser
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models

class Command(BaseCommand):

    help = 'This command creates rooms'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            '--number', default=2, type=int, help='How many rooms do you want to be created?')

    def handle(self, *args: Any, **options: Any) -> str | None:
        number = options.get('number')
        all_room_types = room_models.RoomType.objects.all()
        all_users = user_models.User.objects.all()
        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        house_rules = room_models.HouseRule.objects.all()
        seeder = Seed.seeder()
        seeder.add_entity(room_models.Room, number, {
            'name': lambda x: seeder.faker.address(),
            'host': lambda x: random.choice(all_users),
            'room_type': lambda x: random.choice(all_room_types),
            'price': lambda x: random.randint(1, 10000),
            'beds': lambda x:random.randint(1, 5),
            'bedrooms': lambda x: random.randint(1, 5),
            'baths': lambda x:random.randint(0, 5),
            'guests': lambda x:random.randint(1, 10)
        })     
        created_rooms = seeder.execute() 
        cleared_rooms = flatten(list(created_rooms.values()))

        for pk in cleared_rooms:
            room = room_models.Room.objects.get(pk=pk)
            for num in range(3, random.randint(10, 30)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    file=f'/photos_seed/{random.randint(1,31)}.webp',
                    room=room
                )
            for a in amenities:
                magic_number = random.randint(0, 10)
                if magic_number %2 == 0:
                    room.amenities.add(a)
            for f in facilities:
                magic_number = random.randint(0, 10)
                if magic_number %2 == 0:
                    room.facilities.add(f)
            for r in house_rules:
                magic_number = random.randint(0, 10)
                if magic_number %2 == 0:
                    room.house_rules.add(r)
                  
        self.stdout.write(self.style.SUCCESS(f'{number} rooms created!'))