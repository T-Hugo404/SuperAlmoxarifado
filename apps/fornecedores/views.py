from django.shortcuts import render, redirect
from .forms import FornecedorForm
from .models import Fornecedor
# Create your views here.

def lista_fornecedores(request):
    
    fornecedores = Fornecedor.objects.all()

    context = {'fornecedores': fornecedores}
    return render(request, 'fornecedores/lista.html', context)

def cadastrar_fornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_fornecedores')
        
    else:
        form = FornecedorForm()

    return render(request, 'fornecedores/cadastro.html', {'form': form})


def editar_fornecedor(request, forncedor_id):
    
    fornecedor = Fornecedor.objects.get(id=forncedor_id)
    
    if request.method == 'POST':
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            return redirect('lista_fornecedores')
        
    else:
        form = FornecedorForm(instance=fornecedor)

    return render(request, 'fornecedores/cadastro.html', {'form': form})


def excluir_fornecedor(request, forncedor_id):
    
    fornecedor = Fornecedor.objects.get(id=forncedor_id)
    
    if request.method == 'POST':
        fornecedor.delete()
        return redirect('lista_fornecedores')

    return render(request, 'fornecedores/lista.html')