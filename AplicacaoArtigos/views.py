from django.shortcuts import render, redirect
from .models import Autor, Artigo, Comentario, Avaliacao
from django.shortcuts import get_object_or_404
from django.contrib.auth import models
from .models import AutorForm
from .models import ArtigoForm
from .models import ComentarioForm
from .models import AvaliacaoForm

from django.contrib.auth.decorators import login_required,user_passes_test
# Create your views here.


def is_editor_artigos(user):
    return user.groups.filter(name='artigosgroup').exists()

def principal_view(request):
    context = {
        'autores': Autor.objects.all().order_by('nome'),
        'is_editor' : is_editor_artigos(request.user)
    }
    return render(request, "AplicacaoArtigo/principal.html", context)


def autor_view(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    artigos = Artigo.objects.filter(autor=autor)
    context = {
        'autor': autor,
        'artigos': artigos,
        'is_editor' : is_editor_artigos(request.user)
    }
    return render(request, "AplicacaoArtigo/autor.html", context)

def artigo_view(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    comentarios = Comentario.objects.filter(artigo=artigo)
    avaliacao = Avaliacao.objects.filter(artigo=artigo)

    context = {
        'artigo': artigo,
        'comentarios': comentarios,
        'avaliacao': avaliacao,
        'is_editor' : is_editor_artigos(request.user)
    }
    return render(request, "AplicacaoArtigo/artigo.html", context)

def comentario_view(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    comentarios = Comentario.objects.filter(artigo=artigo)
    context = {
        'artigo': artigo,
        'comentarios': comentarios,
        'is_editor': is_editor_artigos(request.user),
    }
    return render(request, "AplicacaoArtigo/comentario.html", context)

def avaliacao_view(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    context = {
        'avaliacao': Avaliacao.objects.filter(artigo=artigo),
        'is_editor' : is_editor_artigos(request.user)
    }
    return render(request, "AplicacaoArtigo/avaliacao.html", context)


@login_required
@user_passes_test(is_editor_artigos)
def novo_autor_view(request):

 # criar instância de formulário.
    # Se foram submetidos dados, estes estão em request.POST e o formulario com dados é válido.
    # Senão, o form não tem dados e não é válido
    form = AutorForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('AplicacaoArtigo:principal')

    context = {'form': form}
    return render(request, 'criacao/novo_autor.html', context)


@login_required
@user_passes_test(is_editor_artigos)
def edita_autor_view(request, autor_id):
    autor = Autor.objects.get(id=autor_id)

    if request.method == 'POST':
        form = AutorForm(request.POST, request.FILES, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('AplicacaoArtigo:principal')
    else:
        form = AutorForm(instance=autor)

    context = {'form': form, 'autor': autor}
    return render(request, 'criacao/edita_autor.html', context)


@login_required
@user_passes_test(is_editor_artigos)
def apaga_autor_view(request, autor_id):
    autor = Autor.objects.get(id=autor_id)
    autor.delete()
    return redirect('AplicacaoArtigo:principal')


@login_required
@user_passes_test(is_editor_artigos)
def novo_artigo_view(request):

 # criar instância de formulário.
    # Se foram submetidos dados, estes estão em request.POST e o formulario com dados é válido.
    # Senão, o form não tem dados e não é válido
    form = ArtigoForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('AplicacaoArtigo:principal')

    context = {'form': form}
    return render(request, 'criacao/novo_artigo.html', context)


@login_required
@user_passes_test(is_editor_artigos)
def edita_artigo_view(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)

    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES, instance=artigo)
        if form.is_valid():
            form.save()
            return redirect('AplicacaoArtigo:principal')
    else:
        form = ArtigoForm(instance=artigo)

    context = {'form': form, 'artigo':artigo}
    return render(request, 'criacao/edita_artigo.html', context)

@login_required
@user_passes_test(is_editor_artigos)
def apaga_artigo_view(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)
    artigo.delete()
    return redirect('AplicacaoArtigo:principal')



@login_required
@user_passes_test(is_editor_artigos)
def novo_comentario_view(request):

 # criar instância de formulário.
    # Se foram submetidos dados, estes estão em request.POST e o formulario com dados é válido.
    # Senão, o form não tem dados e não é válido
    form = ComentarioForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('AplicacaoArtigo:principal')

    context = {'form': form}
    return render(request, 'criacao/novo_comentario.html', context)


@login_required
@user_passes_test(is_editor_artigos)
def novo_avaliacao_view(request):

 # criar instância de formulário.
    # Se foram submetidos dados, estes estão em request.POST e o formulario com dados é válido.
    # Senão, o form não tem dados e não é válido
    form = AvaliacaoForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('AplicacaoArtigo:principal')

    context = {'form': form}
    return render(request, 'criacao/novo_avaliacao.html', context)

@login_required
@user_passes_test(is_editor_artigos)
def edita_comentario_view(request, comentario_id):
    comentario = Comentario.objects.get(id=comentario_id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST, request.FILES, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('AplicacaoArtigo:principal')
    else:
        form = ComentarioForm(instance=comentario)

    context = {'form': form, 'comentario':comentario}
    return render(request, 'criacao/edita_comentario.html', context)

@login_required
@user_passes_test(is_editor_artigos)
def apaga_comentario_view(request, comentario_id):
    comentario = Comentario.objects.get(id=comentario_id)
    comentario.delete()
    return redirect('AplicacaoArtigo:principal')



@login_required
@user_passes_test(is_editor_artigos)
def edita_avaliacao_view(request, avaliacao_id):
    avaliacao = Avaliacao.objects.get(id=avaliacao_id)

    if request.method == 'POST':
        form = AvaliacaoForm(request.POST, request.FILES, instance=avaliacao)
        if form.is_valid():
            form.save()
            return redirect('AplicacaoArtigo:principal')
    else:
        form = AvaliacaoForm(instance=avaliacao)

    context = {'form': form, 'avaliacao':avaliacao}
    return render(request, 'criacao/edita_avaliacao.html', context)

@login_required
@user_passes_test(is_editor_artigos)
def apaga_avaliacao_view(request, avaliacao_id):
    avaliacao = Avaliacao.objects.get(id=avaliacao_id)
    avaliacao.delete()
    return redirect('AplicacaoArtigo:principal')


