from django.contrib import admin
from solo.admin import SingletonModelAdmin
from unfold.admin import ModelAdmin

from pixbum.addonsapp.models import ContactUs, SiteConfiguration

# SiteConfiguration


@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(SingletonModelAdmin):
    pass


# PageSection


# ContactUs


@admin.register(ContactUs)
class ContactUsAdmin(ModelAdmin):
    list_display = ("id", "name", "email", "phone_number", "subject", "message")
    search_fields = ("name", "email", "phone_number", "subject", "message")
