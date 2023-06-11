from rest_framework import serializers

from . import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = "__all__"


class TinyProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ("id", "name")


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductImages
        fields = "__all__"


class ProductFeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductFeatures
        fields = "__all__"


class DetailedProductSerializer(serializers.ModelSerializer):
    images = ProductImagesSerializer(many=True, source="product_images")
    features = ProductFeaturesSerializer(many=True, source="product_features")

    class Meta:
        model = models.Product
        fields = "__all__"
