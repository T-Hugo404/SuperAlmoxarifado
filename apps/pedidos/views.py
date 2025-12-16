from django.shortcuts import render, redirect
from .models import Pedido
from .forms import PedidoForm

# Create your views here.
def lista_pedidos(request):
    
    pedidos = Pedido.objects.all()

    context = {'pedidos': pedidos}
    return render(request, 'lista.html', context)


def cadastrar_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')
        
    else:
        form = PedidoForm()

    return render(request, 'cadastro.html', {'form': form})


def editar_pedido(request, pedido_id):
    
    pedido = Pedido.objects.get(id=pedido_id)
    
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')
        
    else:
        form = PedidoForm(instance=pedido)

    return render(request, 'cadastro.html', {'form': form})


def excluir_pedido(request, pedido_id):
    
    pedido = Pedido.objects.get(id=pedido_id)
    
    if request.method == 'POST':
        pedido.delete()
        return redirect('lista_pedidos')

    return render(request, 'lista.html')