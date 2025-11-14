from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ONG


@admin.register(ONG)
class ONGAdmin(admin.ModelAdmin):
    list_display = ("nome", "cidade", "representante", "cnpj", "status")
    list_filter = ("status",)
    actions = ["aprovar_ongs", "rejeitar_ongs"]

    def aprovar_ongs(self, request, queryset):
        queryset.update(status="aprovada")
        self.message_user(request, "ONG(s) aprovadas com sucesso!")

    aprovar_ongs.short_description = "Aprovar ONG selecionadas"

    def rejeitar_ongs(self, request, queryset):
        queryset.update(status="rejeitada")
        self.message_user(request, "ONG(s) rejeitadas!")

    rejeitar_ongs.short_description = "Rejeitar ONG selecionadas"
