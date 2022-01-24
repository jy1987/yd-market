from django.db import models
from django.db.models.deletion import CASCADE
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models


class AbstractItem(core_models.TimeStampedModel):

    """abstract item"""

    name = models.CharField(max_length=50)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class ItemColor(AbstractItem):
    class Meta:
        verbose_name = "Item Color"
        ordering = ["name"]


class Nation(AbstractItem):
    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Photo(core_models.TimeStampedModel):

    caption = models.CharField(max_length=20)
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey("Room", related_name="photos", on_delete=CASCADE)

    def __str__(self):
        return self.caption


# Create your models here.
class Room(core_models.TimeStampedModel):

    """Rooms Model Definition"""

    """nation"""

    미국 = "미국"
    일본 = "일본"
    중국 = "중국"
    홍콩 = "홍콩"
    유럽 = "유럽"

    NATION_CHOICE = (
        (미국, "미국"),
        (일본, "일본"),
        (중국, "중국"),
        (홍콩, "홍콩"),
        (유럽, "유럽"),
    )

    """brand"""

    나이키 = "나이키"
    디올 = "디올"
    아디다스 = "아디다스"
    구찌 = "구찌"

    BRAND_CHOICE = (
        (나이키, "나이키"),
        (디올, "디올"),
        (아디다스, "아디다스"),
        (구찌, "구찌"),
    )

    """categories"""

    CLOTHES = "clothes"
    SHOES = "shoes"
    COSMETIC = "cosmetic"
    HEALTH = "health"

    CATEGORIES_CHOICE = (
        (CLOTHES, "의류"),
        (SHOES, "신발"),
        (COSMETIC, "화장품"),
        (HEALTH, "건강식품"),
    )

    """delivery condition"""

    ABROAD = "abroad"
    DOMESTIC = "domestic"

    DELIVERY_CHOICE = ((ABROAD, "해외배송"), (DOMESTIC, "국내배송"))

    """delivery term"""

    THREE = "three"
    SEVEN = "seven"
    TEN = "ten"

    DELIVERY_TERM_CHOICE = ((THREE, "3일이내 배송"), (SEVEN, "7일이내 배송"), (TEN, "10일이내 배송"))

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=30)
    country = CountryField()
    nation = models.ForeignKey(
        Nation, related_name="rooms", on_delete=models.SET_NULL, null=True
    )
    price = models.IntegerField()
    brand = models.CharField(max_length=20, choices=BRAND_CHOICE, default="나이키")
    categories = models.CharField(
        max_length=20, choices=CATEGORIES_CHOICE, default="의류"
    )
    delivery_condition = models.CharField(
        max_length=20, choices=DELIVERY_CHOICE, default="해외배송"
    )
    delivery_term = models.CharField(
        max_length=20, choices=DELIVERY_TERM_CHOICE, default="7일이내 배송"
    )
    discount_rate = models.IntegerField()
    color = models.ManyToManyField(ItemColor, related_name="rooms", blank=True)
    host = models.ForeignKey(
        user_models.User, related_name="rooms", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    def total_value(self):
        reviews = self.reviews.all()
        sum_review = 0
        list = []
        for review in reviews:
            list.append(review)
            sum_review += review.value
        try:
            return sum_review / len(list)
        except:
            return 0
