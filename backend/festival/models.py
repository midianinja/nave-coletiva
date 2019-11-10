from django.db import models
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.dispatch import receiver
from mptt.models import MPTTModel, TreeForeignKey
from mptt.fields import TreeManyToManyField

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
    nome = models.CharField(max_length=64,
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
    categorias = TreeManyToManyField(Categoria)
    rede = models.ForeignKey(Rede,
                             null=True,
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

    def clean(self):
        if self.inicio >= self.fim:
            raise ValidationError("Horário de início deve ser anterior ao fim")

        qs = Atividade.objects.filter(espaco=self.espaco)
        qs = qs.filter(Q(inicio__lte=self.inicio,
                         fim__gte=self.inicio) |
                       Q(inicio__lte=self.fim,
                         fim__gte=self.fim) |
                       Q(inicio__lte=self.inicio,
                         fim__gte=self.fim) |
                       Q(inicio__gte=self.inicio,
                         fim__lte=self.fim))
        if self.id:
            qs = qs.exclude(id=self.id)
        if qs.count() > 2:
            raise ValidationError("Este horário conflita com %d eventos no mesmo espaço" % qs.count())
        elif qs.count() == 1:
            raise ValidationError("Este horário conflita com um evento no mesmo espaço")


    @property
    def categoria(self):
        return self.subcategoria.categoria

    def __str__(self):
        return self.titulo


@receiver(models.signals.post_migrate)
def rebuild_handler(sender, **kwargs):
    if sender.name == 'festival':
        Categoria.objects.rebuild()
