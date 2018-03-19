from django.shortcuts import render, redirect
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

def edital_create(request):
    form = EditalForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid() and request.user.is_staff:
            form.save()
            return redirect(editais)
    return render(request, 'core/editais/novo.html', {'form': form})

def edital_edit(request, id):
    edital = Edital.objects.get(id=id)
    form = EditalForm(request.POST or None, instance = edital)
    if form.is_valid() and request.user.is_staff:
        form.save()
        return redirect(editais)
    return render(request, 'core/editais/novo.html', {'form': form})

def edital_remove(request, id):
    edital = Edital.objects.get(id=id)
    if request.user.is_staff:
        edital.delete()
    return redirect(editais)
