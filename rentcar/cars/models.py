from distutils import extension
from django.db import models
from cars.choices import ( CategoryChoices, 
                           TransmissionChoices,
                           EnigneTypeChoices)
from django.contrib.auth.models import User


class Administrator(models.Model):
    "Класс администратора системы"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"User: {self.user}"


class Customer(models.Model):
    "Класс описания атрибутов клиента"

    user = models.ForeignKey(User, on_delete=models.CASCADE)

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

    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    car = models.ForeignKey("Car", on_delete=models.CASCADE)
    date_getting = models.DateField("Дата сдачии")
    period = models.IntegerField("Период аренды")
    order_price = models.IntegerField("Стоимость")
    condition = models.ManyToManyField("Condition", verbose_name="Условия аренды")
    insurance = models.ManyToManyField("Insurance", verbose_name="Тип страхования")
    delivery = models.ForeignKey("Delivery", on_delete=models.CASCADE)
    order_extension = models.ForeignKey("Extension", on_delete=models.CASCADE)

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


class Insurance(models.Model):
    "Описание типов страхования"

    insurance_name = models.CharField("Тип страхования", max_length=70)

    class Meta:
        verbose_name = "Тип страхования"
        verbose_name_plural = "Типы страхований"

    def __str__(self):
        return self.insurance_name


class DeliveryZone(models.Model):
    "Класс соответствия районов и тарифа на доставку"

    area_name = models.CharField("Название района", max_length=100)
    area_price = models.IntegerField("Тариф")
    
    class Meta:
        verbose_name = "Тариф на доставку"
        verbose_name_plural = "Тарифы на доставку"

    def __str__(self):
        return f"Area name: {self.area_name} - price: {self.area_price}"


class Delivery(models.Model):
    "Описание атрибутов доставки"

    delivery_zone = models.ForeignKey("DeliveryZone", verbose_name="Зоны доставки")
    address = models.CharField("Адрес доставки", max_length=150)
    delivery_time = models.DateTimeField('Время доставки')

    class Meta:
        verbose_name = "Доставка"
        verbose_name_plural = "Доставки"

    def __str__(self):
        return f"Adress: {self.address} - time: {self.delivery_time}"


class Extension(models.Model):
    "Класс продления заказа"

    days_amount = models.IntegerField("Количество дней")

    class Meta:
        verbose_name = "Продление"
        verbose_name_plural = "Продления"

    def __str__(self):
        return f"Days amount: {self.days_amount}"
