from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from seguranca.models import Login


class Index(TemplateView):
    template_name = 'index.html'


class CriaLogin(CreateView):
    template_name = 'cadastro.html'
    model = Login()
    fields = '__all__'
    success_url = reverse_lazy("index")


class ListarLogin(ListView):
    template_name = "lista.html"
    model = Login
    context_object_name = 'Logins'


class AtualizaLogin(UpdateView):
    template_name = "atualiza.html"
    model = Login()
    fields = '__all__'
    context_object_name = 'login'
    success_url = reverse_lazy('lista_login')


class DeletaLogin(DeleteView):
    template_name = 'deleta.html'
    model = Login()
    context_object_name = 'login'
    success_url = reverse_lazy('lista_login')





