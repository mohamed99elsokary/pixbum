from django.contrib import admin
from payment.admin import models as payment_models
from unfold.admin import ModelAdmin, StackedInline

from . import models

admin.site.unregister(payment_models.Payment)


@admin.register(payment_models.Payment)
class PaymentAdmin(ModelAdmin):
    """Admin View for Order"""


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
