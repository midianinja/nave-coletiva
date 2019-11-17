from django.db import models

from utils.models import ModeloComNome

class Andar(ModeloComNome):
    nivel = models.IntegerField()
    nome = models.CharField(max_length=16)

    class Meta:
        verbose_name_plural = 'Andares'

class Espaco(ModeloComNome):
    andar = models.ForeignKey(Andar,
                              on_delete=models.CASCADE)
    nome = models.CharField(max_length=32)
    capacidade = models.IntegerField()
    eventos_simultaneos = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Espaço'
