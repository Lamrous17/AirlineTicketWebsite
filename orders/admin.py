from django.contrib import admin

from .models import (
    CartItem,
    BookingOrder,
    BookingOrderItem
)

admin.site.register(CartItem)
admin.site.register(BookingOrder)
admin.site.register(BookingOrderItem)