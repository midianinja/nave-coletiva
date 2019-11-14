from rest_framework import viewsets
from festival.models import (Atividade, Festival, Encontro, Categoria, Tag)
from festival.serializers import (AtividadeSerializer, FestivalSerializer, EncontroSerializer,
                                  CategoriaSerializer, TagSerializer)


class AtividadeViewSet(viewsets.ModelViewSet):
    queryset = Atividade.objects.all()
    serializer_class = AtividadeSerializer

class FestivalViewSet(viewsets.ModelViewSet):
    queryset = Festival.objects.all()
    serializer_class = FestivalSerializer

class EncontroViewSet (viewsets.ModelViewSet):
    queryset = Encontro.objects.all()
    serializer_class = EncontroSerializer

class CategoriaViewSet (viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class TagViewSet (viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
