
from django.shortcuts import render

from datetime import datetime
# Create your views here.

def IntroducaoDaEmpresa_view(request):
    return render(request, "Empresa/IntroducaoDaEmpresa.html",{
        'data':datetime.today()})

def PaginaDeOrcamento_view(request):
    return render(request, "Empresa/PaginaDeOrcamento.html",{
        'data':datetime.today()})

def PaginaDeCompra_view(request):
    return render(request, "Empresa/PaginaDeCompra.html",{
        'data':datetime.today()})