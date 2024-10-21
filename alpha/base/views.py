from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from master.models import *
from work.models import *

# Create your views here.


class CityView(viewsets.ModelViewSet):
    serializer_class = Cityserialize
    queryset = City.objects.all()


class PlaceView(viewsets.ModelViewSet):
    serializer_class = Placeserialize
    queryset = Place.objects.all()


class CompanyView(viewsets.ModelViewSet):
    serializer_class = Companyserialize
    queryset = Company.objects.all()


class EmployeeView(viewsets.ModelViewSet):
    serializer_class = Employeeserialize
    queryset = Employee.objects.all()


class FoodView(viewsets.ModelViewSet):
    serializer_class = Foodserialize
    queryset = Food.objects.all()


class CustmoerView(viewsets.ModelViewSet):
    serializer_class = Customerserialize
    queryset = Customer.objects.all()


class OrderlineView(viewsets.ModelViewSet):
    serializer_class = Orderlineserialize
    queryset = Orderline.objects.all()


class OrderView(viewsets.ModelViewSet):
    serializer_class = Orderserialize
    queryset = Order.objects.all()


class PaymentView(viewsets.ModelViewSet):
    serializer_class = Paymentserialize
    queryset = Payment.objects.all()
