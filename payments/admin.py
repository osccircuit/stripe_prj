from django.contrib import admin
from payments.models import Item, Order, OrderItem

admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)