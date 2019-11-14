from rest_framework import serializers
from rede.models import Pessoa, Rede


class PessoaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'

class RedeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rede
        fields = '__all__'
