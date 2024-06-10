# Empresa/urls.py

from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'novaapp'

urlpatterns = [
    path('IntroducaoDaNovaapp/', views.IntroducaoDaNovaapp_view, name='IntroducaoDaNovaapp'),
    path('PaginaDeOrcamento/', views.PaginaDeOrcamento_view, name='PaginaDeOrcamento'),
    path('PaginaDeCompra/', views.PaginaDeCompra_view, name='PaginaDeCompra'),
]