from django.contrib import admin
from .models import Professor,Bolsista, Coordenacao, Codesp, SolicitarMatricula, Modalidade, SolicitarModalidade, CategoriaModalidade, EspacoModalidade, Turma, AlunoTurma, FreAluno, Frequencia, AtividadeEspaco
# Register your models here.
admin.site.register(Professor)
admin.site.register(Bolsista)
admin.site.register(Coordenacao)
admin.site.register(Codesp)
admin.site.register(SolicitarMatricula)
admin.site.register(Modalidade)
admin.site.register(SolicitarModalidade)
admin.site.register(EspacoModalidade)
admin.site.register(Turma)
admin.site.register(AlunoTurma)
admin.site.register(FreAluno)
admin.site.register(Frequencia)
admin.site.register(AtividadeEspaco)
