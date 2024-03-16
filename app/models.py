from django.db import models

# Create your models here.
class Carros(models.Model):
    modelo = models.CharField(max_length=150)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField()

    def __unicode__(self):
        return self.modelo