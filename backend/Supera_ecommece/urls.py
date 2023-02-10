from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from .views import *


# Rotas de views para o Rest Framework reconhecer e fazer o CRUD
router = routers.DefaultRouter()
router.register(r'Clientes', ClientesViews, basename='APIclientes')
router.register(r'Funcionarios', FuncionariosViews, basename='APIfuncionarios')
router.register(r'Profissoes', ProfissoesViews, basename='APIProfissoes')
router.register(r'Jogos', JogosViews, basename='APIjogos')

urlpatterns = [
    # Rota para fazer a requisição com o usuario e senha e capturar o Token de acesso
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Rota para recuperar o token expirado
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # Rota para fazer a requisição com o Token para obter a API
    path('api/supera/', include(router.urls))
]