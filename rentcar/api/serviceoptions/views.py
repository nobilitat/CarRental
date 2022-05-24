from rest_framework import generics
from api.serviceoptions.serializers import (
    ConditionSerializer
)
from cars.models import Condition


class ConditionsListView(generics.ListAPIView):
    """Вывод списка условий"""

    serializer_class = ConditionSerializer
    queryset = Condition.objects.all()
