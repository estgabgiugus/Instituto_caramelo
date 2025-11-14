from django import forms
from .models import ONG
from localflavor.br.forms import BRCNPJField, BRCPFField, BRPhoneNumberField
# O nome aqui precisa ser EXATAMENTE OngForm


class OngForm(forms.ModelForm):
    class Meta:
        model = ONG
        fields = [
            'nome',
            'cnpj',
            'endereco',
            'area_atuacao',
            'contato'
        ]


class ONGForm(forms.ModelForm):
    cnpj = BRCNPJField()
    telefone = BRPhoneNumberField()
