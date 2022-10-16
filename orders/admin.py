from django.contrib import admin
from orders.models import OrderItem

admin.site.register(OrderItem)
class OrderItem(admin.ModelAdmin):
    fields = ('status',)