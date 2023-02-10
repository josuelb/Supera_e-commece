from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import *

# Classes de views com authenticação OBRIGATORIA via Token


class ClientesViews(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Clientes.objects.all()
    serializer_class = ClienteSerializer


class FuncionariosViews(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Funcionarios.objects.all()
    serializer_class = FuncionarioSerializer


class ProfissoesViews(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Profissoes.objects.all()
    serializer_class = ProfissoeSerializer


class JogosViews(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Jogos.objects.all().order_by('nome')  # Ordenando por ordem alfabetica dos nomes
    serializer_class = JogoSerializer

