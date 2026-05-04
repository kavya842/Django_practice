from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=32)
    director=models.CharField(max_length=32)
    description=models.TextField()
    Cast=models.TextField()
    budget=models.FloatField()
    collections=models.FloatField()
