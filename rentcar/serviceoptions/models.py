from django.db import models


class Condition(models.Model):
    """Описание условий"""

    condition_name = models.CharField("Условие", max_length=100)

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

    delivery_zone = models.ForeignKey(DeliveryZone, verbose_name="Зоны доставки", on_delete=models.CASCADE)
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
