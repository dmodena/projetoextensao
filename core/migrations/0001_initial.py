# Generated by Django 2.0.1 on 2018-03-15 16:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('logradouro', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=10)),
                ('complemento', models.TextField(blank=True, default='')),
                ('cep', models.CharField(max_length=10)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=2)),
                ('rg', models.CharField(max_length=20)),
                ('cpf', models.CharField(max_length=20, unique=True)),
                ('email', models.CharField(max_length=30)),
                ('telefone', models.CharField(max_length=20)),
                ('nascimento', models.DateField()),
                ('ativo', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Edital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('inicio_inscricoes', models.DateField()),
                ('fim_inscricoes', models.DateField()),
                ('inicio_curso', models.DateField()),
                ('fim_curso', models.DateField()),
                ('vagas', models.IntegerField()),
                ('pre_requisitos', models.TextField()),
                ('edital_link', models.CharField(max_length=100)),
                ('carga_horaria', models.IntegerField(default=1)),
                ('cidade', models.CharField(max_length=100)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inscrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inscrito_em', models.DateTimeField(default=django.utils.timezone.now)),
                ('matriculado_em', models.DateTimeField(null=True)),
                ('aprovado_em', models.DateTimeField(null=True)),
                ('reprovado_em', models.DateTimeField(null=True)),
                ('status', models.IntegerField(default=0)),
                ('observacoes', models.TextField()),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Aluno')),
                ('edital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Edital')),
            ],
        ),
    ]