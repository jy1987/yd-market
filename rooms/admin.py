from django.contrib import admin
from django.contrib.admin.decorators import display
from . import models

# Register your models here.
@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "host",
        "description",
        "nation",
        "price",
        "brand",
        "categories",
        "delivery_condition",
        "delivery_term",
        "discount_rate",
        "count_color",
        "count_photo",
    )

    ordering = (
        "name",
        "price",
    )

    list_filter = (
        "nation",
        "brand",
        "host__superhost",
    )

    search_fields = (
        "nation",
        "brand",
        "host__username",
    )

    def count_color(self, obj):
        colors = []
        for color in obj.color.all():
            colors.append(color)
        return colors

    def count_photo(self, obj):

        return obj.photos.count()


@admin.register(models.ItemColor)
class ItemColorAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "used_by",
        "used_by_count",
    )

    def used_by_count(self, obj):

        return obj.rooms.count()

    def used_by(self, obj):

        list = []
        for i in obj.rooms.all():
            list.append(i)
        return list


@admin.register(models.Nation)
class NationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    pass