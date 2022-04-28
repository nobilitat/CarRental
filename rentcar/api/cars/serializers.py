from dataclasses import field
from tkinter import filedialog
from rest_framework import serializers
from cars.models import Car, Order, Customer
from django.contrib.auth.models import User
from api.serviceoptions.serializers import (
    ConditionSerializer, 
    InsuranceSerializer,
    DeliverySerializer
)
from djoser.serializers import UserSerializer


class CarModelSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели автомобиля"""

    class Meta:
        model = Car
        fields = '__all__'


# class UserSerializer(serializers.ModelSerializer):
#     """Сериалайзер для модели пользователя"""

#     class Meta:
#         model = User
#         fields = (
#             "first_name",
#             "last_name",
#             "username"
#         )


class CustomerSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели клиента"""

    user = UserSerializer()

    class Meta:
        model = Customer
        fields = (
            "user",
        )


class OrderSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели заказа"""

    customer = CustomerSerializer()
    car = CarModelSerializer()
    condition = ConditionSerializer(many=True)
    insurance = InsuranceSerializer(many=True)
    delivery = DeliverySerializer()

    class Meta:
        model = Order
        fields = (
            "id",
            "customer",
            "car",
            "date_getting",
            "period",
            "order_price",
            "condition",
            "insurance",
            "delivery"
        )

