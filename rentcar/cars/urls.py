from django.contrib import admin
from django.urls import path, include
from api.cars.views import CarDetailView,CarListView


urlpatterns = [
    path('list', CarListView.as_view()),
    path('detail/<int:pk>', CarDetailView.as_view())
]
