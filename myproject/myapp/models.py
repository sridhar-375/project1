from django.db import models
import datetime


# Create your models here.
class do(models.Model):
    def __str__(self):
        return self.name

    name = models.TextField(max_length=200)
    priority = models.IntegerField()
    date = models.DateField(default=datetime.date.today)
