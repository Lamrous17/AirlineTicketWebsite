from django.shortcuts import (
    render,
    redirect
)

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

from .forms import RegisterForm

from django.db.models import Q

from .models import Flights
from orders.models import CartItem


def home(request):

    return render(
        request,
        "home.html"
    )


def flight_list(request):

    flights = Flights.objects.all().order_by(
        "departure_time"
    )

    return render(
        request,
        "flight_list.html",
        {
            "flights": flights
        }
    )


def book_flight(request, flight_id):

    flight = Flights.objects.get(
        id=flight_id
    )

    return render(
        request,
        "booking_form.html",
        {
            "flight": flight
        }
    )

def search_flights(request):

    query = request.GET.get(
        "q",
        ""
    ).strip()

    flights = []

    if query:

        flights = Flights.objects.filter(

            Q(
                flight_number__icontains=query
            )
            |
            Q(
                destination__icontains=query
            )

        ).order_by(
            "departure_time"
        )

    return render(
        request,
        "search.html",
        {
            "query": query,
            "flights": flights
        }
    )

def register_user(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect(
                "login"
            )

    else:

        form = RegisterForm()

    return render(
        request,
        "register.html",
        {
            "form": form
        }
    )
def select_seat(request, flight_id):

    seat = request.GET.get(
        "seat"
    )

    seat_class = request.GET.get(
        "class"
    )

    if seat:

        price = 5000

        if seat_class == "business":

            price = 15000

        CartItem.objects.filter(
            user=request.user,
            flight_id=flight_id
        ).update(
            seat_number=seat,
            seat_class=seat_class,
            price=price
        )

        return redirect(
            "my_bookings"
        )

    return render(
        request,
        "seat_selection.html",
        {
            "flight_id": flight_id
        }
    )