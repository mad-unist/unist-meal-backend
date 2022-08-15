from django.db import models
from account.models import User
from menu.models import Menu

# Create your models here.
class Rating(models.Model):
    rating = models.FloatField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='ratings')

    def __str__(self) -> str:
        return f"{self.rating} - {self.user} - {self.menu}"
    
    class Meta:
        constraints = [models.UniqueConstraint(fields=['user', 'menu'], name='unique_rating')]