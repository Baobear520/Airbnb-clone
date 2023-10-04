from django.contrib import admin
from django.utils import timezone

from django.utils.translation import gettext_lazy as _
from . import models
# Register your models here.

class StayStatusFilter(admin.SimpleListFilter):

    title = _('Stay Status')
    parameter_name = 'stay_status'

    def lookups(self, request, model_admin):
        return (
            ('in_progress', _('In Progress')),
            ('to_be_checked_in', _('To Be Checked-In')),
            ('time_to_check-in', _('Time to Check-in!')),
            ('completed', _('Completed')),
            ('check_out_day',_('Check-out day'))
        )

    def queryset(self, request, queryset):
        if self.value() == 'in_progress':
            return queryset.filter(
                check_out__gt=timezone.now().date(),
                check_in__lt=timezone.now().date()
            )
        elif self.value() == 'to_be_checked_in':
            return queryset.filter(check_in__gt=timezone.now().date())
        elif self.value() == 'time_to_check-in':
            return queryset.filter(
                check_in=timezone.now().date())
        elif self.value() == 'completed':
            return queryset.filter(check_out__lt=timezone.now().date())
        elif self.value() == 'check_out_day':
            return queryset.filter(check_out=timezone.now().date())    

@admin.register(models.Reservation)
class RegistrationAdmin(admin.ModelAdmin):

    """ Registration Admin definition """

    list_display = (
        'room',
        'status',
        'check_in',
        'check_out',
        'guest',
        'stay_status'
    )
    list_filter = (StayStatusFilter,)
