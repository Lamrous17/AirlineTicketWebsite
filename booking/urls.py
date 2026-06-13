from django.urls import path

from . import views

from django.contrib.auth.views import (
    LoginView,
    LogoutView
)

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
    path(
        "register/",
        views.register_user,
        name="register"
    ),

    path(
        "login/",
        LoginView.as_view(
            template_name="login.html"
        ),
        name="login"
    ),

    path(
        "logout/",
        LogoutView.as_view(
            next_page="home"
        ),
        name="logout"
    ),
    path(
        "seat/<int:flight_id>/",
        views.select_seat,
        name="select_seat"
    ),
]