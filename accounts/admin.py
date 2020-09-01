from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm 
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    readonly_fields = ('average_O', 'average_C', 'average_E', 'average_A', 'average_N')
    list_display = ('email', 'first_name', 'is_active',)
    list_filter = ('email', 'first_name', 'is_active',)
    fieldsets = (
        ('Informations personnelles', {'fields': ('first_name', 'birthday', 'gender', 'wish_gender')}),
        ('Informations de contact', {'fields':('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}), ('Key moments', {'fields': ('last_login', 'date_joined')}),
        ('Personnalité',  {'fields': ('average_O', 'average_C', 'average_E', 'average_A', 'average_N')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
