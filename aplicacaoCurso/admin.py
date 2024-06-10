from django.contrib import admin

# Register your models here.

from .models import Curso
from .models import AreaCientifica
from .models import Disciplina
from .models import Projeto
from .models import LinguagemProgramacao
from .models import Docente

admin.site.register(Curso)
admin.site.register( AreaCientifica)
admin.site.register(Disciplina)
admin.site.register(Projeto)
admin.site.register(LinguagemProgramacao)
admin.site.register(Docente)