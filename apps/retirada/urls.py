from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_retiradas, name='lista_retiradas'),

    path('novo/', views.cadastrar_retirada, name='cadastrar_retirada'),
    
    path('editar/<int:retirada_id>/', views.editar_retirada, name='editar_retirada'),
    
    path('excluir/<int:retirada_id>/', views.excluir_retirada, name='excluir_retirada'),
]