from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from unittest.mock import patch

from .models import CartItem


class CartItemTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="testuser",
            password="12345"
        )

    # обычный тест модели
    def test_cart_item_creation(self):

        item = CartItem.objects.create(
            user=self.user,
            flight_id=1,
            flight_number="SU1001",
            destination="Москва",
            departure_time="2026-06-10 08:00"
        )

        self.assertEqual(
            item.flight_number,
            "SU1001"
        )

    # тест коллекции
    def test_cart_collection(self):

        CartItem.objects.create(
            user=self.user,
            flight_id=1,
            flight_number="SU1001",
            destination="Москва",
            departure_time="2026-06-10 08:00"
        )

        CartItem.objects.create(
            user=self.user,
            flight_id=2,
            flight_number="SU1002",
            destination="СПб",
            departure_time="2026-06-11 08:00"
        )

        items = CartItem.objects.filter(
            user=self.user
        )

        self.assertEqual(
            len(items),
            2
        )

    # тест исключения
    def test_invalid_user(self):

        with self.assertRaises(
            ValueError
        ):

            User.objects.create_user(
                username=""
            )


class ViewTest(TestCase):

    def test_home_page(self):

        response = self.client.get("/")

        self.assertEqual(
            response.status_code,
            200
        )


class MockTest(TestCase):

    @patch("orders.tasks.send_mail")
    def test_email_notification_mock(
        self,
        mock_send_mail
    ):

        from orders.tasks import (
            send_booking_notification
        )

        send_booking_notification(
            "test@test.ru"
        )

        mock_send_mail.assert_called_once()