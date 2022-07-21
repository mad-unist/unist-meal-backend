from django.db import models


# Create your models here.
class Photo(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name
