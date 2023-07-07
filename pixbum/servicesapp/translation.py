from modeltranslation.translator import TranslationOptions, register

from .models import Category, Service


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("name",)
