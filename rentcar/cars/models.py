from distutils import extension
from django.db import models
from cars.choices import ( CategoryChoices, 
                           TransmissionChoices,
                           EnigneTypeChoices)
from django.contrib.auth.models import User
from serviceoptions.models import (
    Delivery, Condition,
    Insurance, Extension,
)

class Administrator(models.Model):
    "Класс администратора системы"

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Администратор"
        verbose_name_plural = "Администраторы"
    
    def __str__(self):
        return f"User: {self.user}"


class Customer(models.Model):
    "Класс описания атрибутов клиента"

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return f"User: {self.user}"


class Car(models.Model):
    """Класс описания полей для Автомобилей"""

    title = models.CharField("Название", max_length=120)
    category = models.CharField("Категория", max_length=30, choices=CategoryChoices.choices)
    busy = models.BooleanField("Занята")
    image = models.ImageField("Фото автомобиля", blank=True)
    apacity = models.IntegerField("Вместимость(чел)")
    consumption = models.IntegerField("Расход на 100км")
    transmission = models.CharField("Тип трансмиссии", max_length=10, choices=TransmissionChoices.choices)
    engine_power = models.IntegerField("Мощность двигателя")
    engine_type = models.CharField("Тип двигателя", max_length=40, choices=EnigneTypeChoices.choices)

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"

    def __str__(self):
        return self.title


class Order(models.Model):
    """Описание заказа"""

    active_state = models.BooleanField(default=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_getting = models.DateField("Дата сдачии")
    period = models.IntegerField("Период аренды")
    order_price = models.IntegerField("Стоимость")
    condition = models.ManyToManyField(Condition, verbose_name="Условия аренды")
    insurance = models.ManyToManyField(Insurance, verbose_name="Тип страхования")
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    order_extension = models.ForeignKey(Extension, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return str(self.car) + " " + str(self.date_getting)
