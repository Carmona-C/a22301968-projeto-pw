from django.shortcuts import render

# Create your views here.

def principal_view(request):
    imagem_minha = '/portofolio/profile.jpg'
    context = {
        'imagem_minha' : imagem_minha,
        }
    return render(request, 'portofolio/principal.html',context)


def sobre_mim_view(request):
    return render(request, 'portofolio/sobre_mim.html')

def web_view(request):
    return render(request, 'portofolio/web.html')