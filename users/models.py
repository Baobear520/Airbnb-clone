from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    
    """Custom user model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other")
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_CHINESE = "cn"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_CHINESE, "Chinese")
    )

    CURRENCY_USD = "USD"
    CURRENCY_CNY = "CNY"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_CNY, "CNY")
    )

    avatar = models.ImageField(upload_to='avatars',null=True, blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, 
        max_length=10, null=True, blank=True
    )
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, 
        max_length=3, null=True, default="en"
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, 
        max_length=3, 
        default="USD", 
        null=True
    )
    superhost = models.BooleanField(default=False)
