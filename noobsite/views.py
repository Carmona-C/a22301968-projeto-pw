from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index_view(request):
    return HttpResponse("Olá n00b, esta é a página web mais básica do mundo!")

def index_view1(request):
    return HttpResponse("Mais básica e com a mais finalidade do HTML")

def index_view2(request):
    return HttpResponse("Grande página criada!")
