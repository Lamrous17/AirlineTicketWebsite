from django import forms


class OrderForm(forms.Form):

    first_name = forms.CharField(
        label="Имя"
    )

    last_name = forms.CharField(
        label="Фамилия"
    )

    passport_number = forms.CharField(
        label="Паспорт"
    )

    phone = forms.CharField(
        label="Телефон"
    )

class PaymentForm(forms.Form):

    bank = forms.ChoiceField(
        choices=[
            ("sber","Сбербанк"),
            ("vtb","ВТБ"),
            ("tbank","Т-Банк"),
            ("alfabank","Альфа-Банк")
        ]
    )

    card_number = forms.CharField(
        max_length=16
    )