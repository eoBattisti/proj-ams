from django.contrib import admin

# Register your models here.

from orders.models import Order, OrderType


admin.site.register(Order)
admin.site.register(OrderType)
