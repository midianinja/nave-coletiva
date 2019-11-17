from rest_framework import viewsets
from rede.models import Pessoa, Rede
from rede.serializers import PessoaSerializer, RedeSerializer


class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

class RedeViewSet(viewsets.ModelViewSet):
    queryset = Rede.objects.all()
    serializer_class = RedeSerializer
