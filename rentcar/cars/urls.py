from django.contrib import admin
from django.urls import path, include
from api.cars.views import (
    CarDetailView,
    CarListView,
    OrderListView,
    OrderDetailView,
    OrderCreateView,
    UserGetView,
    LogoutView
)


urlpatterns = [
    path('car/list', CarListView.as_view()),
    path('order/list', OrderListView.as_view()),
    path('car/detail/<int:pk>', CarDetailView.as_view()),
    path('order/detail/<int:pk>', OrderDetailView.as_view()),
    path('order/create', OrderCreateView.as_view()),

    # User action
    path('user', UserGetView.as_view()),
    path('logout/', LogoutView.as_view()),
]
