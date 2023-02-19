from django.db import models

# Create your models here.

class csvmodel(models.Model):
    id = models.CharField(primary_key=True),
    date=models.IntegerField(default=0),
    time=models.TimeField(),
    open=models.FloatField(default=0),
    high=models.FloatField(default=0),
    low=models.FloatField(default=0),
    close=models.FloatField(default=0),
    volume=models.FloatField(default=0)
    
    