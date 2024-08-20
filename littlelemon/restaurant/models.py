from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    reservation_date = models.DateTimeField()
    no_of_guests = models.IntegerField()
    reservation_slot = models.SmallIntegerField(default=10)

    def __str__(self): 
        return self.name
    
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    inventory = models.IntegerField()
    description = models.TextField(max_length=1000, default='')
    
    def __str__(self):
      return f'{self.title} : {str(self.price)}'