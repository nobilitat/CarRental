from django.shortcuts import render
from rest_framework import generics
from api.cars.serializers import CarModelSerializer, OrderSerializer
from cars.models import Car, Order
from rest_framework.response import Response


class CarListView(generics.ListAPIView):
    """Вывод списка автомобилей"""

    serializer_class = CarModelSerializer
    queryset = Car.objects.all()


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Редактирование, удаление, просмотр списка автомобилей"""

    serializer_class = CarModelSerializer
    queryset = Car.objects.all()


class OrderListView(generics.ListAPIView):
    """Вывод списка заказов для конкретного пользователя"""

    serializer_class = OrderSerializer

    def list(self, request, *args, **kwargs):
        alldata = request.data
        user = alldata.get("username")

        if user:
            queryset = Order.objects.filter(
                customer__user__username = user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Редактирование, удаление, просмотр списка списка заказов"""

    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderCreateView(generics.CreateAPIView):
    """Создание заказа"""

    serializer_class = OrderSerializer
    queryset = Order.objects.all()