from django.db import models
from django.contrib.auth.models import User


class ONG(models.Model):
    STATUS_CHOICES = [
        ("pendente", "Pendente"),
        ("aprovada", "Aprovada"),
        ("rejeitada", "Rejeitada"),
    ]
    nome = models.CharField(max_length=200)
    cidade = models.CharField(max_length=120, blank=True, null=True)
    representante = models.CharField(max_length=150, blank=True, null=True)
    cnpj = models.CharField(max_length=18, unique=True)
    motivacao = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="pendente"
    )

    def __str__(self):
        return self.nome


class Parceiro(models.Model):
    nome = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    representante = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18)
    motivacao = models.TextField()

    aprovado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
