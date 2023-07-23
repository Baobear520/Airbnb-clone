from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Reservation)
class RegistrationAdmin(admin.ModelAdmin):

    """ Registration Admin definition """

    pass