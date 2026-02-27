from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .genres_model import Genre

class Movie(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    release_year = models.IntegerField(
        validators=[
            MinValueValidator(1888),
            MaxValueValidator(2100)
        ],
        blank=False
    )
    genre = models.ManyToManyField(Genre)
    avaliable_quantity = models.IntegerField(
        validators=[
            MinValueValidator(0)
        ],
        blank=False,
        default=0
    )

    def __str__(self):
        return self.name
