from django.db import models

# Create your models here.


class members(models.Model):
    quality = models.CharField(max_length=250)
    mfg = models.DateTimeField()
    price = models.IntegerField()