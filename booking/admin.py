from django.contrib import admin

from .models import (
    Customer,
    Ticket,
    Payment
)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email",
        "phone"
    )

    search_fields = (
        "first_name",
        "last_name",
        "email"
    )


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "ticket_number",
        "booking_id",
        "issue_date"
    )

    search_fields = (
        "ticket_number",
    )


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "customer",
        "amount",
        "payment_date",
        "status"
    )

    search_fields = (
        "status",
    )

    list_filter = (
        "status",
    )