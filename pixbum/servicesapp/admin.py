from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from unfold.admin import ModelAdmin

from . import models


@admin.register(models.Service)
class ServiceAdmin(ModelAdmin, TranslationAdmin):
    """Admin View for Service"""


@admin.register(models.Category)
class ServiceAdmin(ModelAdmin, TranslationAdmin):
    """Admin View for Service"""
