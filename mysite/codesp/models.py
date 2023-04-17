from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Professor(models.Model):
    nome = models.CharField(max_length=40)
    matricula = models.CharField(max_length=20)
    email = models.CharField(max_length=35)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return f'{self.nome} - {self.id}'

class Bolsista(models.Model):
    nome = models.CharField(max_length=40)
    matricula = models.CharField(max_length=40)
    turno = models.CharField(max_length=40)
    email = models.CharField(max_length=35)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.nome} - {self.matricula} - {self.turno}'

# class Aluno(models.Model):
#     nomeAluno = models.CharField(max_length=40)
#     matricula = models.CharField(max_length=40)

#     def __str__(self):
#         return f'{self.nomeAluno} - {self.matricula}'

class Coordenacao(models.Model):
    nome = models.CharField(max_length=40)
    matricula = models.CharField(max_length=40)
    email = models.CharField(max_length=35)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.nome} - {self.matricula}'


class Modalidade(models.Model):
    nomeModalidade = models.CharField(max_length=40)
    descricao = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.nomeModalidade}'


class CategoriaModalidade(models.Model):
    categoria = models.CharField(max_length=40)
    descricao = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.categoria}'

class SolicitarModalidade(models.Model):
    dataPedido = models.DateTimeField(auto_now_add=True, blank=True)
    categoria = models.ForeignKey(CategoriaModalidade, on_delete = models.CASCADE, blank=True, null=True)
    horarioInicial = models.CharField(max_length=10)
    horarioFinal = models.CharField(max_length=10)
    justificativa = models.CharField(max_length = 80)
    modalidade = models.ForeignKey(Modalidade, on_delete = models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete = models.CASCADE)
    diasDaSemana = models.CharField(max_length=40, blank=True)
    def __str__(self):
        return f'{self.modalidade} - {self.professor}'





class SolicitarMatricula(models.Model):
    nomeAluno = models.CharField(max_length=40)
    matricula = models.CharField(max_length=40)
    tipoCategoria = models.ForeignKey(CategoriaModalidade, on_delete = models.CASCADE)
    dataInscricao = models.DateTimeField(auto_now_add=True, blank=True)
    modalidade = models.ForeignKey(Modalidade, on_delete = models.CASCADE)
    bolsista = models.ForeignKey(Bolsista, on_delete = models.CASCADE)
    autorizado = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id} {self.nomeAluno} - {self.modalidade} - {self.tipoCategoria}'


class Codesp(models.Model):
    solicitacao = models.ForeignKey(SolicitarMatricula, on_delete = models.CASCADE)
    coordenacao = models.ForeignKey(Coordenacao, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.solicitacao} - {self.coordenacao} - {self.id}'





class EspacoModalidade(models.Model):
    nome = models.CharField(max_length=40)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome}'

class Turma(models.Model):
    nomeTurma = models.CharField(max_length=40, blank=True)
    turno = models.CharField(max_length=40, blank=True)
    espaco = models.ForeignKey(EspacoModalidade, on_delete = models.CASCADE, blank=True)
    professor =  models.ForeignKey(SolicitarModalidade, on_delete = models.CASCADE, blank=True, null=True)
    def __str__(self):
        return f'{self.nomeTurma}'

class AlunoTurma(models.Model):
    alunos = models.ForeignKey(Codesp, on_delete = models.CASCADE, blank=True)
    turma = models.ForeignKey(Turma, on_delete = models.CASCADE, blank=True)

    def __str__(self):
        return f'{self.alunos} - {self.turma}'

class Frequencia(models.Model):
    data = models.CharField(max_length=40)
    descricaoAula = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return f'{self.descricaoAula}'

class FreAluno(models.Model):
    aluno = models.ForeignKey(AlunoTurma, on_delete = models.CASCADE, blank=True)
    frequencia = models.ForeignKey(Frequencia, on_delete = models.CASCADE, blank=True)
    presenca = models.IntegerField('presenca', default = 0)
    def __str__(self):
        return f'{self.aluno} - {self.presenca}'

class AtividadeEspaco(models.Model):
    presenca = models.BooleanField(default=False)
    turma = models.ForeignKey(Turma, on_delete = models.CASCADE)
    bolsista = models.ForeignKey(Bolsista, on_delete = models.CASCADE)
    data = models.CharField(max_length=40, blank=True)
    def __str__(self):
        return f'{self.id} - {self.turma} - {self.bolsista}'
