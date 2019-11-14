from django.conf import settings

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
import festival.views as festival_views
import nave.views as nave_views
import rede.views as rede_views

admin.site.site_header = 'Nave Coletiva'

router = routers.DefaultRouter()
router.register(r'festivais', festival_views.FestivalViewSet)
router.register(r'encontros', festival_views.EncontroViewSet)
router.register(r'categorias', festival_views.CategoriaViewSet)
router.register(r'tags', festival_views.TagViewSet)
router.register(r'atividades', festival_views.AtividadeViewSet)
router.register(r'andares', nave_views.AndarViewSet)
router.register(r'espacos', nave_views.EspacoViewSet)
router.register(r'redes', rede_views.RedeViewSet)
router.register(r'pessoas', rede_views.PessoaViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.API_ENABLED:
    urlpatterns.append(path('api/', include(router.urls)))
