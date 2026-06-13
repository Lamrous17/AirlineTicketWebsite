from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from .tasks import send_booking_notification

from booking.models import Flights

from .models import (
    CartItem,
    BookingOrder,
    BookingOrderItem
)

from .forms import (
    OrderForm,
    PaymentForm
)


def my_bookings(request):

    if not request.user.is_authenticated:

        return redirect("login")

    flights = CartItem.objects.filter(
        user=request.user
    )

    return render(
        request,
        "my_bookings.html",
        {
            "flights": flights
        }
    )


def add_booking(request, flight_id):

    if not request.user.is_authenticated:

        return redirect("login")

    flight = Flights.objects.get(
        id=flight_id
    )

    exists = CartItem.objects.filter(
        user=request.user,
        flight_id=flight.id
    ).exists()

    if not exists:

        CartItem.objects.create(
            user=request.user,
            flight_id=flight.id,
            flight_number=flight.flight_number,
            destination=flight.destination,
            departure_time=flight.departure_time
        )

    return redirect(
        "my_bookings"
    )

def create_order(request):

    if not request.user.is_authenticated:

        return redirect("login")

    if request.method == "POST":

        form = OrderForm(request.POST)

        if form.is_valid():

            order = BookingOrder.objects.create(
                user=request.user,
                seat_number=first_item.seat_number,
                seat_class=first_item.seat_class,
                price=sum(
                    item.price
                    for item in cart_items
                )
            )

            cart_items = CartItem.objects.filter(
                user=request.user
            )

            for item in cart_items:
                BookingOrderItem.objects.create(
                    order=order,
                    flight_number=item.flight_number,
                    destination=item.destination,
                    departure_time=item.departure_time,
                    seat_number=item.seat_number,
                    seat_class=item.seat_class,
                    price=item.price
                )

            cart_items.delete()
            if request.user.email:
                send_booking_notification(
                    request.user.email
                )

            return render(
                request,
                "order_success.html",
                {
                    "created_at": timezone.now()
                }
            )

    else:

        form = OrderForm()

    return render(
        request,
        "order_create.html",
        {
            "form": form
        }
    )

def remove_booking(request, item_id):

    if not request.user.is_authenticated:

        return redirect("login")

    CartItem.objects.filter(
        id=item_id,
        user=request.user
    ).delete()

    return redirect(
        "my_bookings"
    )

def payment(request):

    cart_items = CartItem.objects.filter(
        user=request.user
    )

    total = sum(
        item.price for item in cart_items
    )

    if request.method == "POST":

        form = PaymentForm(
            request.POST
        )

        if form.is_valid():

            return redirect(
                "create_order"
            )

    else:

        form = PaymentForm()

    return render(
        request,
        "payment.html",
        {
            "form": form,
            "total": total
        }
    )
def order_history(request):

    orders = BookingOrder.objects.filter(
        user=request.user
    ).order_by(
        "-created_at"
    )

    return render(
        request,
        "order_history.html",
        {
            "orders": orders
        }
    )