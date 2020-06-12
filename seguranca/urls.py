from django.contrib import admin
from django.urls import path
from seguranca.models import Login
from seguranca.views import Index, CriaLogin, ListarLogin, AtualizaLogin, DeletaLogin


urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('cadastrar/', CriaLogin.as_view(model=Login), name="cadastra_login"),
    path('listar/', ListarLogin.as_view(model=Login), name="lista_login"),
    path('atualizar/<pk>', AtualizaLogin.as_view(model=Login), name="atualiza_login"),
    path('deletar/<pk>', DeletaLogin.as_view(model=Login), name="deletar_login"),




]
