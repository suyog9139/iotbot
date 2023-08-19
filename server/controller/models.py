
# Create your models here.
from django.db import models

class IoTData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
