from django.shortcuts import render, redirect
from core.models import Edital, Aluno, Inscrito
from core.forms import EditalForm, AlunoForm
from core.utils import static_files_url
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# from django.core.email import send_email

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

def inscricoes(request):
    editais = Edital.objects.all().order_by('titulo')
    return render(request, 'core/inscricoes/lista.html', {'editais': editais, 'static_url': static_files_url})

def inscricoes_edital(request, id):
    edital = Edital.objects.get(id=id)
    inscritos = Inscrito.objects.filter(edital=edital).order_by('inscrito_em')
    return render(request, 'core/inscricoes/edital.html', {'inscritos': inscritos, 'static_url': static_files_url})

def inscricoes_aluno(request):
    aluno = Aluno.objects.get(created_by=request.user)
    inscritos = Inscrito.objects.filter(aluno=aluno).order_by('inscrito_em')
    return render(request, 'core/inscricoes/aluno.html', {'inscritos': inscritos, 'static_url': static_files_url})

def inscricoes_create(request, id):
    edital = Edital.objects.get(id=id)
    aluno = Aluno.objects.get(created_by=request.user)
    if aluno == None:
        return redirect(editais)
    qtd_inscricoes = Inscrito.objects.filter(aluno=aluno, edital=edital).count()
    if qtd_inscricoes > 0:
        mensagem = "Aluno já inscrito!"
        return editais(request, mensagem)
    inscrito = Inscrito()
    inscrito.aluno = aluno
    inscrito.edital = edital
    inscrito.status = 1
    inscrito.save()
    mensagem = "Inscrição realizada com sucesso!"
    # send_email('SisExtensão - Inscrição em curso', 'Obrigado por se inscrever em um de nosso cursos! Aguarde a confirmação de sua matrícula.', 'sisextensao@example.com', [inscrito.email])
    return editais(request, mensagem)

def inscricoes_matricular(request, id):
    inscrito = Inscrito.objects.get(id=id)
    edital = inscrito.edital
    inscrito.status = 2
    inscrito.matriculado_em = timezone.now()
    inscrito.save()
    # send_email('SisExtensão - Matrícula em curso', 'Parabéns! Você foi selecionado para iniciar seu curso! Entre em contato com o Campus para realizar sua matrícula.', 'sisextensao@example.com', [inscrito.email])
    return redirect('inscricoes/edital', id=edital.id)

def inscricoes_cancelar(request, id):
    inscrito = Inscrito.objects.get(id=id)
    edital = inscrito.edital
    inscrito.status = 1
    inscrito.matriculado_em = None
    inscrito.save()
    return redirect('inscricoes/edital', id=edital.id)

def inscricoes_aprovar(request, id):
    inscrito = Inscrito.objects.get(id=id)
    edital = inscrito.edital
    inscrito.status = 3
    inscrito.aprovado_em = timezone.now()
    inscrito.save()
    return redirect('inscricoes/edital', id=edital.id)

def inscricoes_reprovar(request, id):
    inscrito = Inscrito.objects.get(id=id)
    edital = inscrito.edital
    inscrito.status = 4
    inscrito.reprovado_em = timezone.now()
    inscrito.save()
    return redirect('inscricoes/edital', id=edital.id)

def inscricoes_remove(request, id):
    inscrito = Inscrito.objects.get(id=id)
    inscrito.delete()
    return redirect('inscricoes/aluno')

def certificado(request, id):
    inscrito = Inscrito.objects.get(id=id)
    edital = Edital.objects.get(id=inscrito.edital.id)
    aluno = Aluno.objects.get(id=inscrito.aluno.id)
    return render(request, 'core/certificados/certificado.html', {'inscrito': inscrito, 'edital': edital, 'aluno': aluno, 'static_url': static_files_url})

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
