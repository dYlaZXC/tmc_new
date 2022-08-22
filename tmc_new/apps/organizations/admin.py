from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.organizations.models import Organization


@admin.register(Organization)
class OrganizationAdmin(ModelAdmin):
    list_display = ['name', 'region']
    list_filter = ['region']
    search_fields = ['name']
