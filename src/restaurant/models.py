from django.db import models


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    content = models.CharField(max_length=100)
    url = models.CharField(max_length=500, blank=True)

    def __str__(self) -> str:
        return self.name
