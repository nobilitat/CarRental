from django.contrib import admin
from django.urls import path, include
from api.cars.views import (
    CarDetailView,
    CarListView,
    OrderListView,
    OrderDetailView,
    OrderCreateView
)


urlpatterns = [
    path('car/list', CarListView.as_view()),
    path('order/list', OrderListView.as_view()),
    path('car/detail/<int:pk>', CarDetailView.as_view()),
    path('order/detil/<int:pk>', OrderDetailView.as_view()),
    path('order/create', OrderCreateView.as_view())
]
