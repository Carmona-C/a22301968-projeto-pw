from django.db import models

# Create your models here.

class Pessoa(models.Model):

    primeiro_nome = models.CharField(max_length=50)
    ultimo_nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    identificacao = models.CharField(max_length=50)

    def __str__(self):
        return f"Primeiro nome: {self.primeiro_nome}| ultimo nome: {self.ultimo_nome} | idade: {self.idade} | identificacao: {self.identificacao}"


class Aluno(models.Model):
    nome = models.CharField(max_length=60)


class Computador(models.Model):
    nome = models.CharField(max_length=50)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)




