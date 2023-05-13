from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from pixbum.services.views import BulkCreateModelMixin

from . import models, serializers


class OrderViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class OrderDetailsViewSet(
    BulkCreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.OrderDetails.objects.all()
    serializer_class = serializers.OrderDetailsSerializer


class DraftViewSet(viewsets.ModelViewSet):
    queryset = models.Drafts.objects.all()
    serializer_class = serializers.DraftSerializer

    def get_queryset(self):
        if self.action == "list":
            return self.queryset.filter(user=self.request.user)
        return super().get_queryset()

    def get_serializer_class(self):
        if self.action in {"list", "retrieve"}:
            return serializers.DraftGetSerializer
        if self.action == "add_to_cart":
            return serializers.AddToCartSerializer
        return super().get_serializer_class()

    @action(methods=["post"], detail=False)
    def add_to_cart(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class CartViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.Cart.objects.all()
    serializer_class = serializers.CartSerializer

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    @action(methods=["DELETE"], detail=False)
    def clear_cart(self, request):
        cart = self.queryset.filter(user=self.request.user).first()
        drafts = models.Drafts.objects.filter(cart=cart)
        drafts.update(cart=None)
        return Response("success")
