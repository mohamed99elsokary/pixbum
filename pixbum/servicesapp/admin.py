from django.contrib import admin
from unfold.admin import ModelAdmin

from . import models


@admin.register(models.Service)
class ServiceAdmin(ModelAdmin):
    """Admin View for Service"""


@admin.register(models.Category)
class ServiceAdmin(ModelAdmin):
    """Admin View for Service"""
