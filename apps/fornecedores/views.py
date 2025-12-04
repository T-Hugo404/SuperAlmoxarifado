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