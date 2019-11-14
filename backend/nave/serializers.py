from rest_framework import serializers
from nave.models import Espaco, Andar


class EspacoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Espaco
        fields = '__all__'

class AndarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Andar
        fields = '__all__'
