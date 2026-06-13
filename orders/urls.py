from django.urls import path

from . import views

urlpatterns = [

    path(
        "my-bookings/",
        views.my_bookings,
        name="my_bookings"
    ),

    path(
        "add-booking/<int:flight_id>/",
        views.add_booking,
        name="add_booking"
    ),
    path(
        "create-order/",
        views.create_order,
        name="create_order"
    ),
    path(
        "remove-booking/<int:item_id>/",
        views.remove_booking,
        name="remove_booking"
    ),
    path(
        "payment/",
        views.payment,
        name="payment"
    ),
    path(
        "history/",
        views.order_history,
        name="order_history"
    ),
]