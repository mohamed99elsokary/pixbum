from dj_rest_auth.serializers import JWTSerializer
from dj_rest_auth.views import LoginView
from django.conf import settings
from rest_framework import serializers


class CustomJWTSerializer(JWTSerializer):
    is_new = serializers.SerializerMethodField()

    def get_is_new(self, obj):
        user = obj["user"]
        return user.is_new


class CustomLoginView(LoginView):
    def get_response_serializer(self):
        if getattr(settings, "REST_USE_JWT", False):
            if getattr(settings, "JWT_AUTH_RETURN_EXPIRATION", True):
                return CustomJWTSerializer
        return super().get_response_serializer()
