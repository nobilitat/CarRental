from django.contrib import admin
from cars.models import Car, Condition, Rent


@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    pass


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass


@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    pass