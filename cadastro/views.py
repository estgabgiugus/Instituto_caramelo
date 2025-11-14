from django.shortcuts import render, redirect
from .forms import ONG


'''def index(request):
    return render(request, "index.html")


def registrar_ong(request):
    if request.method == "POST":
        ONG.objects.create(
            nome=request.POST.get("nome"),
            cidade=request.POST.get("cidade"),
            representante=request.POST.get("representante"),
            cnpj=request.POST.get("CNPJ"),
            motivacao=request.POST.get("motivacao"),
        )
        return redirect("cadastro_sucesso")

    return redirect("index")


def cadastro_sucesso(request):
    return render(request, "sucesso.html")'''

from django.shortcuts import render, redirect
from .models import ONG


def registrar_ong(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        cidade = request.POST.get("cidade")
        representante = request.POST.get("representante")
        cnpj = request.POST.get("CNPJ")
        motivacao = request.POST.get("motivacao")

        ONG.objects.create(
            nome=nome,
            cidade=cidade,
            representante=representante,
            cnpj=cnpj,
            motivacao=motivacao
        )

        return redirect("cadastro_sucesso")

    return redirect("index")
