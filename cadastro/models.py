from django.db import models
from django.contrib.auth.models import User 

class ONG(models.Model):
    usuarios = models.ManyToManyField(User, blank=True, related_name="ongs")

    nome = models.CharField(max_length=200, verbose_name="Nome da ONG")
    cnpj = models.CharField(max_length=18, unique=True)
    endereco = models.CharField(max_length=255)
    area_atuacao = models.CharField(max_length=150, verbose_name="Área de Atuação")
    contato = models.CharField(max_length=100, help_text="E-mail ou telefone principal")
    
    def __str__(self):
        return self.nome

class Documento(models.Model):
    ong = models.ForeignKey(ONG, on_delete=models.CASCADE, related_name="documentos")
    
    tipo = models.CharField(max_length=100, verbose_name="Tipo de Documento")
    arquivo = models.FileField(upload_to='documentos_ongs/')
    data_upload = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.tipo} - {self.ong.nome}"

class Avaliacao(models.Model):
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('APROVADO', 'Aprovado'),
        ('REJEITADO', 'Rejeitado'),
    ]

    ong = models.ForeignKey(ONG, on_delete=models.CASCADE, related_name="avaliacoes")
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDENTE')
    comentario = models.TextField(blank=True, null=True, verbose_name="Comentário da Avaliação")
    data = models.DateTimeField(auto_now_add=True, verbose_name="Data da Avaliação")
    avaliador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Avaliação de {self.ong.nome} - {self.status}"

class Selo(models.Model):
    ong = models.ForeignKey(ONG, on_delete=models.CASCADE, related_name="selos")
    avaliacao_origem = models.OneToOneField(Avaliacao, on_delete=models.PROTECT, null=True)

    data_emissao = models.DateField(auto_now_add=True, verbose_name="Data de Emissão")
    data_validade = models.DateField(verbose_name="Data de Validade")
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"Selo para {self.ong.nome} (Válido até: {self.data_validade})"