from django.contrib import admin

from apps.agenda.models import Fotografia, FazerMeta

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicada")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_filter =("categoria", "usuario",)
    list_editable = ("publicada",)
    list_per_page = 10

class ListandoMetas(admin.ModelAdmin):
    list_display = ("id", "nomeMeta", "data_inicio", "data_fim", "quantidade_passos")
    list_display_links = ("id", "nomeMeta")
    search_fields = ("nomeMeta",)
    list_per_page = 10
    
admin.site.register(Fotografia, ListandoFotografias)
admin.site.register(FazerMeta, ListandoMetas)

