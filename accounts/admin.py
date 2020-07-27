from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'first_name', 'is_active',)
    list_filter = ('email', 'first_name', 'is_active',)
    fieldsets = (
        ('Informations personnelles', {'fields': ('email', 'first_name', 'password', 'gender', 'wish_gender')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}), ('Key moments', {'fields': ('last_login', 'date_joined')}),
        ('Personnalité',  {'fields': ('q1', 's1')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
