from django.db import models
from django import forms    # formulários Django


# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=200)
    biografia = models.TextField()

    def __str__(self):
        return self.nome

class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    data_artigo = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor}: {self.conteudo}"

class Avaliacao(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE)
    nome_avaliacao = models.ForeignKey(Autor, on_delete=models.CASCADE)
    avaliacao = models.IntegerField()

    def __str__(self):
        return f"{self.nome_avaliacao}: {self.avaliacao}"


class AutorForm(forms.ModelForm):
  class Meta:
    model = Autor
    fields = '__all__'


class ArtigoForm(forms.ModelForm):
  class Meta:
    model = Artigo
    fields = '__all__'

class ComentarioForm(forms.ModelForm):
  class Meta:
    model = Comentario
    fields = '__all__'

class AvaliacaoForm(forms.ModelForm):
  class Meta:
    model = Avaliacao
    fields = '__all__'