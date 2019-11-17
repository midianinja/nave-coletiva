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
    ordem = models.IntegerField()
    capacidade = models.IntegerField()
    eventos_simultaneos = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Espaço'

    def save(self, *args, **kwargs):
        if self.ordem is None:
            try:
                self.ordem = Espaco.objects.all().order_by('-ordem')[0].ordem + 1
            except IndexError:
                self.ordem = 1
        else:
            qs = Espaco.objects.filter(ordem=self.ordem)
            if self.id:
                qs = qs.exclude(id=self.id)
            if qs.count() > 0:
                qs = Espaco.objects.filter(ordem__gte=self.ordem).order_by('-ordem')
                if self.id:
                    qs = qs.exclude(id=self.id)
                for espaco in qs:
                    Espaco.objects.filter(id=espaco.id).update(ordem = espaco.ordem + 1)

            ordem = 1
            for espaco in Espaco.objects.all().order_by('ordem'):
                Espaco.objects.filter(id=espaco.id).update(ordem=ordem)
                ordem += 1

        super().save(*args, **kwargs)
