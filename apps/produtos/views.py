from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm

# Create your views here.
def lista_produtos(request):
    
    produtos = Produto.objects.all()

    context = {'produtos': produtos}
    return render(request, 'lista.html', context)


def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
        
    else:
        form = ProdutoForm()

    return render(request, 'cadastro.html', {'form': form})


def editar_produto(request, produto_id):
    
    produto = Produto.objects.get(id=produto_id)
    
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
        
    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'cadastro.html', {'form': form})


def excluir_produto(request, produto_id):
    
    produto = Produto.objects.get(id=produto_id)
    
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')

    return render(request, 'lista.html')