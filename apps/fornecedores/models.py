# fornecedores/models.py

from django.db import models

class Fornecedor(models.Model):
    nome_empresa = models.CharField(max_length=255)
    contato_nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    endereco = models.TextField()

    def __str__(self):
        return self.nome_empresa