from typing import Text
from django.db.models import TextChoices


class CategoryChoices(TextChoices):
    """Перечисление категорий автомобиля"""

    ECONOMY = ("Эконом", "Эконом")
    STANDARD = ("Стандарт", "Стандарт")
    BUSINESS = ("Бизнес", "Бизнес")
    PREMIUM = ("Премиум", "Премиум")
    MINIBUS = ("Микроавтобус", "Микроавтобус")
    CROSSOVER = ("Кроссовер", "Кроссовер")
    SUV = ("Внедорожник", "Внедорожник")


class TransmissionChoices(TextChoices):
    """Перечисление типов трансмиссии"""

    Automatic = ("Автомат", "Автомат")
    Mechanics = ("Механика", "Механика")
    Hybrid = ("Вариатор", "Вариатор")


class EnigneTypeChoices(TextChoices):
    """Перечисление типов двигателей"""

    Gas = ("Бензиновый", "Бензиновый")
    Hybrid = ("Гибрид", "Гибрид")
    Electric = ("Электродвигатель", "Электродвигатель")
