from rest_framework import serializers
from cars.models import Car


class CarModelSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели автомобиля"""

    class Meta:
        model = Car
        fields = '__all__'