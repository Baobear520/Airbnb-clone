from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from rooms.models import Amenity

class Command(BaseCommand):

    help = 'This command creates amenities'

    #def add_arguments(self, parser: CommandParser) -> None:
        #parser.add_argument('--times', help='How can i help?')

    def handle(self, *args: Any, **options: Any) -> str | None:
        amenities = [
            "Air conditioning or fans (for hot seasons)",
            "Bed with comfortable mattress and bedding",
            "Blankets or comforters",
            "Broom and dustpan",
            "Carbon monoxide detector (if applicable)",
            "Coffee maker or kettle",
            "Comfortable seating (sofa, chairs)",
            "Cooking utensils (pots, pans, spatula, etc.)",
            "Dish soap and sponge",
            "Fire extinguisher",
            "Garden/backyard",
            "Glasses and mugs",
            "Hairdryer",
            "Hangers",
            "Heating (for cold seasons)",
            "Internet/Wi-Fi access",
            "Iron and ironing board",
            "Microwave",
            "Parking (if available)",
            "Patio or balcony with seating",
            "Plates, bowls, and cutlery",
            "Refrigerator",
            "Shampoo and conditioner",
            "Smoke detector",
            "Soap (hand soap and body soap)",
            "Stove or cooktop",
            "Television (if mentioned in the listing)",
            "Toilet",
            "Toilet paper",
            "Towels (bath and hand towels)",
            "Trash bags",
            "Trash cans and recycling bins",
            "Vacuum cleaner",
            "Wardrobe or closet for storing clothes",
            "Washer and dryer (laundry facilities)",
            "Workspace or desk (for business travelers)",
        ]
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS('Amenities created!'))