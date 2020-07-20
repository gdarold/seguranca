from django.db import models

# Create your models here.
from pessoa.models import Person


class Disciplina(models.Model):
    nome = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.CharField(max_length=255, null=False, blank=False)
    cargahoraria = models.IntegerField()

    alunos = models.ManyToManyField(Person)


    def __str__(self):
        return self.nome