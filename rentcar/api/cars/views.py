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
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)

class CarListView(generics.ListAPIView):
    """Вывод списка автомобилей"""

    serializer_class = CarModelSerializer
    queryset = Car.objects.all()


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Редактирование, удаление, просмотр списка автомобилей"""

    permission_classes = (IsAuthenticatedOrReadOnly,)

    serializer_class = CarModelSerializer
    queryset = Car.objects.all()


class OrderListView(views.APIView):
    """Вывод списка заказов для конкретного пользователя"""

    permission_classes = (IsAuthenticated,)
    
    def post(self, request):
        alldata = request.data
        user = alldata.get("username")
        queryset = Order.objects.filter(
            customer__user__username = user)
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Редактирование, удаление, просмотр списка списка заказов"""

    permission_classes = (IsAuthenticated,)

    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderCreateView(generics.CreateAPIView):
    """Создание заказа"""

    permission_classes = (IsAuthenticated,)

    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class UserGetView(views.APIView):
    """Получение пользователя"""

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        alldata = request.data
        user_id = alldata.get("user_id")
        queryset = User.objects.filter(id = user_id)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


class LogoutView(APIView):
    """Выход пользователя из системы"""

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)