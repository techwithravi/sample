from django.db import models


# Create your models here.

class Capital(models.Model):
    name = models.CharField(max_length=50)
    usage = models.CharField(max_length=250)
    amount = models.CharField(max_length=259)
