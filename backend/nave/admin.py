from django.contrib import admin
from admin_numeric_filter.admin import RangeNumericFilter

from nave.models import Andar, Espaco

@admin.register(Espaco)
class EspacoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'andar', 'capacidade', 'colunas']
    search_fields = ['nome']
    list_filter = [
        'andar',
        ('capacidade', RangeNumericFilter),
        ]
    actions = ['traz_pra_frente']

    def traz_pra_frente(modeladmin, request, queryset):
        for espaco in queryset.all():
            espaco.ordem = 1
            espaco.save()
    traz_pra_frente.short_description = "Traz pra frente (fica sendo o primeiro espaço)"

admin.site.register(Andar)
