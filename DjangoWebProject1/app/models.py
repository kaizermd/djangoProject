"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField("artist",max_length=50)
    year_formed=models.PositiveIntegerField()

class Album(models.Model):
    name = models.CharField("album",max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)