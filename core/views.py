from django.shortcuts import render, redirect
from core.models import Edital, Aluno, Inscrito
from core.forms import EditalForm, AlunoForm
from core.utils import static_files_url
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

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
    return render(request, 'core/editais/novo.html', {'form': form, 'static_url': static_files_url})

def edital_edit(request, id):
    edital = Edital.objects.get(id=id)
    form = EditalForm(request.POST or None, instance = edital)
    if form.is_valid() and request.user.is_staff:
        form.save()
        return redirect(editais)
    return render(request, 'core/editais/novo.html', {'form': form, 'static_url': static_files_url})

def edital_remove(request, id):
    edital = Edital.objects.get(id=id)
    if request.user.is_staff:
        edital.delete()
    return redirect(editais)

def alunos(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            alunos = Aluno.objects.all().order_by('nome')
        else:
            alunos = Aluno.objects.all().filter(created_by=request.user)
        return render(request, 'core/alunos/lista.html', {'alunos':alunos, 'static_url': static_files_url})
    return redirect(editais)

def aluno_create(request):
    form = AlunoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid() and request.user.is_authenticated:
            aluno = form.save()
            aluno.created_by = request.user
            aluno.save()
            return redirect(alunos)
    return render(request, 'core/alunos/novo.html', {'form': form, 'static_url': static_files_url})

def aluno_edit(request, id):
    aluno = Aluno.objects.get(id=id)
    form = AlunoForm(request.POST or None, instance = aluno)
    if form.is_valid() and request.user.is_authenticated:
        form.save()
        return redirect(alunos)
    return render(request, 'core/alunos/novo.html', {'form': form, 'static_url': static_files_url})

def signup(request):
    if request.method == 'POST':
        form_user = UserCreationForm(request.POST)
        form_aluno = AlunoForm(request.POST)
        if form_user.is_valid() and form_aluno.is_valid():
            usuario = form_user.save()
            aluno = form_aluno.save()
            aluno.created_by = usuario
            aluno.save()
            username = form_user.cleaned_data.get('username')
            raw_password = form_user.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(editais)
    else:
        form_user = UserCreationForm()
        form_aluno = AlunoForm()
    return render(request, 'core/signup.html', {'form_user': form_user, 'form_aluno': form_aluno, 'static_url': static_files_url})
