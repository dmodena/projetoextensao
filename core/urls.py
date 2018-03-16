from django.urls import path
from core import views

urlpatterns = [
    path('', views.home),
    
    path('editais/', views.editais, name='editais'),
    path('editais/novo/', views.edital_create, name='editais/novo'),
    path('editais/editar/<id>', views.edital_edit, name='editais/editar'),
    path('editais/excluir/<id>', views.edital_remove, name='editais/excluir'),
]
