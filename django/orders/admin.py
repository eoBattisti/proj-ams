from django.contrib import admin

from orders.models import Order, OrderType


admin.site.register(Order)
admin.site.register(OrderType)
