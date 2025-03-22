from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "first_name",
        "last_name",
        "phone_number",
        "profile_picture",
        "is_staff",
        "is_active",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("phone_number","profile_picture")}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("phone_number","profile_picture")}),)

admin.site.register(CustomUser, CustomUserAdmin)
