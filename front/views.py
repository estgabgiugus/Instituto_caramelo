from django.shortcuts import render
from cadastro.models import ONG, Parceiro


def registrar_ong(request):
    mensagem = None

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

        mensagem = "Enviado com sucesso! Aguarde contato."

    return render(request, "index.html", {"mensagem": mensagem})


def index(request):
    return render(request, "index.html")


def parceiros(request):
    parceiros = Parceiro.objects.filter(aprovado=True)
    return render(request, "parceiros.html", {"parceiros": parceiros})
