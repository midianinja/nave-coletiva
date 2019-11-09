from django.db import models


class Rede(models.Model):
    nome = models.CharField(max_length=32)


class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
