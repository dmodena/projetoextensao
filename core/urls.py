from django.urls import path
from core import views

urlpatterns = [
    path('', views.home),

    path('editais/', views.editais, name='editais'),
    path('editais/novo/', views.edital_create, name='editais/novo'),
    path('editais/editar/<id>', views.edital_edit, name='editais/editar'),
    path('editais/excluir/<id>', views.edital_remove, name='editais/excluir'),

    path('alunos/', views.alunos, name='alunos'),
    path('alunos/novo/', views.aluno_create, name='alunos/novo'),
    path('alunos/editar/<id>', views.aluno_edit, name='alunos/editar'),

    path('inscricoes/', views.inscricoes, name='inscricoes'),
    path('inscricoes/edital/<id>', views.inscricoes_edital, name='inscricoes/edital'),
    path('inscricoes/aluno/', views.inscricoes_aluno, name='inscricoes/aluno'),
    path('inscricoes/edital/novo/<id>', views.inscricoes_create, name='inscricao/nova'),
    path('inscricoes/matricular/<id>', views.inscricoes_matricular, name='inscricao/matricular'),
    path('inscricoes/cancelar/<id>', views.inscricoes_cancelar, name='inscricao/cancelar'),
    path('inscricoes/aprovar/<id>', views.inscricoes_aprovar, name='inscricao/aprovar'),
    path('inscricoes/reprovar/<id>', views.inscricoes_reprovar, name='inscricao/reprovar'),
    path('inscricoes/excluir/<id>', views.inscricoes_remove, name='inscricao/excluir'),

    path('registrar/', views.signup, name='registrar'),
]
