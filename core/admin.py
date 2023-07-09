from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


# Register your models here.


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # list_display = ["username", "email", 'phone_number', "auth_provider", "is_staff"]
    list_display = [ 'phone_number', "email", "auth_provider", "is_staff"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("phone_number","username", "password1",  "password2", "auth_provider", "email", "auth_provider"),
            },
        ),
    )
