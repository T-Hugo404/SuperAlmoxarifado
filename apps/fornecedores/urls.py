from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_fornecedores, name='lista_fornecedores'),

    path('novo/', views.cadastrar_fornecedor, name='cadastrar_fornecedor'),
]