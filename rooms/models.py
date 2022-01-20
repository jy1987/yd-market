from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models

# Create your models here.
class Room(core_models.TimeStampedModel):

    """Rooms Model Definition"""

    """nation"""

    USA = "usa"
    JAPAN = "japan"
    CHINA = "china"
    HOKONG = "hokong"
    EU = "europe"

    NATION_CHOICE = (
        (USA, "미국"),
        (JAPAN, "일본"),
        (CHINA, "중국"),
        (HOKONG, "홍콩"),
        (EU, "유럽"),
    )

    """brand"""

    NIKE = "nike"
    DIOR = "dior"
    ADIDAS = "adidas"
    CUGGI = "cuggi"

    BRAND_CHOICE = (
        (NIKE, "나이키"),
        (DIOR, "디올"),
        (ADIDAS, "아디다스"),
        (CUGGI, "구찌"),
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
    nation = models.CharField(max_length=20, choices=NATION_CHOICE, default="미국")
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
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
