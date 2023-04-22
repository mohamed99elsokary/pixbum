from django.urls import include, path
from rest_framework import routers

from pixbum.userapp.views import AddressViewSet, FacebookLogin, UserViewSet

router = routers.DefaultRouter()
router.register("users", UserViewSet, basename="users")
router.register("address", AddressViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("users/facebook/", FacebookLogin.as_view(), name="fb_login"),
]
