from os import name

from django.db import models


class Atracao(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    time = models.TextField()
    age = models.IntegerField()

    def __str__(self):
        return name
