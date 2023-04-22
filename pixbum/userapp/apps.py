from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UserappConfig(AppConfig):
    name = "pixbum.userapp"
    verbose_name = _("User App")
