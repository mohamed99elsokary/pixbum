from rest_framework import serializers

from pixbum.productapp.serializers import ProductSerializer, TinyProductSerializer
from pixbum.servicesapp.serializers import ServiceSerializer
from pixbum.userapp.serializers import AddressSerializer

from . import models


class DefaultUserAddress:
    requires_context = True

    def __call__(self, serializer_field):
        user = serializer_field.context["request"].user
        return models.Address.objects.filter(user=user).first()

    def __repr__(self):
        return "%s()" % self.__class__.__name__


class OrderDetailsSerializer(serializers.ModelSerializer):
    order = serializers.SlugRelatedField(read_only=True, slug_field="id")

    class Meta:
        model = models.OrderDetails
        read_only_fields = ("price",)
        fields = "__all__"

    def get_or_create_order(self):
        user = self.context["request"].user
        order = models.Order.objects.filter(user=user, is_checkout=False)
        if order:
            return order.first()
        return models.Order.objects.create(
            user=user, address=models.Address.objects.filter(user=user).first()
        )

    def create(self, validated_data):
        validated_data["order"] = self.get_or_create_order()
        return super().create(validated_data)


class TinyOrderDetailsSerializer(OrderDetailsSerializer):
    product = TinyProductSerializer()


class OrderSerializer(serializers.ModelSerializer):
    order_details = TinyOrderDetailsSerializer(many=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    address = AddressSerializer()

    class Meta:
        model = models.Order
        fields = "__all__"


class DraftSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Drafts
        fields = "__all__"


class DraftGetSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    service = ServiceSerializer()
    product = ProductSerializer()

    class Meta:
        model = models.Drafts
        fields = "__all__"


class AddToCartSerializer(serializers.Serializer):
    draft = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        user = self.context["request"].user
        user_cart = models.Cart.objects.filter(user=user).first()
        draft = models.Drafts.objects.filter(id=validated_data["draft"]).first()
        draft.cart = user_cart
        draft.quantity = 1
        draft.save()
        return draft


class CartSerializer(serializers.ModelSerializer):
    drafts = DraftGetSerializer(many=True, source="cart_drafts")

    class Meta:
        model = models.Cart
        fields = "__all__"


class OrderCheckOutSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = models.Order
        fields = ("url",)

    def get_url(self, obj):
        return "https://www.google.com/"
        return obj.payment.payment_url
