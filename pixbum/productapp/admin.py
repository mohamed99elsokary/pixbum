from django.contrib import admin
from unfold.admin import ModelAdmin

from . import models


@admin.register(models.Product)
class ProductAdmin(ModelAdmin):
    """Admin View for Product"""


@admin.register(models.ProductFeatures)
class ProductFeaturesAdmin(ModelAdmin):
    """Admin View for ProductFeatures"""


@admin.register(models.ProductImages)
class ProductImagesAdmin(ModelAdmin):
    """Admin View for ProductImages"""
