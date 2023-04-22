from django_filters import rest_framework as filters

from . import models


class CategoryFilter(filters.FilterSet):
    class Meta:
        model = models.Category
        fields = [
            "service",
        ]
