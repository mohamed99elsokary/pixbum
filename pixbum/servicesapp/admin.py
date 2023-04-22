from django.contrib import admin

from . import models


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    """Admin View for Service"""


@admin.register(models.Category)
class ServiceAdmin(admin.ModelAdmin):
    """Admin View for Service"""
