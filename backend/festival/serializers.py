from rest_framework import serializers
from festival.models import Atividade, Festival, Encontro, Categoria, Tag


class AtividadeSerializer(serializers.HyperlinkedModelSerializer):
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
