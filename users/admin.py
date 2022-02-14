from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from . import models
from rooms import models as room_models

# Register your models here.


class RoomInline(admin.TabularInline):

    model = room_models.Room


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """custom User Admin"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "customs",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "superhost",
                    "nation",
                    "brand",
                    "categories",
                )
            },
        ),
    )

    # inlines = (RoomInline,)

    list_display = (
        "username",
        "user_img",
        "gender",
        "superhost",
        "nation",
        "brand",
        "categories",
    )

    def user_img(self, obj):
        # print(dir(obj.avatar))
        try:
            return mark_safe(f'<img width=50px, height=50px src="{obj.avatar.url}"/>')
        except:
            None

    def save_model(self, request, obj, form, change):
        print(obj, change, form)
        super().save_model(request, obj, form, change)
