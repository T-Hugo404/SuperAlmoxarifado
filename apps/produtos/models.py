# produtos/models.py

from django.db import models
from apps.fornecedores.models import Fornecedor

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    quantidade_em_estoque = models.PositiveIntegerField(default=0)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    data_de_entrada = models.DateTimeField(auto_now_add=True)
    ultima_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome