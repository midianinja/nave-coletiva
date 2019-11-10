from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from festival.models import Festival, Encontro, Categoria, Atividade

class AtividadeAdmin(admin.ModelAdmin):
    autocomplete_fields = ['categorias', 'convidados']


class CategoriaAdmin(DraggableMPTTAdmin):
    search_fields = ['nome', 'parent__nome']
    mptt_indent_field = "some_node_field"


admin.site.register(Festival)
admin.site.register(Encontro)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Atividade, AtividadeAdmin)
