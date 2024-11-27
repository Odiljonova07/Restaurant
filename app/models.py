from django.db import models
import decimal

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Food(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    info = models.TextField()
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    discount_percent = models.DecimalField(max_digits = 3, decimal_places = 1, null=True, blank=True)
    photo = models.ImageField(upload_to='media/food/')
    is_food_of_day = models.BooleanField(default=False)

    def discounted_price(self):
        if self.discount_percent:
            discounted_price = self.price - self.discount_percent*self.price/100
            return discounted_price

    def __str__(self):
        return self.name
    

class Reservation(models.Model):
    name = models.CharField(max_length=255)
    number_of_guests = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name