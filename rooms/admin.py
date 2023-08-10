from django.contrib import admin
from django.utils.html import mark_safe
from . import models
# Register your models here.


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    
    """ Item admin class """
    
    list_display = ('name', 'used_by')
 
    def used_by(self, obj):
        return obj.rooms.count()


class PhotoInline(admin.TabularInline):

    """ Photo inline in the room admin"""

    model = models.Photo
@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room admin class """
    fieldsets = (
        (
            "Basic Info",
            {"fields": ('name', 'description', 'country', 'address', 'price')}
        ),
        (
            "Host Info",
            {"fields": ('host',)}
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
        'count_amenities',
        'count_photos',
        'overall_rating'
    )
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
    raw_id_fields = ('host',)
    search_fields = ('^city', '^host__username')
    filter_horizontal = ('amenities', 'facilities', 'house_rules')
    inlines = (PhotoInline,)

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()
    
    
@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo admin definition """
    
    list_display = ('__str__', 'get_thumbnail')

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}"/>')
    get_thumbnail.short_description = 'Thumbnail'