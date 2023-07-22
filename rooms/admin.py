from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    
    """ Item admin class """
    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room admin class """
    pass