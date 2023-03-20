from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from DjangoPetstagram.accounts.forms import AppRegisterForm

user_model = get_user_model()

@admin.register(user_model)
class AppUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email')
    list_filter = ()
    add_form = AppRegisterForm

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", 'email', "password1", "password2"),
            },
        ),
    )

    fieldsets = (
        ('User', {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("email", )}),
    )
