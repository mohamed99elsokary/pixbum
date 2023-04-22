from cities_light.models import Country, Region
from rest_framework import serializers
from pixbum.addonsapp import models
from pixbum.services.custom_ModelSerializer import ErrorMixin

""" PageSection """


class SliderPictureSerializer(ErrorMixin, serializers.ModelSerializer):
    class Meta:
        model = models.SliderPicture
        fields = "__all__"


class SectionContentSerializer(ErrorMixin, serializers.ModelSerializer):
    class Meta:
        model = models.SectionContent
        fields = "__all__"


class PageSectionSerializer(ErrorMixin, serializers.ModelSerializer):
    sectioncontent_set = SectionContentSerializer(many=True)
    sliderpicture_set = SliderPictureSerializer(many=True)

    class Meta:
        model = models.PageSection
        fields = "__all__"


""" Contact us """


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactUs
        fields = "__all__"


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"
