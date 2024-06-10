from django.urls import path
from . import views

app_name = 'AplicacaoArtigo'

urlpatterns = [
    path('', views.principal_view, name='principal'),
    path('autor/<int:autor_id>/', views.autor_view, name='autor'),
    path('artigo/<int:artigo_id>/', views.artigo_view, name='artigo'),
    path('comentario/<int:artigo_id>/', views.comentario_view, name='comentario'),
    path('avaliacao/<int:artigo_id>/', views.avaliacao_view, name='avaliacao'),


    path('AplicacaoArtigo/', views.novo_autor_view, name="novo_autor"),
    path('AplicacaoArtigo/<int:autor_id>/edita', views.edita_autor_view, name="edita_autor"),
    path('AplicacaoArtigo/<int:autor_id>/apaga', views.apaga_autor_view, name="apaga_autor"),


    path('AplicacaoArtigo/artigo', views.novo_artigo_view, name="novo_artigo"),
    path('AplicacaoArtigo/artigo<int:artigo_id>/edita', views.edita_artigo_view, name="edita_artigo"),
    path('AplicacaoArtigo/artigo<int:artigo_id>/apaga', views.apaga_artigo_view, name="apaga_artigo"),


    path('AplicacaoArtigo/comentario', views.novo_comentario_view, name="novo_comentario"),
    path('AplicacaoArtigo/comentario<int:comentario_id>/edita', views.edita_comentario_view, name="edita_comentario"),
    path('AplicacaoArtigo/comentario<int:comentario_id>/apaga', views.apaga_comentario_view, name="apaga_comentario"),

    path('AplicacaoArtigo/avaliacao', views.novo_avaliacao_view, name="novo_avaliacao"),
    path('AplicacaoArtigo/avaliacao<int:avaliacao_id>/edita', views.edita_avaliacao_view, name="edita_avaliacao"),
    path('AplicacaoArtigo/avaliacao<int:avaliacao_id>/apaga', views.apaga_avaliacao_view, name="apaga_avaliacao"),


]
