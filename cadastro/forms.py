from django import forms
from .models import ONG

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