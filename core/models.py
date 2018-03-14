from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Edital(models.Model):
    titulo = models.CharField(max_length = 100)
    descricao = models.TextField()
    inicio_inscricoes = models.DateField()
    fim_inscricoes = models.DateField()
    inicio_curso = models.DateField()
    fim_curso = models.DateField()
    vagas = models.IntegerField()
    pre_requisitos = models.TextField()
    edital_link = models.CharField(max_length = 100)
    carga_horaria = models.IntegerField(default = 1)
    cidade = models.CharField(max_length = 100)
    ativo = models.BooleanField(default = True)

    def __str__(self):
        return self.titulo

class Aluno(models.Model):
    nome = models.CharField(max_length = 100)
    logradouro = models.CharField(max_length = 100)
    numero = models.CharField(max_length = 10)
    complemento = models.TextField(blank = True, default = '')
    cep = models.CharField(max_length = 10)
    cidade = models.CharField(max_length = 100)
    estado = models.CharField(max_length = 2)
    rg = models.CharField(max_length = 20)
    cpf = models.CharField(unique = True, max_length = 20)
    email = models.CharField(max_length = 30)
    telefone = models.CharField(max_length = 20)
    nascimento = models.DateField()
    created_by = models.ForeignKey(User, null = True, on_delete = models.SET_NULL)
    ativo = models.BooleanField(default = True)

    def __str__(self):
        return self.nome

class Inscrito(models.Model):
    inscrito_em = models.DateTimeField(default = timezone.now)
    matriculado_em = models.DateTimeField(null = True)
    aprovado_em = models.DateTimeField(null = True)
    reprovado_em = models.DateTimeField(null = True)
    aluno = models.ForeignKey(Aluno, on_delete = models.CASCADE)
    edital = models.ForeignKey(Aluno, on_delete = models.CASCADE)
    status = models.IntegerField(default = 0)
    observacoes = models.TextField()
