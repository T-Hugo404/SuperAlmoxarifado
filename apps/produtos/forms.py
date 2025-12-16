from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        
        

        fields = [ 'nome', 'descricao', 'quantidade_em_estoque', 'preco_unitario', 'categoria', 'fornecedor']