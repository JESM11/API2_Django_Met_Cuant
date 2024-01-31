from django.db import models

# Create your models here.

class Sim(models.Model):
    planchas= models.PositiveIntegerField()
    CMYK= models.PositiveIntegerField()
    orden_CMYK= models.PositiveIntegerField()
    orden_Planchas= models.PositiveIntegerField()