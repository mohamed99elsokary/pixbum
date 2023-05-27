from django.db import models
from payment.models import Payment

from pixbum.productapp.models import Product
from pixbum.servicesapp.models import Service
from pixbum.userapp.models import Address, User


class Order(models.Model):
    # relations
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    payment = models.OneToOneField(
        Payment,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )
    # fields
    is_checkout = models.BooleanField(default=False)


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


class Drafts(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, default=None
    )
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, null=True, blank=True, default=None
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, blank=True, default=None
    )
    images = models.JSONField(null=True, blank=True, default=None)
    layouts = models.JSONField(null=True, blank=True, default=None)
    cart = models.ForeignKey(
        "Cart",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
        related_name="cart_drafts",
    )
    quantity = models.IntegerField(null=True, blank=True, default=None)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
