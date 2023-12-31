from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from django_seed import Seed
from users.models import User

class Command(BaseCommand):

    help = 'This command creates users'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            '--number',default=1,type=int, help='How many users do you want to be created?')

    def handle(self, *args: Any, **options: Any) -> str | None:
        number = options.get('number')
        seeder = Seed.seeder()

        seeder.add_entity(User, number, {
            'is_staff': False,
            'is_superuser': False,
        })
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f'{number} users created!'))