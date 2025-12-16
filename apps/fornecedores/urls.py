from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_fornecedores, name='lista_fornecedores'),

    path('novo/', views.cadastrar_fornecedor, name='cadastrar_fornecedor'),
    
    path('editar/<int:forncedor_id>/', views.editar_fornecedor, name='editar_fornecedor'),
    
    path('excluir/<int:forncedor_id>/', views.excluir_fornecedor, name='excluir_fornecedor'),
]