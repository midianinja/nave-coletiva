from utils import viewsets
from nave.models import Andar, Espaco
from nave.serializers import AndarSerializer, EspacoSerializer


class AndarViewSet(viewsets.ModelViewSet):
    queryset = Andar.objects.all()
    serializer_class = AndarSerializer

class EspacoViewSet(viewsets.ModelViewSet):
    queryset = Espaco.objects.exclude(atividade__isnull=True)
    serializer_class = EspacoSerializer
