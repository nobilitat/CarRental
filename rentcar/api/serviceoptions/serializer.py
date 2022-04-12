from serviceoptions.models import Condition
from rest_framework import serializers


class ConditionSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели условий"""

    class Meta:
        model = Condition
        fields = '__all__'