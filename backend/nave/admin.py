from django.contrib import admin

from nave.models import Andar, Espaco

class EspacoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'andar', 'capacidade']
    search_fields = ['nome']
    list_filter = ['andar', 'capacidade']


admin.site.register(Andar)
admin.site.register(Espaco, EspacoAdmin)
