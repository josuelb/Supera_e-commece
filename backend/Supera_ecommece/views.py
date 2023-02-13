import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate

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
    queryset = Jogos.objects.all().order_by('nome')  # Ordenando por ordem alfabetica dos nomes
    serializer_class = JogoSerializer


# Faz a pesquisa dos dados unica e exclusivamente de um cliente
class ClienteView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ClienteSerializer

    def get_queryset(self):
        username = self.request.user
        queryset = Clientes.objects.filter(user=username)
        return queryset


# Faz a verificação de existencia de cadastro
@csrf_exempt
def Authentication(request):
    if request.method == "POST":
        dados = request.body
        dados = json.loads(dados)

        user = authenticate(username=dados['username'], password=dados['password'])
        if user:
            response = {
                "Authorization": "Usuário e senha corretos"
            }
            return HttpResponse(json.dumps(response))
        else:
            response = {
                "Authorization": "Usuário ou senha incorretos"
            }
            return HttpResponse(json.dumps(response))
    elif request.method == "GET":
        return HttpResponse('Olá Mundo')
