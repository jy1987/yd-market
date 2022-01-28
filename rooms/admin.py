from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models

# Register your models here.
class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    inlines = (PhotoInline,)

    list_display = (
        "name",
        "get_thumbnail",
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
        "total_value",
    )

    ordering = (
        "name",
        "price",
    )

    list_filter = (
        "nation",
        "brand",
        "host__superhost",
        "categories",
        "delivery_condition",
        "delivery_term",
    )

    search_fields = (
        "name",
        "nation__name",
        "brand__name",
        "host__username",
    )

    raw_id_fields = (
        "host",
        "nation",
        "color",
    )

    def count_color(self, obj):
        colors = []
        for color in obj.color.all():
            colors.append(color)
        return colors

    def count_photo(self, obj):

        return obj.photos.count()

    def get_thumbnail(self, obj):
        # print(dir(obj.photos.all))
        try:
            photo = obj.photos.all()[0]

            return mark_safe(f'<img width=50px, height=50px src="{photo.file.url}"/>')
        except:
            None


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

    list_display = ("__str__",)


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):

    list_display = ("__str__",)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ("__str__",)


@admin.register(models.DeliveryFrom)
class DeliveryFromAdmin(admin.ModelAdmin):

    list_display = ("__str__",)


@admin.register(models.DeliveryTerm)
class DeliveryTermAdmin(admin.ModelAdmin):

    list_display = ("__str__",)


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "get_thumbnail",
    )

    def get_thumbnail(self, obj):
        # print(dir(obj.file))
        return mark_safe(f'<img width=100px, height=100px src="{obj.file.url}"/>')
