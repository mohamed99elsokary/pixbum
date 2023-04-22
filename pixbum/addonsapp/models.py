from django.db import models
from django.utils.translation import gettext_lazy as _
from solo.models import SingletonModel

from pixbum.addonsapp.conf import HOME_PAGE
from pixbum.addonsapp.model_mixins import ContactUsMixin
from pixbum.services.helpers import file_upload


class SiteConfiguration(SingletonModel):
    def __str__(self):
        return "Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"


class AbstractSection(models.Model):
    title = models.TextField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    button_text = models.TextField(null=True, blank=True)
    button_hex_color = models.CharField(
        max_length=255, null=True, blank=True, help_text=_("color of button")
    )
    button_text_color = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text=_("color of text inside button"),
    )
    button_url = models.TextField(null=True, blank=True)
    button_float = models.TextField(
        choices=[("right", "right"), ("left", "left"), ("middle", "middle")],
        null=True,
        blank=True,
    )
    color = models.CharField(
        max_length=255, null=True, blank=True, help_text=_("section color")
    )
    hidden = models.BooleanField(default=False)

    class Meta:
        abstract = True


# Contact Us


class ContactUs(ContactUsMixin, models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=12)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    class Meta:
        verbose_name = "Contact us"
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return f"{self.name}"
