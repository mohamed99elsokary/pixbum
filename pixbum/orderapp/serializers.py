from rest_framework import serializers

from pixbum.productapp.serializers import ProductSerializer
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


class DefaultUserOrder:
    requires_context = True

    def __call__(self, serializer_field):
        user = serializer_field.context["request"].user
        order = models.Order.objects.filter(user=user)
        if order:
            return order.first()
        return models.Order.objects.create(
            user=user, address=models.Address.objects.filter(user=user).first()
        )

    def __repr__(self):
        return "%s()" % self.__class__.__name__


class OrderDetailsSerializer(serializers.ModelSerializer):
    order = serializers.HiddenField(default=DefaultUserOrder())

    class Meta:
        model = models.OrderDetails
        # fields = "__all__"
        exclude = ("pdf",)


class OrderSerializer(serializers.ModelSerializer):
    order_details = OrderDetailsSerializer(many=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    total = serializers.SerializerMethodField()
    address = AddressSerializer()

    class Meta:
        model = models.Order
        fields = "__all__"

    def get_total(self, obj):
        total = 0
        for product in obj.order_details.all():
            price = product.product.price * product.quantity
            total += price
        return total


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
