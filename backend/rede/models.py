from django.db import models

from utils.models import ModeloComNome


class Rede(ModeloComNome):
    nome = models.CharField(max_length=64,
                            db_index=True)


class Pessoa(ModeloComNome):
    nome = models.CharField(max_length=255,
                            db_index=True)
    redes = models.ManyToManyField(Rede)
