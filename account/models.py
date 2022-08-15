from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.email} - {self.id}"