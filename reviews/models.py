from django.db import models
from core import models as core_models

# Create your models here.
class Review(core_models.TimeStampedModel):

    """review model"""

    review = models.TextField()
    accuracy = models.IntegerField()
    value = models.IntegerField()
    guarantee = models.BooleanField(default=True)
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.room}by{self.user}"
