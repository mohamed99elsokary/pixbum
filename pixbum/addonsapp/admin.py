from django.contrib import admin
from solo.admin import SingletonModelAdmin
from unfold.admin import ModelAdmin

from pixbum.addonsapp.forms import SectionContentForm, SliderPictureForm
from pixbum.addonsapp.models import (
    ContactUs,
    PageSection,
    SectionContent,
    SiteConfiguration,
    SliderPicture,
)

# SiteConfiguration


@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(SingletonModelAdmin):
    pass


# PageSection


class SectionContentInline(admin.StackedInline):
    model = SectionContent
    form = SectionContentForm
    min_num = 0
    extra = 0
    classes = ["collapse"]


class SliderPictureInline(admin.StackedInline):
    model = SliderPicture
    form = SliderPictureForm
    min_num = 0
    extra = 0
    classes = ["collapse"]


@admin.register(PageSection)
class PageSectionAdmin(ModelAdmin):
    list_display = ["id", "page_type", "section_number"]
    list_filter = ("page_type", "section_number")
    inlines = [SectionContentInline, SliderPictureInline]


# ContactUs


@admin.register(ContactUs)
class ContactUsAdmin(ModelAdmin):
    list_display = ("id", "name", "email", "phone_number", "subject", "message")
    search_fields = ("name", "email", "phone_number", "subject", "message")
