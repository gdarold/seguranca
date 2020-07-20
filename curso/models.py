from django.db import models

# Create your models here.
from disciplinas.models import Disciplina
from pessoa.models import Person


class Curso(models.Model):
    nome = models.CharField(max_length=255)
    coordenador = models.OneToOneField(Person, on_delete=models.CASCADE)
    disciplinas = models.ManyToManyField(Disciplina)

    def __str__(self):
        return self.nome