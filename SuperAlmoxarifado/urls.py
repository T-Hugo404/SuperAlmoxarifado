
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('fornecedores/', include('apps.fornecedores.urls')),
    
    path('pedidos/', include('apps.pedidos.urls')),
    
    path('produtos/', include('apps.produtos.urls')),
    
    path('retirada/', include('apps.retirada.urls')),
    
    path('usuarios/', include('apps.usuarios.urls')),
]
