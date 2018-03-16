from django.urls import path
from core import views

urlpatterns = [
    path('', views.home),
    path('editais/', views.editais, name='editais'),
]
