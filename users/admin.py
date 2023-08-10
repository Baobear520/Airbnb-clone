from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from rooms import models as room_models
from . import models
# Register your models here.

class RoomInline(admin.StackedInline):

    """Room inline in user admin """

    model = room_models.Room
    filter_horizontal = ('amenities','facilities', 'house_rules')
    extra = 1

@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custome User Admin """
    
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom profile",
            {
                "fields": (
                    'avatar', 'gender', 'bio', 
                    'birthdate', 'language', 'currency', 'superhost')
            }
        ),
    )
    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
        'is_active',
        'language',
        'currency',
        'superhost',
        'is_staff',
        'is_superuser'
    )
    list_filter = UserAdmin.list_filter + ('superhost',)
    inlines = (RoomInline,)