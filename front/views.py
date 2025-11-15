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

        mensagem = "Cadastrado com sucesso! Aguarde o resultado."

    return render(request, "index.html", {"mensagem": mensagem})


def index(request):
    return render(request, "index.html")


def parceiros(request):
    parceiros = Parceiro.objects.filter(aprovado=True)
    if not parceiros:
        mensagem = "Nenhum parceiro aprovado no momento."
    else:
        mensagem = None
    return render(request, 'parceiros.html', {'parceiros': parceiros, 'mensagem': mensagem})
