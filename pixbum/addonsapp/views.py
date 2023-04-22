from rest_framework import mixins, viewsets

from pixbum.addonsapp.models import ContactUs
from pixbum.addonsapp.serializers import ContactUsSerializer

""" PageSection """


""" Contact us """


class ContactUsViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = ContactUs.objects
    serializer_class = ContactUsSerializer

    def perform_create(self, serializer):
        serializer.save()
