from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):

    """review admin"""

    list_display = (
        "__str__",
        "user",
        "review",
        "accuracy",
        "value",
    )
