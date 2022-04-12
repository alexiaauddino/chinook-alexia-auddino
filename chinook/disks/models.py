from pickle import NONE
from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Album(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    
class Track(models.Model):
    name = models.CharField(max_length=200)
    milliseconds = models.IntegerField()
    bytes = models.IntegerField()
    unitPrice = models.DecimalField(..., max_digits=5, decimal_places=2)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    composer = models.CharField(max_length=200)
    
    def __str__(self):
        return self.composer if self.composer else "No composer"
    