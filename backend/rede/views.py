from utils import viewsets
from rede.models import Pessoa, Rede
from rede.serializers import PessoaSerializer, RedeSerializer


class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.exclude(convidade_para__isnull=True)
    serializer_class = PessoaSerializer

class RedeViewSet(viewsets.ModelViewSet):
    queryset = Rede.objects.all()
    serializer_class = RedeSerializer
