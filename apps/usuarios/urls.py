from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_usuarios, name='lista_usuarios'),

    path('novo/', views.cadastrar_usuario, name='cadastrar_usuario'),
    
    path('editar/<int:usuario_id>/', views.editar_usuario, name='editar_usuario'),
    
    path('excluir/<int:usuario_id>/', views.excluir_usuario, name='excluir_usuario'),
]