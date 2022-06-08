from django.db import models

# Create your models here.
class user_detail(models.Model):
    f_name = models.CharField(max_length=100)
    s_name = models.CharField(max_length=100)
    u_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
