from django.db import models
from cars.choices import ( CategoryChoices, 
                           TransmissionChoices,
                           EnigneTypeChoices)


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


class Rent(models.Model):
    """Описание сервиса аренды автомобилей"""

    car = models.ForeignKey("Car", on_delete=models.CASCADE)
    date_out = models.DateField("Дата сдачии")
    period = models.IntegerField("Период аренды")
    price = models.IntegerField("Стоимость")
    condition = models.ManyToManyField("Condition", verbose_name="Условия аренды")

    class Meta:
        verbose_name = "Сервис аренды"
        verbose_name_plural = "Сервис Аренды"

    def __str__(self):
        return str(self.car) + " " + str(self.date_out)


class Condition(models.Model):
    
    """Описание условий"""
    condition_name = models.CharField("Условие", max_length=50)

    class Meta:
        verbose_name = "Условие"
        verbose_name_plural = "Условия"

    def __str__(self):
        return self.condition_name