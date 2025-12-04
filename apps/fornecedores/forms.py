from django import forms
from .models import Fornecedor

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor

        fields = ['nome_empresa', 'contato_nome', 'telefone', 'email', 'endereco']