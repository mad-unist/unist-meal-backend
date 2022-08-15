from django.db import models

# Create your models here.
class User(models.Model):
    id = models.CharField(unique=True, primary_key=True, max_length=255)
    email = models.EmailField(unique=True, null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.email} - {self.id}"