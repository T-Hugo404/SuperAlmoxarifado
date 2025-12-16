from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),

    path('novo/', views.cadastrar_produto, name='cadastrar_produto'),
    
    path('editar/<int:produto_id>/', views.editar_produto, name='editar_produto'),
    
    path('excluir/<int:produto_id>/', views.excluir_produto, name='excluir_produto'),
]