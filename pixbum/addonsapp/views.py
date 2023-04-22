from cities_light.models import Country, Region
from rest_framework import mixins, viewsets
from pixbum.addonsapp.models import ContactUs, PageSection
from pixbum.addonsapp.serializers import (
    ContactUsSerializer,
    CountrySerializer,
    PageSectionSerializer,
    RegionSerializer,
)

""" PageSection """


class PageSectionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PageSectionSerializer
    queryset = PageSection.objects.all()
    pagination_class = None
    filterset_fields = ("page_type",)


""" Contact us """


class ContactUsViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = ContactUs.objects
    serializer_class = ContactUsSerializer

    def perform_create(self, serializer):
        serializer.save()
        # serializer.instance.send_notification_email()


# cities_light


class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
    pagination_class = None


class RegionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()
    pagination_class = None
    filterset_fields = ("country",)
