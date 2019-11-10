from django.contrib import admin

from rede.models import Rede, Pessoa

class RedeAdmin(admin.ModelAdmin):
    search_fields = ['nome']

class PessoaAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    autocomplete_fields = ['redes']

admin.site.register(Rede, RedeAdmin)
admin.site.register(Pessoa, PessoaAdmin)
