from rest_framework import serializers

from pixbum.addonsapp import models
from pixbum.services.custom_ModelSerializer import ErrorMixin

""" Contact us """


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactUs
        fields = "__all__"
