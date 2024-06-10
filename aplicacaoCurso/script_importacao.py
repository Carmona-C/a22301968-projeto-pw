from aplicacaoCurso.models import Curso, Disciplina, AreaCientifica, Projeto, LinguagemProgramacao, Docente
import json

Disciplina.objects.all().delete()
Curso.objects.all().delete()
Projeto.objects.all().delete()


with open('aplicacaoCurso/json/importar_curso.json') as f:
    dados = json.load(f)

    disciplinas_data = dados.get('courseFlatPlan', [])
    for disci in disciplinas_data:
        Disciplina.objects.create(
            nome_disciplina=disci.get('curricularUnitName'),
            ano=disci.get('curricularYear', 0),
            semestre=disci.get('semester'),
            ects=disci.get('ects'),
            curricularIUnitReadableCode=disci.get('curricularIUnitReadableCode'),
        )

    Curso.objects.create(
        apresentacao=dados.get('courseDetail', {}).get('presentation'),
        objetivos=dados.get('courseDetail', {}).get('objectives'),
        competencias=dados.get('courseDetail', {}).get('competences'),
    )

    if 'projetos' in dados:
        for projeto_data in dados['projetos']:
            projeto = Projeto.objects.create(
                descricao=projeto_data.get('descricao'),
                conceitos_aplicados=projeto_data.get('conceitos_aplicados'),
                tecnologias_utilizadas=projeto_data.get('tecnologias_utilizadas'),
                imagem=projeto_data.get('imagem'),
                video_demo_link=projeto_data.get('video_demo_link'),
                github_link=projeto_data.get('github_link')
            )

            linguagens_programacao = projeto_data.get('linguagens_programacao', [])
            for linguagem_data in linguagens_programacao:
                linguagem, created = LinguagemProgramacao.objects.get_or_create(
                    nome_linguagem=linguagem_data
                )
                projeto.linguagemprogramacao_set.add(linguagem)

    if 'docentes' in dados:
        for docente_data in dados['docentes']:
            disciplinas_ids = docente_data.get('disciplinas', [])
            disciplinas = Disciplina.objects.filter(id__in=disciplinas_ids)
            docente = Docente.objects.create(
                nome_docente=docente_data.get('nome_docente')
            )
            docente.disciplinas.set(disciplinas)


