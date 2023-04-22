from rest_framework import serializers

from pixbum.productapp.serializers import ProductSerializer

from . import models


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, source="category_products")

    class Meta:
        model = models.Category
        fields = "__all__"
