from django.db import models
from core import models as core_models
# Create your models here.


class Reservation(core_models.TimeStampedModel):

    """ Reservation model definition """

    STATUS_PENDING = 'Pending'
    STATUS_CONFIRMED = 'Confirmed'
    STATUS_CANCELLED = 'Cancelled'
    STATUS_USED = 'Used'

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELLED, "Cancelled"),
        (STATUS_USED, "Used")
    )

    status = models.CharField(
        max_length=12, 
        choices=STATUS_CHOICES, default='Pending')
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.room} - {self.check_in}'
    
    