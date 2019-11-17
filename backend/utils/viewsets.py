from rest_framework import viewsets, mixins

class ModelViewSet(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    pass
