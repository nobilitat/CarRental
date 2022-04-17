from serviceoptions.models import (
    Condition, 
    Insurance, 
    Delivery, 
    DeliveryZone
)
from rest_framework import serializers


class ConditionSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели условий"""

    class Meta:
        model = Condition
        fields = '__all__'


class InsuranceSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели - тип страхования"""

    class Meta:
        model = Insurance
        fields = '__all__'


class DeliveryZoneSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели - Зоны Доставки"""

    class Meta:
        model = DeliveryZone
        fields = '__all__'


class DeliverySerializer(serializers.ModelSerializer):
    """Сериалайзер для модели условий"""

    delivery_zone = DeliveryZoneSerializer()

    class Meta:
        model = Delivery
        fields = (
            'delivery_zone',
            'address',
            'delivery_time'
        )