from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date

class Customer(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    address = models.CharField(max_length=150, blank=False)
    address_number = models.IntegerField(blank=False)
    tel = models.BigIntegerField(blank=False)
    document = models.BigIntegerField(blank=False)
    born_year = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(date.today().year)], blank=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"