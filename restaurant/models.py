from django.db import models


# Create your models here.
class Restaurant(models.Model):
    place = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    content = models.CharField(max_length=100)
