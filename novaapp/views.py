from django.shortcuts import render

from datetime import datetime
# Create your views here.

def IntroducaoDaNovaapp_view(request):
    return render(request, "novaapp/IntroducaoDaNovaapp.html",{
        'data':datetime.today()})

def PaginaDeOrcamento_view(request):
    return render(request, "novaapp/PaginaDeOrcamento.html",{
        'data':datetime.today()})

def PaginaDeCompra_view(request):
    return render(request, "novaapp/PaginaDeCompra.html",{
        'data':datetime.today()})