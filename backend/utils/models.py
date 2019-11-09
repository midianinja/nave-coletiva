from django.db import models

class ModeloComNome(models.Model):
    class Meta:
        abstract = True

    def __str__(self):
        return self.nome
