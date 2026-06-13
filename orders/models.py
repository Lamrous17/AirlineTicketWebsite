from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class CartItem(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    flight_id = models.IntegerField()

    flight_number = models.CharField(
        max_length=20
    )

    destination = models.CharField(
        max_length=100
    )

    departure_time = models.DateTimeField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    seat_number = models.CharField(
        max_length=5,
        default=""
    )

    seat_class = models.CharField(
        max_length=20,
        default="Эконом"
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    def __str__(self):

        return self.flight_number
    
class BookingOrder(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        default=timezone.now
    )

    seat_number = models.CharField(
        max_length=5,
        default=""
    )

    seat_class = models.CharField(
        max_length=20,
        default="Эконом"
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    def __str__(self):

        return f"Order #{self.id}"
    
class BookingOrderItem(models.Model):

    order = models.ForeignKey(
        BookingOrder,
        on_delete=models.CASCADE
    )

    flight_number = models.CharField(
        max_length=20
    )

    destination = models.CharField(
        max_length=100
    )

    departure_time = models.DateTimeField()

    seat_number = models.CharField(
        max_length=5,
        default=""
    )

    seat_class = models.CharField(
        max_length=20,
        default="Эконом"
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )