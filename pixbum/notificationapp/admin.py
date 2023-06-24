from distutils.command import register

from bit68_notifications.models import BulkNotification
from django.contrib import admin
from unfold.admin import ModelAdmin

from . import models

admin.site.unregister(BulkNotification)


@admin.register(models.Notification)
class NotificationAdmin(ModelAdmin):
    """Admin View for Notification"""


@admin.register(BulkNotification)
class BulkNotificationAdmin(ModelAdmin):
    """Admin View for BulkNotification"""
