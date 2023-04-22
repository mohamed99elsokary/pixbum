from django.db import models


class Service(models.Model):
    # relations

    # fields
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    # relations
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    # fields
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
