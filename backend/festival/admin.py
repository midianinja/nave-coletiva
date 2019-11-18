from datetime import datetime
from django.contrib import admin
from django.db.models import Q
from mptt.admin import DraggableMPTTAdmin
from admin_auto_filters.filters import AutocompleteFilter

from festival.models import Festival, Encontro, Categoria, Atividade, Tag
from festival.forms import AtividadeAdminForm

class DateFilter(admin.SimpleListFilter):

    title = 'Data'
    parameter_name = 'inicio'

    def lookups(self, request, model_admin):
        return (
            ('21/11', '21/11'),
            ('22/11', '22/11'),
            ('23/11', '23/11'),
            ('24/11', '24/11'),
        )

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset
        day = int(self.value()[:2])
        inicio = datetime(2019, 11, day, 10, 0)
        fim = datetime(2019, 11, day, 23, 59)
        time_filters = (Q(inicio__lte=inicio,
                          fim__gt=inicio) |
                        Q(inicio__lt=fim,
                          fim__gte=fim) |
                        Q(inicio__lte=inicio,
                          fim__gte=fim) |
                        Q(inicio__gte=inicio,
                          fim__lte=fim))
        return queryset.filter(time_filters)

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

class ConvidadeFilter(AutocompleteFilter):
    title = 'Convidade'
    field_name = 'convidades'

class EspacoFilter(AutocompleteFilter):
    title = 'Espaço'
    field_name = 'espaco'

class AtividadeAdmin(admin.ModelAdmin):
    form = AtividadeAdminForm
    list_filter = [DateFilter, 'pendente', EspacoFilter, EncontroFilter, CategoriasFilter, TagsFilter, RedeFilter, ResponsavelFilter, ConvidadeFilter]
    list_display = ['titulo', 'espaco', 'inicio_fmt', 'fim_fmt', 'coluna', 'convidades_list']
    search_fields = ['titulo', 'descricao']
    autocomplete_fields = ['categorias', 'tags', 'responsavel', 'convidades']
    save_on_top = True

    def convidades_list(self, obj):
        return obj.convidades.count()
    convidades_list.short_description = '# convidades'

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
