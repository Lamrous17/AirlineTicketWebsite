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
