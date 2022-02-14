from django.contrib.auth.models import AbstractUser

from django.db import models
from django.db.models.deletion import SET_NULL


# Create your models here.
class User(AbstractUser):

    """ custom user model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "남자"),
        (GENDER_FEMALE, "여자"),
        (GENDER_OTHER, "Other"),
    )

    avatar = models.ImageField(upload_to="avatar", blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(default="", blank=True)
    superhost = models.BooleanField(default=False)
    nation = models.ForeignKey(
        "rooms.Nation", related_name="users", on_delete=SET_NULL, null=True
    )
    brand = models.ForeignKey(
        "rooms.Brand", related_name="users", on_delete=SET_NULL, null=True
    )
    categories = models.ForeignKey(
        "rooms.Category", related_name="users", on_delete=SET_NULL, null=True
    )
