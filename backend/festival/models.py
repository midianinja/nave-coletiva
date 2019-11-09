from django.db import models

from nave.models import Espaco
from rede.models import Pessoa, Rede

class Festival(models.Model):
    inicio = models.DateField()
    fim = models.DateField()
    nome = models.CharField(max_length=255)


class Encontro(models.Model):
    festival = models.ForeignKey(Festival,
                                 on_delete=models.CASCADE)


class Categoria(models.Model):
    nome = models.CharField(max_length=32)


class Subcategoria(models.Model):
    categoria = models.ForeignKey(Categoria,
                                 on_delete=models.CASCADE)
    nome = models.CharField(max_length=32)


class Tag(models.Model):
    tag = models.CharField(max_length=64,
                           db_index=True)


class Atividade(models.Model):
    festival = models.ForeignKey(Festival,
                                 on_delete=models.CASCADE)
    encontro = models.ForeignKey(Encontro,
                                 null=True,
                                 on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(Subcategoria,
                                 on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    rede = models.ForeignKey(Rede,
                             on_delete=models.CASCADE)
    espaco = models.ForeignKey(Espaco,
                               on_delete=models.CASCADE)
    responsavel = models.ForeignKey(Pessoa,
                                    related_name='responsavel_por',
                                    on_delete=models.CASCADE)
    convidados = models.ManyToManyField(Pessoa,
                                        related_name='convidado_para')

    inicio = models.DateTimeField()
    fim = models.DateTimeField()
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()

    @property
    def categoria(self):
        return self.subcategoria.categoria
