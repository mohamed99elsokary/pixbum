from rest_framework import mixins, viewsets

from . import filters, models, serializers


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer


class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    filterset_class = filters.CategoryFilter

    def get_queryset(self):
        if self.action == "list":
            return models.Category.objects.all().prefetch_related("category_products")
        return super().get_queryset()
