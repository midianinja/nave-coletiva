from django.db import models

from utils.models import ModeloComNome


class Rede(ModeloComNome):
    nome = models.CharField(max_length=32)


class Pessoa(ModeloComNome):
    nome = models.CharField(max_length=255)
    redes = models.ManyToManyField(Rede)
