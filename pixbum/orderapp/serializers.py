from rest_framework import serializers

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
