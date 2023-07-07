from modeltranslation.translator import TranslationOptions, register

from .models import Product, ProductFeatures


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ("name", "description")


@register(ProductFeatures)
class ProductFeaturesTranslationOptions(TranslationOptions):
    fields = ("name",)
