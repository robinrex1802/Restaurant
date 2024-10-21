from django.db import models
from base.models import *
from master.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from user.models import CustomUser
from django.contrib.auth.models import Group


# Create your models here.


class Customer(models.Model):
    name = models.CharField("Name", max_length=255, null=True, blank=False)
    phoneno = models.BigIntegerField("Phone", null=True, blank=False)
    address = models.CharField(
        "Address", max_length=255, null=True, blank=False)
    # City = models.ForeignKey(
    #     City, on_delete=models.CASCADE, null=True, blank=False)
    # Place = models.ForeignKey(
    #     Place, on_delete=models.CASCADE, null=True, blank=False)
    pincode = models.IntegerField("Pincode", null=True, blank=False)
    email = models.EmailField('Email', null=True, blank=False)
    # password = models.CharField(
    #     "Password", max_length=225, null=True, blank=False)
    customertype = models.CharField(
        "CustomerType", max_length=100, null=True, blank=True, default='NewCustomer')

    def __str__(self):
        return str(self.name)


@receiver(post_save, sender=Customer)
def event_attender_create(sender, instance, *args, **kwargs):
    if instance and kwargs['created']:
        user = CustomUser.objects.create(email=instance.email, username=instance.name.lower(),
                                         customer=instance, role="NewCustomer", is_staff=True)
        user.set_password(instance.email)
    if instance.customertype == "NewCustomer":
        if Group.objects.filter(name='NewUser').exists():
            user.groups.add(Group.objects.get(name='NewUser'))
            user.save()
            return True


class Orderline(models.Model):
    food = models.ForeignKey(
        Food, on_delete=models.CASCADE, null=True, blank=False)
    quantity = models.IntegerField("Quanity", null=True, blank=False)
    amount = models.FloatField("amount", null=True, blank=False)

    def __str__(self):
        print(self.food)
        return str(self.food.name)


class Order(models.Model):
    name = models.CharField(
        "Order_refernce", max_length=255, null=True, blank=False)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True, blank=False)
    order_date = models.DateField("Orderdate", null=True, blank=False)
    amount = models.ForeignKey(
        Orderline, on_delete=models.CASCADE, null=True, blank=False)
    address = models.CharField(
        "Address", max_length=255, null=True, blank=False)
    City = models.ForeignKey(
        City, on_delete=models.CASCADE, null=True, blank=False)
    Place = models.ForeignKey(
        Place, on_delete=models.CASCADE, null=True, blank=False)
    pincode = models.IntegerField("Pincode", null=True, blank=False)

    # def __str__(self):
    #     return self.name
    def __str__(self):
        # print(self.amount)
        return str(self.amount.food)+"-"+str(self.amount.amount)
        # return self.amount


class Payment(models.Model):
    name = models.CharField(
        "Pay_refernce", max_length=255, null=True, blank=False)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True, blank=False)
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, null=True, blank=False)
    pay = models.CharField("Paytype", choices=[('googlepay', 'Googlepay'), (
        'phonepay', 'Phonepay'), ('paytym', 'Paytym')], max_length=250, null=True, blank=False)
    amount = models.ForeignKey(
        Orderline, on_delete=models.CASCADE, null=True, blank=False)
    paydate = models.DateField("Paydate",

                               null=True, blank=False)

    def __str__(self):
        return str(self.amount.amount) if self.amount else ""
