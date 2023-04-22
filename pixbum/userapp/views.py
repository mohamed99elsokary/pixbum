from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework import mixins, status ,viewsets
from rest_framework.decorators import action
from rest_framework.response import Response



from pixbum.userapp import models
from pixbum.userapp.serializers import (
    LoginSerializer,
    UserDataSerializer,
    UserSerializer,
)
class UserViewSet(viewsets.GenericViewSet):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == "login":
            return LoginSerializer
        elif self.action == "update_me":
            return UserDataSerializer
        elif self.action == "get_me":
            return UserDataSerializer
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

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

# TODO forget password cycle 
# TODO verify user cycle