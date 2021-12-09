from django.db import models


# Create your models here.

class Favorito(models.Model):
    usuario = models.CharField(max_length=100)
    tienda = models.CharField(max_length=100)


    def __str__(self):
        return self.title

