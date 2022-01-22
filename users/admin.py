from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """custom User Admin"""

    fieldsets = UserAdmin.fieldsets + (
        ("customs", {"fields": ("avatar", "gender", "superhost")}),
    )

    list_display = (
        "username",
        "first_name",
        "last_name",
        "gender",
        "superhost",
    )
