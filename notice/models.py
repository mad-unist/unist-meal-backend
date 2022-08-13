from django.db import models

# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self) -> str:
        return self.title