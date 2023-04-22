from django.db import models

from pixbum.productapp.models import Product
from pixbum.servicesapp.models import Service
from pixbum.userapp.models import Address, User


class Order(models.Model):
    # relations
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    # fields


class OrderDetails(models.Model):
    # relations
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="order_details",
    )
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # fields
    pdf = models.FileField(upload_to=None, max_length=100)
    quantity = models.IntegerField(default=1)
