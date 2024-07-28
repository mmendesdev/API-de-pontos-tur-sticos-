from atracoes.models import Atracao
from comentario.models import Comentarios
from django.db import models


class PontoTuristico(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentarios)


def __str__(self):
    return self.name
