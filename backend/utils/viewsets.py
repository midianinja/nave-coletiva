from rest_framework import viewsets, mixins
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.db.models.signals import post_save
from django.core.cache import cache

class ModelViewSet(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):

    @method_decorator(cache_page(60*10))
    def get(self, request, format=None):
        super().get(request, format)


def clear_cache(*args, **kwargs):
    cache.clear()
post_save.connect(clear_cache)
