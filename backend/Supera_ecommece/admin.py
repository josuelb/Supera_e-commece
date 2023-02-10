from django.contrib import admin
from .models import *


@admin.register(Clientes)
class Cliente(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
        'sobrenome',
        'user',
        'data_nasc',
        'cpf',
        'email'
    )
    list_display_links = (
        'id',
        'nome',
        'cpf',
        'email',
        'user'
    )
    search_fields = (
        'id',
        'nome',
        'cpf',
        'email',
        'user'
    )


@admin.register(Funcionarios)
class Funcionario(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
        'sobrenome',
        'user',
        'n_Inscricao',
        'data_nasc',
        'cpf',
        'email',
        'cargo'
    )
    list_display_links = (
        'id',
        'nome',
        'user',
        'cpf',
        'email'
    )
    search_fields = (
        'id',
        'nome',
        'user',
        'data_nasc',
        'cpf',
        'email'
    )


@admin.register(Profissoes)
class Profissoe(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('id', 'nome')


@admin.register(Jogos)
class Jogo(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
        'price',
        'score'
    )
    list_display_links = (
        'id',
        'nome'
    )
    search_fields = (
        'id',
        'nome',
        'price',
        'score',
    )
