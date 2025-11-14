from django.shortcuts import render, redirect
from .forms import ONG
from .models import Parceiro


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


def ongs_aprovadas(request):
    aprovadas = ONG.objects.filter(status="aprovada")
    return render(request, "ongs_aprovadas.html", {"ongs": aprovadas})


def ongs_rejeitadas(request):
    rejeitadas = ONG.objects.filter(status="rejeitada")
    return render(request, "ongs_rejeitadas.html", {"ongs": rejeitadas})


def parceiros(request):
    parceiros = Parceiro.objects.filter(aprovado=True)
    return render(request, "parceiros.html", {"parceiros": parceiros})
