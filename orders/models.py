from django.db import models

# Create your models here.
class Topping(models.Model):
    name = models.CharField(max_length = 32)


class RegularPizza(models.Model):
    SIZES = (
        ('Small', 'Small'),
        ('Large', 'Large')
    )
    name = models.CharField(max_length = 32)
    size = models.CharField(max_length = 5, choices = SIZES)
    TOPPINGS_NUMBER = models.IntegerField()
    toppings = models.ManyToManyField(Topping, blank = True)
    price = models.FloatField()


class SicilianPizza(models.Model):
    SIZES = (
        ('Small', 'Small'),
        ('Large', 'Large')
    )
    name = models.CharField(max_length = 32)
    size = models.CharField(max_length = 5, choices = SIZES)
    toppings = models.ManyToManyField(Topping, blank = True)
    price = models.FloatField()


class Subs(models.Model):
    SIZES = (
        ('Small', 'Small'),
        ('Large', 'Large')
    )
    name = models.CharField(max_length = 32)
    size = models.CharField(max_length = 5, choices = SIZES, default = 'Small')
    toppings = models.ManyToManyField(Topping, blank = True)
    price = models.FloatField()


class Pasta(models.Model):
    name = models.CharField(max_length = 32)
    price = models.FloatField()


class Salads(models.Model):
    name = models.CharField(max_length = 32)
    price = models.FloatField()


class DinnerPlatters(models.Model):
    SIZES = (
        ('Small', 'Small'),
        ('Large', 'Large')
    )
    name = models.CharField(max_length = 32)
    size = models.CharField(max_length = 5, choices = SIZES, default = 'Small')
    price = models.FloatField()
