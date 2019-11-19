from django.db.models import Q
from rest_framework import serializers
from festival.models import Atividade, Festival, Encontro, Categoria, Tag

class AtividadeSerializer(serializers.HyperlinkedModelSerializer):
    largura = serializers.SerializerMethodField('calcula_largura')

    def calcula_largura(self, atividade):
        if atividade.espaco.colunas <= 1:
            return 1
        largura = 1
        coluna = atividade.coluna + 1
        while coluna <= atividade.espaco.colunas:
            qs = Atividade.objects.filter(espaco=atividade.espaco,
                                          coluna=coluna)
            time_filters = (Q(inicio__lte=atividade.inicio,
                              fim__gt=atividade.inicio) |
                            Q(inicio__lt=atividade.fim,
                              fim__gte=atividade.fim) |
                            Q(inicio__lte=atividade.inicio,
                              fim__gte=atividade.fim) |
                            Q(inicio__gte=atividade.inicio,
                              fim__lte=atividade.fim))
            qs = qs.filter(time_filters)
            qs = qs.exclude(id=atividade.id)
            if qs.count() == 0:
                largura += 1
                coluna += 1
            else:
                return largura
        return largura

    class Meta:
        model = Atividade
        fields = '__all__'

class FestivalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Festival
        fields = '__all__'

class EncontroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Encontro
        fields = '__all__'

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class TagSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
