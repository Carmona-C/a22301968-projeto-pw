from django.shortcuts import render,redirect
from .models import AreaCientifica, Curso, Disciplina, Projeto, LinguagemProgramacao, Docente
from django.contrib.auth import models
from django.shortcuts import render, get_object_or_404
from .models import CursoForm
from .models import DisciplinaForm
from .models import DocenteForm
from .models import ProjetoForm



from django.contrib.auth.decorators import login_required,user_passes_test

def is_editor_curso(user):
    return user.groups.filter(name='cursogroup').exists()

def principal_view(request):
    context = {
        'cursos': Curso.objects.all(),
        'is_editor' : is_editor_curso(request.user)
    }
    return render(request, "curso/principal.html", context)

def curso_view(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    disciplinas = Disciplina.objects.all()
    context = {
        'curso': curso,
        'disciplinas': disciplinas,
        'is_editor' : is_editor_curso(request.user)
    }
    return render(request, "curso/curso.html", context)

def disciplina_view(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)
    docentes = Docente.objects.filter(disciplina=disciplina)
    projetos = Projeto.objects.filter(disciplina=disciplina)
    linguagens = LinguagemProgramacao.objects.all()

    context = {
        'disciplina': disciplina,
        'docentes': docentes,
        'projetos': projetos,
        'linguagens': linguagens,
        'is_editor' : is_editor_curso(request.user)
    }
    return render(request, "curso/disciplina.html", context)


def projeto_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    context = {
        'projeto': projeto,
        'is_editor': is_editor_curso(request.user)
    }
    return render(request, "curso/projeto.html", context)

def linguagem_view(request, linguagem_id):
    linguagem = get_object_or_404(LinguagemProgramacao, id=linguagem_id)
    disciplinas = linguagem.disciplina_set.all()
    context = {
        'linguagem': linguagem,
        'disciplinas': disciplinas,
        'is_editor': is_editor_curso(request.user)
    }
    return render(request, "curso/linguagem.html", context)

def docente_view(request, docente_id):
    docente = get_object_or_404(Docente, id=docente_id)
    context = {
        'docente': docente,
        'is_editor': is_editor_curso(request.user)
    }
    return render(request, "curso/docente.html", context)

@login_required
@user_passes_test(is_editor_curso)
def novo_curso_view(request):

 # criar instância de formulário.
    # Se foram submetidos dados, estes estão em request.POST e o formulario com dados é válido.
    # Senão, o form não tem dados e não é válido
    form = CursoForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('curso:principal')

    context = {'form': form}
    return render(request, 'criacao/novo_curso.html', context)

@login_required
@user_passes_test(is_editor_curso)
def edita_curso_view(request, curso_id):
    curso = Curso.objects.get(id=curso_id)

    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('curso:principal')
    else:
        form = CursoForm(instance=curso)

    context = {'form': form, 'curso': curso}
    return render(request, 'criacao/edita_curso.html', context)

@login_required
@user_passes_test(is_editor_curso)
def apaga_curso_view(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    curso.delete()
    return redirect('curso:principal')


@login_required
@user_passes_test(is_editor_curso)
def novo_disciplina_view(request):

 # criar instância de formulário.
    # Se foram submetidos dados, estes estão em request.POST e o formulario com dados é válido.
    # Senão, o form não tem dados e não é válido
    form = DisciplinaForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('curso:principal')

    context = {'form': form}
    return render(request, 'criacao/novo_disciplina.html', context)

@login_required
@user_passes_test(is_editor_curso)
def edita_disciplina_view(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)

    if request.method == 'POST':
        form = DisciplinaForm(request.POST, request.FILES, instance=disciplina)
        if form.is_valid():
            form.save()
            return redirect('curso:principal')
    else:
        form = DisciplinaForm(instance=disciplina)

    context = {'form': form, 'disciplina': disciplina}
    return render(request, 'criacao/edita_disciplina.html', context)

@login_required
@user_passes_test(is_editor_curso)
def apaga_disciplina_view(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)
    disciplina.delete()
    return redirect('curso:principal')


@login_required
@user_passes_test(is_editor_curso)
def novo_docente_view(request):

 # criar instância de formulário.
    # Se foram submetidos dados, estes estão em request.POST e o formulario com dados é válido.
    # Senão, o form não tem dados e não é válido
    form = DocenteForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('curso:principal')

    context = {'form': form}
    return render(request, 'criacao/novo_docente.html', context)

@login_required
@user_passes_test(is_editor_curso)
def edita_docente_view(request, docente_id):
    docente = Docente.objects.get(id=docente_id)

    if request.method == 'POST':
        form = DocenteForm(request.POST, request.FILES, instance=docente)
        if form.is_valid():
            form.save()
            return redirect('curso:principal')
    else:
        form = DocenteForm(instance=docente)

    context = {'form': form, 'docente': docente}
    return render(request, 'criacao/edita_docente.html', context)

@login_required
@user_passes_test(is_editor_curso)
def apaga_docente_view(request, docente_id):
    docente = Docente.objects.get(id=docente_id)
    docente.delete()
    return redirect('curso:principal')



@login_required
@user_passes_test(is_editor_curso)
def novo_projeto_view(request):

 # criar instância de formulário.
    # Se foram submetidos dados, estes estão em request.POST e o formulario com dados é válido.
    # Senão, o form não tem dados e não é válido
    form = ProjetoForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('curso:principal')

    context = {'form': form}
    return render(request, 'criacao/novo_projeto.html', context)

@login_required
@user_passes_test(is_editor_curso)
def edita_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)

    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('curso:principal')
    else:
        form = ProjetoForm(instance=projeto)

    context = {'form': form, 'projeto': projeto}
    return render(request, 'criacao/edita_projeto.html', context)

@login_required
@user_passes_test(is_editor_curso)
def apaga_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    projeto.delete()
    return redirect('curso:principal')

