from django.shortcuts import render
from .models import Festival,Localizacao

def principal_view(request):
    context = {
        'festivais':Festival.objects.all(),
    }
    return render(request, "festivais/principal.html", context)


def festival_view(request, banda_id):
    context = {
        'festival': Festival.objects.all,
        'localizacao': Localizacao.objects.all,
    }
    return render(request, "festivais/festival.html", context)



def localizacao_view(request, album_id):
    context = {
        'localizacao': Localizacao.objects.all,
    }
    return render(request, "festivais/localizacao.html", context)
