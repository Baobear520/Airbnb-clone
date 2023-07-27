from django.db import models
from django_countries.fields import CountryField
from core import models as core_models

# Create your models here.


class AbstractItem(core_models.TimeStampedModel):
    """ Abstract item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name


class RoomType(AbstractItem):
    
    """ Room type """
    
    class Meta:
        verbose_name = "Room Type"


class Amenity(AbstractItem):

    """ Amenity model definition """

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    """ Facility model definition"""

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    """ House rule model definition """

    class Meta:
        verbose_name_plural = "House Rules"


class Photo(core_models.TimeStampedModel):

    """ Photo model definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.caption
    

class Room(core_models.TimeStampedModel):

    """ Room model definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    guests = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_booking = models.BooleanField(default=False)
    host = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name='rooms')
    room_type = models.ForeignKey("RoomType", on_delete=models.SET_NULL, null=True, related_name='rooms')
    amenities = models.ManyToManyField("Amenity", blank=True, related_name='rooms')
    facilities = models.ManyToManyField("Facility", blank=True, related_name='rooms')
    house_rules = models.ManyToManyField("HouseRule", blank=True, related_name='rooms')

    def __str__(self) -> str:
        return self.name
    