from django.contrib import admin
from work.models import Customer, Orderline, Order, Payment

# Register your models here.

admin.site.register(Customer)
admin.site.register(Orderline)
admin.site.register(Order)
admin.site.register(Payment)
