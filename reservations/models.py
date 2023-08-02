from django.db import models
from django.utils import timezone
from core import models as core_models
# Create your models here.

    

class Reservation(core_models.TimeStampedModel):

    """ Reservation model definition """

    STATUS_PENDING = 'Pending'
    STATUS_CONFIRMED = 'Confirmed'
    STATUS_CANCELLED = 'Cancelled'

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELLED, "Cancelled"),
    )

    status = models.CharField(
        max_length=12, 
        choices=STATUS_CHOICES, 
        default='Pending'
    )
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name='reservations')
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE, related_name='reservations')

    def __str__(self) -> str:
        return f'{self.room} - {self.check_in}'
    
    
    def stay_status(self):
        today = timezone.now().date()
        
        check_in = self.check_in
        check_out = self.check_out
        print(today - check_in)
        if today > check_out:
            return 'Completed'
        elif today == check_out:
            return 'Check-out day'
        elif today > check_in:
            return 'In progress'
        elif check_in == today:
            return 'Almost time!'
        else:
            return 'To be checked-in'
