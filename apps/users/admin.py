from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.users.models import User


@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = ['username', 'get_full_name', 'email', 'is_staff', 'is_superuser']
    list_filter = ['is_staff']
