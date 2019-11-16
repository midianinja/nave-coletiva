from django.db import models
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.dispatch import receiver
from django.utils.safestring import mark_safe
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
        if self.parent:
            return '%s: %s' % (self.parent.nome, self.nome)
        else:
            return self.nome

    class MPTTMeta:
        order_insertion_by = ['nome']


class Tag(ModeloComNome):
    nome = models.CharField(max_length=32)


class Atividade(models.Model):
    pendente = models.BooleanField(default=True)
    observacoes = models.TextField(blank=True,
                                   verbose_name='observações')
    festival = models.ForeignKey(Festival,
                                 on_delete=models.CASCADE)
    encontro = models.ForeignKey(Encontro,
                                 null=True,
                                 blank=True,
                                 on_delete=models.CASCADE)
    categorias = TreeManyToManyField(Categoria)
    tags = models.ManyToManyField(Tag,
                                  blank=True)
    rede = models.ForeignKey(Rede,
                             null=True,
                             blank=True,
                             on_delete=models.CASCADE)
    espaco = models.ForeignKey(Espaco,
                               null=True,
                               blank=True,
                               on_delete=models.CASCADE,
                               verbose_name='espaço')
    responsavel = models.ForeignKey(Pessoa,
                                    related_name='responsavel_por',
                                    on_delete=models.CASCADE,
                                    verbose_name='responsável')
    convidados = models.ManyToManyField(Pessoa,
                                        blank=True,
                                        related_name='convidado_para')
    coincide_horario = models.BooleanField(default=False)
    inicio = models.DateTimeField(verbose_name='início',
                                  null=True,
                                  blank=True)
    fim = models.DateTimeField(null=True,
                               blank=True)
    titulo = models.CharField(max_length=255,
                              verbose_name='título')
    descricao = models.TextField(verbose_name='descrição')

    def clean(self):
        if not self.espaco and not self.pendente:
            raise ValidationError("O evento deve ter espaço, ou ser marcado como pendente")

        if not self.pendente and (self.inicio is None or self.fim is None):
            raise ValidationError("O evento deve ter início e fim, ou ser marcado como pendente")

        if self.inicio is None or self.fim is None:
            return

        if self.inicio >= self.fim:
            raise ValidationError("Horário de início deve ser anterior ao fim")

        if self.espaco is None:
            return

        qs = Atividade.objects.filter(espaco=self.espaco)
        time_filters = (Q(inicio__lte=self.inicio,
                          fim__gte=self.inicio) |
                        Q(inicio__lte=self.fim,
                          fim__gte=self.fim) |
                        Q(inicio__lte=self.inicio,
                          fim__gte=self.fim) |
                        Q(inicio__gte=self.inicio,
                          fim__lte=self.fim))
        qs = qs.filter(time_filters)
        if self.id:
            qs = qs.exclude(id=self.id)

        full_qs = qs
        if self.coincide_horario:
            qs = qs.exclude(inicio=self.inicio, fim=self.fim)
        if qs.count() > self.espaco.eventos_simultaneos - 1:
            if qs.count() > 2:
                msg = "Este horário conflita com %d eventos no mesmo espaço" % qs.count()
            else:
                msg = "Este horário conflita com um evento no mesmo espaço"
            espacos = []
            for espaco in Espaco.objects.all():
                qs = Atividade.objects.filter(espaco=espaco).filter(time_filters)
                if qs.count() == 0:
                    espacos.append(espaco)
            if len(espacos) > 0:
                msg += '<br />Os seguintes espaços estão livres:<ul>'
                msg += '\n'.join(['<li>%s</li>' % espaco.nome for espaco in espacos])
                msg += '</ul>'
            else:
                msg += '<br />Não há espaços disponíveis neste horário'

            raise ValidationError(mark_safe(msg))

        if full_qs.count() > 0:
            full_qs.filter(inicio=self.inicio, fim=self.fim).update(coincide_horario=True)


    @property
    def categoria(self):
        return self.subcategoria.categoria

    def __str__(self):
        return self.titulo


@receiver(models.signals.post_migrate)
def rebuild_handler(sender, **kwargs):
    if sender.name == 'festival':
        Categoria.objects.rebuild()
