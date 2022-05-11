from django.db import models

# Create your models here.
class Menu(models.Model):
    place = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    content = models.TextField()
    calorie = models.IntegerField()
    date = models.DateTimeField()
