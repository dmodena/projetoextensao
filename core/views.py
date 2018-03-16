from django.shortcuts import render
from core.models import Edital, Aluno, Inscrito
from core.forms import EditalForm, AlunoForm
from core.utils import static_files_url

def home(request):
    return render(request, 'core/index.html')

def editais(request, mensagem = None):
    editais = Edital.objects.all().order_by('-id')
    return render(request, 'core/editais/lista.html', {'editais': editais, 'mensagem': mensagem, 'static_url': static_files_url})

def r_editais(request):
    return redirect(editais)

def edital_create():
    form = EditalForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(editais)
    return render(request, 'core/editais/novo.html', {'form': form})

def edital_edit():
    return None

def edital_remove():
    return None
