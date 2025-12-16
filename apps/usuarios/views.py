from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm

# Create your views here.
def lista_usuarios(request):
    
    usuarios = Usuario.objects.all()

    context = {'usuarios': usuarios}
    return render(request, 'lista.html', context)


def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
        
    else:
        form = UsuarioForm()

    return render(request, 'cadastro.html', {'form': form})


def editar_usuario(request, usuario_id):
    
    usuario = Usuario.objects.get(id=usuario_id)
    
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
        
    else:
        form = UsuarioForm(instance=usuario)

    return render(request, 'cadastro.html', {'form': form})


def excluir_usuario(request, usuario_id):
    
    usuario = Usuario.objects.get(id=usuario_id)
    
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuarios')

    return render(request, 'lista.html')