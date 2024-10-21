from dataclasses import field
from importlib import import_module

from rest_framework import serializers
from .models import *
from master.models import *
from work.models import *


class Cityserialize(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


class Placeserialize(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = "__all__"


class Companyserialize(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = "__all__"

    def to_representation(self, instance):
        result = super().to_representation(instance)
        result['City'] = [instance.City.id, instance.City.name]
        result['Place'] = [instance.Place.id, instance.Place.name]
        return result


class Employeeserialize(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

    def to_representation(self, instance):
        result = super().to_representation(instance)
        result['code'] = [instance.code.id, instance.code.name]
        result['City'] = [instance.City.id, instance.City.name]
        result['Place'] = [instance.Place.id, instance.Place.name]
        return result


class Foodserialize(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"


class Customerserialize(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

    # def to_representation(self, instance):
    #     result = super().to_representation(instance)

    #     result['City'] = [instance.City.id, instance.City.name]
    #     result['Place'] = [instance.Place.id, instance.Place.name]
    #     return result


class Orderlineserialize(serializers.ModelSerializer):
    class Meta:
        model = Orderline
        fields = "__all__"

    def to_representation(self, instance):
        result = super().to_representation(instance)
        result['food'] = [instance.food.id, instance.food.name]
        return result


class Orderserialize(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

    def to_representation(self, instance):
        result = super().to_representation(instance)
        result['customer'] = [instance.customer.id, instance.customer.name]
        result['amount'] = [instance.amount.id, instance.amount.amount]
        result['City'] = [instance.City.id, instance.City.name]
        result['Place'] = [instance.Place.id, instance.Place.name]
        return result


class Paymentserialize(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"

    def to_representation(self, instance):
        result = super().to_representation(instance)
        result['customer'] = [instance.customer.id, instance.customer.name]
        result['amount'] = [instance.amount.id, instance.amount.amount]

        return result
