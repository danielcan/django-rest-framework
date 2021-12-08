from django.db import models


# Create your models here.

class Tiendas(models.Model):
    brand = models.CharField(max_length=100)
    identifier = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.title


