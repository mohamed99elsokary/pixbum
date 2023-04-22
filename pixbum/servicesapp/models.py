from django.db import models


class Service(models.Model):
    # relations

    # fields
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name