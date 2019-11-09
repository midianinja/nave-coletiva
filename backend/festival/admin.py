from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from festival.models import Festival, Encontro, Categoria, Atividade

class CategoriaAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "some_node_field"


admin.site.register(Festival)
admin.site.register(Encontro)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Atividade)
