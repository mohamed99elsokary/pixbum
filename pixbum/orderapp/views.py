from rest_framework import mixins, viewsets

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
