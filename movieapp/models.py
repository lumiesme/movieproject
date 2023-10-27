import datetime

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import (MinLengthValidator, MinValueValidator, MaxValueValidator)
from django.db import models

# Create your models here.

class Country(models.Model):
    common = models.CharField(max_length=100)
    official = models.CharField(max_length=100)
    capital = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    subregion = models.CharField(max_length=50, null=True)
    flag = models.CharField(max_length=100)
    map = models.CharField(max_length=100)


    class Meta:
        verbose_name_plural = 'countries'
        ordering = ['common']

    def __str__(self):
        return self.common

class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    imdbID = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    poster= models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'movies'
        ordering = ['title']

    def __str__(self):
        return self.title
