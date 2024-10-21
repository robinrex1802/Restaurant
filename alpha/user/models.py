from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
ROLE = [('Admin', 'Admin'), ('Employee', 'Employee'),
        ('NewCustomer', 'NewCustomer')]


class CustomUser(AbstractUser):
    role = models.CharField("Role", max_length=255,
                            choices=ROLE, null=True, blank=True)
    email = models.EmailField("Email", max_length=255,
                              unique=True, null=True, blank=True)
    customer = models.ForeignKey(
        "work.customer", verbose_name="coustomer", on_delete=models.CASCADE, null=True, blank=True)
