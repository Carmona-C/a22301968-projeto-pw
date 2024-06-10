from django.db import models

class Festival(models.Model):
    nome = models.CharField(max_length=100)
    localizacao = models.ForeignKey('Localizacao', on_delete=models.CASCADE)
    cartaz = models.ImageField(upload_to='media/festivais/', null=True, blank=True)

    def __str__(self):
        return self.nome

class Localizacao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Banda(models.Model):
    nome = models.CharField(max_length=100)
    festivais = models.ManyToManyField(Festival)

    def __str__(self):
        return self.nome
