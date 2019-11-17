from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from admin_auto_filters.filters import AutocompleteFilter

from festival.models import Festival, Encontro, Categoria, Atividade, Tag
from festival.forms import AtividadeAdminForm

class EncontroFilter(AutocompleteFilter):
    title = 'Encontro'
    field_name = 'encontro'

class CategoriasFilter(AutocompleteFilter):
    title = 'Categoria'
    field_name = 'categorias'

class TagsFilter(AutocompleteFilter):
    title = 'Tags'
    field_name = 'tags'

class RedeFilter(AutocompleteFilter):
    title = 'Rede'
    field_name = 'rede'

class ResponsavelFilter(AutocompleteFilter):
    title = 'Responsável'
    field_name = 'responsavel'

class ConvidadoFilter(AutocompleteFilter):
    title = 'Convidado'
    field_name = 'convidados'

class AtividadeAdmin(admin.ModelAdmin):
    form = AtividadeAdminForm
    list_filter = ['pendente', EncontroFilter, CategoriasFilter, TagsFilter, RedeFilter, ResponsavelFilter, ConvidadoFilter]
    list_display = ['titulo', 'espaco', 'inicio_fmt', 'fim_fmt', 'coluna']
    search_fields = ['titulo', 'descricao']
    autocomplete_fields = ['categorias', 'tags', 'responsavel', 'convidados']
    save_on_top = True

    def inicio_fmt(self, obj):
        try:
            return obj.inicio.strftime("%d/%m %H:%M")
        except AttributeError:
            return '-'
    def fim_fmt(self, obj):
        try:
            return obj.fim.strftime("%d/%m %H:%M")
        except AttributeError:
            return '-'
    inicio_fmt.short_description = 'início'
    fim_fmt.short_description = 'fim'
    inicio_fmt.admin_order_field = 'inicio'
    fim_fmt.admin_order_field = 'fim'

    class Media:
        pass

class TagAdmin(admin.ModelAdmin):
    search_fields = ['nome']

class CategoriaAdmin(DraggableMPTTAdmin):
    search_fields = ['nome', 'parent__nome']
    mptt_indent_field = "some_node_field"


admin.site.register(Festival)
admin.site.register(Encontro)
admin.site.register(Tag, TagAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Atividade, AtividadeAdmin)
