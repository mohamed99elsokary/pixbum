from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from . import filters, models, serializers


class ProductViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.Product.objects.all()
    serializer_class = serializers.DetailedProductSerializer
    filterset_fields = ["category"]

    def get_queryset(self):
        if self.action == "list":
            return self.queryset.prefetch_related("product_images", "product_features")
        return super().get_queryset()
