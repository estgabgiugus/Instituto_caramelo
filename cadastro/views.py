# dentro de cadastro/views.py

from django.shortcuts import render, redirect
from .forms import OngForm

# Função para a página do formulário
def registrar_ong(request):
    if request.method == 'POST':
        form = OngForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastro_sucesso')
    else:
        form = OngForm()
    
    return render(request, 'cadastro/formulario.html', {'form': form})

# Função para a página de sucesso
def cadastro_sucesso(request):
    return render(request, 'cadastro/sucesso.html')