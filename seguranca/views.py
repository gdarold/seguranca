import re
from django.http import request, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
import bcrypt
from seguranca.forms import LoginForm
from seguranca.models import Login



class Index(TemplateView):
    template_name = 'index.html'


class Redirect(TemplateView):
    template_name = 'redireciona.html'


class CriaLogin(CreateView):
    #template_name = 'login_form.html'
    model = Login
    fields = '__all__'

    # interrompe a criação do login para verificar
    def form_valid(self, form):
        login = form.save(commit=False)

        if valida(login.password):
            print("não deu pau")

        else:
            # devolve mensagem informando que a senha não atende os requisitos
            mensagem = 'Senha invalida, volte para página anterior e tente novamente'
            return HttpResponse(mensagem)

        # magica da validação
        # gera um sal para a senha sendo criada
        salt = bcrypt.gensalt()
        # salva salt
        login.salto = salt
        # cria a criptografia para senha usando biblioteca bcript, senha + salt
        login.password = bcrypt.hashpw(login.password.encode('utf-8'), salt)
        login.permissions = 'leitura'
        login.save()
        return super(CriaLogin, self).form_valid(form)


# validação das senhas com a biblioteca de regex
def valida(senha):
    return (
            # conter letras maiusculas
            re.search(r'[A-Z]', senha) and \
            #minusculas
            re.search(r'[a-z]', senha) and \
            #numeros
            re.search(r'[0-9]', senha) and \
            #caracteres especiais
            re.search(r'[!@#$%<^&*?]', senha) and \
            # conter pelo menos 8 digitos
            re.match(r'^[a-zA-Z0-9!@#$%<^&*?]{8,}$', senha)) \



def logar_view(request):
    legal = True
    form = LoginForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        login = form.save(commit=False)
        # pega a senha que veio via formulario, e codifica em utf-8
        senha = login.password.encode('utf-8')
        print(senha)
        # busca no banco a senha do usuario que esta tentando logar
        try:
            login = Login.objects.get(nome=login.nome)
        except:
            message = "usuario inexistente"
            return render(request, 'logar.html', {'message': message})
        # resgata o salt que foi salvo no banco
        salt = login.salto
        s = salt[2:31]# retira sujeira do salt b' e no final '
        #print(s)
        #print(login.password)
        gambiarra = login.password
        z = gambiarra[2:62]
        #print(z)
        # parte contraditoria, tem outras maneiras
        # pega a senha digitada e cria hast, com ajuda do salt resgatado
        value = bcrypt.hashpw(senha, s.encode('utf-8'))
        #print(value)
        gambiarra2 = str(value)
        x = gambiarra2[2:62]
        print('x',x)
        # compara senha do banco com senha de comparação, não funcionou

        #if bcrypt.checkpw(senha, value):
        if x == z:
            acesso = login
            print(acesso)
            print("passou")
            return render(request,'redireciona.html', {'acesso': acesso})

        else:
            legal = False
            print('deu pau')
            message = "password invalido"
            return render(request, 'logar.html', {'message': message})
    if legal:
        return render(request, 'logar.html', {'form': form})


class ListarLogin(ListView):
    template_name = "lista.html"
    model = Login
    context_object_name = 'Logins'


class ListarLoginSemAcesso(ListView):
    template_name = "lista2.html"
    model = Login
    context_object_name = 'Logis'


class AtualizaLogin(UpdateView):
    template_name = "atualiza.html"
    model = Login()
    fields = ['nome', 'status','permissions']
    context_object_name = 'login'
    success_url = reverse_lazy('lista_login')


class DeletaLogin(DeleteView):
    template_name = 'deleta.html'
    model = Login()
    context_object_name = 'login'
    success_url = reverse_lazy('lista_login')
