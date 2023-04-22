from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("contact-us", views.ContactUsViewset)

urlpatterns = [
    path("", include(router.urls)),
]
