# retirada/models.py

from django.db import models
from django.conf import settings
from apps.produtos.models import Produto

class Retirada(models.Model):
    solicitante = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data_retirada = models.DateTimeField(auto_now_add=True)
    aprovado = models.BooleanField(default=False)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Retirada {self.id} por {self.solicitante.get_full_name()}"

class ItemRetirada(models.Model):
    retirada = models.ForeignKey(Retirada, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome}"