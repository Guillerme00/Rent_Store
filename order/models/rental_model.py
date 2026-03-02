from django.db import models
from customer.models import Customer
from movie.models import Movie
from django.utils import timezone
from datetime import timedelta

def default_return_day():
    return (timezone.now() + timedelta(days=7))


class RentalModel(models.Model):

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE
    )
    rental_day = models.DateTimeField(auto_now_add=True, blank=False)
    return_day = models.DateTimeField(default=default_return_day)
    returned = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.customer} - {self.movie}"
    
    @property
    def is_late(self):
        if not self.returned and timezone.now() > self.return_day:
            return True
        return False