from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from .views import *


routers = routers.DefaultRouter()
routers.register("City", CityView)
routers.register("Place", PlaceView)
routers.register("Company", CompanyView)
routers.register("Employee", EmployeeView)
routers.register("Food", FoodView)
routers.register("Customer", CustmoerView)
routers.register("Orderline", OrderlineView)
routers.register("Order", OrderView)
routers.register("Payment", PaymentView)


urlpatterns = [
    path("api/", include(routers.urls)),
]
