# Generated by Django 4.1.6 on 2023-02-10 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='')),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=100)),
                ('data_nasc', models.DateField()),
                ('sexo', models.CharField(max_length=9)),
                ('cpf', models.IntegerField(unique=True)),
                ('cep', models.IntegerField()),
                ('user', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('n_telefone', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Jogos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('score', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Profissoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='')),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=100)),
                ('data_nasc', models.DateField()),
                ('sexo', models.CharField(max_length=9)),
                ('cpf', models.IntegerField(unique=True)),
                ('cep', models.IntegerField()),
                ('user', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('n_Inscricao', models.IntegerField()),
                ('cargo', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Supera_ecommece.profissoes')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
