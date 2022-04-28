from this import d
from django.shortcuts import render
from rest_framework import generics
from rest_framework import views
from api.cars.serializers import (
    CarModelSerializer, 
    OrderSerializer
)
from cars.models import Car, Order
from rest_framework.response import Response
from django.contrib.auth.models import User
from djoser.serializers import UserSerializer


class CarListView(generics.ListAPIView):
    """Вывод списка автомобилей"""

    serializer_class = CarModelSerializer
    queryset = Car.objects.all()


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Редактирование, удаление, просмотр списка автомобилей"""

    serializer_class = CarModelSerializer
    queryset = Car.objects.all()


class OrderListView(views.APIView):
    
    def post(self, request):
        alldata = request.data
        user = alldata.get("username")
        queryset = Order.objects.filter(
            customer__user__username = user)
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Редактирование, удаление, просмотр списка списка заказов"""

    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderCreateView(generics.CreateAPIView):
    """Создание заказа"""

    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class UserGetView(views.APIView):
    """Получение пользователя"""

    def post(self, request):
        alldata = request.data
        user = alldata.get("username")
        queryset = User.objects.filter(username = user)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)