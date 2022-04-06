from django.contrib import admin
from cars.models import (
    Car, Condition, Order,
    DeliveryZone, Delivery,
    Insurance, Extension,
    Customer, Administrator
)


@admin.register(Order)
class RentAdmin(admin.ModelAdmin):
    pass


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass


@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    pass


@admin.register(DeliveryZone)
class DeliveryZoneAdmin(admin.ModelAdmin):
    pass


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    pass


@admin.register(Insurance)
class InsuranceAdmin(admin.ModelAdmin):
    pass


@admin.register(Extension)
class ExtensionAdmin(admin.ModelAdmin):
    pass


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(Administrator)
class AdministratorAdmin(admin.ModelAdmin):
    pass