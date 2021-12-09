from django.db import models

# Create your models here.

class Marcas(models.Model):
    name = models.CharField(max_length=100)
    logo = models.CharField(max_length=100)

    def __str__(self):
        return self.title
