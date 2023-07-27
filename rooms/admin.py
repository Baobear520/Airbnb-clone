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
    fieldsets = (
        (
            "Basic Info",
            {"fields": ('name', 'description', 'country', 'address', 'price', 'host')}
        ),
        (
            "Booking Info",
            {"fields": ('check_in', 'check_out', 'instant_booking')}
        ),
        (
            "Guest Info",
            {"fields": ('guests',)}

        ),
        (
            "Room Info",
            {"fields": ('room_type', 'beds', 'bedrooms', 'baths')}
        ),
        (
            "Room Detail Info", {
                "classes": ('collapse',),
                "fields": ('amenities', 'facilities')
            }
        ),
        (
            "Extra Info",
            {"fields": ('house_rules',)}
        )
    )
    list_display = (
        'name',
        'country', 
        'city', 
        'price', 
        'guests', 
        'beds', 
        'bedrooms', 
        'baths',
        'check_in', 
        'check_out', 
        'instant_booking',
        'count_amenities')
    ordering = ('price',)
    list_filter = (
        'instant_booking',
        'host__superhost',
        'room_type', 
        'amenities', 
        'facilities', 
        'house_rules',  
        'city', 
        'country')
    search_fields = ('^city', '^host__username')
    filter_horizontal = ('amenities', 'facilities', 'house_rules')

    def count_amenities(self, obj):
        return obj.amenities.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ """
    pass