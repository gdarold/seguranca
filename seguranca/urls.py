from django.contrib import admin
from django.urls import path
from seguranca.models import Login
from seguranca.views import Index, CriaLogin, ListarLogin, AtualizaLogin, \
    DeletaLogin, logar_view, Redirect, ListarLoginSemAcesso, Coordenador, Aluno, Professor

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('rediretc', Redirect.as_view(), name="redireciona"),
    path('coordena', Coordenador.as_view(), name="cordena"),
    path('professor', Professor.as_view(), name="professor"),
    path('aluno', Aluno.as_view(), name="aluno"),
    path('cadastrar/', CriaLogin.as_view(model=Login), name="cadastra_login"),
    path('valida/', logar_view, name="logar_login"),
    path('listar/', ListarLogin.as_view(model=Login), name="lista_login"),
    path('listarLimitado/', ListarLoginSemAcesso.as_view(model=Login), name="lista_login2"),
    path('atualizar/<pk>', AtualizaLogin.as_view(model=Login), name="atualiza_login"),
    path('deletar/<pk>', DeletaLogin.as_view(model=Login), name="deletar_login"),




]
