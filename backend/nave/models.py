from django.db import models

class Andar(models.Model):
    nivel = models.IntegerField()
    nome = models.CharField(max_length=16)


class Espaco(models.Model):
    andar = models.ForeignKey(Andar,
                              on_delete=models.CASCADE)
    nome = models.CharField(max_length=32)
