from django.db import models

# Create your models here.


class Ofertas(models.Model):
    name = models.CharField(max_length=100)
    store = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.title

