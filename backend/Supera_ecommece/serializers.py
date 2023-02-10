from rest_framework import serializers
from .models import *

# Classes Serializadoras para a formação a API


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'


class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionarios
        fields = '__all__'


class ProfissoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profissoes
        fields = '__all__'


class JogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogos
        fields = '__all__'
