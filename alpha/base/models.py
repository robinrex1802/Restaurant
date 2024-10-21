from tabnanny import verbose
from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField("City", max_length=255, null=True, blank=False)

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField("Place", max_length=255, null=True, blank=False)

    def __str__(self):
        return self.name
