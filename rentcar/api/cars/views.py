from django.shortcuts import render
from rest_framework import generics
from api.cars.serializers import CarModelSerializer
from cars.models import Car


class CarListView(generics.ListAPIView):
    """Вывод списка автомобилей"""

    serializer_class = CarModelSerializer
    queryset = Car.objects.all()


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Редактирование, удаление, просмотр списка автомобилей"""

    serializer_class = CarModelSerializer
    queryset = Car.objects.all()