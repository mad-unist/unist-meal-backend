from django.db import models

# Create your models here.
class Menu(models.Model):
    place = models.CharField(max_length=50)
    type = models.CharField(max_length=50, blank=True)
    time = models.CharField(max_length=50)
    content = models.TextField()
    calorie = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.place}-{self.time}-{self.date.month}/{self.date.day}-{self.type}"

    class Meta:
        ordering = ['-date']