from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from rooms.models import Facility

class Command(BaseCommand):

    help = 'This command creates facilities'

    #def add_arguments(self, parser: CommandParser) -> None:
        #parser.add_argument('--times', help='How can i help?')

    def handle(self, *args: Any, **options: Any) -> str | None:
        facilities = [
            "Accessible parking",
            "BBQ grill",
            "Beachfront access",
            "Elevator",
            "Free parking on premises",
            "Gym",
            "Hot tub",
            "Indoor fireplace",
            "Luggage dropoff allowed",
            "Outdoor pool",
            "Pets allowed",
            "Private entrance",
            "Self check-in",
            "Ski-in/Ski-out",
            "Smoking allowed",
            "Wheelchair accessible",
        ]
        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f'{len(facilities)} facilities created!'))