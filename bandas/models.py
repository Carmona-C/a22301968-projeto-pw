from django.db import models
from django import forms    # formulários Django


# Create your models here.

class Banda(models.Model):
    nome_da_banda = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=100)
    genero = models.CharField(max_length=100, null=True)
    ano_criacao = models.IntegerField()
    foto = models.ImageField(upload_to='foto_da_banda')

    def __str__(self):
        return self.nome_da_banda

class Album(models.Model):
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE)
    nome_do_album = models.CharField(max_length=100)
    capa = models.ImageField(upload_to='capas_de_album')

    def __str__(self):
        return f"{self.banda.nome_da_banda} - ({self.nome_do_album})"


class Musica(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    nome_da_musica = models.CharField(max_length=100)
    duracao = models.CharField(max_length=100)
    spotify_link = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.album.nome_do_album} - ({self.nome_da_musica})"




class BandaForm(forms.ModelForm):
  class Meta:
    model = Banda
    fields = '__all__'


class AlbumForm(forms.ModelForm):
  class Meta:
    model = Album
    fields = '__all__'


class MusicaForm(forms.ModelForm):
  class Meta:
    model = Musica
    fields = '__all__'
