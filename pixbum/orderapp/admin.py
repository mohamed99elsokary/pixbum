from django.contrib import admin
from unfold.admin import ModelAdmin, StackedInline

from . import models


class OrderDetailsAdminInline(StackedInline):
    model = models.OrderDetails


@admin.register(models.Order)
class OrderAdmin(ModelAdmin):
    """Admin View for Order"""

    inlines = [
        OrderDetailsAdminInline,
    ]


@admin.register(models.OrderDetails)
class OrderDetailsAdmin(ModelAdmin):
    """Admin View for OrderDetails"""


@admin.register(models.Drafts)
class DraftAdmin(ModelAdmin):
    """Admin View for Draft"""
