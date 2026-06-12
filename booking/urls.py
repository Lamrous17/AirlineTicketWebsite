from django.urls import path

from . import views

urlpatterns = [
    path(
        "",
        views.home,
        name="home"
    ),

    path(
        "flights/",
        views.flight_list,
        name="flight_list"
    ),

    path(
        "search/",
        views.search_flights,
        name="search_flights"
    ),

    path(
        "booking/<int:flight_id>/",
        views.book_flight,
        name="book_flight"
    ),
]