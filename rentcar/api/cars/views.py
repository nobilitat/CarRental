from django.shortcuts import render
from rest_framework import generics
from api.cars.serializers import CarModelSerializer, OrderSerializer
from cars.models import Car, Order


class CarListView(generics.ListAPIView):
    """Вывод списка автомобилей"""

    serializer_class = CarModelSerializer
    queryset = Car.objects.all()


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Редактирование, удаление, просмотр списка автомобилей"""

    serializer_class = CarModelSerializer
    queryset = Car.objects.all()


class OrderListView(generics.ListAPIView):
    """Вывод списка заказов"""

    serializer_class = OrderSerializer
    queryset = Order.objects.all()