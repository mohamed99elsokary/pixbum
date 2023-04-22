from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProductappConfig(AppConfig):
    name = "pixbum.productapp"
    verbose_name = _("Productapp")
