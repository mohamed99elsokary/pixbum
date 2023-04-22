from django.db import models

from pixbum.servicesapp.models import Category, Service


class Product(models.Model):
    # relations
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name="service_products"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category_products"
    )
    # fields
    width = models.IntegerField(default=1)
    height = models.IntegerField(default=1)
    cover_photo = models.ImageField(
        upload_to="media/",
        height_field=None,
        width_field=None,
        max_length=None,
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=50)
    min_photos_amount = models.IntegerField(default=1)
    max_photos_amount = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class ProductImages(models.Model):
    # relations
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_images"
    )
    # fields
    image = models.ImageField(
        upload_to="media/", height_field=None, width_field=None, max_length=None
    )


class ProductFeatures(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_features"
    )
    # fields
    logo = models.ImageField(
        upload_to="media/", height_field=None, width_field=None, max_length=None
    )
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
