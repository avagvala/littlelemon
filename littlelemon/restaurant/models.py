from django.db import models
from django.core.validators import MaxLengthValidator, MaxValueValidator, MinLengthValidator, MinValueValidator

# Create your models here.
class Booking(models.Model):
    Name = models.CharField(max_length=255)  
    No_of_guests = models.IntegerField(validators=[MaxValueValidator(999999),MinValueValidator(0),])
    BookingDate = models.DateField()

class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField(validators=[MaxValueValidator(99999),MinValueValidator(0),])

    def __str__(self):
        return f'{self.Title} : {str(self.Price)}'