from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pedidos, name='lista_pedidos'),

    path('novo/', views.cadastrar_pedido, name='cadastrar_pedido'),
    
    path('editar/<int:pedido_id>/', views.editar_pedido, name='editar_pedido'),
    
    path('excluir/<int:pedido_id>/', views.excluir_pedido, name='excluir_pedido'),
]