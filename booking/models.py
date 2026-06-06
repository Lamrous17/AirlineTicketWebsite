from django.db import models





class Aircraft(models.Model):

    model = models.CharField(max_length=50)

    capacity = models.IntegerField()



    class Meta:

        managed = False

        db_table = 'aircraft'





class Flights(models.Model):

    flight_number = models.CharField(unique=True, max_length=10)

    destination = models.CharField(max_length=100)

    departure_time = models.DateTimeField()

    aircraft = models.ForeignKey(Aircraft, models.DO_NOTHING, blank=True, null=True)



    class Meta:

        managed = False

        db_table = 'flights'





class Passengers(models.Model):

    first_name = models.CharField(max_length=50)

    last_name = models.CharField(max_length=50)

    passport_number = models.CharField(unique=True, max_length=20)



    class Meta:

        managed = False

        db_table = 'passengers'





class Bookings(models.Model):

    passenger = models.ForeignKey(Passengers, models.DO_NOTHING)

    flight = models.ForeignKey(Flights, models.DO_NOTHING)

    seat = models.CharField(max_length=5, blank=True, null=True)

    booking_date = models.DateTimeField(blank=True, null=True)



    class Meta:

        managed = False

        db_table = 'bookings'

class Customer(models.Model):

    id = models.AutoField(primary_key=True)

    first_name = models.CharField(
        "Имя",
        max_length=50
    )

    last_name = models.CharField(
        "Фамилия",
        max_length=50
    )

    email = models.EmailField(
        "Email",
        unique=True
    )

    phone = models.CharField(
        "Телефон",
        max_length=20
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Payment(models.Model):

    id = models.AutoField(primary_key=True)

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )

    amount = models.DecimalField(
        "Сумма",
        max_digits=10,
        decimal_places=2
    )

    payment_date = models.DateTimeField(
        "Дата оплаты",
        auto_now_add=True
    )

    status = models.CharField(
        "Статус",
        max_length=20
    )

    def __str__(self):
        return f"Платеж #{self.id}"
    
class Ticket(models.Model):

    id = models.AutoField(primary_key=True)

    booking_id = models.IntegerField(
        "ID бронирования"
    )

    ticket_number = models.CharField(
        "Номер билета",
        max_length=20,
        unique=True
    )

    issue_date = models.DateField(
        "Дата выдачи"
    )

    def __str__(self):
        return self.ticket_number