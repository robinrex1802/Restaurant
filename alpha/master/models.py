from distutils.command.upload import upload
from django.db import models
from base .models import City, Place

# Create your models here.


class Company(models.Model):
    name = models.CharField("Name", max_length=255, null=True, blank=False)
    code = models.CharField("Code", max_length=255, null=True, blank=False)
    phoneno = models.BigIntegerField("Phone", null=True, blank=False)
    start_date = models.DateField("Start_date", null=True, blank=False)
    approvel_date = models.DateField("Approvel_date", null=True, blank=False)
    address = models.CharField(
        "Address", max_length=255, null=True, blank=False)
    state = models.CharField("State", max_length=255, null=True, blank=False)
    City = models.ForeignKey(
        City, on_delete=models.CASCADE, null=True, blank=False)
    Place = models.ForeignKey(
        Place, on_delete=models.CASCADE, null=True, blank=False)
    email = models.EmailField('Email', null=True, blank=False)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField("Name", max_length=255, null=True, blank=False)
    code = models.ForeignKey(
        Company, on_delete=models.CASCADE, null=True, blank=False)

    state = models.CharField("State", max_length=255, null=True, blank=False)
    address = models.CharField(
        "Address", max_length=255, null=True, blank=False)
    City = models.ForeignKey(
        City, on_delete=models.CASCADE, null=True, blank=False)
    Place = models.ForeignKey(
        Place, on_delete=models.CASCADE, null=True, blank=False)
    phoneno = models.BigIntegerField("Phone", null=True, blank=False)
    email = models.EmailField('Email', null=True, blank=False)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField("Name", max_length=255, null=True, blank=False)
 # variety = models.CharField(
    # "Variety", max_length=255, null=True, blank=False)
    # food_refernce = models.CharField( "Food_refernce", max_length=255, null=True, blank=False)
    description = models.CharField(
        " Description ", max_length=250, null=True, blank=False)
    quantity = models.IntegerField("Quantity", null=True, blank=False)
    # time = models.TimeField("Timing", null=True, blank=False)
    price = models.FloatField("Price", null=True, blank=False)
    image = models.ImageField(
        upload_to="Picture", null=True, blank=False)

    def __str__(self):
        return self.name
