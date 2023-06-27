from allauth.socialaccount.providers.apple.views import AppleOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from bit68_notifications.models import ExpoDevice
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from pixbum.services.custom_all_auth import CustomLoginView
from pixbum.services.views import ModelViewSetClones
from pixbum.userapp import models
from pixbum.userapp.serializers import (
    AddressSerializer,
    ChangePasswordSerializer,
    ExpoDeviceSerializer,
    GenerateUserSerializer,
    LoginSerializer,
    RefreshTokenSerializer,
    UserDataSerializer,
    UserSerializer,
)


class ExpoDeviceViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = ExpoDevice.objects.all()
    serializer_class = ExpoDeviceSerializer


class UserViewSet(ModelViewSetClones, viewsets.GenericViewSet):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == "login":
            return LoginSerializer
        elif self.action == "update_me":
            return UserDataSerializer
        elif self.action == "get_me":
            return UserDataSerializer
        elif self.action == "generate_user":
            return GenerateUserSerializer
        elif self.action == "change_password":
            return ChangePasswordSerializer
        elif self.action == "refresh_token":
            return RefreshTokenSerializer
        return super().get_serializer_class()

    @action(methods=["post"], detail=False)
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(methods=["post"], detail=False)
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    @action(methods=["get"], detail=False)
    def get_me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    @action(methods=["put"], detail=False)
    def update_me(self, request):
        instance = request.user
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(methods=["delete"], detail=False)
    def delete_me(self, request):
        request.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=["post"], detail=False)
    def generate_user(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    @action(methods=["patch"], detail=False)
    def change_password(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(methods=["post"], detail=False)
    def refresh_token(self, request, *args, **kwargs):
        return super().create_clone(request, data=False, *args, **kwargs)


class AddressViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.Address.objects.all()
    serializer_class = AddressSerializer

    def get_queryset(self):
        if self.action == "list":
            return self.queryset.filter(user=self.request.user)
        return super().get_queryset()


class CustomSocialLoginView(CustomLoginView, SocialLoginView):
    ...


class FacebookLogin(CustomSocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class GmailLogin(CustomSocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class AppleLogin(CustomSocialLoginView):
    adapter_class = AppleOAuth2Adapter


# TODO forget password cycle
# TODO verify user cycle
