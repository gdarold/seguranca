from django.forms import ModelForm

from disciplinas.models import Disciplina


class DisciplinaForm(ModelForm):
    class Meta:
        model = Disciplina
        fields = ['nome', 'descricao','cargahoraria', 'alunos']