from django.contrib import admin
from unfold.admin import ModelAdmin

from . import models


@admin.register(models.Order)
class OrderAdmin(ModelAdmin):
    """Admin View for Order"""


@admin.register(models.OrderDetails)
class OrderDetailsAdmin(ModelAdmin):
    """Admin View for OrderDetails"""
