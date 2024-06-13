from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=255)
    number_of_guests = models.IntegerField(default='6')
    booking_date = models.DateTimeField()

class Menu(models.Model):
   title = models.CharField(max_length=200) 
   price = models.DecimalField(max_digits=6, decimal_places=2) 
   inventory = models.IntegerField(default='5')