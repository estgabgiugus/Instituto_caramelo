from django.contrib import admin
from .models import ONG, Parceiro


@admin.register(ONG)
class ONGAdmin(admin.ModelAdmin):
    list_display = ("nome", "cidade", "representante", "cnpj", "status")
    list_filter = ("status",)
    actions = ["aprovar_ongs", "rejeitar_ongs"]

    def aprovar_ongs(self, request, queryset):
        for ong in queryset:
            ong.status = "aprovada"
            ong.save()
            Parceiro.objects.create(
                nome=ong.nome,
                cidade=ong.cidade,
                representante=ong.representante,
                cnpj=ong.cnpj,
                motivacao=ong.motivacao,
                aprovado=True,
                ong=ong
            )
        self.message_user(
            request, "ONG(s) aprovadas com sucesso! E parceiros criados.")

    aprovar_ongs.short_description = "Aprovar ONG selecionadas"

    def rejeitar_ongs(self, request, queryset):
        queryset.update(status="rejeitada")
        self.message_user(request, "ONG(s) rejeitadas!")

    rejeitar_ongs.short_description = "Rejeitar ONG selecionadas"


class ParceiroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'representante', 'aprovado')
    list_filter = ('aprovado',)
    search_fields = ('nome', 'cidade', 'representante')
    list_editable = ('aprovado',)

    actions = ["aprovar_parceiros", "desaprovar_parceiros"]

    def aprovar_parceiros(self, request, queryset):
        ong = ONG.objects.get(id=1)
        queryset.update(aprovado=True, ong=ong)
        self.message_user(request, "Parceiro(s) aprovado(s) com sucesso!")

    aprovar_parceiros.short_description = "Aprovar parceiro(s) selecionado(s)"

    def desaprovar_parceiros(self, request, queryset):
        queryset.update(aprovado=False)
        self.message_user(request, "Parceiro(s) desaprovado(s) com sucesso!")

    desaprovar_parceiros.short_description = "Desaprovar parceiro(s) selecionado(s)"


admin.site.register(Parceiro, ParceiroAdmin)
