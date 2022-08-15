from django.db import models

# Create your models here.
class User(models.Model):
    kakao_id = models.IntegerField(unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.email