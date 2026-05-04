from django.db import models

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=32)
    sal=models.FloatField()
    phone=models.PositiveBigIntegerField()
    role=models.CharField(max_length=100)
    email=models.EmailField()
    doj=models.DateField()
    loc=models.TextField(default="Bangalore")
