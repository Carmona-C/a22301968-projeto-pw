from django.urls import path
from . import views

app_name = 'curso'

urlpatterns = [
    path('', views.principal_view, name='principal'),
    path('curso/<int:curso_id>/', views.curso_view, name='curso'),
    path('disciplina/<int:disciplina_id>/', views.disciplina_view, name='disciplina'),
    path('projeto/<int:projeto_id>/', views.projeto_view, name='projeto'),
    path('linguagem/<int:linguagem_id>/', views.linguagem_view, name='linguagem'),
    path('docente/<int:docente_id>/', views.docente_view, name='docente'),


    path('curso/', views.novo_curso_view, name="novo_curso"),
    path('curso/<int:curso_id>/edita', views.edita_curso_view,name="edita_curso"),
    path('curso/<int:curso_id>/apaga', views.apaga_curso_view,name="apaga_curso"),


    path('curso/disciplina', views.novo_disciplina_view, name="novo_disciplina"),
    path('curso/disciplina<int:disciplina_id>/edita', views.edita_disciplina_view,name="edita_disciplina"),
    path('curso/disciplina<int:disciplina_id>/apaga', views.apaga_disciplina_view,name="apaga_disciplina"),


    path('curso/docente', views.novo_docente_view, name="novo_docente"),
    path('curso/docente<int:docente_id>/edita', views.edita_docente_view,name="edita_docente"),
    path('curso/docente<int:docente_id>/apaga', views.apaga_docente_view,name="apaga_docente"),


    path('curso/projeto', views.novo_projeto_view, name="novo_projeto"),
    path('curso/projeto<int:projeto_id>/edita', views.edita_projeto_view,name="edita_projeto"),
    path('curso/projeto<int:projeto_id>/apaga', views.apaga_projeto_view,name="apaga_projeto"),



]
