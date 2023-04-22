from django.db import models

from pixbum.productapp.models import Product
from pixbum.servicesapp.models import Service
from pixbum.userapp.models import Address, User


class Order(models.Model):
    # relations
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    # fields

    def __str__(self):
        return self.name


class OrderDetails(models.Model):
    # relations
    oder = models.ForeignKey(Order, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # fields
    pdf = models.FileField(upload_to=None, max_length=100)

    def __str__(self):
        return self.name
