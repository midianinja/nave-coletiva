from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from nave.models import Espaco
from rede.models import Pessoa, Rede

from utils.models import ModeloComNome

class Festival(ModeloComNome):
    inicio = models.DateField()
    fim = models.DateField()
    nome = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Festivais'

class Encontro(ModeloComNome):
    festival = models.ForeignKey(Festival,
                                 on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    descricao = models.TextField()


class Categoria(MPTTModel):
    nome = models.CharField(max_length=32,
                            db_index=True)
    parent = TreeForeignKey('self',
                            on_delete=models.CASCADE,
                            null=True,
                            blank=True,
                            related_name='children')

    def __str__(self):
        return self.nome

    class MPTTMeta:
        order_insertion_by = ['nome']


class Atividade(models.Model):
    festival = models.ForeignKey(Festival,
                                 on_delete=models.CASCADE)
    encontro = models.ForeignKey(Encontro,
                                 null=True,
                                 on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria)
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

    def __repr__(self):
        return self.titulo
