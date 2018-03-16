from django.forms import ModelForm
from core.models import Edital, Aluno
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class EditalForm(ModelForm):
    class Meta:
        model = Edital
        fields = ['titulo', 'descricao', 'inicio_inscricoes', 'fim_inscricoes', 'inicio_curso', 'fim_curso', 'vagas', 'pre_requisitos', 'edital_link', 'carga_horaria', 'cidade', 'ativo']

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'logradouro', 'numero', 'complemento', 'cep', 'cidade', 'estado', 'rg', 'cpf', 'email', 'telefone', 'nascimento', 'ativo']
