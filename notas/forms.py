from django.forms import ModelForm

from notas.models import Notas


class NotasForm(ModelForm):
    class Meta:
        model = Notas
        fields = ['disciplina', 'aluno','nota1', 'nota2']