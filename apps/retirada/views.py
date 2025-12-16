
from django.shortcuts import render, redirect
from .models import Retirada
from .forms import RetiradaForm

# Create your views here.
def lista_retiradas(request):
    
    retiradas = Retirada.objects.all()

    context = {'retiradas': retiradas}
    return render(request, 'retirada/lista.html', context)


def cadastrar_retirada(request):
    if request.method == 'POST':
        form = RetiradaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_retiradas')
        
    else:
        form = RetiradaForm()

    return render(request, 'retirada/cadastro.html', {'form': form})


def editar_retirada(request, retirada_id):
    
    retirada = Retirada.objects.get(id=retirada_id)
    
    if request.method == 'POST':
        form = RetiradaForm(request.POST, instance=retirada)
        if form.is_valid():
            form.save()
            return redirect('lista_retiradas')
        
    else:
        form = RetiradaForm(instance=retirada)

    return render(request, 'retirada/cadastro.html', {'form': form})


def excluir_retirada(request, retirada_id):
    
    retirada = Retirada.objects.get(id=retirada_id)
    
    if request.method == 'POST':
        retirada.delete()
        return redirect('lista_retiradas')

    return render(request, 'retirada/lista.html')