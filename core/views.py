from django.shortcuts import render
from core.models import Edital, Aluno, Inscrito
from core.utils import static_files_url

def home(request):
    return render(request, 'core/index.html')

def editais(request, mensagem = None):
    editais = Edital.objects.all().order_by('-id')
    return render(request, 'core/editais/lista.html', {'editais': editais, 'mensagem': mensagem, 'static_url': static_files_url})
