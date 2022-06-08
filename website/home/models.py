from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    password = models.CharField(max_length=15)