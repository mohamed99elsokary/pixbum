from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from unfold.admin import ModelAdmin

from . import models


@admin.register(models.Product)
class ProductAdmin(ModelAdmin, TranslationAdmin):
    """Admin View for Product"""


@admin.register(models.ProductFeatures)
class ProductFeaturesAdmin(ModelAdmin, TranslationAdmin):
    """Admin View for ProductFeatures"""


@admin.register(models.ProductImages)
class ProductImagesAdmin(ModelAdmin):
    """Admin View for ProductImages"""
