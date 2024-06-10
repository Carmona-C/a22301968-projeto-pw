from django.shortcuts import render,redirect
from .models import Banda, Album, Musica, BandaForm
from django.contrib.auth import models
from .models import AlbumForm
from .models import MusicaForm

from django.contrib.auth.decorators import login_required,user_passes_test

def is_editor_bandas(user):
    return user.groups.filter(name='bandasgroup').exists()


def principal_view(request):
    context = {
        'bandas': Banda.objects.all().order_by('nome_da_banda'),
        'is_editor' : is_editor_bandas(request.user)
    }
    return render(request, "bandas/principal.html", context)


def banda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)
    albuns = Album.objects.filter(banda=banda)
    context = {'banda': banda, 'albuns': albuns, 'is_editor' : is_editor_bandas(request.user)}

    return render(request, "bandas/banda.html", context)


def album_view(request, album_id):
    album = Album.objects.get(id=album_id)
    musicas = Musica.objects.filter(album=album)
    context = {'album': album, 'musicas': musicas, 'is_editor' : is_editor_bandas(request.user)}

    return render(request, "bandas/album.html", context)

def musica_view(request, musica_id):
    context = {
        'musica': Musica.objects.get(id=musica_id,),
        'is_editor' : is_editor_bandas(request.user)
    }
    return render(request, "bandas/musica.html", context)


@login_required
@user_passes_test(is_editor_bandas)
def nova_banda_view(request):

 # criar instância de formulário.
    # Se foram submetidos dados, estes estão em request.POST e o formulario com dados é válido.
    # Senão, o form não tem dados e não é válido
    form = BandaForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('bandas:principal')

    context = {'form': form}
    return render(request, 'criacao/nova_banda.html', context)

@login_required
@user_passes_test(is_editor_bandas)
def edita_banda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)

    if request.method == 'POST':
        form = BandaForm(request.POST, request.FILES, instance=banda)
        if form.is_valid():
            form.save()
            return redirect('bandas:principal')
    else:
        form = BandaForm(instance=banda)

    context = {'form': form, 'banda': banda}
    return render(request, 'criacao/edita_banda.html', context)

@login_required
@user_passes_test(is_editor_bandas)
def apaga_banda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)
    banda.delete()
    return redirect('bandas:principal')




@login_required
@user_passes_test(is_editor_bandas)
def novo_album_view(request):

 # criar instância de formulário.
    # Se foram submetidos dados, estes estão em request.POST e o formulario com dados é válido.
    # Senão, o form não tem dados e não é válido
    form = AlbumForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('bandas:principal')

    context = {'form': form}
    return render(request, 'criacao/novo_album.html', context)

@login_required
@user_passes_test(is_editor_bandas)
def edita_album_view(request, album_id):
    album = Album.objects.get(id=album_id)

    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('bandas:principal')
    else:
        form = AlbumForm(instance=album)

    context = {'form': form, 'album': album}
    return render(request, 'criacao/edita_album.html', context)

@login_required
@user_passes_test(is_editor_bandas)
def apaga_album_view(request, album_id):
    album = Album.objects.get(id=album_id)
    album.delete()
    return redirect('bandas:principal')

@login_required
@user_passes_test(is_editor_bandas)
def nova_musica_view(request):

 # criar instância de formulário.
    # Se foram submetidos dados, estes estão em request.POST e o formulario com dados é válido.
    # Senão, o form não tem dados e não é válido
    form = MusicaForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('bandas:principal')

    context = {'form': form}
    return render(request, 'criacao/nova_musica.html', context)

@login_required
@user_passes_test(is_editor_bandas)
def edita_musica_view(request, musica_id):
    musica = Musica.objects.get(id=musica_id)

    if request.method == 'POST':
        form = MusicaForm(request.POST, request.FILES, instance=musica)
        if form.is_valid():
            form.save()
            return redirect('bandas:principal')
    else:
        form = MusicaForm(instance=musica)

    context = {'form': form, 'musica': musica}
    return render(request, 'criacao/edita_musica.html', context)

@login_required
@user_passes_test(is_editor_bandas)
def apaga_musica_view(request, musica_id):
    musica = Musica.objects.get(id=musica_id)
    musica.delete()
    return redirect('bandas:principal')







