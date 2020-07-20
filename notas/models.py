from django.db import models

# Create your models here.
from disciplinas.models import Disciplina
from pessoa.models import Person


class Notas(models.Model):
    disciplina = models.ForeignKey(Disciplina, null=False, blank=False, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Person, null=False, blank=False, on_delete=models.CASCADE)
    nota1 = models.FloatField(blank=True, null=True)
    nota2 = models.FloatField(blank=True, null=True)
    media = models.FloatField(blank=True, null=True)

    def media(self, num, num2):
        if self.nota1 or self.nota2 ==None:
            self.media = 0

        else:
            self.media = (self.nota1+ self.nota2)/2


    def __str__(self):
        return self.aluno

