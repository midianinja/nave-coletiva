from django.contrib import admin
from admin_numeric_filter.admin import RangeNumericFilter

from nave.models import Andar, Espaco

@admin.register(Espaco)
class EspacoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'andar', 'capacidade']
    search_fields = ['nome']
    list_filter = [
        'andar',
        ('capacidade', RangeNumericFilter),
        ]

admin.site.register(Andar)
